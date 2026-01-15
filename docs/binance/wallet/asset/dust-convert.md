---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/dust-convert
api_type: REST
updated_at: 2026-01-15T23:49:27.260538
---

# Dust Convert (USER_DATA)

## API Description[​](/docs/wallet/asset/dust-convert#api-description "Direct link to API Description")

Convert dust assets

## HTTP Request[​](/docs/wallet/asset/dust-convert#http-request "Direct link to HTTP Request")

POST `/sapi/v1/asset/dust-convert/convert`

## Request Weight(UID)[​](/docs/wallet/asset/dust-convert#request-weightuid "Direct link to Request Weight\(UID\)")

**10**

## Request Parameters[​](/docs/wallet/asset/dust-convert#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| ARRAY| YES|   
clientId| STRING| NO| A unique id for the request  
targetAsset| STRING| NO|   
thirdPartyClientId| STRING| NO|   
dustQuotaAssetToTargetAssetPrice| BIGDECIMAL| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/asset/dust-convert#response-example "Direct link to Response Example")
    
    
    {  
        "totalTransfered": "3.5971223",  
        "totalServiceCharge": "0.0794964",  
        "transferResult": [  
            {  
                "tranId": 2987331510,  
                "fromAsset": "USDT",  
                "amount": "1",  
                "transferedAmount": "3.5971223",  
                "serviceChargeAmount": "0.0794964",  
                "operateTime": 1765212029749  
            }  
        ]  
    }

---

# 小额资产兑换(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/dust-convert#接口描述 "接口描述的直接链接")

小额兑换

## HTTP请求[​](/docs/zh-CN/wallet/asset/dust-convert#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/asset/dust-convert/convert`

## 请求权重(UID)[​](/docs/zh-CN/wallet/asset/dust-convert#请求权重uid "请求权重\(UID\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/wallet/asset/dust-convert#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| ARRAY| YES|   
clientId| STRING| NO| 用户自定义的请求号 ｜  
targetAsset| STRING| NO|   
thirdPartyClientId| STRING| NO|   
dustQuotaAssetToTargetAssetPrice| BIGDECIMAL| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/asset/dust-convert#响应示例 "响应示例的直接链接")
    
    
    {  
        "totalTransfered": "3.5971223",  
        "totalServiceCharge": "0.0794964",  
        "transferResult": [  
            {  
                "tranId": 2987331510,  
                "fromAsset": "USDT",  
                "amount": "1",  
                "transferedAmount": "3.5971223",  
                "serviceChargeAmount": "0.0794964",  
                "operateTime": 1765212029749  
            }  
        ]  
    }