---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/dust-transfer
api_type: REST
updated_at: 2026-01-15T23:49:30.415813
---

# Dust Transfer (USER_DATA)

## API Description[​](/docs/wallet/asset/dust-transfer#api-description "Direct link to API Description")

Convert dust assets to BNB.

## HTTP Request[​](/docs/wallet/asset/dust-transfer#http-request "Direct link to HTTP Request")

POST `/sapi/v1/asset/dust`

## Request Weight(UID)[​](/docs/wallet/asset/dust-transfer#request-weightuid "Direct link to Request Weight\(UID\)")

**10**

## Request Parameters[​](/docs/wallet/asset/dust-transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| ARRAY| YES| The asset being converted. For example: asset=BTC,USDT  
accountType| STRING| NO| `SPOT` or `MARGIN`,default `SPOT`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to open`Enable Spot & Margin Trading` permission for the API Key which requests this endpoint.
> 


## Response Example[​](/docs/wallet/asset/dust-transfer#response-example "Direct link to Response Example")
    
    
    {  
        "totalServiceCharge":"0.02102542",  
        "totalTransfered":"1.05127099",  
        "transferResult":[  
            {  
                "amount":"0.03000000",  
                "fromAsset":"ETH",  
                "operateTime":1563368549307,  
                "serviceChargeAmount":"0.00500000",  
                "tranId":2970932918,  
                "transferedAmount":"0.25000000"  
            },  
            {  
                "amount":"0.09000000",  
                "fromAsset":"LTC",  
                "operateTime":1563368549404,  
                "serviceChargeAmount":"0.01548000",  
                "tranId":2970932918,  
                "transferedAmount":"0.77400000"  
            },  
            {  
                "amount":"248.61878453",  
                "fromAsset":"TRX",  
                "operateTime":1563368549489,  
                "serviceChargeAmount":"0.00054542",  
                "tranId":2970932918,  
                "transferedAmount":"0.02727099"  
            }  
        ]  
    }

---

# 小额资产转换(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/dust-transfer#接口描述 "接口描述的直接链接")

小额资产转换

## HTTP请求[​](/docs/zh-CN/wallet/asset/dust-transfer#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/asset/dust`

## 请求权重(UID)[​](/docs/zh-CN/wallet/asset/dust-transfer#请求权重uid "请求权重\(UID\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/wallet/asset/dust-transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| ARRAY| YES| 正在转换的资产。 例如：asset=BTC,USDT  
accountType| STRING| NO| `SPOT`或`MARGIN`,默认`SPOT`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 您需要为API Key开通`允许现货和杠杆交易`权限才能发送此请求
> 


## 响应示例[​](/docs/zh-CN/wallet/asset/dust-transfer#响应示例 "响应示例的直接链接")
    
    
    {  
        "totalServiceCharge":"0.02102542",  
        "totalTransfered":"1.05127099",  
        "transferResult":[  
            {  
                "amount":"0.03000000",  
                "fromAsset":"ETH",  
                "operateTime":1563368549307,  
                "serviceChargeAmount":"0.00500000",  
                "tranId":2970932918,  
                "transferedAmount":"0.25000000"  
            },  
            {  
                "amount":"0.09000000",  
                "fromAsset":"LTC",  
                "operateTime":1563368549404,  
                "serviceChargeAmount":"0.01548000",  
                "tranId":2970932918,  
                "transferedAmount":"0.77400000"  
            },  
            {  
                "amount":"248.61878453",  
                "fromAsset":"TRX",  
                "operateTime":1563368549489,  
                "serviceChargeAmount":"0.00054542",  
                "tranId":2970932918,  
                "transferedAmount":"0.02727099"  
            }  
        ]  
    }