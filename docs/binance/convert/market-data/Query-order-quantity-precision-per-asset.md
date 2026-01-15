---
exchange: binance
source_url: https://developers.binance.com/docs/convert/market-data/Query-order-quantity-precision-per-asset
api_type: Market Data
updated_at: 2026-01-15T23:50:16.047041
---

# Query order quantity precision per asset(USER_DATA)

## API Description[​](/docs/convert/market-data/Query-order-quantity-precision-per-asset#api-description "Direct link to API Description")

Query for supported asset’s precision information

## HTTP Request[​](/docs/convert/market-data/Query-order-quantity-precision-per-asset#http-request "Direct link to HTTP Request")

GET `/sapi/v1/convert/assetInfo`

## Request Weight[​](/docs/convert/market-data/Query-order-quantity-precision-per-asset#request-weight "Direct link to Request Weight")

**100(IP)**

## Request Parameters[​](/docs/convert/market-data/Query-order-quantity-precision-per-asset#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/convert/market-data/Query-order-quantity-precision-per-asset#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "asset": "BTC",   
        "fraction": 8  
      },  
      {  
        "asset": "SHIB",   
        "fraction": 2  
      }  
    ]

---

# 查询可交易币种精度(USER_DATA)

## 接口描述[​](/docs/zh-CN/convert/market-data/Query-order-quantity-precision-per-asset#接口描述 "接口描述的直接链接")

查询每个可交易币种的精度信息

## HTTP请求[​](/docs/zh-CN/convert/market-data/Query-order-quantity-precision-per-asset#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/convert/assetInfo`

## 请求权重[​](/docs/zh-CN/convert/market-data/Query-order-quantity-precision-per-asset#请求权重 "请求权重的直接链接")

**100(IP)**

## 请求参数[​](/docs/zh-CN/convert/market-data/Query-order-quantity-precision-per-asset#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 此值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/convert/market-data/Query-order-quantity-precision-per-asset#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "asset": "BTC",   
        "fraction": 8  
      },  
      {  
        "asset": "SHIB",   
        "fraction": 2  
      }  
    ]