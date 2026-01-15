---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/account/account-status
api_type: Account
updated_at: 2026-01-15T23:49:20.817367
---

# Account Status (USER_DATA)

## API Description[​](/docs/wallet/account/account-status#api-description "Direct link to API Description")

Fetch account status detail.

## HTTP Request[​](/docs/wallet/account/account-status#http-request "Direct link to HTTP Request")

GET `/sapi/v1/account/status`

## Request Weight(IP)[​](/docs/wallet/account/account-status#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/account/account-status#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/account/account-status#response-example "Direct link to Response Example")
    
    
    {  
        "data": "Normal"  
    }

---

# 账户状态(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/account/account-status#接口描述 "接口描述的直接链接")

账户状态(USER_DATA)

## HTTP请求[​](/docs/zh-CN/wallet/account/account-status#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/account/status`

## 请求权重(IP)[​](/docs/zh-CN/wallet/account/account-status#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/account/account-status#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/account/account-status#响应示例 "响应示例的直接链接")
    
    
    {  
        "data": "Normal"   
    }