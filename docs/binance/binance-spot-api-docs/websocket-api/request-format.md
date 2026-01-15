---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/request-format
api_type: WebSocket
updated_at: 2026-01-15T23:37:20.935962
---

# Request format

Requests must be sent as JSON in **text frames** , one request per frame.

Example of request:
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "BUY",  
            "type": "LIMIT",  
            "price": "0.1",  
            "quantity": "10",  
            "timeInForce": "GTC",  
            "timestamp": 1655716096498,  
            "apiKey": "T59MTDLWlpRW16JVeZ2Nju5A5C98WkMm8CSzWC4oqynUlTm1zXOxyauT8LmwXEv9",  
            "signature": "5942ad337e6779f2f4c62cd1c26dba71c91514400a24990a3e7f5edec9323f90"  
        }  
    }  
    

Request fields:

Name| Type| Mandatory| Description  
---|---|---|---  
`id`| INT / STRING / `null`| YES| Arbitrary ID used to match responses to requests  
`method`| STRING| YES| Request method name  
`params`| OBJECT| NO| Request parameters. May be omitted if there are no parameters  
  
  * Request `id` is truly arbitrary. You can use UUIDs, sequential IDs, current timestamp, etc. The server does not interpret `id` in any way, simply echoing it back in the response.

You can freely reuse IDs within a session. However, be careful to not send more than one request at a time with the same ID, since otherwise it might be impossible to tell the responses apart.

  * Request method names may be prefixed with explicit version: e.g., `"v3/order.place"`.

  * The order of `params` is not significant.

---

# 请求格式

请求必须在 **text 帧** 中以 JSON 格式发送，每帧一个请求。

请求示例:
    
    
    {  
        "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",  
        "method": "order.place",  
        "params": {  
            "symbol": "BTCUSDT",  
            "side": "BUY",  
            "type": "LIMIT",  
            "price": "0.1",  
            "quantity": "10",  
            "timeInForce": "GTC",  
            "timestamp": 1655716096498,  
            "apiKey": "T59MTDLWlpRW16JVeZ2Nju5A5C98WkMm8CSzWC4oqynUlTm1zXOxyauT8LmwXEv9",  
            "signature": "5942ad337e6779f2f4c62cd1c26dba71c91514400a24990a3e7f5edec9323f90"  
        }  
    }  
    

请求字段:

名称| 类型| 是否必需| 描述  
---|---|---|---  
`id`| INT / STRING / `null`| YES| 任意的 ID 用于匹配对请求的响应  
`method`| STRING| YES| 请求函数名称  
`params`| OBJECT| NO| 请求参数。如果没有参数可以省略  
  
  * 请求 `id` 是任意的。可以使用 UUID、顺次 ID、当前时间戳等。 服务器不会以任何方式解释 `id`，只是在响应中回显它。

可以在一个会话中自由重复使用 ID，不过请注意不要一次发送多个具有相同 ID 的请求，因为否则可能无法区分响应。

  * 请求函数名称可以以显式版本为前缀，例如：`"v3/order.place"`

  * `params` 的顺序不重要。