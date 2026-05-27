#!/usr/bin/env python3
"""
自动更新项目 README
"""
import json
import re
import yaml
from pathlib import Path
from datetime import datetime


class ReadmeUpdater:
    """README 更新器"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.readme_path = self.project_root / "README.md"
        self.index_dir = self.project_root / "index"

    def update_exchange_table(self):
        """更新 README 中由项目状态生成的内容。"""
        if not self.readme_path.exists():
            return

        # 读取所有交易所索引
        exchanges_data = self._load_all_exchanges()

        # 读取当前 README
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        table_lines = (
            '> 此表由 `src/utils/readme_updater.py` 根据 `config/*.yaml` 和 '
            '`index/*.json` 自动生成。\n\n'
            f'{self._generate_table(exchanges_data)}'
        )
        structure_lines = self._generate_project_structure(exchanges_data)

        updated_content = self._replace_section(content, '支持的交易所', table_lines)
        updated_content = self._replace_section(updated_content, '项目结构', structure_lines)

        # 写回文件
        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        return str(self.readme_path)

    def _replace_section(self, content: str, heading: str, body: str) -> str:
        """替换指定二级标题的内容，保留后续章节。"""
        pattern = rf'(## {re.escape(heading)}\n\n)(.*?)(?=\n\n## |\Z)'
        return re.sub(pattern, lambda match: f'{match.group(1)}{body}', content, flags=re.DOTALL)

    def _load_all_exchanges(self):
        """从 config/*.yaml 和 index/*.json 动态加载交易所状态。"""
        exchanges = {}
        config_dir = self.project_root / "config"

        # 先从配置文件发现已接入的交易所；没有索引时显示为待完成。
        if config_dir.exists():
            for config_file in sorted(config_dir.glob("*.yaml")):
                if config_file.name.endswith("_test.yaml"):
                    continue
                exchange_name = self._safe_exchange_name(config_file.stem)
                if not exchange_name:
                    continue

                display_name = self._display_name(exchange_name)
                try:
                    with open(config_file, 'r', encoding='utf-8') as f:
                        config = yaml.safe_load(f) or {}
                    configured_name = self._safe_exchange_name(config.get('name', exchange_name))
                    if configured_name:
                        exchange_name = configured_name
                        display_name = self._display_name(exchange_name)
                except Exception:
                    pass

                exchanges[exchange_name] = {
                    'display_name': display_name,
                    'status': '🔜',
                    'total': '-',
                    'updated_at': '-'
                }

        # 扫描 index 目录
        if self.index_dir.exists():
            for json_file in sorted(self.index_dir.glob("*.json")):
                exchange_name = self._safe_exchange_name(json_file.stem)
                if not exchange_name:
                    continue

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
                        'display_name': self._display_name(exchange_name),
                        'status': '✅',
                        'total': str(data.get('total', 0)),
                        'updated_at': formatted_date
                    }
                except Exception:
                    pass

        return exchanges

    def _generate_table(self, exchanges_data):
        """生成 Markdown 表格"""
        lines = [
            '| 交易所 | 状态 | 文档数量 | 最后更新 |',
            '|--------|------|----------|----------|'
        ]

        for key in self._sort_exchange_keys(exchanges_data):
            data = exchanges_data.get(key, {})
            display_name = data.get('display_name') or self._display_name(key)
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

    def _generate_project_structure(self, exchanges_data):
        """根据当前文件和索引生成 README 项目结构。"""
        exchange_keys = self._sort_exchange_keys(exchanges_data)
        config_files = self._list_files(self.project_root / 'config', '*.yaml')
        workflow_files = self._list_files(self.project_root / '.github' / 'workflows', '*.yml')
        adapter_files = self._ordered_python_files(self.project_root / 'src' / 'adapters')
        util_files = self._ordered_python_files(self.project_root / 'src' / 'utils')

        lines = [
            '> 此结构由 `src/utils/readme_updater.py` 根据当前仓库文件自动生成。',
            '',
            '```',
            'crypto-api-docs/',
        ]

        if workflow_files:
            lines.extend([
                '├── .github/',
                '│   └── workflows/        # GitHub Actions',
            ])
            self._append_tree_entries(lines, workflow_files, '│       ')

        lines.append('├── config/                 # 交易所配置（YAML）')
        self._append_tree_entries(lines, config_files, '│   ')

        doc_entries = []
        for key in exchange_keys:
            docs_dir = self.project_root / 'docs' / key
            if not docs_dir.exists():
                continue
            total = exchanges_data.get(key, {}).get('total', '-')
            doc_entries.append(f'{key}/'.ljust(24) + f'# {total} Markdown docs')
        lines.append('├── docs/                   # 生成的 Markdown 文档')
        self._append_tree_entries(lines, doc_entries, '│   ')

        index_entries = [
            f'{key}.json'
            for key in exchange_keys
            if (self.project_root / 'index' / f'{key}.json').exists()
        ]
        lines.append('├── index/                  # JSON 索引（供 AI 读取）')
        self._append_tree_entries(lines, index_entries, '│   ')

        lines.extend([
            '├── src/',
            '│   ├── adapters/           # 交易所适配器',
        ])
        self._append_tree_entries(lines, adapter_files, '│   │   ')
        lines.append('│   ├── utils/              # 工具类')
        self._append_tree_entries(lines, util_files, '│   │   ')
        lines.append('│   └── main.py             # 主程序入口')

        if (self.project_root / 'requirements.txt').exists():
            lines.append('├── requirements.txt')
        lines.extend([
            '└── README.md',
            '```',
        ])

        return '\n'.join(lines)

    def _list_files(self, directory: Path, pattern: str) -> list:
        """列出目录下的文件名。"""
        if not directory.exists():
            return []
        return sorted(path.name for path in directory.glob(pattern) if path.is_file())

    def _ordered_python_files(self, directory: Path) -> list:
        """列出 Python 文件，优先展示 __init__ 和 base。"""
        files = self._list_files(directory, '*.py')
        priority = {'__init__.py': 0, 'base.py': 1}
        return sorted(files, key=lambda name: (priority.get(name, 2), name))

    def _append_tree_entries(self, lines: list, entries: list, prefix: str) -> None:
        """给树形结构追加同级节点。"""
        for index, entry in enumerate(entries):
            connector = '└──' if index == len(entries) - 1 else '├──'
            lines.append(f'{prefix}{connector} {entry}')

    def _safe_exchange_name(self, name: str) -> str:
        """只接受安全的交易所标识。"""
        name = (name or '').strip().lower()
        if not re.fullmatch(r'[a-z0-9_-]+', name):
            return ''
        return name

    def _display_name(self, exchange_name: str) -> str:
        """把 exchange key 转成人类可读名称。"""
        display_overrides = {
            'okx': 'OKX',
            'gateio': 'Gate.io',
        }
        if exchange_name in display_overrides:
            return display_overrides[exchange_name]

        return ' '.join(
            part.capitalize()
            for part in re.split(r'[-_]+', exchange_name)
            if part
        )

    def _sort_exchange_keys(self, exchanges_data):
        """完成项优先，再按名称排序，避免 README 依赖硬编码列表。"""
        return sorted(
            exchanges_data,
            key=lambda key: (
                exchanges_data[key].get('status') != '✅',
                self._display_name(key).lower()
            )
        )
