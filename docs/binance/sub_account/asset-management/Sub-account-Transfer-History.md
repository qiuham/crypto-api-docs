---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Sub-account-Transfer-History
api_type: Account
updated_at: 2026-01-15T23:51:17.523016
---

# Sub-account Transfer History (For Sub-account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Sub-account-Transfer-History#api-description "Direct link to API Description")

Sub-account Transfer History

## HTTP Request[​](/docs/sub_account/asset-management/Sub-account-Transfer-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/transfer/subUserHistory`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Sub-account-Transfer-History#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Sub-account-Transfer-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO| If not sent, result of all assets will be returned  
type| INT| NO| 1: transfer in, 2: transfer out  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| Default 500  
returnFailHistory| BOOLEAN| NO| Default `False`, return PROCESS and SUCCESS status history; If `True`,return PROCESS and SUCCESS and FAILURE status history  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If type is not sent, the records of type 2: transfer out will be returned by default.
>   * If startTime and endTime are not sent, the recent 30-day data will be returned.
> 


## Response Example[​](/docs/sub_account/asset-management/Sub-account-Transfer-History#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "counterParty":"master",  
        "email":"master@test.com",  
        "type":1,  // 1 for transfer in, 2 for transfer out  
        "asset":"BTC",  
        "qty":"1",  
        "fromAccountType":"SPOT",  
        "toAccountType":"SPOT",  
        "status":"SUCCESS", // status: PROCESS / SUCCESS / FAILURE  
        "tranId":11798835829,  
        "time":1544433325000  
      },  
      {  
        "counterParty":"subAccount",  
        "email":"sub2@test.com",  
        "type":1,                                   
        "asset":"ETH",  
        "qty":"2",  
        "fromAccountType":"SPOT",  
        "toAccountType":"COIN_FUTURE",  
        "status":"SUCCESS",  
        "tranId":11798829519,  
        "time":1544433326000  
      }  
    ]

---

# 查询子账户划转历史 (仅适用子账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Transfer-History#接口描述 "接口描述的直接链接")

查询子账户划转历史

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Transfer-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/transfer/subUserHistory`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Transfer-History#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Transfer-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO| 如不提供，返回所有asset 划转记录  
type| INT| NO| 1: transfer in, 2: transfer out; 如不提供，返回transfer out方向划转记录  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| 默认值: 500  
returnFailHistory| BOOLEAN| NO| 默认`False`，返回PROCESS和SUCCESS状态的数据；如果传`True`返回PROCESS、SUCCESS、FAILURE状态的数据  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果 type 均未发送，默认只返回type 2: transfer out 数据.
>   * 如果startTime和endTime均未发送，默认只返回最近30天数据.
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Transfer-History#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "counterParty":"master",  
        "email":"master@test.com",  
        "type":1,  // 1 for transfer in , 2 for transfer out  
        "asset":"BTC",  
        "qty":"1",  
        "fromAccountType":"SPOT",  
        "toAccountType":"SPOT",  
        "status":"SUCCESS", // status: PROCESS / SUCCESS / FAILURE  
        "tranId":11798835829,  
        "time":1544433325000  
      },  
      {  
        "counterParty": "subAccount",  
        "email": "sub2@test.com",  
        "type":  1,                                   
        "asset":"ETH",  
        "qty":"2",  
        "fromAccountType":"SPOT",  
        "toAccountType":"COIN_FUTURE",  
        "status":"SUCCESS",  
        "tranId":11798829519,  
        "time":1544433326000  
      }  
    ]