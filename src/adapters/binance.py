#!/usr/bin/env python3
"""
Binance 适配器（Docusaurus 格式）
"""
import time
from typing import List, Dict, Any
from loguru import logger as log
from .base import ExchangeAdapter, DocumentPage
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


class BinanceAdapter(ExchangeAdapter):
    """Binance Docusaurus 适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()

    def get_products(self) -> List[Dict[str, str]]:
        """获取'金融交易'分类下的所有产品"""
        # 打开任意币安文档页面来访问产品菜单
        homepage = "https://developers.binance.com/docs/zh-CN/derivatives/Introduction"
        if not self.browser.open(homepage, wait=3):
            raise Exception(f"无法打开页面: {homepage}")

        # 点击产品按钮并获取"金融交易"分类下的产品
        js_get_products = '''
        (function() {
            // 点击产品按钮
            const btn = document.querySelector('button[class*="productSelector"]');
            if (btn) {
                btn.click();
            }

            // 等待菜单展开
            const start = Date.now();
            while (Date.now() - start < 1000);

            // 点击"金融交易"分类
            const groups = document.querySelectorAll('[class*="groupItem"]');
            let tradingGroup = null;
            groups.forEach(g => {
                if (g.textContent.trim() === '金融交易') {
                    tradingGroup = g;
                    g.click();
                }
            });

            if (!tradingGroup) {
                return { error: '找不到金融交易分类' };
            }

            // 再等待一下让产品列表更新
            const start2 = Date.now();
            while (Date.now() - start2 < 500);

            // 获取金融交易分类下的所有产品
            const products = [];
            const productItems = document.querySelectorAll('a[class*="productItem"]');

            productItems.forEach(item => {
                const titleEl = item.querySelector('[class*="Title"]');
                const title = titleEl ? titleEl.textContent.trim() : '';
                const href = item.href;

                if (title && href) {
                    products.push({
                        name: title,
                        url: href
                    });
                }
            });

            return {
                category: '金融交易',
                products: products,
                total: products.length
            };
        })()
        '''

        result = self.browser.eval_js(js_get_products)

        if not result or 'error' in result:
            log.error("获取产品列表失败")
            return []

        products = result.get('products', [])
        log.info(f"发现 {len(products)} 个金融交易产品")

        return products

    def discover_pages(self) -> List[str]:
        """发现所有API文档页面"""
        start_url = self.config['crawler']['start_url']

        if not self.browser.open(start_url, wait=3):
            raise Exception(f"无法打开页面: {start_url}")

        # 展开所有折叠菜单
        collapsed_selector = self.config['crawler']['selectors']['collapsed_menu']
        max_iterations = 50  # 防止死循环

        for i in range(max_iterations):
            # 统计折叠菜单数量
            count = self.browser.count_elements(collapsed_selector)
            if count == 0:
                log.info("所有菜单已展开")
                break

            log.info(f"[轮次 {i+1}] 折叠菜单: {count} 个")

            # 点击折叠菜单里的 a[role="button"]
            js_expand = '''
            const collapsedItems = document.querySelectorAll('.menu__list-item--collapsed');
            let expanded = 0;

            collapsedItems.forEach(item => {
                const link = item.querySelector('a[role="button"]');
                if (link) {
                    try {
                        link.click();
                        expanded++;
                    } catch(e) {}
                }
            });

            expanded;
            '''

            clicked = self.browser.eval_js(js_expand)
            if not clicked or clicked == 0:
                break

            # 不需要 sleep，下一轮会自动检测变化

        # 提取所有文档链接
        doc_link_selector = self.config['crawler']['selectors']['doc_link']
        js = f'''
        Array.from(document.querySelectorAll('{doc_link_selector}'))
            .map(a => a.href)
            .filter(href => href && !href.endsWith('#'))
        '''

        links = self.browser.eval_js(js)

        if not links:
            return []

        # 去重并排序
        unique_links = list(set(links))
        unique_links.sort()

        log.info(f"发现 {len(unique_links)} 个页面")
        return unique_links

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取页面内容"""

        # 打开页面
        if not skip_open:
            self.browser.open(url, wait=2)

        # 提取标题（在 article 内查找第一个 h1）
        title_js = '''
        (function() {
            // 优先从 article 内查找 h1
            const article = document.querySelector('main article');
            if (article) {
                const h1 = article.querySelector('h1');
                if (h1) return h1.textContent.trim();
            }

            // 其次查找页面任意 h1
            const anyH1 = document.querySelector('h1');
            if (anyH1) return anyH1.textContent.trim();

            // 最后用 document.title，去掉后缀
            return document.title.split('|')[0].trim();
        })()
        '''
        title = self.browser.eval_js(title_js) or "Untitled"

        # 提取主内容
        content_selector = self.config['crawler']['selectors']['main_content']
        js_extract = f'''
        (function() {{
            const main = document.querySelector('{content_selector}');
            if (!main) return null;

            // 克隆节点
            const clone = main.cloneNode(true);

            // 清理不需要的元素
            const selectors = [
                'nav', 'header', 'footer', 'button',
                '[class*="copy"]', 'svg'
            ];

            selectors.forEach(sel => {{
                clone.querySelectorAll(sel).forEach(el => el.remove());
            }});

            return clone.innerHTML;
        }})()
        '''

        html_content = self.browser.eval_js(js_extract)

        if not html_content:
            log.warning(f"无法提取内容: {url}")
            return DocumentPage(
                url=url,
                title=title,
                content="",
                metadata={},
                raw_html=""
            )

        # 转换为 Markdown
        markdown = self.md_processor.html_to_markdown(html_content)
        markdown = self._clean_markdown(markdown)

        # 移除第一个 h1（避免和 create_document 添加的标题重复）
        markdown = self._remove_first_h1(markdown)

        # 提取元数据
        metadata = {
            'exchange': self.name,
            'language': self.language,
            'source_url': url,
            'api_type': self._detect_api_type(url, title)
        }

        return DocumentPage(
            url=url,
            title=title,
            content=markdown,
            metadata=metadata,
            raw_html=html_content
        )

    def save_page(self, page: DocumentPage, output_path: str):
        """保存页面到文件"""
        import os
        from ..utils.markdown import MarkdownProcessor

        processor = MarkdownProcessor()

        # 创建完整文档
        doc_content = processor.create_document(
            title=page.title,
            content=page.content,
            metadata=page.metadata
        )

        # 确保目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(doc_content)

        return output_path

    def _clean_markdown(self, markdown: str) -> str:
        """清理Markdown内容"""
        import re

        # 移除常见的UI元素文本
        ui_patterns = [
            r'copyCopy.*?\\n',
            r'\\[Previous.*?\\]\\(.*?\\)',
            r'\\[Next.*?\\]\\(.*?\\)',
            r'Last updated.*?\\n'
        ]

        for pattern in ui_patterns:
            markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)

        # 清理多余的空行
        markdown = re.sub(r'\\n{3,}', '\\n\\n', markdown)

        return markdown.strip()

    def _remove_first_h1(self, markdown: str) -> str:
        """移除第一个 h1 标题"""
        import re

        # 匹配第一个 h1（行首的 # ）
        pattern = r'^# .+?$'
        markdown = re.sub(pattern, '', markdown, count=1, flags=re.MULTILINE)

        # 清理开头的空行
        return markdown.lstrip()

    def _detect_api_type(self, url: str, title: str) -> str:
        """检测API类型"""
        url_lower = url.lower()
        title_lower = title.lower()

        if 'websocket' in url_lower or 'websocket' in title_lower or 'ws' in url_lower:
            return 'WebSocket'
        elif 'market' in url_lower or '行情' in title_lower:
            return 'Market Data'
        elif 'trade' in url_lower or '交易' in title_lower:
            return 'Trading'
        elif 'account' in url_lower or '账户' in title_lower:
            return 'Account'
        else:
            return 'REST'
