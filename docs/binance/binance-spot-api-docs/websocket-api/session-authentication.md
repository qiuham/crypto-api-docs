---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/session-authentication
api_type: WebSocket
updated_at: 2026-01-15T23:37:21.202220
---

# Session Authentication

**Note:** Only _Ed25519_ keys are supported for this feature.

If you do not want to specify `apiKey` and `signature` in each individual request, you can authenticate your API key for the active WebSocket session.

Once authenticated, you no longer have to specify `apiKey` and `signature` for those requests that need them. Requests will be performed on behalf of the account owning the authenticated API key.

**Note:** You still have to specify the `timestamp` parameter for `SIGNED` requests.

### Authenticate after connection[​](/docs/binance-spot-api-docs/websocket-api/session-authentication#authenticate-after-connection "Direct link to Authenticate after connection")

You can authenticate an already established connection using session authentication requests:

  * [`session.logon`](/docs/binance-spot-api-docs/websocket-api/session-authentication#log-in-with-api-key-signed) – authenticate, or change the API key associated with the connection
  * [`session.status`](/docs/binance-spot-api-docs/websocket-api/session-authentication#query-session-status) – check connection status and the current API key
  * [`session.logout`](/docs/binance-spot-api-docs/websocket-api/session-authentication#log-out-of-the-session) – forget the API key associated with the connection



**Regarding API key revocation:**

If during an active session the API key becomes invalid for _any reason_ (e.g. IP address is not whitelisted, API key was deleted, API key doesn't have correct permissions, etc), after the next request the session will be revoked with the following error message:
    
    
    {  
        "id": null,  
        "status": 401,  
        "error": {  
            "code": -2015,  
            "msg": "Invalid API-key, IP, or permissions for action."  
        }  
    }  
    

### Authorize _ad hoc_ requests[​](/docs/binance-spot-api-docs/websocket-api/session-authentication#authorize-ad-hoc-requests "Direct link to authorize-ad-hoc-requests")

Only one API key can be authenticated with the WebSocket connection. The authenticated API key is used by default for requests that require an `apiKey` parameter. However, you can always specify the `apiKey` and `signature` explicitly for individual requests, overriding the authenticated API key and using a different one to authorize a specific request.

For example, you might want to authenticate your `USER_DATA` key to be used by default, but specify the `TRADE` key with an explicit signature when placing orders.

---

# 会话身份验证

**注意：** 仅支持 _Ed25519_ 密钥用于此功能。

如果你不想在每个单独的请求中指定`apiKey`和`signature`，你可以为有效的WebSocket会话进行API密钥身份验证。

一旦完成身份验证，你将不需在需要它们的请求中指定`apiKey`和`signature`。 这些请求将代表拥有已验证API密钥的帐户执行。

**注意：** 对于`SIGNED`请求，你仍需要指定`timestamp`参数。

### 连接后进行身份验证[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/session-authentication#连接后进行身份验证 "连接后进行身份验证的直接链接")

你可以使用会话身份验证请求对已经建立的连接进行身份验证：

  * [`session.logon`](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#session-logon) – 进行身份验证，或更改与连接相关联的API密钥。
  * [`session.status`](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#query-session-status) – 检查连接状态和当前API密钥。
  * [`session.logout`](/docs/zh-CN/binance-spot-api-docs/websocket-api/authentication-requests#session-logout) – 忘记与连接关联的API密钥。



**关于吊销API密钥:**

如果在活动会话期间，由于 _任何_ 原因（例如IP地址未被加入白名单、API密钥被删除、API密钥没有正确的权限等），在下一个请求后，会话将被吊销，并显示以下错误消息:
    
    
    {  
        "id": null,  
        "status": 401,  
        "error": {  
            "code": -2015,  
            "msg": "Invalid API-key, IP, or permissions for action."  
        }  
    }  
    

### 授权 _临时_ 请求[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/session-authentication#授权-临时-请求 "授权-临时-请求的直接链接")

WebSocket连接只能通过一个API密钥进行身份验证。 默认情况下，经过身份验证的API密钥将用于需要`apiKey`参数的请求。 但是，你始终可以为单个请求明确指定`apiKey`和`signature`，覆盖已认证的API密钥，以使用不同的API密钥授权特定请求。

例如，你可能希望用默认密钥来验证 `USER_DATA`，但在下单时使用`TRADE`密钥来签名。