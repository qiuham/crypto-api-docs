#!/usr/bin/env python3
"""
文档索引生成器
"""
import os
import yaml
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime


class DocumentIndexer:
    """文档索引生成器"""

    def __init__(self, docs_dir: str):
        self.docs_dir = Path(docs_dir)

    def scan_documents(self) -> List[Dict[str, Any]]:
        """扫描目录下所有文档"""
        docs = []

        for md_file in sorted(self.docs_dir.glob("*.md")):
            if md_file.name.lower() in ['index.md', 'readme.md']:
                continue

            doc_info = self._parse_document(md_file)
            if doc_info:
                docs.append(doc_info)

        return docs

    def _parse_document(self, file_path: Path) -> Dict[str, Any]:
        """解析单个文档的元数据"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 提取 frontmatter
            if not content.startswith('---'):
                return None

            parts = content.split('---', 2)
            if len(parts) < 3:
                return None

            metadata = yaml.safe_load(parts[1])

            # 提取标题（第一个 h1）
            lines = parts[2].strip().split('\n')
            title = None
            for line in lines:
                if line.startswith('# '):
                    title = line[2:].strip()
                    break

            return {
                'filename': file_path.name,
                'title': title or file_path.stem.replace('-', ' ').title(),
                'metadata': metadata
            }

        except Exception as e:
            return None

    def generate_index(self, index_dir: str) -> str:
        """生成 AI 可读的 JSON 索引文件"""
        docs = self.scan_documents()

        if not docs:
            return ""

        # 构建索引结构
        exchange_name = docs[0]['metadata'].get('exchange', 'unknown')

        # 按 api_type 分组
        grouped = {}
        for doc in docs:
            api_type = doc['metadata'].get('api_type', 'Other')
            if api_type not in grouped:
                grouped[api_type] = []
            grouped[api_type].append({
                'title': doc['title'],
                'filename': doc['filename'],
                'path': f"docs/{exchange_name}/{doc['filename']}",
                'source_url': doc['metadata'].get('source_url', ''),
                'updated_at': str(doc['metadata'].get('updated_at', ''))
            })

        # 获取最新更新时间（转成字符串）
        latest_update = max(
            (str(doc['metadata'].get('updated_at', '')) for doc in docs),
            default=''
        )

        index_data = {
            'exchange': exchange_name,
            'total': len(docs),
            'updated_at': latest_update,
            'documents_by_type': grouped,
            'all_documents': [
                {
                    'title': doc['title'],
                    'filename': doc['filename'],
                    'path': f"docs/{exchange_name}/{doc['filename']}",
                    'api_type': doc['metadata'].get('api_type', 'Other'),
                    'source_url': doc['metadata'].get('source_url', ''),
                    'updated_at': str(doc['metadata'].get('updated_at', ''))
                }
                for doc in sorted(docs, key=lambda x: x['title'])
            ]
        }

        # 确保索引目录存在
        import os
        os.makedirs(index_dir, exist_ok=True)

        # 写入 JSON 文件
        import json
        output_path = os.path.join(index_dir, f"{exchange_name}.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)

        return output_path

    def generate_structure(self) -> Dict[str, Any]:
        """生成文档结构树"""
        docs = self.scan_documents()

        structure = {
            'exchange': docs[0]['metadata'].get('exchange', '') if docs else '',
            'total': len(docs),
            'by_type': {},
            'documents': []
        }

        # 按类型统计
        for doc in docs:
            api_type = doc['metadata'].get('api_type', 'Other')
            structure['by_type'][api_type] = structure['by_type'].get(api_type, 0) + 1

            structure['documents'].append({
                'title': doc['title'],
                'filename': doc['filename'],
                'api_type': api_type,
                'source_url': doc['metadata'].get('source_url', '')
            })

        return structure
