---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master
api_type: Account
updated_at: 2026-01-15T23:51:17.728348
---

# Transfer to Sub-account of Same Master (For Sub-account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#api-description "Direct link to API Description")

Transfer to Sub-account of Same Master

## HTTP Request[​](/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/transfer/subToSub`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
toEmail| STRING| YES| [Sub-account email](/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#email-address)  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.
> 


## Response Example[​](/docs/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#response-example "Direct link to Response Example")
    
    
    {  
        "txnId":"2966662589"  
    }

---

# 向共同主账户下的子账户主动划转 (仅适用子账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#接口描述 "接口描述的直接链接")

向共同主账户下的子账户主动划转

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/transfer/subToSub`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
toEmail| STRING| YES| 接收者子邮箱地址 [备注](/docs/zh-CN/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#request-email-address)  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Transfer-to-Sub-account-of-Same-Master#响应示例 "响应示例的直接链接")
    
    
    {  
        "txnId":"2966662589"  
    }