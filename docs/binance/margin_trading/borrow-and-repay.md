---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/borrow-and-repay
api_type: REST
updated_at: 2026-01-15T23:48:21.877370
---

# Get future hourly interest rate (USER_DATA)

## API Description[​](/docs/margin_trading/borrow-and-repay#api-description "Direct link to API Description")

Get future hourly interest rate

## HTTP Request[​](/docs/margin_trading/borrow-and-repay#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/next-hourly-interest-rate`

## Request Weight(IP)[​](/docs/margin_trading/borrow-and-repay#request-weightip "Direct link to Request Weight\(IP\)")

**100**

## Request Parameters[​](/docs/margin_trading/borrow-and-repay#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
assets| String| YES| List of assets, separated by commas, up to 20  
isIsolated| Boolean| YES| for isolated margin or not, "TRUE", "FALSE"  
  
## Response Example[​](/docs/margin_trading/borrow-and-repay#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "asset": "BTC",  
            "nextHourlyInterestRate": "0.00000571"  
        },  
        {  
            "asset": "ETH",  
            "nextHourlyInterestRate": "0.00000578"  
        }  
    ]

---

# 查询下小时预估利率 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/borrow-and-repay#接口描述 "接口描述的直接链接")

查询用户币种下小时预估利率

## HTTP请求[​](/docs/zh-CN/margin_trading/borrow-and-repay#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/next-hourly-interest-rate`

## 请求权重(IP)[​](/docs/zh-CN/margin_trading/borrow-and-repay#请求权重ip "请求权重\(IP\)的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/margin_trading/borrow-and-repay#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
assets| String| YES| 资产列表，以逗号分隔，最多20个  
isIsolated| Boolean| YES| 是否逐仓杠杆，"TRUE", "FALSE"  
  
## 响应示例[​](/docs/zh-CN/margin_trading/borrow-and-repay#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "asset": "BTC",  
            "nextHourlyInterestRate": "0.00000571"  
        },  
        {  
            "asset": "ETH",  
            "nextHourlyInterestRate": "0.00000578"  
        }  
    ]