---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage
api_type: Trading
updated_at: 2026-01-15T23:48:51.350625
---

# Query Current Margin Order Count Usage (TRADE)

## API Description[​](/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#api-description "Direct link to API Description")

Displays the user's current margin order count usage for all intervals.

## HTTP Request[​](/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/rateLimit/order`

## Request Weight[​](/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#request-weight "Direct link to Request Weight")

**20(IP)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
symbol| STRING| NO| isolated symbol, mandatory for isolated margin  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#response-example "Direct link to Response Example")
    
    
    [  
      
      {  
        "rateLimitType": "ORDERS",  
        "interval": "SECOND",  
        "intervalNum": 10,  
        "limit": 10000,  
        "count": 0  
      },  
      {  
        "rateLimitType": "ORDERS",  
        "interval": "DAY",  
        "intervalNum": 1,  
        "limit": 20000,  
        "count": 0  
      }  
    ]

---

# 查询目前杠杆账户下单数 (TRADE)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#接口描述 "接口描述的直接链接")

获取用户在当前时间区间内的杠杆账户下单总数。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/rateLimit/order`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#请求权重 "请求权重的直接链接")

**20(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
symbol| STRING| NO| 逐仓交易对，查询逐仓杠杆账户必需  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Current-Margin-Order-Count-Usage#响应示例 "响应示例的直接链接")
    
    
    [  
      
      {  
        "rateLimitType": "ORDERS",  
        "interval": "SECOND",  
        "intervalNum": 10,  
        "limit": 10000,  
        "count": 0  
      },  
      {  
        "rateLimitType": "ORDERS",  
        "interval": "DAY",  
        "intervalNum": 1,  
        "limit": 20000,  
        "count": 0  
      }  
    ]