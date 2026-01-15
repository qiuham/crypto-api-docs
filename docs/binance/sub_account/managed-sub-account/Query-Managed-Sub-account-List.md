---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-List
api_type: Account
updated_at: 2026-01-15T23:51:32.117892
---

# Query Managed Sub-account List (For Investor) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-List#api-description "Direct link to API Description")

Get investor's managed sub-account list.

## HTTP Request[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-List#http-request "Direct link to HTTP Request")

GET `/sapi/v1/managed-subaccount/info`

## Request Weight(UID)[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-List#request-weightuid "Direct link to Request Weight\(UID\)")

**60**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| NO| Managed sub-account email  
page| INT| NO| Default value: 1  
limit| INT| NO| Default value: 20, Max value: 20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-List#response-example "Direct link to Response Example")
    
    
    {  
        "total": 3,  
        "managerSubUserInfoVoList": [  
            {  
                "rootUserId": 1000138475670  
                "managersubUserId": 1000137842513  
                "bindParentUserId": 1000138475669  
                "email": "test_0_virtual@kq3kno9imanagedsub.com"  
                "insertTimeStamp": 1678435149000  
                "bindParentEmail": "wdyw8xsh8pey@test.com"  
                "isSubUserEnabled": true  
                "isUserActive": true  
                "isMarginEnabled": false  
                "isFutureEnabled": false  
                "isSignedLVTRiskAgreement": false  
            },  
            {  
                "rootUserId": 1000138475670  
                "managersubUserId": 1000137842514  
                "bindParentUserId": 1000138475669  
                "email": "test_1_virtual@4qd2u7zxmanagedsub.com"  
                "insertTimeStamp": 1678435152000  
                "bindParentEmail": "wdyw8xsh8pey@test.com"  
                "isSubUserEnabled": true  
                "isUserActive": true  
                "isMarginEnabled": false  
                "isFutureEnabled": false  
                "isSignedLVTRiskAgreement": false  
            },  
            {  
                "rootUserId": 1000138475670  
                "managersubUserId": 1000137842515  
                "bindParentUserId": 1000138475669  
                "email": "test_2_virtual@akc05o8hmanagedsub.com"  
                "insertTimeStamp": 1678435153000  
                "bindParentEmail": "wdyw8xsh8pey@test.com"  
                "isSubUserEnabled": true  
                "isUserActive": true  
                "isMarginEnabled": false  
                "isFutureEnabled": false  
                "isSignedLVTRiskAgreement": false  
            }  
        ]  
    }

---

# 查询托管子账户列表 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-List#接口描述 "接口描述的直接链接")

获取投资人之托管子账户列表

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-List#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/info`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-List#请求权重uid "请求权重\(UID\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| NO| 托管子账户邮箱  
page| INT| NO| 默认值: 1  
limit| INT| NO| 默认值: 20, 最大值: 20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-List#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 3,  
        "managerSubUserInfoVoList": [  
            {  
                "rootUserId": 1000138475670,  
                "managersubUserId": 1000137842513,  
                "bindParentUserId": 1000138475669,  
                "email": "test_0_virtual@kq3kno9imanagedsub.com",  
                "insertTimeStamp": 1678435149000,  
                "bindParentEmail": "wdyw8xsh8pey@test.com",  
                "isSubUserEnabled": true,  
                "isUserActive": true,  
                "isMarginEnabled": false,  
                "isFutureEnabled": false,  
                "isSignedLVTRiskAgreement": false  
            },  
            {  
                "rootUserId": 1000138475670,  
                "managersubUserId": 1000137842514,  
                "bindParentUserId": 1000138475669,  
                "email": "test_1_virtual@4qd2u7zxmanagedsub.com",  
                "insertTimeStamp": 1678435152000,  
                "bindParentEmail": "wdyw8xsh8pey@test.com",  
                "isSubUserEnabled": true,  
                "isUserActive": true,  
                "isMarginEnabled": false,  
                "isFutureEnabled": false,  
                "isSignedLVTRiskAgreement": false  
            },  
            {  
                "rootUserId": 1000138475670,  
                "managersubUserId": 1000137842515,  
                "bindParentUserId": 1000138475669,  
                "email": "test_2_virtual@akc05o8hmanagedsub.com",  
                "insertTimeStamp": 1678435153000,  
                "bindParentEmail": "wdyw8xsh8pey@test.com",  
                "isSubUserEnabled": true,  
                "isUserActive": true,  
                "isMarginEnabled": false,  
                "isFutureEnabled": false,  
                "isSignedLVTRiskAgreement": false  
            }  
        ]  
    }