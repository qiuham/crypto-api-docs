---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading
api_type: Trading
updated_at: 2026-01-15T23:48:43.701182
---

# Edit ip for Special Key(Low-Latency Trading)(TRADE)

## API Description[​](/docs/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#api-description "Direct link to API Description")

Edit ip restriction. This only applies to Special Key for Low Latency Trading.

You need to enable Permits “Enable Spot & Margin Trading” option for the API Key which requests this endpoint.

## HTTP Request[​](/docs/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#http-request "Direct link to HTTP Request")

PUT `/sapi/v1/margin/apiKey/ip`

## Request Weight[​](/docs/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#request-weight "Direct link to Request Weight")

**1(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
apiKey| STRING| YES|   
symbol| STRING| NO| isolated margin pair  
ip| STRING| YES| Can be added in batches, separated by commas. Max 30 for an API key  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#response-example "Direct link to Response Example")
    
    
    {  
    }

---

# 修改可供SpecialKey执行的IP地址(TRADE)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#接口描述 "接口描述的直接链接")

修改可供低延迟交易的SpecialKey执行的IP地址, 仅适用低延迟交易SpecialKey。

该接口需开通“Enable Spot & Margin Trading”的权限。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#http请求 "HTTP请求的直接链接")

PUT `/sapi/v1/margin/apiKey/ip`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#请求权重 "请求权重的直接链接")

**1(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#请求参数 "请求参数的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
apiKey| STRING| YES|   
symbol| STRING| NO| isolated margin pair  
ip| STRING| YES| Can be added in batches, separated by commas. Max 30 for an API key  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Edit-ip-for-Special-Key-of-Low-Latency-Trading#响应示例 "响应示例的直接链接")
    
    
    {  
    }