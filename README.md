# 加密货币交易所 API 文档

自动爬取和维护主流加密货币交易所的 API 文档。

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 确保已安装 agent-browser
npm install -g agent-browser
agent-browser install

# 爬取文档
PYTHONPATH=. python src/main.py crawl -e hyperliquid -c 5
```

## 支持的交易所

| 交易所 | 状态 | 文档数量 | 最后更新 |
|--------|------|----------|----------|
| [Hyperliquid](./docs/hyperliquid/) | ✅ | 15 | 2026-01-14 |
| [Binance](./docs/binance/) | ✅ | 10 | 2026-01-15 |
| OKX | 🔜 | - | - |
| Bybit | 🔜 | - | - |
| Kraken | 🔜 | - | - |
| Coinbase | 🔜 | - | - |
| Gate.io | 🔜 | - | - |

## 项目结构

```
crypto-api-docs/
├── config/                 # 交易所配置（YAML）
│   ├── binance.yaml
│   ├── okx.yaml
│   └── hyperliquid.yaml
├── docs/                   # 生成的 Markdown 文档
│   ├── hyperliquid/        # 按交易所分目录
│   ├── binance/
│   └── okx/
├── index/                  # JSON 索引（供 AI 读取）
├── src/
│   ├── adapters/           # 交易所适配器
│   │   ├── base.py         # 基类
│   │   ├── hyperliquid.py  # Hyperliquid (GitBook)
│   │   ├── binance.py      # Binance (Docusaurus)
│   │   └── okx.py          # OKX (SPA)
│   ├── utils/              # 工具类
│   │   ├── browser.py      # 浏览器自动化
│   │   ├── markdown.py     # HTML → Markdown
│   │   ├── indexer.py      # 索引生成
│   │   └── path_generator.py # 路径生成工具
│   └── main.py             # 主程序入口
├── scripts/                # 工具脚本
└── README.md
```

## 技术栈

- **爬虫引擎**: agent-browser（浏览器自动化）
- **文档格式**: Markdown with YAML frontmatter
- **HTML 转换**: markdownify
- **日志**: loguru
- **配置**: YAML
