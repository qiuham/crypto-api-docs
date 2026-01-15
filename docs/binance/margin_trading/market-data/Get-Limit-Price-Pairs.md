---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data/Get-Limit-Price-Pairs
api_type: Market Data
updated_at: 2026-01-15T23:48:31.350646
---

# Get Limit Price Pairs(MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data/Get-Limit-Price-Pairs#api-description "Direct link to API Description")

Query trading pairs with restriction on limit price range. In margin trading, you can place orders with limit price. Limit price should be within (-15%, 15%) of current index price for a list of margin trading pairs. This rule only impacts limit sell orders with limit price that is lower than current index price and limit buy orders with limit price that is higher than current index price.

  * Buy order: Your order will be rejected with an error message notification if the limit price is 15% above the index price.
  * Sell order: Your order will be rejected with an error message notification if the limit price is 15% below the index price. Please review the limit price order placing strategy, backtest and calibrate the planned order size with the trading volume and order book depth to prevent trading loss.



## HTTP Request[​](/docs/margin_trading/market-data/Get-Limit-Price-Pairs#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/limit-price-pairs`

## Request Weight(IP)[​](/docs/margin_trading/market-data/Get-Limit-Price-Pairs#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/margin_trading/market-data/Get-Limit-Price-Pairs#request-parameters "Direct link to Request Parameters")

NA

## Response Example[​](/docs/margin_trading/market-data/Get-Limit-Price-Pairs#response-example "Direct link to Response Example")
    
    
     {  "crossMarginSymbols":    
     	[  "BLURUSDC",    
      	"SANDBTC",   
      	"QKCBTC",   
      	"SEIFDUSD",   
      	"NEOUSDC",   
      	"ARBFDUSD",   
      	"ORDIUSDC"   
     	]   
     }

---

# 查询出价限定的交易对 (MARKET_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data/Get-Limit-Price-Pairs#接口描述 "接口描述的直接链接")

查询所有对于高买低卖的限价单施加了价格区间限制的出价限定的交易对。 在杠杆交易中，用户可以设置限价委托单。对于杠杆交易对，限价应在当前指数价格的(-15%, 15%)范围内。此规则仅适用于低于当前指数价格的限价卖出价和高于当前指数价格的限价买入价。

  * 买入订单：如果限价高于指数价格的15%，您的委托将被拒绝，并显示错误消息。
  * 卖出订单：如果限价低于指数价格的15%，您的委托将被拒绝，并显示错误消息。 请优化修改限价委托策略，并根据交易量和订单簿深度回测和校准计划的限价委托数量规模，以防止交易亏损。



## HTTP请求[​](/docs/zh-CN/margin_trading/market-data/Get-Limit-Price-Pairs#http请求 "HTTP��请求的直接链接")

GET `/sapi/v1/margin/limit-price-pairs`

## 请求权重(IP)[​](/docs/zh-CN/margin_trading/market-data/Get-Limit-Price-Pairs#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data/Get-Limit-Price-Pairs#请求参数 "请求参数的直接链接")

NA

## 响应示例[​](/docs/zh-CN/margin_trading/market-data/Get-Limit-Price-Pairs#响应示例 "响应示例的直接链接")
    
    
     {  "crossMarginSymbols":    
     	[  "BLURUSDC",    
      	"SANDBTC",   
      	"QKCBTC",   
      	"SEIFDUSD",   
      	"NEOUSDC",   
      	"ARBFDUSD",   
      	"ORDIUSDC"   
     	]   
     }