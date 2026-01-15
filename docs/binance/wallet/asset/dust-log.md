---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/dust-log
api_type: REST
updated_at: 2026-01-15T23:49:30.350420
---

# DustLog(USER_DATA)

## API Description[​](/docs/wallet/asset/dust-log#api-description "Direct link to API Description")

Dustlog

## HTTP Request[​](/docs/wallet/asset/dust-log#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/dribblet`

## Request Weight(IP)[​](/docs/wallet/asset/dust-log#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/asset/dust-log#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| NO|   
endTime| LONG| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Only return last 100 records
>   * Only return records after 2020/12/01
> 


## Response Example[​](/docs/wallet/asset/dust-log#response-example "Direct link to Response Example")
    
    
    {  
            "total": 8,   //Total counts of exchange  
            "userAssetDribblets": [  
                {  
                    "operateTime": 1615985535000,  
                    "totalTransferedAmount": "0.00132256",   // Total transfered BNB amount for this exchange.  
                    "totalServiceChargeAmount": "0.00002699",    //Total service charge amount for this exchange.  
                    "transId": 45178372831,  
                    "userAssetDribbletDetails": [           //Details of  this exchange.  
                        {  
                            "transId": 4359321,  
                            "serviceChargeAmount": "0.000009",  
                            "amount": "0.0009",  
                            "operateTime": 1615985535000,  
                            "transferedAmount": "0.000441",  
                            "fromAsset": "USDT"  
                        },  
                        {  
                            "transId": 4359321,  
                            "serviceChargeAmount": "0.00001799",  
                            "amount": "0.0009",  
                            "operateTime": 1615985535000,  
                            "transferedAmount": "0.00088156",  
                            "fromAsset": "ETH"  
                        }  
                    ]  
                },  
                {  
                    "operateTime":1616203180000,  
                    "totalTransferedAmount": "0.00058795",  
                    "totalServiceChargeAmount": "0.000012",  
                    "transId": 4357015,  
                    "userAssetDribbletDetails": [         
                        {  
                            "transId": 4357015,  
                            "serviceChargeAmount": "0.00001",  
                            "amount": "0.001",  
                            "operateTime": 1616203180000,  
                            "transferedAmount": "0.00049",  
                            "fromAsset": "USDT"  
                        },  
                        {  
                            "transId": 4357015,  
                            "serviceChargeAmount": "0.000002",           
                            "amount": "0.0001",  
                            "operateTime": 1616203180000,  
                            "transferedAmount": "0.00009795",  
                            "fromAsset": "ETH"  
                        }  
                    ]  
                }  
            ]  
    }

---

# 小额资产转换BNB历史(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/dust-log#接口描述 "接口描述的直接链接")

小额资产转换BNB历史(USER_DATA)

## HTTP请求[​](/docs/zh-CN/wallet/asset/dust-log#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/dribblet`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/dust-log#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/asset/dust-log#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
accountType| STRING| NO| `SPOT`或`MARGIN`,默认`SPOT`  
startTime| LONG| NO|   
endTime| LONG| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 只返回最近100条记录
>   * 只返回 2020/12/01 之后记录
> 


## 响应示例[​](/docs/zh-CN/wallet/asset/dust-log#响应示例 "响应示例的直接链接")
    
    
    {  
            "total": 8,   //共计发生过的转换笔数  
            "userAssetDribblets": [  
                {  
                    "operateTime": 1615985535000,  
                    "totalTransferedAmount": "0.00132256",   //本次转换所得BNB  
                    "totalServiceChargeAmount": "0.00002699",   //本次转换手续费(BNB)  
                    "transId": 45178372831,  
                    "userAssetDribbletDetails": [           //本次转换的细节  
                        {  
                            "transId": 4359321,  
                            "serviceChargeAmount": "0.000009",  
                            "amount": "0.0009",  
                            "operateTime": 1615985535000,  
                            "transferedAmount": "0.000441",  
                            "fromAsset": "USDT"  
                        },  
                        {  
                            "transId": 4359321,  
                            "serviceChargeAmount": "0.00001799",  
                            "amount": "0.0009",  
                            "operateTime": 1615985535000,  
                            "transferedAmount": "0.00088156",  
                            "fromAsset": "ETH"  
                        }  
                    ]  
                },  
                {  
                    "operateTime":1616203180000,  
                    "totalTransferedAmount": "0.00058795",  
                    "totalServiceChargeAmount": "0.000012",  
                    "transId": 4357015,  
                    "userAssetDribbletDetails": [         
                        {  
                            "transId": 4357015,  
                            "serviceChargeAmount": "0.00001"  
                            "amount": "0.001",  
                            "operateTime": 1616203180000,  
                            "transferedAmount": "0.00049",  
                            "fromAsset": "USDT"  
                        },  
                        {  
                            "transId": 4357015,  
                            "serviceChargeAmount": "0.000002"           
                            "amount": "0.0001",  
                            "operateTime": 1616203180000,  
                            "transferedAmount": "0.00009795",  
                            "fromAsset": "ETH"  
                        }  
                    ]  
                }  
            ]  
    }