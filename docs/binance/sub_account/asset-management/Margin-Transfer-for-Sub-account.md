---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account
api_type: Account
updated_at: 2026-01-15T23:51:09.067004
---

# Margin Transfer for Sub-account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account#api-description "Direct link to API Description")

Margin Transfer for Sub-account

## HTTP Request[​](/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/margin/transfer`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account#email-address)  
asset| STRING| YES| The asset being transferred, e.g., BTC  
amount| DECIMAL| YES| The amount to be transferred  
type| INT| YES| 1: transfer from subaccount's spot account to margin account 2: transfer from subaccount's margin account to its spot account  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to open Enable Spot & Margin Trading permission for the API Key which requests this endpoint.
> 


## Response Example[​](/docs/sub_account/asset-management/Margin-Transfer-for-Sub-account#response-example "Direct link to Response Example")
    
    
    {  
        "txnId":"2966662589"  
    }

---

# 子账户Margin划转 (仅适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Margin-Transfer-for-Sub-account#接口描述 "接口描述的直接链接")

子账户Margin划转

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Margin-Transfer-for-Sub-account#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/margin/transfer`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Margin-Transfer-for-Sub-account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Margin-Transfer-for-Sub-account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Margin-Transfer-for-Sub-account#request-email-address)  
asset| STRING| YES| 划转资产, e.g., USDT  
amount| DECIMAL| YES| 划转数量  
type| INT| YES| 1: 由子账户的现货账户划转至其杠杆账户; 2: 由子账户的杠杆账户划转至其现货账户  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 您需要打开 API Key 的 Spot & Margin Trading 权限以使用此接口。
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Margin-Transfer-for-Sub-account#响应示例 "响应示例的直接链接")
    
    
    {  
        "txnId":"2966662589"  
    }