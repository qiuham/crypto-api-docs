---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/account-management/Query-Sub-account-List
api_type: Account
updated_at: 2026-01-15T23:50:55.034122
---

# Query Sub-account List (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/account-management/Query-Sub-account-List#api-description "Direct link to API Description")

Query Sub-account List

## HTTP Request[​](/docs/sub_account/account-management/Query-Sub-account-List#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/list`

## Request Weight(IP)[​](/docs/sub_account/account-management/Query-Sub-account-List#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/account-management/Query-Sub-account-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| NO| [Sub-account email](/docs/sub_account/account-management/Query-Sub-account-List#email-address)  
isFreeze| STRING| NO| true or false  
page| INT| NO| Default value: 1  
limit| INT| NO| Default value: 1, Max value: 200  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/account-management/Query-Sub-account-List#response-example "Direct link to Response Example")
    
    
    {  
        "subAccounts":[  
            {  
                "subUserId": 123456,  
                "email":"testsub@gmail.com",  
                "remark": "remark",  
                "isFreeze":false,  
                "createTime":1544433328000,  
                "isManagedSubAccount": false,  
                "isAssetManagementSubAccount": false  
            },  
            {  
                "subUserId": 1234567,  
                "email":"virtual@oxebmvfonoemail.com",  
                "remark": "remarks",  
                "isFreeze":false,  
                "createTime":1544433328000,  
                "isManagedSubAccount": false,  
                "isAssetManagementSubAccount": false  
            }  
        ]  
    }

---

# 查询子账户列表 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-List#接口描述 "接口描述的直接链接")

查询子账户列表(适用主账户)

## HTTP请求[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-List#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/list `

## 请求权重(IP)[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-List#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-List#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| NO| [Sub-account email](/docs/zh-CN/sub_account/account-management/Query-Sub-account-List#email-address)  
isFreeze| STRING| NO| true or false  
page| INT| NO| 默认: 1  
limit| INT| NO| 默认: 1, 最大: 200  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/account-management/Query-Sub-account-List#响应示例 "响应示例的直接链接")
    
    
    {  
        "subAccounts":[  
            {  
                "subUserId": 123456,  
                "email":"testsub@gmail.com",  
                "remark": "remark",  
                "isFreeze":false,  
                "createTime":1544433328000,  
                "isManagedSubAccount": false,  
                "isAssetManagementSubAccount": false  
            },  
            {  
                "subUserId": 1234567,  
                "email":"virtual@oxebmvfonoemail.com",  
                "remark": "remarks",  
                "isFreeze":false,  
                "createTime":1544433328000,  
                "isManagedSubAccount": false,  
                "isAssetManagementSubAccount": false  
            }  
        ]  
    }