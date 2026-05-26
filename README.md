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

# 只刷新 README 交易所表格
PYTHONPATH=. python src/main.py readme
```

## 支持的交易所

| 交易所 | 状态 | 文档数量 | 最后更新 |
|--------|------|----------|----------|
| [Binance](./docs/binance/) | ✅ | 804 | 2026-01-16 |
| [Bybit](./docs/bybit/) | ✅ | 294 | 2026-01-16 |
| [Coinbase](./docs/coinbase/) | ✅ | 71 | 2026-05-26 |
| [Gate.io](./docs/gateio/) | ✅ | 66 | 2026-05-26 |
| [Hyperliquid](./docs/hyperliquid/) | ✅ | 34 | 2026-05-26 |
| [Kraken](./docs/kraken/) | ✅ | 243 | 2026-05-26 |
| [OKX](./docs/okx/) | ✅ | 470 | 2026-01-15 |

## 项目结构

```
crypto-api-docs/
├── config/                 # 交易所配置（YAML）
│   └── <exchange>.yaml
├── docs/                   # 生成的 Markdown 文档
│   └── <exchange>/         # 按交易所分目录
├── index/                  # JSON 索引（供 AI 读取）
│   └── <exchange>.json
├── src/
│   ├── adapters/           # 交易所适配器
│   │   ├── base.py         # 基类
│   │   └── <exchange>.py
│   ├── utils/              # 工具类
│   │   ├── browser.py      # 浏览器自动化
│   │   ├── markdown.py     # HTML → Markdown
│   │   ├── indexer.py      # 索引生成
│   │   └── path_generator.py # 路径生成工具
│   └── main.py             # 主程序入口
└── README.md
```

## 技术栈

- **爬虫引擎**: agent-browser（浏览器自动化）
- **文档格式**: Markdown with YAML frontmatter
- **HTML 转换**: html2text
- **日志**: loguru
- **配置**: YAML
