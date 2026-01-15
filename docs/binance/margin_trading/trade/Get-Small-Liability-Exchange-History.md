---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Get-Small-Liability-Exchange-History
api_type: Trading
updated_at: 2026-01-15T23:48:43.826250
---

# Get Small Liability Exchange History (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-History#api-description "Direct link to API Description")

Get Small liability Exchange History

## HTTP Request[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/exchange-small-liability-history`

## Request Weight[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-History#request-weight "Direct link to Request Weight")

**100(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
current| INT| YES| Currently querying page. Start from 1. Default:1  
size| INT| YES| Default:10, Max:100  
startTime| LONG| NO| Default: 30 days from current timestamp  
endTime| LONG| NO| Default: present timestamp  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Get-Small-Liability-Exchange-History#response-example "Direct link to Response Example")
    
    
    {  
        "total": 1,  
        "rows": [  
          {  
            "asset": "ETH",  
            "amount": "0.00083434",  
            "targetAsset": "BUSD",  
            "targetAmount": "1.37576819",  
            "bizType": "EXCHANGE_SMALL_LIABILITY",  
            "timestamp": 1672801339253  
          }  
        ]  
    }

---

# 查询全仓杠杆小额负债转换历史  (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-History#接口描述 "接口描述的直接链接")

查询全仓杠杆小额负债转换历史

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/exchange-small-liability-history`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-History#请求权重 "请求权重的直接链接")

**100(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
current| INT| YES| 当前页面，默认1，最小值为1  
size| INT| YES| 页面大小，默认10，最大值为100  
startTime| LONG| NO| 默认当前时间30天前的时间戳  
endTime| LONG| NO| 默认当前时间戳  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Get-Small-Liability-Exchange-History#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 1,  
        "rows": [  
          {  
            "asset": "ETH",  
            "amount": "0.00083434",  
            "targetAsset": "BUSD",  
            "targetAmount": "1.37576819",  
            "bizType": "EXCHANGE_SMALL_LIABILITY",  
            "timestamp": 1672801339253  
          }  
        ]  
    }