#!/usr/bin/env python3
"""
交易所适配器基类
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class DocumentPage:
    """文档页面数据结构"""
    url: str
    title: str
    content: str  # Markdown 格式
    metadata: Dict[str, Any]
    raw_html: str = ""


class ExchangeAdapter(ABC):
    """交易所适配器抽象基类"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.name = config['name']
        self.language = config.get('language', 'en')

    def get_products(self) -> List[Dict[str, str]]:
        """
        获取需要爬取的产品列表（可选，用于多产品交易所）

        Returns:
            List[Dict]: 产品列表，每个产品包含 name 和 url
                       返回 None 或空列表表示单产品模式（传统模式）
        """
        return None

    @abstractmethod
    def discover_pages(self) -> List[str]:
        """
        发现所有文档页面URL

        Returns:
            List[str]: 所有页面的URL列表
        """
        pass

    @abstractmethod
    def extract_content(self, url: str) -> DocumentPage:
        """
        提取指定页面的内容

        Args:
            url: 页面URL

        Returns:
            DocumentPage: 提取的页面内容
        """
        pass

    def get_exchange_name(self) -> str:
        """返回交易所名称"""
        return self.name

    def get_output_path(self, product_name: str = None) -> str:
        """
        获取输出路径

        Args:
            product_name: 产品名称（用于多产品模式）

        Returns:
            str: 输出目录路径
        """
        base_dir = self.config.get('output', {}).get('base_dir', 'docs')
        exchange_dir = self.config.get('output', {}).get('dir_name', self.name)

        if product_name:
            # 将产品名转换为安全的目录名
            import re
            safe_name = re.sub(r'[^\w\-]', '_', product_name.lower())
            safe_name = re.sub(r'_+', '_', safe_name).strip('_')
            return f"{base_dir}/{exchange_dir}/{safe_name}"
        else:
            return f"{base_dir}/{exchange_dir}"
