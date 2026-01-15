---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Margin-Manual-Liquidation
api_type: Trading
updated_at: 2026-01-15T23:48:51.288542
---

# Margin Manual Liquidation(MARGIN)

## API Description[​](/docs/margin_trading/trade/Margin-Manual-Liquidation#api-description "Direct link to API Description")

Margin Manual Liquidation

## HTTP Request[​](/docs/margin_trading/trade/Margin-Manual-Liquidation#http-request "Direct link to HTTP Request")

POST `/sapi/v1/margin/manual-liquidation`

## Request Weight(UID)[​](/docs/margin_trading/trade/Margin-Manual-Liquidation#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/margin_trading/trade/Margin-Manual-Liquidation#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
type| STRING| YES| `MARGIN`,`ISOLATED`  
symbol| STRING| NO| When type selects `ISOLATED`, `symbol` must be filled in  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
Additional notes:

  * This endpoint can support Cross Margin Classic Mode and Pro Mode.
  * And only support Isolated Margin for restricted region.



## Response Example[​](/docs/margin_trading/trade/Margin-Manual-Liquidation#response-example "Direct link to Response Example")
    
    
    {  
      "asset": "ETH",  
      "interest": "0.00083334",  
      "principal": "0.001",  
      "liabilityAsset": "USDT",  
      "liabilityQty": 0.3552  
    }

---

# 杠杆手动强平(MARGIN)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Margin-Manual-Liquidation#接口描述 "接口描述的直接链接")

杠杆手动强平

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Margin-Manual-Liquidation#http请求 "HTTP请求的直接链接")

POST /sapi/v1/margin/manual-liquidation

## 请求权重(UID)[​](/docs/zh-CN/margin_trading/trade/Margin-Manual-Liquidation#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Margin-Manual-Liquidation#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
type| STRING| YES| `MARGIN`,`ISOLATED`  
symbol| STRING| NO| `type`选择`ISOLATED`后，`symbol`需要填入  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
备注:

  * 该接口支持全仓经典模式和专业模式。
  * 逐仓仅支持受限区域。



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Margin-Manual-Liquidation#响应示例 "响应示例的直接链接")
    
    
    {  
      "asset": "ETH",  
      "interest": "0.00083334",  
      "principal": "0.001",  
      "liabilityAsset": "USDT",  
      "liabilityQty": 0.3552  
    }