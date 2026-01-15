---
exchange: binance
source_url: https://developers.binance.com/docs/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist
api_type: REST
updated_at: 2026-01-15T23:50:06.008648
---

# Get Futures Lead Trading Symbol Whitelist(USER_DATA)

## API Description[​](/docs/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#api-description "Direct link to API Description")

Get Futures Lead Trading Symbol Whitelist

## HTTP Request[​](/docs/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#http-request "Direct link to HTTP Request")

GET `/sapi/v1/copyTrading/futures/leadSymbol`

## Request Weight(IP)[​](/docs/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#request-weightip "Direct link to Request Weight\(IP\)")

**20**

## Request Parameters[​](/docs/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#response-example "Direct link to Response Example")
    
    
    {  
       "code": "000000",  
       "message": "success",  
       "data": [  
         {  
            "symbol": "BTCUSDT",  
            "baseAsset": "BTC",  
            "quoteAsset": "USDT"  
         },  
         {  
            "symbol": "ETHUSDT",  
            "baseAsset": "ETH",  
            "quoteAsset": "USDT"  
         }  
       ],  
    }

---

# 查询带单币种白名单(USER_DATA)

## 接口描述[​](/docs/zh-CN/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#接口描述 "接口描述的直接链接")

查询带单币种白名单

## HTTP请求[​](/docs/zh-CN/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/copyTrading/futures/leadSymbol` 

## 请求权重(IP)[​](/docs/zh-CN/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#请求权重ip "请求权重\(IP\)的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/copy_trading/future-copy-trading/Get-Futures-Lead-Trading-Symbol-Whitelist#响应示例 "响应示例的直接链接")
    
    
    {  
       "code": "000000",  
       "message": "success",  
       "data": [  
         {  
            "symbol": "BTCUSDT",  
            "baseAsset": "BTC",  
            "quoteAsset": "USDT"  
         },  
         {  
            "symbol": "ETHUSDT",  
            "baseAsset": "ETH",  
            "quoteAsset": "USDT"  
         }  
       ],  
    }