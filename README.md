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

# 刷新 README 动态内容
PYTHONPATH=. python src/main.py readme
```

## 支持的交易所

> 此表由 `src/utils/readme_updater.py` 根据 `config/*.yaml` 和 `index/*.json` 自动生成。

| 交易所 | 状态 | 文档数量 | 最后更新 |
|--------|------|----------|----------|
| [Binance](./docs/binance/) | ✅ | 822 | 2026-06-06 |
| [Bybit](./docs/bybit/) | ✅ | 459 | 2026-06-06 |
| [Coinbase](./docs/coinbase/) | ✅ | 71 | 2026-06-06 |
| [Gate.io](./docs/gateio/) | ✅ | 66 | 2026-06-02 |
| [Hyperliquid](./docs/hyperliquid/) | ✅ | 34 | 2026-06-06 |
| [Kraken](./docs/kraken/) | ✅ | 248 | 2026-06-05 |
| [OKX](./docs/okx/) | ✅ | 510 | 2026-06-06 |

## GitHub Actions

可以用 GitHub 免费 runner 手动更新文档：

1. 打开仓库的 `Actions` 页面。
2. 选择 `Crawl Docs` workflow。
3. 点击 `Run workflow`。
4. 选择 `exchange`，按需设置 `concurrency`、`limit`、`lang` 和 `commit_changes`。

默认会提交更新；如果只是用 `limit=3` 小范围测试，把 `commit_changes` 改成 `false`。Kraken 和 Gate.io 这类动态/保护较强站点优先使用 `concurrency=1`。

工作流也会每天自动全量刷新一次：北京时间 02:00 触发。定时任务按交易所拆成独立 job，并通过 `max-parallel=1` 一个一个更新，避免多个 runner 同时提交造成冲突。默认并发为 Coinbase 5、Hyperliquid 3、Binance/Bybit/OKX 5、Kraken/Gate.io 2。

## 项目结构

> 此结构由 `src/utils/readme_updater.py` 根据当前仓库文件自动生成。

```
crypto-api-docs/
├── .github/
│   └── workflows/        # GitHub Actions
│       └── crawl-docs.yml
├── config/                 # 交易所配置（YAML）
│   ├── binance.yaml
│   ├── bybit.yaml
│   ├── coinbase.yaml
│   ├── gateio.yaml
│   ├── hyperliquid.yaml
│   ├── kraken.yaml
│   └── okx.yaml
├── docs/                   # 生成的 Markdown 文档
│   ├── binance/                # 822 Markdown docs
│   ├── bybit/                  # 459 Markdown docs
│   ├── coinbase/               # 71 Markdown docs
│   ├── gateio/                 # 66 Markdown docs
│   ├── hyperliquid/            # 34 Markdown docs
│   ├── kraken/                 # 248 Markdown docs
│   └── okx/                    # 510 Markdown docs
├── index/                  # JSON 索引（供 AI 读取）
│   ├── binance.json
│   ├── bybit.json
│   ├── coinbase.json
│   ├── gateio.json
│   ├── hyperliquid.json
│   ├── kraken.json
│   └── okx.json
├── src/
│   ├── adapters/           # 交易所适配器
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── binance.py
│   │   ├── bybit.py
│   │   ├── coinbase.py
│   │   ├── gateio.py
│   │   ├── hyperliquid.py
│   │   ├── kraken.py
│   │   └── okx.py
│   ├── utils/              # 工具类
│   │   ├── __init__.py
│   │   ├── browser.py
│   │   ├── indexer.py
│   │   ├── markdown.py
│   │   ├── path_generator.py
│   │   ├── readme_updater.py
│   │   └── repair.py
│   └── main.py             # 主程序入口
├── requirements.txt
└── README.md
```

## 技术栈

- **爬虫引擎**: agent-browser（浏览器自动化）
- **文档格式**: Markdown with YAML frontmatter
- **HTML 转换**: html2text
- **日志**: loguru
- **配置**: YAML

## TODO

- 观察定时全量任务对 Kraken 和 Gate.io 的长期成功率。
- 如果免费 runner 风控失败，再考虑为受保护站点单独加备用方案。
- 如果多个交易所全量更新耗时过长，再拆成按天错峰的多个 schedule。
