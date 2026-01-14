#!/usr/bin/env python3
"""
Hyperliquid 适配器（GitBook格式）
"""
import time
from typing import List, Dict, Any
from loguru import logger as log
from .base import ExchangeAdapter, DocumentPage
from ..utils.browser import BrowserManager
from ..utils.markdown import MarkdownProcessor


class HyperliquidAdapter(ExchangeAdapter):
    """Hyperliquid GitBook 适配器"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.browser = BrowserManager(f"{self.name}-crawler")
        self.md_processor = MarkdownProcessor()

    def discover_pages(self) -> List[str]:
        """发现所有API文档页面"""
        start_url = self.config['crawler']['start_url']

        if not self.browser.open(start_url, wait=3):
            raise Exception(f"无法打开页面: {start_url}")

        # GitBook 页面，直接提取侧边栏所有链接
        js = '''
        Array.from(document.querySelectorAll('a'))
            .filter(a => a.href.includes('/for-developers/api/'))
            .filter(a => !a.href.endsWith('#'))
            .map(a => a.href)
        '''

        links = self.browser.eval_js(js)

        if not links:
            return []

        # 去重
        unique_links = list(set(links))
        unique_links.sort()

        return unique_links

    def extract_content(self, url: str, skip_open: bool = False) -> DocumentPage:
        """提取页面内容"""

        # 打开页面（并发模式下已打开则跳过）
        if not skip_open:
            self.browser.open(url, wait=2)  # 减少到 2 秒

        # 提取标题
        title_js = 'document.querySelector("h1")?.textContent?.trim() || document.title'
        title = self.browser.eval_js(title_js) or "Untitled"

        # GitBook特殊处理：提取页面正文，排除导航和UI元素
        js_extract = r'''
        (function() {
            const main = document.querySelector('main, article, [role="main"]');
            if (!main) return null;

            // 克隆节点避免修改原始DOM
            const clone = main.cloneNode(true);

            // 1. 转换 role="table" 为真正的 <table>
            clone.querySelectorAll('[role="table"]').forEach(divTable => {
                const table = document.createElement('table');

                divTable.querySelectorAll('[role="rowgroup"]').forEach((rowGroup, idx) => {
                    const section = idx === 0 ? document.createElement('thead') : document.createElement('tbody');

                    rowGroup.querySelectorAll('[role="row"]').forEach(divRow => {
                        const tr = document.createElement('tr');

                        divRow.querySelectorAll('[role="columnheader"], [role="cell"]').forEach(divCell => {
                            const cell = divCell.getAttribute('role') === 'columnheader'
                                ? document.createElement('th')
                                : document.createElement('td');
                            cell.innerHTML = divCell.innerHTML;
                            tr.appendChild(cell);
                        });

                        section.appendChild(tr);
                    });

                    table.appendChild(section);
                });

                divTable.replaceWith(table);
            });

            // 2. 清理标题中的 "hashtag" 文本
            clone.querySelectorAll('h1, h2, h3, h4, h5, h6').forEach(heading => {
                // 移除包含 "hashtag" 的子元素
                heading.querySelectorAll('.hash, [class*="hash"]').forEach(el => el.remove());
                // 清理文本
                heading.textContent = heading.textContent.replace(/^hashtag\s*/i, '').trim();
            });

            // 3. 移除不需要的元素
            const selectors = [
                'nav', 'header', 'footer',
                '.page-api-block:first-child',  // 面包屑
                'button',  // 所有按钮
                '[class*="copy"]',  // 复制按钮
                'svg'  // SVG图标
            ];

            selectors.forEach(sel => {
                clone.querySelectorAll(sel).forEach(el => el.remove());
            });

            return clone.innerHTML;
        })()
        '''

        html_content = self.browser.eval_js(js_extract)

        if not html_content:
            log.warning("无法提取内容")
            return DocumentPage(
                url=url,
                title=title,
                content="",
                metadata={},
                raw_html=""
            )

        # 转换为 Markdown
        markdown = self.md_processor.html_to_markdown(html_content)

        # 后处理：清理多余文本
        markdown = self._clean_markdown(markdown)

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
        from ..utils.markdown import MarkdownProcessor, sanitize_filename

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
            r'copyCopy.*?\n',
            r'chevron-right',
            r'chevron-left',
            r'chevron-down',
            r'chevron-up',
            r'arrow-up-right',
            r'arrow-down',
            r'\[Previous.*?\]\(.*?\)',
            r'\[Next.*?\]\(.*?\)',
            r'Last updated.*?\n'
        ]

        for pattern in ui_patterns:
            markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)

        # 清理空的标题标记（只有 # 但没有文本）
        markdown = re.sub(r'^(#{1,6})\s*$', '', markdown, flags=re.MULTILINE)

        # 清理多余的空行
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)

        return markdown.strip()

    def _detect_api_type(self, url: str, title: str) -> str:
        """检测API类型"""
        url_lower = url.lower()
        title_lower = title.lower()

        if 'websocket' in url_lower or 'websocket' in title_lower:
            return 'WebSocket'
        else:
            return 'REST'
