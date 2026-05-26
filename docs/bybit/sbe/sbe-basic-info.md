---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/sbe/sbe-basic-info
api_type: REST
updated_at: 2026-01-16T09:40:59.874150
---

# SBE Basic Information

MMWS / Gateway only

All SBE-based feeds are described in this section are available **only** via the **Market Maker WebSocket (MMWS) / Market Maker Gateway (GW)** infrastructure.

For access and architecture details, see the official announcement: [Market Maker Gateway](https://announcements.bybit.global/article/introducing-the-market-maker-gateway-for-enhanced-api-connectivity-and-performance-bltfaba80a427cac5e5/)

From January 15, 2026, sbe connection will only be avaiable via **v5/public-sbe**

This page gives a unified introduction to Bybit's **SBE-based market data** channels and how they fit into the MMWS/GW environment. Detailed, feature-specific behavior and code examples are provided in the sub-pages for:

  * **BBO SBE** (Level 1, with RPI fields)
  * **Level-50 SBE** (50-level order book snapshots + deltas)



## What is SBE?

Bybit uses **Simple Binary Encoding (SBE)** in accordance with the FIX/SBE 1.0 specification:

  * Binary, little-endian encoding
  * Fixed-width fields where possible
  * Explicit **message header** \+ **message body** layout
  * High-efficiency decoding suitable for HFT and MM strategies



Compared with JSON WebSocket feeds, SBE provides:

  * Smaller payloads (up to ~30–50% reduction vs equivalent JSON data)
  * Deterministic binary layouts
  * Microsecond timestamp precision
  * Lower CPU usage for both encoding and decoding

---

# SBE 基本信息

僅限 MMWS / Gateway

本節中所描述的所有基於 SBE 的行情資料頻道，只能透過 **Market Maker WebSocket (MMWS) / Market Maker Gateway (GW)** 基礎設施使用。

如需接入方式與架構細節，請參考官方公告: [做市商網關](https://announcements.bybit.global/article/introducing-the-market-maker-gateway-for-enhanced-api-connectivity-and-performance-bltfaba80a427cac5e5/)

自2026年1月15日起，SBE連接將僅能通過 **v5/public-sbe** 使用。

本頁提供 Bybit **基於 SBE 的市場數據** 通道在 MMWS/GW 環境中的統一介紹。關於各功能的詳細行為與程式碼範例，請參考以下子頁面:

  * **BBO SBE** (Level 1, 含 RPI 欄位)
  * **Level-50 SBE** (50 檔深度訂單簿快照 + 增量更新)



## 什麼是 SBE?

Bybit 採用符合 FIX/SBE 1.0 規範的 **Simple Binary Encoding (SBE)** :

  * 二進位資料, little-endian 編碼
  * 儘可能使用固定長度欄位
  * 明確區分 **訊息標頭 (message header)** 與 **訊息主體 (message body)** 佈局
  * 高效率解碼, 適用於高頻交易 (HFT) 與做市策略



與 JSON WebSocket 行情相比, SBE 具備以下優點:

  * 較小的訊息負載 (相較等價 JSON 資料可降低約 30–50%)
  * 決定性的二進位結構
  * 微秒級時間戳精度
  * 在編碼與解碼時皆有較低的 CPU 消耗