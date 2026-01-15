---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data
api_type: Market Data
updated_at: 2026-01-15T23:48:33.843618
---

# Query Isolated Margin Tier Data (USER_DATA)

## API Description[​](/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#api-description "Direct link to API Description")

Get isolated margin tier data collection with any tier as <https://www.binance.com/en/margin-data>

## HTTP Request[​](/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/isolatedMarginTier`

## Request Weight[​](/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
tier| INTEGER| NO| All margin tier data will be returned if tier is omitted  
recvWindow| LONG| NO| No more than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "tier": 1,  
            "effectiveMultiple": "10",  
            "initialRiskRatio": "1.111",  
            "liquidationRiskRatio": "1.05",  
            "baseAssetMaxBorrowable": "9",  
            "quoteAssetMaxBorrowable": "70000"  
        }  
    ]

---

# 获取逐仓档位信息 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#接口描述 "接口描述的直接链接")

通过档位获取逐仓杠杆档位数据， 如： <https://www.binance.com/en/margin-data>

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/isolatedMarginTier`

## 请求权重[​](/docs/zh-CN/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
symbol| STRING| YES|   
tier| INTEGER| NO| 不传则返回所有逐仓杠杆档位  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Query-Isolated-Margin-Tier-Data#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "tier": 1,  
            "effectiveMultiple": "10",  
            "initialRiskRatio": "1.111",  
            "liquidationRiskRatio": "1.05",  
            "baseAssetMaxBorrowable": "9",  
            "quoteAssetMaxBorrowable": "70000"  
        }  
    ]