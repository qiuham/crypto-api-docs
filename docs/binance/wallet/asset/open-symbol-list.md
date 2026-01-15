---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/open-symbol-list
api_type: REST
updated_at: 2026-01-15T23:49:30.546510
---

# Get Open Symbol List (MARKET_DATA)

## API Description[​](/docs/wallet/asset/open-symbol-list#api-description "Direct link to API Description")

Get the list of symbols that are scheduled to be opened for trading in the market.

## HTTP Request[​](/docs/wallet/asset/open-symbol-list#http-request "Direct link to HTTP Request")

GET `/sapi/v1/spot/open-symbol-list`

## Request Weight(IP)[​](/docs/wallet/asset/open-symbol-list#request-weightip "Direct link to Request Weight\(IP\)")

**100**

## Request Parameters[​](/docs/wallet/asset/open-symbol-list#request-parameters "Direct link to Request Parameters")

No parameters required.

## Response Example[​](/docs/wallet/asset/open-symbol-list#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "openTime": 1686161202000,  
        "symbols": [  
          "BNBBTC",  
          "BNBETH"  
        ]  
      },  
      {  
        "openTime": 1686222232000,  
        "symbols": [  
          "BTCUSDT"  
        ]  
      }  
    ]

---

# 查询开放币对列表 (MARKET_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/open-symbol-list#接口描述 "接口描述的直接链接")

查询即将开放交易的币对列表。

## HTTP请求[​](/docs/zh-CN/wallet/asset/open-symbol-list#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/spot/open-symbol-list`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/open-symbol-list#请求权重ip "请求权重\(IP\)的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/wallet/asset/open-symbol-list#请求参数 "请求参数的直接链接")

无需参数。

## 响应示例[​](/docs/zh-CN/wallet/asset/open-symbol-list#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "openTime": 1686161202000,  
        "symbols": [  
          "BNBBTC",  
          "BNBETH"  
        ]  
      },  
      {  
        "openTime": 1686222232000,  
        "symbols": [  
          "BTCUSDT"  
        ]  
      }  
    ]