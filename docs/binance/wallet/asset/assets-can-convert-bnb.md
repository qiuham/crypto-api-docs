---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/assets-can-convert-bnb
api_type: REST
updated_at: 2026-01-15T23:49:27.030584
---

# Get Assets That Can Be Converted Into BNB (USER_DATA)

## API Description[​](/docs/wallet/asset/assets-can-convert-bnb#api-description "Direct link to API Description")

Get Assets That Can Be Converted Into BNB

## HTTP Request[​](/docs/wallet/asset/assets-can-convert-bnb#http-request "Direct link to HTTP Request")

POST `/sapi/v1/asset/dust-btc`

## Request Weight(IP)[​](/docs/wallet/asset/assets-can-convert-bnb#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/asset/assets-can-convert-bnb#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
accountType| STRING| NO| `SPOT` or `MARGIN`,default `SPOT`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/asset/assets-can-convert-bnb#response-example "Direct link to Response Example")
    
    
    {  
        "details": [  
            {  
                "asset": "ADA",           
                "assetFullName": "ADA",   
                "amountFree": "6.21",   //Convertible amount  
                "toBTC": "0.00016848",  //BTC amount  
                "toBNB": "0.01777302",  //BNB amount（Not deducted commission fee）  
                "toBNBOffExchange": "0.01741756", //BNB amount（Deducted commission fee）  
                "exchange": "0.00035546" //Commission fee  
            }  
        ],  
        "totalTransferBtc": "0.00016848",  
        "totalTransferBNB": "0.01777302",  
        "dribbletPercentage": "0.02"     //Commission fee  
    }

---

# 获取可以转换成BNB的小额资产 (USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/assets-can-convert-bnb#接口描述 "接口描述的直接链接")

获取可以转换成BNB的小额资产

## HTTP请求[​](/docs/zh-CN/wallet/asset/assets-can-convert-bnb#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/asset/dust-btc`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/assets-can-convert-bnb#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/asset/assets-can-convert-bnb#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
accountType| STRING| NO| `SPOT`或`MARGIN`,默认`SPOT`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/asset/assets-can-convert-bnb#响应示例 "响应示例的直接链接")
    
    
    {  
        "details": [  
            {  
                "asset": "ADA",         //资产名  
                "assetFullName": "ADA", //资产全称  
                "amountFree": "6.21",   //可转换数量  
                "toBTC": "0.00016848",  //等值BTC  
                "toBNB": "0.01777302",  //可转换BNB（未扣除手续费）  
                "toBNBOffExchange": "0.01741756", //可转换BNB（已扣除手续费）  
                "exchange": "0.00035546" //手续费  
            }  
        ],  
        "totalTransferBtc": "0.00016848",//全部资产等值BTC  
        "totalTransferBNB": "0.01777302",//总共可以转换的BNB数量  
        "dribbletPercentage": "0.02"     //转换手续费  
    }