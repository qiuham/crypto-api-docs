---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/risk-data-stream/Start-User-Data-Stream
api_type: REST
updated_at: 2026-01-15T23:48:37.063512
---

# Start User Data Stream (USER_STREAM)

## API Description[​](/docs/margin_trading/risk-data-stream/Start-User-Data-Stream#api-description "Direct link to API Description")

Start a new user data stream.

## HTTP Request[​](/docs/margin_trading/risk-data-stream/Start-User-Data-Stream#http-request "Direct link to HTTP Request")

POST `/sapi/v1/margin/listen-key`

## Request Weight(UID)[​](/docs/margin_trading/risk-data-stream/Start-User-Data-Stream#request-weightuid "Direct link to Request Weight\(UID\)")

**1**

## Request Parameters[​](/docs/margin_trading/risk-data-stream/Start-User-Data-Stream#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/margin_trading/risk-data-stream/Start-User-Data-Stream#response-example "Direct link to Response Example")
    
    
    {  
      "listenKey": "T3ee22BIYuWqmvne0HNq2A2WsFlEtLhvWCtItw6ffhhd"  
    }

---

# 生成listenKey (USER_STREAM)

## 接口描述[​](/docs/zh-CN/margin_trading/risk-data-stream/Start-User-Data-Stream#接口描述 "接口描述的直接链接")

创建一个新的user data stream，返回值为一个listenKey

## HTTP请求[​](/docs/zh-CN/margin_trading/risk-data-stream/Start-User-Data-Stream#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/margin/listen-key`

## 请求权重(UID)[​](/docs/zh-CN/margin_trading/risk-data-stream/Start-User-Data-Stream#请求权重uid "请求权重\(UID\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/margin_trading/risk-data-stream/Start-User-Data-Stream#请求参数 "请求参数的直接链接")

None

## 响应示例[​](/docs/zh-CN/margin_trading/risk-data-stream/Start-User-Data-Stream#响应示例 "响应示例的直接链接")
    
    
    {  
      "listenKey": "T3ee22BIYuWqmvne0HNq2A2WsFlEtLhvWCtItw6ffhhd"  
    }