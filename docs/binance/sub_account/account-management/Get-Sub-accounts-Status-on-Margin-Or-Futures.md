---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures
api_type: Account
updated_at: 2026-01-15T23:50:54.974412
---

# Get Sub-account's Status on Margin Or Futures (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#api-description "Direct link to API Description")

Get Sub-account's Status on Margin Or Futures

## HTTP Request[​](/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/status`

## Request Weight(IP)[​](/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| NO| [Sub-account email](/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#email-address)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If no email sent, all sub-accounts' information will be returned.
> 


## Response Example[​](/docs/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "email":"123@test.com",      // user email  
            "isSubUserEnabled": true,  	 // true or false  
            "isUserActive": true, 		 // true or false  
            "insertTime": 1570791523523,  // sub account create time  
            "isMarginEnabled": true,     // true or false for margin  
            "isFutureEnabled": true,      // true or false for futures.  
            "mobile": 1570791523523   	 // user mobile number  
        }  
    ]

---

# 查询子账户Margin/Futures状态 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#接口描述 "接口描述的直接链接")

查询子账户Margin/Futures状态

## HTTP请求[​](/docs/zh-CN/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/status`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| NO| 子账户邮箱 [备注](/docs/zh-CN/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#request-email-address)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果不提交子账户email，返回所有子账户情况。
> 


## 响应示例[​](/docs/zh-CN/sub_account/account-management/Get-Sub-accounts-Status-on-Margin-Or-Futures#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "email":"123@test.com",      // user email  
            "isSubUserEnabled": true,  	 // true or false  
            "isUserActive": true, 		 // true or false  
            "insertTime": 1570791523523,  // sub account create time  
            "isMarginEnabled": true,     // true or false for margin  
            "isFutureEnabled": true,      // true or false for futures.  
            "mobile": 1570791523523   	 // user mobile number  
        }  
    ]