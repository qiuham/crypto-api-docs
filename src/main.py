#!/usr/bin/env python3
"""
加密货币交易所 API 文档爬取工具
"""
import os
import sys
import yaml
import argparse
import re
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
    if not re.fullmatch(r'[a-z0-9_-]+', exchange_name):
        raise ValueError(f"非法交易所名称: {exchange_name}")

    # 获取项目根目录
    project_root = Path(__file__).parent.parent
    config_dir = (project_root / "config").resolve()
    config_file = (config_dir / f"{exchange_name}.yaml").resolve()

    if config_dir not in config_file.parents:
        raise ValueError(f"配置路径越界: {exchange_name}")

    if not config_file.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_file}")

    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def crawl_exchange(exchange_name: str, concurrency: int = 1, limit: int = None, languages: list = None):
    """爬取指定交易所"""
    from src.adapters.base import get_adapter

    log.info(f"开始爬取: {exchange_name} (并发: {concurrency})")
    if limit:
        log.warning(f"限制模式：每个入口最多爬取 {limit} 页")
    if languages:
        log.info(f"指定语言: {', '.join(languages)}")

    # 加载配置
    config = load_config(exchange_name)

    # 动态获取适配器（通过装饰器注册表）
    adapter = get_adapter(config)

    # 统一接口：每个适配器实现自己的爬取逻辑
    adapter.crawl(concurrency=concurrency, limit=limit, languages=languages)


def main():
    parser = argparse.ArgumentParser(description='爬取交易所API文档')
    parser.add_argument('command', choices=['crawl', 'readme'], help='命令')
    parser.add_argument('--exchange', '-e', help='交易所名称')
    parser.add_argument('--concurrency', '-c', type=int, default=1,
                        help='并发数（标签页数量），默认 1')
    parser.add_argument('--limit', '-l', type=int, default=None,
                        help='每个入口限制爬取的页面数')
    parser.add_argument('--lang', type=str, default=None,
                        help='指定爬取的语言，多个语言用逗号分隔（如：en,zh）。不指定则爬取所有语言')

    args = parser.parse_args()

    if args.command == 'crawl':
        if not args.exchange:
            parser.error('crawl 命令需要指定 --exchange/-e')

        # 解析语言参数
        languages = args.lang.split(',') if args.lang else None
        crawl_exchange(args.exchange, concurrency=args.concurrency, limit=args.limit, languages=languages)
    elif args.command == 'readme':
        from src.utils.readme_updater import ReadmeUpdater

        project_root = Path(__file__).parent.parent
        readme_path = ReadmeUpdater(str(project_root)).update_exchange_table()
        log.success(f"README 已更新: {readme_path}")


if __name__ == '__main__':
    main()
