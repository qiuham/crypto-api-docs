---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Open-OCO
api_type: Trading
updated_at: 2026-01-15T23:48:55.382796
---

# Query Margin Account's Open OCO (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Query-Margin-Account-Open-OCO#api-description "Direct link to API Description")

Query Margin Account's Open OCO

## HTTP Request[​](/docs/margin_trading/trade/Query-Margin-Account-Open-OCO#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/openOrderList`

## Request Weight[​](/docs/margin_trading/trade/Query-Margin-Account-Open-OCO#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Margin-Account-Open-OCO#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
symbol| STRING| NO| mandatory for isolated margin, not supported for cross margin  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Query-Margin-Account-Open-OCO#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "orderListId": 31,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "wuB13fmulKj3YjdqWEcsnp",  
        "transactionTime": 1565246080644,  
        "symbol": "LTCBTC",  
        "isIsolated": false,       // if isolated margin  
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 4,  
            "clientOrderId": "r3EH2N76dHfLoSZWIUw1bT"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 5,  
            "clientOrderId": "Cv1SnyPD3qhqpbjpYEHbd2"  
          }  
        ]  
      }  
    ]

---

# 查询杠杆账户 OCO 挂单 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-OCO#接口描述 "接口描述的直接链接")

查询杠杆账户 OCO 挂单

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-OCO#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/openOrderList`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-OCO#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-OCO#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
isIsolated| STRING| NO| 是否逐仓杠杆，"TRUE", "FALSE", 默认 "FALSE"  
symbol| STRING| NO| 逐仓杠杆必填，全仓杠杆不支持该参数  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Open-OCO#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "orderListId": 31,  
        "contingencyType": "OCO",  
        "listStatusType": "EXEC_STARTED",  
        "listOrderStatus": "EXECUTING",  
        "listClientOrderId": "wuB13fmulKj3YjdqWEcsnp",  
        "transactionTime": 1565246080644,  
        "symbol": "LTCBTC",  
        "isIsolated": true,       // 是否是逐仓symbol交易   
        "orders": [  
          {  
            "symbol": "LTCBTC",  
            "orderId": 4,  
            "clientOrderId": "r3EH2N76dHfLoSZWIUw1bT"  
          },  
          {  
            "symbol": "LTCBTC",  
            "orderId": 5,  
            "clientOrderId": "Cv1SnyPD3qhqpbjpYEHbd2"  
          }  
        ]  
      }  
    ]