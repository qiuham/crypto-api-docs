---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/fetch-withdraw-quota
api_type: REST
updated_at: 2026-01-15T23:49:39.725693
---

# Fetch withdraw quota (USER_DATA)

## API Description[​](/docs/wallet/capital/fetch-withdraw-quota#api-description "Direct link to API Description")

Fetch withdraw quota

## HTTP Request[​](/docs/wallet/capital/fetch-withdraw-quota#http-request "Direct link to HTTP Request")

GET `/sapi/v1/capital/withdraw/quota`

## Request Weight(IP)[​](/docs/wallet/capital/fetch-withdraw-quota#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/wallet/capital/fetch-withdraw-quota#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/wallet/capital/fetch-withdraw-quota#response-example "Direct link to Response Example")
    
    
    {  
        "wdQuota" : "10000", //User's total withdrawal quota in the past 24 hours (including on-chain withdrawal and internal transfer), unit in USD  
        "usedWdQuota" : "1000" //User withdrawal quota usage in the past 24 hours, unit in USD  
    }

---

# 获取用户提现额度

## 接口描述[​](/docs/zh-CN/wallet/capital/fetch-withdraw-quota#接口描述 "接口描述的直接链接")

获取用户提现额度

## HTTP请求[​](/docs/zh-CN/wallet/capital/fetch-withdraw-quota#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/capital/withdraw/quota`

## 请求权重(IP)[​](/docs/zh-CN/wallet/capital/fetch-withdraw-quota#请求权重ip "请��求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/wallet/capital/fetch-withdraw-quota#请求参数 "请求参数的直接链接")

NONE

## 响应示例[​](/docs/zh-CN/wallet/capital/fetch-withdraw-quota#响应示例 "响应示例的直接链接")
    
    
    {  
        "wdQuota": "10000", //用户过去24小时的提币额度（包含链上提币和内部转账），单位为 USD  
        "usedWdQuota": "1000" //用户过去24小时内已用提币额度，单位为 USD  
    }