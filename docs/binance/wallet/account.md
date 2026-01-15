---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/account
api_type: Account
updated_at: 2026-01-15T23:49:20.687805
---

# Account info (USER_DATA)

## API Description[​](/docs/wallet/account#api-description "Direct link to API Description")

Fetch account info detail.

## HTTP Request[​](/docs/wallet/account#http-request "Direct link to HTTP Request")

GET `/sapi/v1/account/info`

## Request Weight(IP)[​](/docs/wallet/account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/account#response-example "Direct link to Response Example")
    
    
    {  
      "vipLevel": 0,  
      "isMarginEnabled": true,     // true or false for margin.  
      "isFutureEnabled": true,      // true or false for futures.  
      "isOptionsEnabled":true,      // true or false for options.  
      "isPortfolioMarginRetailEnabled":true      // true or false for portfolio margin retail.  
    }

---

# 帐户信息(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/account#接口描述 "接口描述的直接链接")

获取帐户信息详情。

## HTTP请求[​](/docs/zh-CN/wallet/account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/account/info`

## 请求权重(IP)[​](/docs/zh-CN/wallet/account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/account#响应示例 "响应示例的直接链接")
    
    
    {  
      "vipLevel": 0,  
      "isMarginEnabled": true,      
      "isFutureEnabled": true,  
      "isOptionsEnabled":true,  
      "isPortfolioMarginRetailEnabled":true  
    }