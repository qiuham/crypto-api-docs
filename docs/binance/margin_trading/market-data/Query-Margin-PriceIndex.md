---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Query-Margin-PriceIndex
api_type: Market Data
updated_at: 2026-01-15T23:48:33.964696
---

# Query Margin PriceIndex (MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data/Query-Margin-PriceIndex#api-description "Direct link to API Description")

Query Margin PriceIndex

## HTTP Request[​](/docs/margin_trading/market-data/Query-Margin-PriceIndex#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/priceIndex`

## Request Weight[​](/docs/margin_trading/market-data/Query-Margin-PriceIndex#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/market-data/Query-Margin-PriceIndex#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
  
## Response Example[​](/docs/margin_trading/market-data/Query-Margin-PriceIndex#response-example "Direct link to Response Example")
    
    
    {  
       "calcTime": 1562046418000,  
       "price": "0.00333930",  
       "symbol": "BNBBTC"  
    }

---

# 查询杠杆价格指数 (MARKET_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Query-Margin-PriceIndex#接口描述 "接口描述的直接链接")

查询杠杆价格指数

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Query-Margin-PriceIndex#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/priceIndex`

## 请求权重[​](/docs/zh-CN/margin_trading/market-data/Query-Margin-PriceIndex#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Query-Margin-PriceIndex#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Query-Margin-PriceIndex#响应示例 "响应示例的直接链接")
    
    
    {  
       "calcTime": 1562046418000,  
       "price": "0.00333930",  
       "symbol": "BNBBTC"  
    }