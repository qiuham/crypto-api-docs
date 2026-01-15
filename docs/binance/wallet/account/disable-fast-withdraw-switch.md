---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/account/disable-fast-withdraw-switch
api_type: Account
updated_at: 2026-01-15T23:49:23.202148
---

# Disable Fast Withdraw Switch (USER_DATA)

## HTTP Request[​](/docs/wallet/account/disable-fast-withdraw-switch#http-request "Direct link to HTTP Request")

POST `/sapi/v1/account/disableFastWithdrawSwitch`

## Request Weight(IP)[​](/docs/wallet/account/disable-fast-withdraw-switch#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/account/disable-fast-withdraw-switch#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * **Caution:**

This request will disable fastwithdraw switch under your account.   
  
You need to enable "trade" option for the api key which requests this endpoint.




## Response Example[​](/docs/wallet/account/disable-fast-withdraw-switch#response-example "Direct link to Response Example")
    
    
    {}

---

# 关闭站内划转(USER_DATA)

关闭站内划转

## HTTP请求[​](/docs/zh-CN/wallet/account/disable-fast-withdraw-switch#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/account/disableFastWithdrawSwitch`

## 请求权重(IP)[​](/docs/zh-CN/wallet/account/disable-fast-withdraw-switch#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/account/disable-fast-withdraw-switch#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * **注意:**
        
        此请求会关闭您账户的站内快速划转。您需要为api-key开通"trade"权限才能发送此请求。  
        




## 响应示例[​](/docs/zh-CN/wallet/account/disable-fast-withdraw-switch#响应示例 "响应示例的直接链接")
    
    
    {}