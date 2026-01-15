---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol
api_type: Market Data
updated_at: 2026-01-15T23:48:31.165086
---

# Get All Isolated Margin Symbol(MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#api-description "Direct link to API Description")

Get All Isolated Margin Symbol

## HTTP Request[​](/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/isolated/allPairs`

## Request Weight[​](/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO| No more than 60000  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "base": "BNB",  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "BNBBTC"       
        },  
        {  
            "base": "TRX",  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "TRXBTC"      
        }  
    ]

---

# 获取所有逐仓杠杆交易对(MARKET_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#接口描述 "接口描述的直接链接")

获取所有逐仓杠杆交易对

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/isolated/allPairs`

## 请求权重[​](/docs/zh-CN/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO|   
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Get-All-Isolated-Margin-Symbol#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "base": "BNB",  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "BNBBTC"       
        },  
        {  
            "base": "TRX",  
            "isBuyAllowed": true,  
            "isMarginTrade": true,  
            "isSellAllowed": true,  
            "quote": "BTC",  
            "symbol": "TRXBTC"      
        }  
    ]