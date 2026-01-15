---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/others/system-status
api_type: REST
updated_at: 2026-01-15T23:49:46.490192
---

# System Status (System)

## API Description[​](/docs/wallet/others/system-status#api-description "Direct link to API Description")

Fetch system status.

## HTTP Request[​](/docs/wallet/others/system-status#http-request "Direct link to HTTP Request")

GET `/sapi/v1/system/status`

## Request Weight(IP)[​](/docs/wallet/others/system-status#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Response Example[​](/docs/wallet/others/system-status#response-example "Direct link to Response Example")
    
    
    {   
        "status": 0,              // 0: normal，1：system maintenance  
        "msg": "normal"           // "normal", "system_maintenance"  
    }

---

# 系统状态(System)

## 接口描述[​](/docs/zh-CN/wallet/others/system-status#接口描述 "接口描述的直接链接")

获取系统状态。

## HTTP请求[​](/docs/zh-CN/wallet/others/system-status#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/system/status`

## 请求权重(IP)[​](/docs/zh-CN/wallet/others/system-status#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 响应示例[​](/docs/zh-CN/wallet/others/system-status#响应示例 "响应示例的直接链接")
    
    
    {   
        "status": 0,              // 0: normal，1：system maintenance  
        "msg": "normal"           // "normal", "system_maintenance"  
    }