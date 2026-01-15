---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details
api_type: Account
updated_at: 2026-01-15T23:51:26.680908
---

# Query Managed Sub-account Asset Details (For Investor Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#api-description "Direct link to API Description")

Query Managed Sub-account Asset Details

## HTTP Request[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#http-request "Direct link to HTTP Request")

GET `/sapi/v1/managed-subaccount/asset`

## Request Weight(IP)[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#response-example "Direct link to Response Example")
    
    
    [  
      {  
         "coin": "INJ",                  
         "name": "Injective Protocol",   
         "totalBalance": "0",            
         "availableBalance": "0",        
         "inOrder": "0",                  
         "btcValue": "0"                 
      },  
      {  
         "coin": "FILDOWN",  
         "name": "FILDOWN",  
         "totalBalance": "0",  
         "availableBalance": "0",  
         "inOrder": "0",  
         "btcValue": "0"  
      }  
    ]

---

# 投资人账户查询托管子账户资产 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#接口描述 "接口描述的直接链接")

投资人账户查询托管子账户资产

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/asset`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Asset-Details#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
         "coin": "INJ",                //币种  
         "name": "Injective Protocol", //名称  
         "totalBalance": "0",          //总资产  
         "availableBalance": "0",      //可用资产  
         "inOrder": "0",               //下单冻结  
         "btcValue": "0"               //btc估值  
      },  
      {  
         "coin": "FILDOWN",  
         "name": "FILDOWN",  
         "totalBalance": "0",  
         "availableBalance": "0",  
         "inOrder": "0",  
         "btcValue": "0"   
      }  
    ]