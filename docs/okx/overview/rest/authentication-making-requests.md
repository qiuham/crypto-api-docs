---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#overview-rest-authentication-making-requests
anchor_id: overview-rest-authentication-making-requests
api_type: REST
updated_at: 2026-01-15T23:27:48.572284
---

# Making Requests

All private REST requests must contain the following headers:

  * `OK-ACCESS-KEY` The API key as a String.

  * `OK-ACCESS-SIGN` The Base64-encoded signature (see Signing Messages subsection for details).

  * `OK-ACCESS-TIMESTAMP` The UTC timestamp of your request .e.g : 2020-12-08T09:08:57.715Z

  * `OK-ACCESS-PASSPHRASE` The passphrase you specified when creating the API key.

Request bodies should have content type `application/json` and be in valid JSON format.

---

# 发起请求

所有REST私有请求头都必须包含以下内容：

  * `OK-ACCESS-KEY`字符串类型的APIKey。

  * `OK-ACCESS-SIGN`使用HMAC SHA256哈希函数获得哈希值，再使用Base-64编码（请参阅签名）。

  * `OK-ACCESS-TIMESTAMP`发起请求的时间（UTC），如：2020-12-08T09:08:57.715Z

  * `OK-ACCESS-PASSPHRASE`您在创建API密钥时指定的Passphrase。

所有请求都应该含有application/json类型内容，并且是有效的JSON。