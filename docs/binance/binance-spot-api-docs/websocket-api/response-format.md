---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/response-format
api_type: WebSocket
updated_at: 2026-01-15T23:37:21.120765
---

# Response format

Responses are returned as JSON in **text frames** , one response per frame.

Example of successful response:
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12510053279,  
            "orderListId": -1,  
            "clientOrderId": "a097fe6304b20a7e4fc436",  
            "transactTime": 1655716096505,  
            "price": "0.10000000",  
            "origQty": "10.00000000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "workingTime": 1655716096505,  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 12  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 4043  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 321  
            }  
        ]  
    }  
    

Example of failed response:
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "status": 400,  
        "error": {  
            "code": -2010,  
            "msg": "Account has insufficient balance for requested action."  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 13  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 4044  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 322  
            }  
        ]  
    }  
    

Response fields:

Name | Type | Mandatory | Description  
---|---|---|---  
`id` | INT / STRING / `null` | YES | Same as in the original request  
`status` | INT | YES | Response status. See [Status codes](/docs/binance-spot-api-docs/websocket-api/response-format#status-codes)  
`result` | OBJECT / ARRAY | YES | Response content. Present if request succeeded  
`error` | OBJECT | Error description. Present if request failed  
`rateLimits` | ARRAY | NO | Rate limiting status. See [Rate limits](/docs/binance-spot-api-docs/websocket-api/response-format#rate-limits)  
  
### Status codes[​](/docs/binance-spot-api-docs/websocket-api/response-format#status-codes "Direct link to Status codes")

Status codes in the `status` field are the same as in HTTP.

Here are some common status codes that you might encounter:

  * `200` indicates a successful response.
  * `4XX` status codes indicate invalid requests; the issue is on your side. 
    * `400` – your request failed, see `error` for the reason.
    * `403` – you have been blocked by the Web Application Firewall. This can indicate a rate limit violation or a security block. See <https://www.binance.com/en/support/faq/detail/360004492232> for more details.
    * `409` – your request partially failed but also partially succeeded, see `error` for details.
    * `418` – you have been auto-banned for repeated violation of rate limits.
    * `429` – you have exceeded API request rate limit, please slow down.
  * `5XX` status codes indicate internal errors; the issue is on Binance's side. 
    * **Important:** If a response contains 5xx status code, it **does not** necessarily mean that your request has failed. Execution status is _unknown_ and the request might have actually succeeded. Please use query methods to confirm the status. You might also want to establish a new WebSocket connection for that.



See [Error codes for Binance](/docs/binance-spot-api-docs/errors) for a list of error codes and messages.

---

# 响应格式

响应在 **text 帧** 中以 JSON 格式返回，每帧一个响应。

成功响应示例:
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "status": 200,  
        "result": {  
            "symbol": "BTCUSDT",  
            "orderId": 12510053279,  
            "orderListId": -1,  
            "clientOrderId": "a097fe6304b20a7e4fc436",  
            "transactTime": 1655716096505,  
            "price": "0.10000000",  
            "origQty": "10.00000000",  
            "executedQty": "0.00000000",  
            "origQuoteOrderQty": "0.000000",  
            "cummulativeQuoteQty": "0.00000000",  
            "status": "NEW",  
            "timeInForce": "GTC",  
            "type": "LIMIT",  
            "side": "BUY",  
            "workingTime": 1655716096505,  
            "selfTradePreventionMode": "NONE"  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 12  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 4043  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 321  
            }  
        ]  
    }  
    

失败响应示例:
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "status": 400,  
        "error": {  
            "code": -2010,  
            "msg": "Account has insufficient balance for requested action."  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "SECOND",  
                "intervalNum": 10,  
                "limit": 50,  
                "count": 13  
            },  
            {  
                "rateLimitType": "ORDERS",  
                "interval": "DAY",  
                "intervalNum": 1,  
                "limit": 160000,  
                "count": 4044  
            },  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 322  
            }  
        ]  
    }  
    

响应字段:

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`id` | INT / STRING / `null` | YES | 与原来请求的ID一样  
`status` | INT | YES | 响应状态。请看 [状态代码](/docs/zh-CN/binance-spot-api-docs/websocket-api/response-format#状态代码)  
`result` | OBJECT / ARRAY | YES | 响应内容。请求成功则显示  
`error` | OBJECT | 错误描述。请求失败则显示  
`rateLimits` | ARRAY | NO | 速率限制状态。请看 [速率限制](/docs/zh-CN/binance-spot-api-docs/websocket-api/event-format#ratelimits)  
  
### 状态代码[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/response-format#状态代码 "状态代码的直接链接")

`status` 字段的状态代码与HTTP的状态代码相同。

一些常见状态代码：

  * `200` 代码指示成功响应。
  * `4XX` 错误码用于指示错误的请求内容、行为、格式。问题在于请求者。 
    * `400` – 错误码表示请求失败，请参阅 `error` 了解原因。
    * `403` – 错误码表示违反 WAF 限制(Web应用程序防火墙)。这可能表示触发了速率限制或安全拦截。详情请参见 <https://www.binance.com/zh-CN/support/faq/detail/360004492232> 。
    * `409` – 错误码表示请求有一部分成功，一部分失败。请参阅 `error` 了解更多详细
    * `418` – 表示收到 429 后继续访问，于是被封了。
    * `429` – 错误码表示警告访问频次超限，即将被封IP。
  * `5XX` 错误码用于指示Binance服务侧的问题。 
    * **重要** ：如果响应包含 5xx 状态码，**并不** 一定意思请求失败。 执行状态为 _unknown_ ，请求可能实际成功。 请使用 query 函数确认状态。 建议建立一个新 WebSocket 连接用于确认状态。



有关错误代码和消息的列表，请参阅 [Binance 的错误代码](/docs/zh-CN/binance-spot-api-docs/errors)。