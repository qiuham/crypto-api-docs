---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/account/enable-fast-withdraw-switch
api_type: Account
updated_at: 2026-01-15T23:49:23.260457
---

# Enable Fast Withdraw Switch (USER_DATA)

## API Description[​](/docs/wallet/account/enable-fast-withdraw-switch#api-description "Direct link to API Description")

Enable Fast Withdraw Switch (USER_DATA)

## HTTP Request[​](/docs/wallet/account/enable-fast-withdraw-switch#http-request "Direct link to HTTP Request")

POST `/sapi/v1/account/enableFastWithdrawSwitch`

## Request Weight(IP)[​](/docs/wallet/account/enable-fast-withdraw-switch#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/account/enable-fast-withdraw-switch#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * This request will enable fastwithdraw switch under your account.   
>   
>  You need to enable "trade" option for the api key which requests this endpoint.
>   * When Fast Withdraw Switch is on, transferring funds to a Binance account will be done instantly. There is no on-chain transaction, no transaction ID and no withdrawal fee.
> 


## Response Example[​](/docs/wallet/account/enable-fast-withdraw-switch#response-example "Direct link to Response Example")
    
    
    {}

---

# 开启站内划转(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/account/enable-fast-withdraw-switch#接口描述 "接口描述的直接链接")

开启站内划转(USER_DATA)

## HTTP请求[​](/docs/zh-CN/wallet/account/enable-fast-withdraw-switch#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/account/enableFastWithdrawSwitch`

## 请求权重(IP)[​](/docs/zh-CN/wallet/account/enable-fast-withdraw-switch#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/account/enable-fast-withdraw-switch#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * 此请求会开启您账户的站内快速划转。您需要为api-key开通"trade"权限才能发送此请求。
  * 开启以后, 如果收款方为币安账户地址，转账费用为0, 速度快, 不需要提交上链请求。



## 响应示例[​](/docs/zh-CN/wallet/account/enable-fast-withdraw-switch#响应示例 "响应示例的直接链接")
    
    
    {}