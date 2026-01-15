---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Assets-V4
api_type: Account
updated_at: 2026-01-15T23:51:13.203419
---

# Query Sub-account Assets (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Query-Sub-account-Assets-V4#api-description "Direct link to API Description")

Fetch sub-account assets

## HTTP Request[​](/docs/sub_account/asset-management/Query-Sub-account-Assets-V4#http-request "Direct link to HTTP Request")

GET `/sapi/v4/sub-account/assets`

## Request Weight(UID)[​](/docs/sub_account/asset-management/Query-Sub-account-Assets-V4#request-weightuid "Direct link to Request Weight\(UID\)")

**60**

## Request Parameters[​](/docs/sub_account/asset-management/Query-Sub-account-Assets-V4#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Sub Account Email  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Query-Sub-account-Assets-V4#response-example "Direct link to Response Example")
    
    
    {  
        "balances":[  
            {  
                "freeze":"0",  
                "withdrawing":"0",  
                "asset":"ADA",  
                "free":"10000",  
                "locked":"0"  
            },  
            {  
                "freeze":"0",  
                "withdrawing":"0",  
                "asset":"BNB",  
                "free":"10003",  
                "locked":"0"  
            },  
            {  
                "freeze":"0",  
                "withdrawing":"0",  
                "asset":"BTC",  
                "free":"11467.6399",  
                "locked":"0"  
            }  
        ]  
    }

---

# 查询子账户资产 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Assets-V4#接口描述 "接口描述的直接链接")

获取子账户资产

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Assets-V4#http请求 "HTTP请求的直接链接")

GET `/sapi/v4/sub-account/assets`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Assets-V4#请求权重uid "请求权重\(UID\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Assets-V4#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Assets-V4#响应示例 "响应示例的直接链接")
    
    
    {  
        "balances":[  
            {  
                "freeze":"0",  
                "withdrawing":"0",  
                "asset":"ADA",  
                "free":"10000",  
                "locked":"0"  
            },  
            {  
                "freeze":"0",  
                "withdrawing":"0",  
                "asset":"BNB",  
                "free":"10003",  
                "locked":"0"  
            },  
            {  
                "freeze":"0",  
                "withdrawing":"0",  
                "asset":"BTC",  
                "free":"11467.6399",  
                "locked":"0"  
            }  
        ]  
    }