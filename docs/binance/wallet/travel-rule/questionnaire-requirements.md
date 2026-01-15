---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/questionnaire-requirements
api_type: REST
updated_at: 2026-01-15T23:49:55.159154
---

# Check Questionnaire Requirements (for local entities that require travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/questionnaire-requirements#api-description "Direct link to API Description")

This API will return user-specific Travel Rule questionnaire requirement information in reference to the current API key.

## HTTP Request[​](/docs/wallet/travel-rule/questionnaire-requirements#http-request "Direct link to HTTP Request")

GET `/sapi/v1/localentity/questionnaire-requirements`

## Request Weight(IP)[​](/docs/wallet/travel-rule/questionnaire-requirements#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/travel-rule/questionnaire-requirements#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/travel-rule/questionnaire-requirements#response-example "Direct link to Response Example")
    
    
      
    {  
        "questionnaireCountryCode":"AE"  
    }

---

# 检查问卷需求(针对需要旅行规则的本地站)(支持多网络)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/questionnaire-requirements#接口描述 "接口描述的直接链接")

基于当前的用户的API key，接口讲返回针对改用户提交问卷所需的信息。

## HTTP 请求[​](/docs/zh-CN/wallet/travel-rule/questionnaire-requirements#http-请求 "HTTP 请求的直接链接")

GET `/sapi/v1/localentity/questionnaire-requirements`

## 请求权重(IP)[​](/docs/zh-CN/wallet/travel-rule/questionnaire-requirements#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/questionnaire-requirements#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/travel-rule/questionnaire-requirements#响应示例 "响应示例的直接链接")
    
    
      
    {  
        "entityCountryCode":"AE"  
    }