---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/onboarded-vasp-list
api_type: REST
updated_at: 2026-01-15T23:49:55.098633
---

# VASP list (for local entities that require travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/onboarded-vasp-list#api-description "Direct link to API Description")

Fetch the VASP list for local entities.

## HTTP Request[​](/docs/wallet/travel-rule/onboarded-vasp-list#http-request "Direct link to HTTP Request")

GET `/sapi/v1/localentity/vasp`

## Request Weight(IP)[​](/docs/wallet/travel-rule/onboarded-vasp-list#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/travel-rule/onboarded-vasp-list#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/travel-rule/onboarded-vasp-list#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "vaspName":"Binance",  
        "vaspCode":"BINANCE"  
      },  
      {  
        "vaspName":"HashKeyGlobal",  
        "vaspCode":"NVBH3Z_nNEHjvqbUfkaL"  
      }  
    ]

---

# 获取VASP列表(针对需要旅行规则的本地站)(支持多网络)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/onboarded-vasp-list#接口描述 "接口描述的直接链接")

获取旅行规则的本地站的VASP列表。

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/onboarded-vasp-list#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/localentity/vasp`

## 请求权重(IP)[​](/docs/zh-CN/wallet/travel-rule/onboarded-vasp-list#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/onboarded-vasp-list#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/travel-rule/onboarded-vasp-list#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "vaspName":"Binance",  
        "vaspCode":"BINANCE"  
      },  
      {  
        "vaspName":"HashKeyGlobal",  
        "vaspCode":"NVBH3Z_nNEHjvqbUfkaL"  
      }  
    ]