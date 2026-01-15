---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/general-information-on-endpoints
api_type: REST
updated_at: 2026-01-15T23:36:14.934472
---

# General Information on Endpoints

* For `GET` endpoints, parameters must be sent as a `query string`.
  * For `POST`, `PUT`, and `DELETE` endpoints, the parameters may be sent as a `query string` or in the `request body` with content type `application/x-www-form-urlencoded`. You may mix parameters between both the `query string` and `request body` if you wish to do so.
  * Parameters may be sent in any order.
  * If a parameter sent in both the `query string` and `request body`, the `query string` parameter will be used.

---

# 接口的基本信息

* `GET` 方法的接口, 参数必须在 `query string`中发送。
  * `POST`, `PUT`, 和 `DELETE` 方法的接口,参数可以在内容形式为`application/x-www-form-urlencoded`的 `query string` 中发送，也可以在 `request body` 中发送。 如果你喜欢，也可以混合这两种方式发送参数。
  * 对参数的顺序不做要求。
  * 但如果同一个参数名在`query string`和`request body`中都有，`query string`中的会被优先采用。