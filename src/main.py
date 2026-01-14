#!/usr/bin/env python3
"""
加密货币交易所 API 文档爬取工具
"""
import os
import sys
import yaml
import argparse
from pathlib import Path
from loguru import logger as log

# 配置日志
log.remove()
log.add(
    sys.stderr,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
    level="INFO",
    colorize=True
)


def load_config(exchange_name: str) -> dict:
    """加载交易所配置"""
    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    config_file = project_root / f"config/exchanges/{exchange_name}.yaml"

    if not config_file.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_file}")

    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_adapter(exchange_name: str, config: dict):
    """根据交易所名称获取适配器"""
    if exchange_name == 'hyperliquid':
        from src.adapters.hyperliquid import HyperliquidAdapter
        return HyperliquidAdapter(config)
    elif exchange_name == 'binance':
        from src.adapters.binance import BinanceAdapter
        return BinanceAdapter(config)
    else:
        raise NotImplementedError(f"暂不支持: {exchange_name}")


def crawl_exchange(exchange_name: str, concurrency: int = 1):
    """爬取指定交易所"""
    log.info(f"开始爬取: {exchange_name} (并发: {concurrency})")

    # 加载配置
    config = load_config(exchange_name)

    # 获取适配器
    adapter = get_adapter(exchange_name, config)

    # Binance 特殊处理：爬取金融交易分类下的所有产品
    if exchange_name == 'binance':
        crawl_binance_trading_products(adapter, concurrency)
        return

    # 其他交易所：原有流程
    # 发现页面
    log.info("发现页面...")
    urls = adapter.discover_pages()

    if not urls:
        log.error("未发现任何页面")
        return

    log.success(f"发现 {len(urls)} 个页面")

    # 初始化输出目录
    output_dir = adapter.get_output_path()
    os.makedirs(output_dir, exist_ok=True)

    # 提取内容
    log.info("开始提取内容...")

    if concurrency == 1:
        # 单线程
        success_count = _crawl_sequential(adapter, urls, output_dir)
    else:
        # 多标签并发
        success_count = _crawl_concurrent(adapter, urls, output_dir, concurrency)

    # 总结
    log.success(f"完成! 成功: {success_count}/{len(urls)}")
    log.info(f"保存在: {output_dir}")

    # 生成索引
    log.info("生成索引...")
    from src.utils.indexer import DocumentIndexer
    project_root = Path(__file__).parent.parent
    index_dir = project_root / "index"
    indexer = DocumentIndexer(output_dir)
    index_path = indexer.generate_index(str(index_dir))
    log.success(f"索引已生成: {index_path}")

    # 更新主 README
    log.info("更新 README...")
    from src.utils.readme_updater import ReadmeUpdater
    updater = ReadmeUpdater(str(project_root))
    readme_path = updater.update_exchange_table()
    log.success(f"README 已更新: {readme_path}")


def crawl_binance_trading_products(adapter, concurrency: int = 1):
    """爬取币安金融交易分类下的所有产品"""
    log.info("获取金融交易产品列表...")

    # 获取产品列表
    products = adapter.get_trading_products()

    if not products:
        log.error("未发现任何产品")
        return

    log.success(f"发现 {len(products)} 个产品")

    # 对每个产品分别爬取
    for i, product in enumerate(products, 1):
        product_name = product['name']
        product_url = product['url']

        log.info(f"\n{'='*60}")
        log.info(f"[{i}/{len(products)}] 开始爬取: {product_name}")
        log.info(f"{'='*60}")

        # 打开产品页面
        if not adapter.browser.open(product_url, wait=3):
            log.error(f"无法打开产品页面: {product_url}")
            continue

        # 发现该产品的所有页面
        log.info(f"发现 {product_name} 的页面...")
        urls = adapter.discover_pages()

        if not urls:
            log.warning(f"{product_name} 未发现任何页面")
            continue

        log.success(f"{product_name} 发现 {len(urls)} 个页面")

        # 为该产品创建输出目录
        output_dir = adapter.get_output_path(product_name)
        os.makedirs(output_dir, exist_ok=True)

        # 提取内容
        log.info(f"开始提取 {product_name} 内容...")

        if concurrency == 1:
            success_count = _crawl_sequential(adapter, urls, output_dir)
        else:
            success_count = _crawl_concurrent(adapter, urls, output_dir, concurrency)

        log.success(f"{product_name} 完成! 成功: {success_count}/{len(urls)}")

    # 全部完成后，生成索引和更新README
    log.info("\n" + "="*60)
    log.info("所有产品爬取完成，生成索引...")

    from src.utils.indexer import DocumentIndexer
    project_root = Path(__file__).parent.parent
    index_dir = project_root / "index"

    # 为整个 binance 目录生成索引
    base_output_dir = adapter.get_output_path()
    indexer = DocumentIndexer(base_output_dir)
    index_path = indexer.generate_index(str(index_dir))
    log.success(f"索引已生成: {index_path}")

    # 更新主 README
    log.info("更新 README...")
    from src.utils.readme_updater import ReadmeUpdater
    updater = ReadmeUpdater(str(project_root))
    readme_path = updater.update_exchange_table()
    log.success(f"README 已更新: {readme_path}")


def _crawl_sequential(adapter, urls, output_dir):
    """顺序爬取"""
    success_count = 0
    for i, url in enumerate(urls, 1):
        try:
            filename = f"{url.split('/')[-1] or 'index'}.md"
            output_path = os.path.join(output_dir, filename)
            page = adapter.extract_content(url)
            adapter.save_page(page, output_path)
            log.success(f"[{i}/{len(urls)}] {page.title}")
            success_count += 1
        except Exception as e:
            log.error(f"[{i}/{len(urls)}] {url} - {e}")
    return success_count


def _crawl_concurrent(adapter, urls, output_dir, concurrency):
    """多标签并发爬取（固定标签，批次复用）"""
    browser = adapter.browser
    total = len(urls)
    success_count = 0

    # 已有tab 0，再创建N-1个新标签
    num_tabs = min(concurrency, total)
    browser.open_tabs_batch(num_tabs - 1)

    for batch_start in range(0, total, num_tabs):
        batch_urls = urls[batch_start:batch_start + num_tabs]
        batch_size = len(batch_urls)

        # 1. 批量加载URLs（并行，复用现有标签）
        browser.load_urls_batch(batch_urls, start_tab=0)

        # 2. 顺序提取内容
        for i, url in enumerate(batch_urls):
            idx = batch_start + i + 1
            try:
                browser.tab_switch(i)

                # 等待页面加载完成
                if not browser.wait_for_element('main', timeout=30):
                    log.warning(f"[{idx}/{total}] 页面加载超时，尝试继续")

                filename = f"{url.split('/')[-1] or 'index'}.md"
                output_path = os.path.join(output_dir, filename)
                page = adapter.extract_content(url, skip_open=True)
                adapter.save_page(page, output_path)

                log.success(f"[{idx}/{total}] {page.title}")
                success_count += 1
            except Exception as e:
                log.error(f"[{idx}/{total}] {url} - {e}")

    return success_count


def main():
    parser = argparse.ArgumentParser(description='爬取交易所API文档')
    parser.add_argument('command', choices=['crawl'], help='命令')
    parser.add_argument('--exchange', '-e', required=True, help='交易所名称')
    parser.add_argument('--concurrency', '-c', type=int, default=1,
                        help='并发数（标签页数量），默认 1')

    args = parser.parse_args()

    if args.command == 'crawl':
        crawl_exchange(args.exchange, concurrency=args.concurrency)


if __name__ == '__main__':
    main()
