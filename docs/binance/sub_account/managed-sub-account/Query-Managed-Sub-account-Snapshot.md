---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot
api_type: Account
updated_at: 2026-01-15T23:51:32.266874
---

# Query Managed Sub-account Snapshot (For Investor Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#api-description "Direct link to API Description")

Query Managed Sub-account Snapshot

## HTTP Request[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#http-request "Direct link to HTTP Request")

GET `/sapi/v1/managed-subaccount/accountSnapshot`

## Request Weight(IP)[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#request-weightip "Direct link to Request Weight\(IP\)")

**2400**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES|   
type| STRING| YES| "SPOT", "MARGIN"（cross）, "FUTURES"（UM）  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| min 7, max 30, default 7  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * The query time period must be less then 30 days
>   * Support query within the last one month only
>   * If startTimeand endTime not sent, return records of the last 7 days by default
> 


## Response Example[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#response-example "Direct link to Response Example")
    
    
    {  
       "code":200, // 200 for success; others are error codes  
       "msg":"", // error message  
       "snapshotVos":[  
          {  
             "data":{  
                "balances":[  
                   {  
                      "asset":"BTC",  
                      "free":"0.09905021",  
                      "locked":"0.00000000"  
                   },  
                   {  
                      "asset":"USDT",  
                      "free":"1.89109409",  
                      "locked":"0.00000000"  
                   }  
                ],  
                "totalAssetOfBtc":"0.09942700"  
             },  
             "type":"spot",  
             "updateTime":1576281599000  
          }  
       ]  
    }  
    

> OR
    
    
    {  
       "code":200, // 200 for success; others are error codes  
       "msg":"", // error message  
       "snapshotVos":[  
          {  
             "data":{  
                "marginLevel":"2748.02909813",  
                "totalAssetOfBtc":"0.00274803",  
                "totalLiabilityOfBtc":"0.00000100",  
                "totalNetAssetOfBtc":"0.00274750",  
                "userAssets":[  
                   {  
                      "asset":"XRP",  
                      "borrowed":"0.00000000",  
                      "free":"1.00000000",  
                      "interest":"0.00000000",  
                      "locked":"0.00000000",  
                      "netAsset":"1.00000000"  
                   }  
                ]  
             },  
             "type":"margin",  
             "updateTime":1576281599000  
          }  
       ]  
    }  
    

> OR
    
    
    {  
       "code":200, // 200 for success; others are error codes  
       "msg":"", // error message  
       "snapshotVos":[  
          {  
             "data":{  
                "assets":[  
                   {  
                      "asset":"USDT",  
                      "marginBalance":"118.99782335",  
                      "walletBalance":"120.23811389"  
                   }  
                ],  
                "position":[  
                   {  
                      "entryPrice":"7130.41000000",  
                      "markPrice":"7257.66239673",  
                      "positionAmt":"0.01000000",  
                      "symbol":"BTCUSDT",  
                      "unRealizedProfit":"1.24029054"  // Only show the value at the time of opening the position  
                   }  
                ]  
             },  
             "type":"futures",  
             "updateTime":1576281599000  
          }  
       ]  
    }

---

# 查询托管子账户资产快照 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#接口描述 "接口描述的直接链接")

查询托管子账户资产快照

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/accountSnapshot`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#请求权重ip "请求权重\(IP\)的直接链接")

**2400**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES|   
type| STRING| YES| "SPOT"（现货）, "MARGIN"（全仓）, "FUTURES"（U本位合约）  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO| min 7, max 30, default 7  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 查询时间范围最大不得超过30天
>   * 仅支持查询最近 1 个月数据
>   * 若startTime和endTime没传，则默认返回最近7天数据
> 


## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Snapshot#响应示例 "响应示例的直接链接")
    
    
    {  
       "code":200, // 200表示返回正确，否则即为错误码  
       "msg":"", // 与错误码对应的报错信息  
       "snapshotVos":[  
          {  
             "data":{  
                "balances":[  
                   {  
                      "asset":"BTC",  
                      "free":"0.09905021",  
                      "locked":"0.00000000"  
                   },  
                   {  
                      "asset":"USDT",  
                      "free":"1.89109409",  
                      "locked":"0.00000000"  
                   }  
                ],  
                "totalAssetOfBtc":"0.09942700"  
             },  
             "type":"spot",  
             "updateTime":1576281599000  
          }  
       ]  
    }  
    

> 或
    
    
    {  
       "code":200, // 200表示返回正确，否则即为错误码  
       "msg":"", // 与错误码对应的报错信息  
       "snapshotVos":[  
          {  
             "data":{  
                "marginLevel":"2748.02909813",  
                "totalAssetOfBtc":"0.00274803",  
                "totalLiabilityOfBtc":"0.00000100",  
                "totalNetAssetOfBtc":"0.00274750",  
                "userAssets":[  
                   {  
                      "asset":"XRP",  
                      "borrowed":"0.00000000",  
                      "free":"1.00000000",  
                      "interest":"0.00000000",  
                      "locked":"0.00000000",  
                      "netAsset":"1.00000000"  
                   }  
                ]  
             },  
             "type":"margin",  
             "updateTime":1576281599000  
          }  
       ]  
    }  
    

> 或
    
    
    {  
       "code":200, // 200表示返回正确，否则即为错误码  
       "msg":"", // 与错误码对应的报错信息  
       "snapshotVos":[  
          {  
             "data":{  
                "assets":[  
                   {  
                      "asset":"USDT",  
                      "marginBalance":"118.99782335",  
                      "walletBalance":"120.23811389"  
                   }  
                ],  
                "position":[  
                   {  
                      "entryPrice":"7130.41000000",  
                      "markPrice":"7257.66239673",  
                      "positionAmt":"0.01000000",  
                      "symbol":"BTCUSDT",  
                      "unRealizedProfit":"1.24029054" //只显示开仓当时的未实现盈亏，不会实时更新，可以忽略  
                   }  
                ]  
             },  
             "type":"futures",  
             "updateTime":1576281599000  
          }  
       ]  
    }