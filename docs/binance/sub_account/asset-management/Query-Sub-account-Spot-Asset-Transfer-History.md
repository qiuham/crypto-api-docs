---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History
api_type: Account
updated_at: 2026-01-15T23:51:13.330706
---

# Query Sub-account Spot Asset Transfer History (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#api-description "Direct link to API Description")

Query Sub-account Spot Asset Transfer History

## HTTP Request[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/sub/transfer/history`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromEmail| STRING| NO|   
toEmail| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| NO| Default value: 1  
limit| INT| NO| Default value: 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * fromEmail and toEmail cannot be sent at the same time.
>   * Return fromEmail equal master account email by default.
> 


## Response Example[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "from":"aaa@test.com",  
            "to":"bbb@test.com",  
            "asset":"BTC",  
            "qty":"10",  
            "status": "SUCCESS",  
            "tranId": 6489943656,  
            "time":1544433328000  
        },  
        {  
            "from":"bbb@test.com",  
            "to":"ccc@test.com",  
            "asset":"ETH",  
            "qty":"2",  
            "status": "SUCCESS",  
            "tranId": 6489938713,  
            "time":1544433328000  
        }  
    ]

---

# 查询子账户现货资金划转历史 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#接口描述 "接口描述的直接链接")

查询子账户现货资金划转历史

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/sub/transfer/history `

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromEmail| STRING| NO|   
toEmail| STRING| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| NO| 默认: 1  
limit| INT| NO| 默认: 500  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * fromEmail 和 toEmail 不可以同时发送
>   * 若 fromEmail 和 toEmail 都未传，默认返回fromEmail 为母账户的记录。
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Asset-Transfer-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "from":"aaa@test.com",  
            "to":"bbb@test.com",  
            "asset":"BTC",  
            "qty":"10",  
            "status": "SUCCESS",  
            "tranId": 6489943656,  
            "time":1544433328000  
        },  
        {  
            "from":"bbb@test.com",  
            "to":"ccc@test.com",  
            "asset":"ETH",  
            "qty":"2",  
            "status": "SUCCESS",  
            "tranId": 6489938713,  
            "time":1544433328000  
        }  
    ]