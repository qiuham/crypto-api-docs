---
exchange: binance
source_url: https://developers.binance.com/docs/convert/trade/Cancel-Order
api_type: Trading
updated_at: 2026-01-15T23:50:19.672990
---

# Cancel limit order (USER_DATA)

## API Description[​](/docs/convert/trade/Cancel-Order#api-description "Direct link to API Description")

Enable users to cancel a limit order

## HTTP Request[​](/docs/convert/trade/Cancel-Order#http-request "Direct link to HTTP Request")

POST `/sapi/v1/convert/limit/cancelOrder`

## Request Weight[​](/docs/convert/trade/Cancel-Order#request-weight "Direct link to Request Weight")

**200(UID)**

## Request Parameters[​](/docs/convert/trade/Cancel-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
orderId| LONG| YES| The orderId from `placeOrder` api  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/convert/trade/Cancel-Order#response-example "Direct link to Response Example")
    
    
    {  
        "orderId": 1603680255057330400,   
        "status": "CANCELED"  
    }

---

# 取消闪兑限价单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/convert/trade/Cancel-Order#接口描述 "接口描述的直接链接")

用户取消闪兑限价单

## HTTP请求[​](/docs/zh-CN/convert/trade/Cancel-Order#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/convert/limit/cancelOrder`

## 请求权重[​](/docs/zh-CN/convert/trade/Cancel-Order#请求权重 "请求权重的直接链接")

**200(UID)**

## 请求参数[​](/docs/zh-CN/convert/trade/Cancel-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
orderId| LONG| YES| orderId 在 `placeOrder`接口响应中获得  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/convert/trade/Cancel-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "orderId": 1603680255057330400,   
        "status": "CANCELED"  
    }