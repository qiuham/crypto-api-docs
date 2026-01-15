---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-api-information
api_type: WebSocket
updated_at: 2026-01-15T23:37:13.596050
---

# General API Information

* The base endpoint is: **`wss://ws-api.binance.com:443/ws-api/v3`**.   
    * If you experience issues with the standard 443 port, alternative port 9443 is also available.
    * The base endpoint for [testnet](https://testnet.binance.vision/) is: `wss://ws-api.testnet.binance.vision/ws-api/v3`
  * A single connection to the API is only valid for 24 hours; expect to be disconnected after the 24-hour mark.
  * We support HMAC, RSA, and Ed25519 keys. For more information, please see [API Key types](/docs/binance-spot-api-docs/faqs/api_key_types).
  * Responses are in JSON by default. To receive responses in SBE, refer to the [SBE FAQ](/docs/binance-spot-api-docs/faqs/sbe_faq) page.
  * If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
  * Some methods may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.
  * The WebSocket server will send a `ping frame` every 20 seconds. 
    * If the WebSocket server does not receive a `pong frame` back from the connection within a minute the connection will be disconnected.
    * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
    * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**
  * Data is returned in **chronological order** , unless noted otherwise. 
    * Without `startTime` or `endTime`, returns the most recent items up to the limit.
    * With `startTime`, returns oldest items from `startTime` up to the limit.
    * With `endTime`, returns most recent items up to `endTime` and the limit.
    * With both, behaves like `startTime` but does not exceed `endTime`.
  * All timestamps in the JSON responses are in **milliseconds in UTC by default**. To receive the information in microseconds, please add the parameter `timeUnit=MICROSECOND` or `timeUnit=microsecond` in the URL.
  * Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp`) can be passed in milliseconds or microseconds.
  * All field names and values are **case-sensitive** , unless noted otherwise.
  * If there are enums or terms you want clarification on, please see [SPOT Glossary](/docs/binance-spot-api-docs/faqs/spot_glossary) for more information.
  * APIs have a timeout of 10 seconds when processing a request. If a response from the Matching Engine takes longer than this, the API responds with "Timeout waiting for response from backend server. Send status unknown; execution status unknown." [(-1007 TIMEOUT)](/docs/binance-spot-api-docs/errors#-1007-timeout)
    * This does not always mean that the request failed in the Matching Engine.
    * If the status of the request has not appeared in [User Data Stream](/docs/binance-spot-api-docs/user-data-stream), please perform an API query for its status.
  * **Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.

---

# API 基本信息

* 本篇所列出的 wss 接口的 base URL：**`wss://ws-api.binance.com:443/ws-api/v3`**  
    * 如果使用标准443端口时遇到问题，可以使用替代端口9443。
    * [现货测试网](https://testnet.binance.vision)的 base URL 是 `wss://ws-api.testnet.binance.vision/ws-api/v3`。
  * 每个到 base URL 的链接有效期不超过24小时，请妥善处理断线重连。
  * 我们支持 HMAC，RSA 以及 Ed25519 Key 类型。 如需进一步了解，请参考 [API Key 类型](/docs/zh-CN/binance-spot-api-docs/faqs/api_key_types)。
  * 响应默认为 JSON 格式。如果您想接收 SBE 格式的响应，请参考 [简单二进制编码 （SBE） 常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/sbe_faq)。
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么响应中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 即使请求本身不包含非 ASCII 字符，某些方法也可能会返回包含以 UTF-8 编码的非 ASCII 字符的资产和/或交易对名称。
  * WebSocket 服务器**每20秒** 发送 PING 消息。 
    * 如果websocket 服务器没有在一分钟之内收到PONG 消息应答，连接会被断开。
    * 当客户收到PING消息，必须尽快回复PONG消息，同时payload需要和PING消息一致。
    * 服务器允许未经请求的PONG消息，但这不会保证连接不断开。**对于这些PONG 消息，建议payload为空。**
  * 除非另有说明，否则数据将按**时间顺序** 返回。 
    * 如果未指定 `startTime` 或 `endTime`，则返回最近的条目，直至达到限制值。
    * 如果指定 `startTime`，则返回从 `startTime` 到限制值为止最老的条目。
    * 如果指定 `endTime`，则返回截至 `endTime` 和限制值为止最近的条目。
    * 如果同时指定 `startTime` 和 `endTime`，则行为类似于 `startTime`，但不超过 `endTime`。
  * JSON 响应中的所有时间和时间戳相关字段均以**UTC 毫秒为默认单位** 。要以微秒为单位接收信息，请在 URL 中添加参数 `timeUnit=MICROSECOND` 或 `timeUnit=microsecond`。
  * 时间戳参数（例如 `startTime`、`endTime`、`timestamp`）可以以毫秒或微秒为单位传递。
  * 除非另有说明，所有字段名称和值都**大小写敏感** 。
  * 如需进一步了解枚举或术语，请参考 [现货交易API术语表](/docs/zh-CN/binance-spot-api-docs/faqs/spot_glossary) 页面。
  * API 处理请求的超时时间为 10 秒。如果撮合引擎的响应时间超过此时间，API 将返回 “Timeout waiting for response from backend server. Send status unknown; execution status unknown.”。[(-1007 超时)](/docs/zh-CN/binance-spot-api-docs/errors#-1007-timeout)
    * 这并不总是意味着该请求在撮合引擎中失败。
    * 如果请求状态未显示在 [WebSocket 账户接口](/docs/zh-CN/binance-spot-api-docs/user-data-stream) 中，请执行 API 查询以获取其状态。
  * **请避免在请求中使用 SQL 关键字** ，因为这可能会触发 Web 应用防火墙（WAF）规则导致安全拦截。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232>