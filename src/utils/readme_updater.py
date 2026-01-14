#!/usr/bin/env python3
"""
自动更新项目 README
"""
import os
import json
import re
from pathlib import Path
from datetime import datetime


class ReadmeUpdater:
    """README 更新器"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.readme_path = self.project_root / "README.md"
        self.index_dir = self.project_root / "index"

    def update_exchange_table(self):
        """更新交易所表格"""
        if not self.readme_path.exists():
            return

        # 读取所有交易所索引
        exchanges_data = self._load_all_exchanges()

        # 生成新的表格
        table_lines = self._generate_table(exchanges_data)

        # 读取当前 README
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 替换表格部分
        pattern = r'(## 支持的交易所\n\n)(.*?)(\n\n##)'
        new_section = f'## 支持的交易所\n\n{table_lines}\n\n##'

        updated_content = re.sub(
            pattern,
            new_section,
            content,
            flags=re.DOTALL
        )

        # 写回文件
        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        return str(self.readme_path)


    def _load_all_exchanges(self):
        """加载所有交易所的索引数据"""
        exchanges = {
            'hyperliquid': {'status': '🔜', 'total': '-', 'updated_at': '-'},
            'binance': {'status': '🔜', 'total': '-', 'updated_at': '-'},
            'okx': {'status': '🔜', 'total': '-', 'updated_at': '-'},
            'bybit': {'status': '🔜', 'total': '-', 'updated_at': '-'},
            'kraken': {'status': '🔜', 'total': '-', 'updated_at': '-'},
            'coinbase': {'status': '🔜', 'total': '-', 'updated_at': '-'},
            'gateio': {'status': '🔜', 'total': '-', 'updated_at': '-'},
        }

        # 扫描 index 目录
        if self.index_dir.exists():
            for json_file in self.index_dir.glob("*.json"):
                exchange_name = json_file.stem
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # 格式化更新时间
                    updated_at = data.get('updated_at', '')
                    if updated_at:
                        try:
                            dt = datetime.fromisoformat(updated_at)
                            formatted_date = dt.strftime('%Y-%m-%d')
                        except:
                            formatted_date = updated_at.split()[0] if ' ' in updated_at else updated_at
                    else:
                        formatted_date = '-'

                    exchanges[exchange_name] = {
                        'status': '✅',
                        'total': str(data.get('total', 0)),
                        'updated_at': formatted_date
                    }
                except Exception:
                    pass

        return exchanges

    def _generate_table(self, exchanges_data):
        """生成 Markdown 表格"""
        # 交易所名称映射
        name_map = {
            'hyperliquid': 'Hyperliquid',
            'binance': 'Binance',
            'okx': 'OKX',
            'bybit': 'Bybit',
            'kraken': 'Kraken',
            'coinbase': 'Coinbase',
            'gateio': 'Gate.io'
        }

        lines = [
            '| 交易所 | 状态 | 文档数量 | 最后更新 |',
            '|--------|------|----------|----------|'
        ]

        for key, display_name in name_map.items():
            data = exchanges_data.get(key, {})
            status = data.get('status', '🔜')
            total = data.get('total', '-')
            updated = data.get('updated_at', '-')

            # 如果已完成，添加文档链接
            if status == '✅':
                name_link = f'[{display_name}](./docs/{key}/)'
            else:
                name_link = display_name

            lines.append(f'| {name_link} | {status} | {total} | {updated} |')

        return '\n'.join(lines)
