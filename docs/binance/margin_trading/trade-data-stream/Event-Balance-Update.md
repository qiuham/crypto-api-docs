---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade-data-stream/Event-Balance-Update
api_type: Trading
updated_at: 2026-01-15T23:48:39.820802
---

# Payload: Balance update

## Event Description[​](/docs/margin_trading/trade-data-stream/Event-Balance-Update#event-description "Direct link to Event Description")

Balance Update occurs during the following:

  * Deposits or withdrawals from the account
  * Transfer of funds between accounts (e.g. Spot to Margin)



## Event Name[​](/docs/margin_trading/trade-data-stream/Event-Balance-Update#event-name "Direct link to Event Name")

`balanceUpdate`

## Response Example[​](/docs/margin_trading/trade-data-stream/Event-Balance-Update#response-example "Direct link to Response Example")

> **Payload:**
    
    
    {  
      "e": "balanceUpdate",         //Event Type  
      "E": 1573200697110,           //Event Time  
      "a": "BTC",                   //Asset  
      "d": "100.00000000",          //Balance Delta  
      "T": 1573200697068            //Clear Time  
    }

---

# 余额更新

## 事件描述[​](/docs/zh-CN/margin_trading/trade-data-stream/Event-Balance-Update#事件描述 "事件描述的直接链接")

当下列情形发生时更新:

  * 账户发生充值或提取
  * 交易账户之间发生划转(例如 现货向杠杆账户划转)



## 事件类型[​](/docs/zh-CN/margin_trading/trade-data-stream/Event-Balance-Update#事件类型 "事件类型的直接链接")

`USER_LIABILITY_CHANGE`

## 响应示例[​](/docs/zh-CN/margin_trading/trade-data-stream/Event-Balance-Update#响应示例 "响应示例的直接链接")

> **Payload:**
    
    
    {  
      "e": "balanceUpdate",         //Event Type  
      "E": 1573200697110,           //Event Time  
      "a": "ABC",                   //Asset  
      "d": "100.00000000",          //Balance Delta  
      "T": 1573200697068            //Clear Time  
    }