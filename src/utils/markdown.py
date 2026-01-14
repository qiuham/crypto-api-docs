#!/usr/bin/env python3
"""
Markdown 处理工具
"""
import html2text
from typing import Dict, Any
from datetime import datetime


class MarkdownProcessor:
    """Markdown 转换和处理"""

    def __init__(self):
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        self.converter.ignore_images = False
        self.converter.ignore_emphasis = False
        self.converter.body_width = 0
        # 表格处理
        self.converter.bypass_tables = False  # 转换表格为 Markdown
        self.converter.use_automatic_links = True

    def html_to_markdown(self, html: str) -> str:
        """HTML 转 Markdown"""
        return self.converter.handle(html)

    def generate_frontmatter(self, metadata: Dict[str, Any]) -> str:
        """生成文档前置信息"""
        lines = ['---']

        for key, value in metadata.items():
            if isinstance(value, list):
                lines.append(f"{key}:")
                for item in value:
                    lines.append(f"  - {item}")
            elif isinstance(value, datetime):
                lines.append(f"{key}: {value.isoformat()}")
            else:
                lines.append(f"{key}: {value}")

        lines.append('---')
        return '\n'.join(lines)

    def create_document(
        self,
        title: str,
        content: str,
        metadata: Dict[str, Any]
    ) -> str:
        """创建完整的Markdown文档"""
        # 添加更新时间
        if 'updated_at' not in metadata:
            metadata['updated_at'] = datetime.now()

        frontmatter = self.generate_frontmatter(metadata)

        return f"{frontmatter}\n\n# {title}\n\n{content}"


def sanitize_filename(name: str, max_length: int = 100) -> str:
    """清理文件名"""
    import re

    # 移除特殊字符
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # 空格转连字符
    name = re.sub(r'\s+', '-', name)
    # 移除多余的连字符
    name = re.sub(r'-+', '-', name)
    # 转小写
    name = name.lower().strip('-')
    # 限制长度
    return name[:max_length]
