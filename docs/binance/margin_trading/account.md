---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account
api_type: Account
updated_at: 2026-01-15T23:48:14.289506
---

# Adjust cross margin max leverage (USER_DATA)

## API Description[​](/docs/margin_trading/account#api-description "Direct link to API Description")

Adjust cross margin max leverage

## HTTP Request[​](/docs/margin_trading/account#http-request "Direct link to HTTP Request")

POST `/sapi/v1/margin/max-leverage`

## Request Weight(UID)[​](/docs/margin_trading/account#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Limit[​](/docs/margin_trading/account#request-limit "Direct link to Request Limit")

1 times/min per IP

## Request Parameters[​](/docs/margin_trading/account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
maxLeverage| Integer| YES| Can only adjust 3 , 5 or 10，Example: maxLeverage = 5 or 3 for Cross Margin Classic; maxLeverage=10 for Cross Margin Pro 10x leverage or 20x if compliance allows.  
  
  * The margin level need higher than the initial risk ratio of adjusted leverage, the initial risk ratio of 3x is 1.5 , the initial risk ratio of 5x is 1.25; The detail conditions on how to switch between Cross Margin Classic and Cross Margin Pro can refer to [the FAQ](https://www.binance.com/en/support/faq/how-to-activate-the-cross-margin-pro-mode-on-binance-e27786da05e743a694b8c625b3bc475d).



## Response Example[​](/docs/margin_trading/account#response-example "Direct link to Response Example")
    
    
    {  
        "success": true  
    }

---

# 调整全仓最大杠杆 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account#接口描述 "接口描述的直接链接")

调整全仓最大杠杆倍数

## HTTP请求[​](/docs/zh-CN/margin_trading/account#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/margin/max-leverage`

## 请求权重(UID)[​](/docs/zh-CN/margin_trading/account#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

**访问限制**

1次/分钟/IP

## 请求参数[​](/docs/zh-CN/margin_trading/account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
maxLeverage| Integer| YES| 只能调整3, 5 , 或者 10。举例: maxLeverage = 5 或者3是选择全仓Classic模式； maxLeverage=10 是选择切换成全仓 Pro 模式下的10倍杠杆 或者 20倍杠杆（在合规允许的情况下）。  
  
  * 当前的风险率需要大于调整后的初始风险率，3x的初始风险率是1.5，5x的初始风险率是1.25，关于在Classic模式(3x, 5x) 和Pro模式(10x, 20x)之间的切换条件请参考[FAQ](https://www.binance.com/zh-CN/support/faq/%E5%A6%82%E4%BD%95%E5%9C%A8%E5%B8%81%E5%AE%89%E5%BC%80%E9%80%9A%E5%85%A8%E4%BB%93%E6%9D%A0%E6%9D%86%E4%B8%93%E4%B8%9A%E6%A8%A1%E5%BC%8F-e27786da05e743a694b8c625b3bc475d)。



## 响应示例[​](/docs/zh-CN/margin_trading/account#响应示例 "响应示例的直接链接")
    
    
    {  
        "success": true  
    }