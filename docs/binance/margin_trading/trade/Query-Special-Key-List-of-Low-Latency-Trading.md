---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading
api_type: Trading
updated_at: 2026-01-15T23:48:59.807336
---

# Query Special key List(Low Latency Trading)(TRADE)

## API Description[​](/docs/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#api-description "Direct link to API Description")

This only applies to Special Key for Low Latency Trading.

## HTTP Request[​](/docs/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/api-key-list`

## Request Weight[​](/docs/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#request-weight "Direct link to Request Weight")

**1(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| isolated margin pair  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "apiName": "testName1",  
        "apiKey":"znpOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoG",  
        "ip": "192.168.0.1,192.168.0.2",  
        "type": "RSA",  
         "permissionMode": "TRADE"   
      },  
      {  
        "apiName": "testName2",  
        "apiKey":"znpOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoG",  
        "ip": "192.168.0.1,192.168.0.2",  
        "type": "Ed25519",  
         "permissionMode": "READ"   
      }  
    ]

---

# 查询低延迟交易SpecialKey清单(TRADE)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#接口描述 "接口描述的直接链接")

查询SpecialKey清单，仅适用低延迟交易SpecialKey。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/api-key-list`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#请求权重 "请求权重的直接链接")

**1(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#请求参数 "请求参数的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| isolated margin pair  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Special-Key-List-of-Low-Latency-Trading#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "apiName": "testName1",  
        "apiKey":"znpOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoG",  
        "ip": "192.168.0.1,192.168.0.2",  
        "type": "RSA",  
        "permissionMode": "TRADE"   
      },  
      {  
        "apiName": "testName2",  
        "apiKey":"znpOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoG",  
        "ip": "192.168.0.1,192.168.0.2",  
        "type": "Ed25519",  
        "permissionMode": "READ"   
      }  
    ]