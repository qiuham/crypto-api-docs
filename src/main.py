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
    config_file = project_root / f"config/{exchange_name}.yaml"

    if not config_file.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_file}")

    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def crawl_exchange(exchange_name: str, concurrency: int = 1, limit: int = None):
    """爬取指定交易所"""
    from src.adapters.base import get_adapter

    log.info(f"开始爬取: {exchange_name} (并发: {concurrency})")
    if limit:
        log.warning(f"限制模式：每个入口最多爬取 {limit} 页")

    # 加载配置
    config = load_config(exchange_name)

    # 动态获取适配器（通过装饰器注册表）
    adapter = get_adapter(config)

    # 统一接口：每个适配器实现自己的爬取逻辑
    adapter.crawl(concurrency=concurrency, limit=limit)


def main():
    parser = argparse.ArgumentParser(description='爬取交易所API文档')
    parser.add_argument('command', choices=['crawl'], help='命令')
    parser.add_argument('--exchange', '-e', required=True, help='交易所名称')
    parser.add_argument('--concurrency', '-c', type=int, default=1,
                        help='并发数（标签页数量），默认 1')
    parser.add_argument('--limit', '-l', type=int, default=None,
                        help='每个入口限制爬取的页面数')

    args = parser.parse_args()

    if args.command == 'crawl':
        crawl_exchange(args.exchange, concurrency=args.concurrency, limit=args.limit)


if __name__ == '__main__':
    main()
