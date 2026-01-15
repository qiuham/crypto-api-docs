---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/risk-data-stream/Event-Liability-Update
api_type: REST
updated_at: 2026-01-15T23:48:36.882492
---

# Payload: liability update

## Event Description[​](/docs/margin_trading/risk-data-stream/Event-Liability-Update#event-description "Direct link to Event Description")

Liability update during the following :

  * borrowing
  * Repayment
  * Interest Calculation



## Event Name[​](/docs/margin_trading/risk-data-stream/Event-Liability-Update#event-name "Direct link to Event Name")

`USER_LIABILITY_CHANGE`

## Response Example[​](/docs/margin_trading/risk-data-stream/Event-Liability-Update#response-example "Direct link to Response Example")

> **Payload:**
    
    
    {  
      "e": "USER_LIABILITY_CHANGE", // Event Type  
      "E": 1701949801133, // Event Time  
      "a": "BTC", // Asset  
      "t": "BORROW", // Liability Update Type  
      "p": "0.00000100", // Principle Quantity  
      "i": "0.00000000" // Interest Quantity  
    }

---

# 负债变化事件

## 事件描述[​](/docs/zh-CN/margin_trading/risk-data-stream/Event-Liability-Update#事件描述 "事件描述的直接链接")

当下列情形发生时,会推送此事件:

  * 借款
  * 计息
  * 还款



## 事件类型[​](/docs/zh-CN/margin_trading/risk-data-stream/Event-Liability-Update#事件类型 "事件类型的直接链接")

`USER_LIABILITY_CHANGE`

## 响应示例[​](/docs/zh-CN/margin_trading/risk-data-stream/Event-Liability-Update#响应示例 "响应示例的直接链接")

> **Payload:**
    
    
    {  
       "e": "USER_LIABILITY_CHANGE", // 事件类型  
       "E": 1701949801133, // 事件时间  
       "a": "BTC", // 资产  
       "t": "BORROW", // 负债变更类型  
       "p": "0.00000100", // 负债本金数量  
       "i": "0.00000000" // 利息数量  
    }