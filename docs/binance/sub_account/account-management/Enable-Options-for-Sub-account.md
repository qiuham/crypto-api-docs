---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/account-management/Enable-Options-for-Sub-account
api_type: Account
updated_at: 2026-01-15T23:50:52.277071
---

# Enable Options for Sub-account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/account-management/Enable-Options-for-Sub-account#api-description "Direct link to API Description")

Enable Options for Sub-account (For Master Account).

## HTTP Request[​](/docs/sub_account/account-management/Enable-Options-for-Sub-account#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/eoptions/enable`

## Request Weight(IP)[​](/docs/sub_account/account-management/Enable-Options-for-Sub-account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/account-management/Enable-Options-for-Sub-account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Sub user email  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/account-management/Enable-Options-for-Sub-account#response-example "Direct link to Response Example")
    
    
    {  
      
        "email":"123@test.com",  
        "isEOptionsEnabled": true  // true or false  
    }

---

# 为子账户开通期权 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/account-management/Enable-Options-for-Sub-account#接口描述 "接口描述的直接链接")

为子账户开通期权 (适用主账户)

## HTTP请求[​](/docs/zh-CN/sub_account/account-management/Enable-Options-for-Sub-account#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/eoptions/enable`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/account-management/Enable-Options-for-Sub-account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/account-management/Enable-Options-for-Sub-account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 托管子账户邮箱  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/account-management/Enable-Options-for-Sub-account#响应示例 "响应示例的直接链接")
    
    
    {  
        "email":"123@test.com",  
        "isEOptionsEnabled": true  // true or false  
    }