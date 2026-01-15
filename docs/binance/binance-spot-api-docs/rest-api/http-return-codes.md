---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/http-return-codes
api_type: REST
updated_at: 2026-01-15T23:36:14.994862
---

# HTTP Return Codes

* HTTP `4XX` return codes are used for malformed requests; the issue is on the sender's side.
  * HTTP `403` return code is used when a WAF (Web Application Firewall) rule has been violated. This can indicate a rate limit violation or a security block. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.
  * HTTP `409` return code is used when a cancelReplace order partially succeeds. (i.e. if the cancellation of the order fails but the new order placement succeeds.)
  * HTTP `429` return code is used when breaking a request rate limit.
  * HTTP `418` return code is used when an IP has been auto-banned for continuing to send requests after receiving `429` codes.
  * HTTP `5XX` return codes are used for internal errors; the issue is on Binance's side. It is important to **NOT** treat this as a failure operation; the execution status is **UNKNOWN** and could have been a success.

---

# HTTP 返回代码

* HTTP `4XX` 错误码用于指示错误的请求内容、行为、格式。问题在于请求者。
  * HTTP `403` 错误码表示违反WAF限制(Web应用程序防火墙)。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232> 。
  * HTTP `409` 错误码表示重新下单(cancelReplace)的请求部分成功。(比如取消订单失败，但是下单成功了)
  * HTTP `429` 错误码表示警告访问频次超限，即将被封IP。
  * HTTP `418` 表示收到429后继续访问，于是被封了。
  * HTTP `5XX` 错误码用于指示Binance服务侧的问题。