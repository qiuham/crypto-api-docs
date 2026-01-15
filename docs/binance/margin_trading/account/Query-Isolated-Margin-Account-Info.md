---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Query-Isolated-Margin-Account-Info
api_type: Account
updated_at: 2026-01-15T23:48:21.619056
---

# Query Isolated Margin Account Info (USER_DATA)

## API Description[​](/docs/margin_trading/account/Query-Isolated-Margin-Account-Info#api-description "Direct link to API Description")

Query Isolated Margin Account Info

## HTTP Request[​](/docs/margin_trading/account/Query-Isolated-Margin-Account-Info#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/isolated/account`

## Request Weight[​](/docs/margin_trading/account/Query-Isolated-Margin-Account-Info#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/account/Query-Isolated-Margin-Account-Info#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbols| STRING| NO| Max 5 symbols can be sent; separated by ",". e.g. "BTCUSDT,BNBUSDT,ADAUSDT"  
recvWindow| LONG| NO| No more than 60000  
timestamp| LONG| YES|   
  
  * If "symbols" is not sent, all isolated assets will be returned.
  * If "symbols" is sent, only the isolated assets of the sent symbols will be returned.



## Response Example[​](/docs/margin_trading/account/Query-Isolated-Margin-Account-Info#response-example "Direct link to Response Example")

> If "symbols" is not sent
    
    
    {  
       "assets":[  
          {  
            "baseAsset":   
            {  
              "asset": "BTC",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "quoteAsset":   
            {  
              "asset": "USDT",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "symbol": "BTCUSDT",  
            "isolatedCreated": true,   
            "enabled": true, // true-enabled, false-disabled  
            "marginLevel": "0.00000000",   
            "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN_CALL", "PRE_LIQUIDATION", "FORCE_LIQUIDATION"  
            "marginRatio": "0.00000000",  
            "indexPrice": "10000.00000000",  
            "liquidatePrice": "1000.00000000",  
            "liquidateRate": "1.00000000",  
            "tradeEnabled": true  
          }  
        ],  
        "totalAssetOfBtc": "0.00000000",  
        "totalLiabilityOfBtc": "0.00000000",  
        "totalNetAssetOfBtc": "0.00000000"   
    }  
    

> If "symbols" is sent
    
    
    {  
       "assets":[  
          {  
            "baseAsset":   
            {  
              "asset": "BTC",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "quoteAsset":   
            {  
              "asset": "USDT",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "symbol": "BTCUSDT",  
            "isolatedCreated": true,   
            "enabled": true, // true-enabled, false-disabled  
            "marginLevel": "0.00000000",   
            "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN_CALL", "PRE_LIQUIDATION", "FORCE_LIQUIDATION"  
            "marginRatio": "0.00000000",  
            "indexPrice": "10000.00000000",  
            "liquidatePrice": "1000.00000000",  
            "liquidateRate": "1.00000000",  
            "tradeEnabled": true  
          }  
        ]  
    }

---

# 查询杠杆逐仓账户信息 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Account-Info#接口描述 "接口描述的直接链接")

查询杠杆逐仓账户信息

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Account-Info#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/isolated/account`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Account-Info#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Account-Info#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbols| STRING| NO| 最多可以传5个symbol; 由","分隔的字符串表示. e.g. "BTCUSDT,BNBUSDT,ADAUSDT"  
recvWindow| LONG| NO| 赋值不能大于 60000  
timestamp| LONG| YES|   
  
  * 不传"symbols",返回所有杠杆逐仓资产
  * 传"symbols", 将只会返回指定symbol的杠杆逐仓资产



## 响应示例[​](/docs/zh-CN/margin_trading/account/Query-Isolated-Margin-Account-Info#响应示例 "响应示例的直接链接")

> 不传"symbols"的返回内容
    
    
    {  
       "assets":[  
          {  
            "baseAsset":   
              {  
              "asset": "BTC",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "quoteAsset":   
            {  
              "asset": "USDT",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "symbol": "BTCUSDT"  
            "isolatedCreated": true,   
            "enabled": true, // 账户是否启用，true-启用，false-停用  
            "marginLevel": "0.00000000",   
            "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN_CALL", "PRE_LIQUIDATION", "FORCE_LIQUIDATION"  
            "marginRatio": "0.00000000",  
            "indexPrice": "10000.00000000",  
            "liquidatePrice": "1000.00000000",  
            "liquidateRate": "1.00000000",  
            "tradeEnabled": true  
          }  
        ],  
        "totalAssetOfBtc": "0.00000000",  
        "totalLiabilityOfBtc": "0.00000000",  
        "totalNetAssetOfBtc": "0.00000000"   
    }  
    

> 传"symbols"的返回内容
    
    
    {  
       "assets":[  
          {  
            "baseAsset":   
            {  
              "asset": "BTC",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "quoteAsset":   
            {  
              "asset": "USDT",  
              "borrowEnabled": true,  
              "borrowed": "0.00000000",  
              "free": "0.00000000",  
              "interest": "0.00000000",  
              "locked": "0.00000000",  
              "netAsset": "0.00000000",  
              "netAssetOfBtc": "0.00000000",  
              "repayEnabled": true,  
              "totalAsset": "0.00000000"  
            },  
            "symbol": "BTCUSDT"  
            "isolatedCreated": true,   
            "enabled": true, // 账户是否启用，true-启用，false-停用  
            "marginLevel": "0.00000000",   
            "marginLevelStatus": "EXCESSIVE", // "EXCESSIVE", "NORMAL", "MARGIN_CALL", "PRE_LIQUIDATION", "FORCE_LIQUIDATION"  
            "marginRatio": "0.00000000",  
            "indexPrice": "10000.00000000",  
            "liquidatePrice": "1000.00000000",  
            "liquidateRate": "1.00000000",  
            "tradeEnabled": true  
          }  
        ]  
    }