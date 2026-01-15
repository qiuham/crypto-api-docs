---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/account-management
api_type: Account
updated_at: 2026-01-15T23:50:52.156314
---

# Create a Virtual Sub-account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/account-management#api-description "Direct link to API Description")

Create a Virtual Sub-account

## HTTP Request[​](/docs/sub_account/account-management#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/virtualSubAccount `

## Request Weight(IP)[​](/docs/sub_account/account-management#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/account-management#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
subAccountString| STRING| YES| Please input a string. We will create a virtual email using that string for you to register  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * This request will generate a virtual sub account under your master account.
>   * You need to enable "trade" option for the API Key which requests this endpoint.
> 


## Response Example[​](/docs/sub_account/account-management#response-example "Direct link to Response Example")
    
    
    {  
        "email":"addsdd_virtual@aasaixwqnoemail.com"  
    }

---

# 创建虚拟子账户 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/account-management#接口描述 "接口描述的直接链接")

创建虚拟子账户

## HTTP请求[​](/docs/zh-CN/sub_account/account-management#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/virtualSubAccount`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/account-management#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/account-management#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
subAccountString| STRING| YES| 请输入字符串，我们将为您创建一个虚拟邮箱进行注册  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 该请求会为您的母账户生成一个虚拟子账户
>   * 您需要为母账户apikey开通"允许现货及杠杆交易" 权限调用此接口
> 


## 响应示例[​](/docs/zh-CN/sub_account/account-management#响应示例 "响应示例的直接链接")
    
    
    {  
        "email":"addsdd_virtual@aasaixwqnoemail.com"  
    }