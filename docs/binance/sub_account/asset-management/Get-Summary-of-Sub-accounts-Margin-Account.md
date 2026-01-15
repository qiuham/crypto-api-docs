---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account
api_type: Account
updated_at: 2026-01-15T23:51:09.007521
---

# Get Summary of Sub-account's Margin Account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#api-description "Direct link to API Description")

Get Summary of Sub-account's Margin Account

## HTTP Request[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/margin/accountSummary`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#response-example "Direct link to Response Example")
    
    
    {  
        "totalAssetOfBtc": "4.33333333",   
        "totalLiabilityOfBtc": "2.11111112",   
        "totalNetAssetOfBtc": "2.22222221",  
        "subAccountList":[  
            {  
                "email":"123@test.com",  
                "totalAssetOfBtc": "2.11111111",  
                "totalLiabilityOfBtc": "1.11111111",  
                "totalNetAssetOfBtc": "1.00000000"  
            },  
            {   
                "email":"345@test.com",  
                "totalAssetOfBtc": "2.22222222",   
                "totalLiabilityOfBtc": "1.00000001",   
                "totalNetAssetOfBtc": "1.22222221"  
            }  
        ]  
    }

---

# 查询子账户Margin账户汇总 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#接口描述 "接口描述的直接链接")

查询子账户Margin账户汇总

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/margin/accountSummary`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Summary-of-Sub-accounts-Margin-Account#响应示例 "响应示例的直接链接")
    
    
    {  
        "totalAssetOfBtc": "4.33333333",   
        "totalLiabilityOfBtc": "2.11111112",   
        "totalNetAssetOfBtc": "2.22222221",  
        "subAccountList":[  
            {  
                "email":"123@test.com",  
                "totalAssetOfBtc": "2.11111111",  
                "totalLiabilityOfBtc": "1.11111111",  
                "totalNetAssetOfBtc": "1.00000000"  
            },  
            {   
                "email":"345@test.com",  
                "totalAssetOfBtc": "2.22222222",   
                "totalLiabilityOfBtc": "1.00000001",   
                "totalNetAssetOfBtc": "1.22222221"  
            }  
        ]  
    }