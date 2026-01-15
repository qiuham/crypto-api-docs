---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-api-information
api_type: REST
updated_at: 2026-01-15T23:36:14.808236
---

# General API Information

* The following base endpoints are available. Please use whichever works best for your setup: 
    * **<https://api.binance.com>**
    * **<https://api-gcp.binance.com>**
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**
  * The last 4 endpoints in the point above (`api1`-`api4`) should give better performance but have less stability.
  * Responses are in JSON by default. To receive responses in SBE, refer to the [SBE FAQ](/docs/binance-spot-api-docs/faqs/sbe_faq) page.
  * If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
  * Some endpoints may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.
  * Data is returned in **chronological order** , unless noted otherwise. 
    * Without `startTime` or `endTime`, returns the most recent items up to the limit.
    * With `startTime`, returns oldest items from `startTime` up to the limit.
    * With `endTime`, returns most recent items up to `endTime` and the limit.
    * With both, behaves like `startTime` but does not exceed `endTime`.
  * All time and timestamp related fields in the JSON responses are in **milliseconds by default.** To receive the information in microseconds, please add the header `X-MBX-TIME-UNIT:MICROSECOND` or `X-MBX-TIME-UNIT:microsecond`.
  * We support HMAC, RSA, and Ed25519 keys. For more information, please see [API Key types](/docs/binance-spot-api-docs/faqs/api_key_types).
  * Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp`) can be passed in milliseconds or microseconds.
  * For APIs that only send public market data, please use the base endpoint **<https://data-api.binance.vision>**. Please refer to [Market Data Only](/docs/binance-spot-api-docs/faqs/market_data_only) page.
  * If there are enums or terms you want clarification on, please see the [SPOT Glossary](/docs/binance-spot-api-docs/faqs/spot_glossary) for more information.
  * APIs have a timeout of 10 seconds when processing a request. If a response from the Matching Engine takes longer than this, the API responds with "Timeout waiting for response from backend server. Send status unknown; execution status unknown." [(-1007 TIMEOUT)](/docs/binance-spot-api-docs/errors#-1007-timeout)
    * This does not always mean that the request failed in the Matching Engine.
    * If the status of the request has not appeared in [User Data Stream](/docs/binance-spot-api-docs/user-data-stream), please perform an API query for its status.
  * **Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.
  * If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
  * Some endpoints may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.

---

# API 基本信息

* 本篇列出接口的 base URL 有: 
    * **<https://api.binance.com>**
    * **<https://api-gcp.binance.com>**
    * **<https://api1.binance.com>**
    * **<https://api2.binance.com>**
    * **<https://api3.binance.com>**
    * **<https://api4.binance.com>**
  * 上述列表的最后4个接口 (`api1`-`api4`) 会提供更好的性能，但其稳定性略为逊色。因此，请务必使用最适合的URL。
  * 响应默认为 JSON 格式。如果您想接收 SBE 格式的响应，请参考 [简单二进制编码 （SBE） 常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/sbe_faq)。
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么响应中可能包含以 UTF-8 编码的非 ASCII 字符。
  * 即使请求本身不包含非 ASCII 字符，某些端点也可能会返回包含以 UTF-8 编码的非 ASCII 字符的资产和/或交易对名称。
  * 除非另有说明，否则数据将按**时间顺序** 返回。 
    * 如果未指定 `startTime` 或 `endTime`，则返回最近的条目，直至达到限制值。
    * 如果指定 `startTime`，则返回从 `startTime` 到限制值为止最老的条目。
    * 如果指定 `endTime`，则返回截至 `endTime` 和限制值为止最近的条目。
    * 如果同时指定 `startTime` 和 `endTime`，则行为类似于 `startTime`，但不超过 `endTime`。
  * JSON 响应中的所有时间和时间戳相关字段均以**毫秒为默认单位** 。要以微秒为单位接收信息，请添加报文头 `X-MBX-TIME-UNIT：MICROSECOND` 或 `X-MBX-TIME-UNIT：microsecond`。
  * 我们支持 HMAC，RSA 以及 Ed25519 Key 类型。 如需进一步了解，请参考 [API Key 类型](/docs/zh-CN/binance-spot-api-docs/faqs/api_key_types)。
  * 时间戳参数（例如 `startTime`、`endTime`、`timestamp`）可以以毫秒或微秒为单位传递。
  * 对于仅发送公开市场数据的 API，您可以使用接口的 base URL <https://data-api.binance.vision> 。请参考 [Market Data Only_CN](/docs/zh-CN/binance-spot-api-docs/faqs/market_data_only) 页面。
  * 如需进一步了解枚举或术语，请参考 [现货交易API术语表](/docs/zh-CN/binance-spot-api-docs/faqs/spot_glossary) 页面。
  * API 处理请求的超时时间为 10 秒。如果撮合引擎的响应时间超过此时间，API 将返回 “Timeout waiting for response from backend server. Send status unknown; execution status unknown.”。[(-1007 超时)](/docs/zh-CN/binance-spot-api-docs/errors#-1007-timeout)
    * 这并不总是意味着该请求在撮合引擎中失败。
    * 如果请求状态未显示在 [WebSocket 账户接口](/docs/zh-CN/binance-spot-api-docs/user-data-stream) 中，请执行 API 查询以获取其状态。
  * **请避免在请求中使用 SQL 关键字** ，因为这可能会触发 Web 应用防火墙（WAF）规则导致安全拦截。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232>
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么响应中可能会包含以 UTF-8 编码的非 ASCII 字符。
  * 即使请求中不包含非 ASCII 字符，某些接口也可能返回包含以 UTF-8 编码的非 ASCII 字符的资产和/或交易对名称。