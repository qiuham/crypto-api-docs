---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/faqs/opo
api_type: REST
updated_at: 2026-01-15T23:35:59.706845
---

# One Pays the Other (OPO)

## What is One Pays the Other?[​](/docs/binance-spot-api-docs/faqs/opo#what-is-one-pays-the-other "Direct link to What is One Pays the Other?")

This is a special behavior of OTO and OTOCO where the received amount from the working order is used for the quantity of the pending order(s). Thus the only balance requirement on order placement is that of the working order.

The received funds from the working order are _locked_ for use by the pending order(s) and not available for trading or withdrawal. If the order list is canceled before the pending order is placed on the Matching Engine then these locked funds are unlocked.

OPO is almost identical to `OTO`, with the exception of the absence of the `quantity` of the pending order(s).

## How can I use this?[​](/docs/binance-spot-api-docs/faqs/opo#how-can-i-use-this "Direct link to How can I use this?")

Please refer to the following table:

API| Request  
---|---  
REST API| `POST /api/v3/orderList/opo`   
`POST /api/v3/orderList/opoco`  
WebSocket API| `orderList.place.opo`   
`orderList.place.opoco`  
FIX API| NewOrderList `<E>` where OPO `(25046)`=`true`  
  
## What is the difference with this order list from other order lists?[​](/docs/binance-spot-api-docs/faqs/opo#what-is-the-difference-with-this-order-list-from-other-order-lists "Direct link to What is the difference with this order list from other order lists?")

  * The pending order(s) are placed into the Matching Engine without quantity; the quantity will be based on the received quantity from the working order once it fully fills.
  * The received quantity will have commission deducted as appropriate. The commission is taken from the available funds instead (i.e. `free` balances) if the received asset is not BNB and there are enough available funds.
  * The quantity of the pending order(s) are evaluated (e.g. filters) after the working order fully fills.
  * If a symbol has `LOT_SIZE` and/or `MARKET_LOT_SIZE` filters configured, the quantity of the pending order(s) are adjusted to meet them. Any of the locked quantity not used in the pending order(s) will be unlocked and returned to the `free` balances.
  * A pending OPO order's quantity may not be amended until the working order has been fully filled.
  * Only working orders on the `BUY` side and pending order(s) on the `SELL` side are accepted.



## Which symbols allow OPO orders?[​](/docs/binance-spot-api-docs/faqs/opo#which-symbols-allow-opo-orders "Direct link to Which symbols allow OPO orders?")

Order| Reqired in Exchange Information  
---|---  
OPO| `otoAllowed` and `opoAllowed`  
OPOCO| `otoAllowed`, `opoAllowed`, and `ocoAllowed`

---

# 一个订单支付另一个订单（One Pays the Other，简称 OPO）

## 什么是一个订单支付另一个订单（OPO）？[​](/docs/zh-CN/binance-spot-api-docs/faqs/opo#什么是一个订单支付另一个订单opo "什么是一个订单支付另一个订单（OPO）？的直接链接")

这是 OTO 和 OTOCO 的一种特殊行为，其中生效订单收到的数量将用作待执行订单的数量。因此，订单触发时唯一的数量要求是生效订单的数量。

生效订单收到的资金会被 _锁定_ ，用于待执行订单，且不可用于交易或提现。如果订单列表在待执行订单被提交到撮合引擎之前被取消，这些锁定的资金将被解锁。

OPO 与 `OTO` 几乎相同，唯一的区别是待执行订单不用指定`数量`。

## 我如何使用它？[​](/docs/zh-CN/binance-spot-api-docs/faqs/opo#我如何使用它 "我如何使用它？的直接链接")

请参考下表：

API| 请求方式  
---|---  
REST API| `POST /api/v3/orderList/opo`   
`POST /api/v3/orderList/opoco`  
WebSocket API| `orderList.place.opo`   
`orderList.place.opoco`  
FIX API| NewOrderList `<E>`，其中 OPO `(25046)`=`true`  
  
## 该订单列表与其他订单列表有什么区别？[​](/docs/zh-CN/binance-spot-api-docs/faqs/opo#该订单列表与其他订单列表有什么区别 "该订单列表与其他订单列表有什么区别？的直接链接")

  * 待执行订单在提交到撮合引擎时没有数量；数量将基于生效订单完全成交后收到的数量确定。
  * 收到的数量会扣除相应的手续费。如果收到的资产不是 BNB 且有足够的可用资金，手续费将从可用资金（即 `free` 余额）中扣除。
  * 待执行订单的数量会在生效订单完全成交后进行检查（例如过滤器）。
  * 如果某个交易对配置了 `LOT_SIZE` 和/或 `MARKET_LOT_SIZE` 过滤器，待执行订单的数量会被调整以满足这些要求。未使用的锁定数量将被解锁并返还到 `free` 余额。
  * 待执行的 OPO 订单的数量在生效订单完全成交之前不可修改。
  * 仅接受生效订单为买入（BUY）方向，待执行订单为卖出（SELL）方向的情况。



## 哪些交易对支持 OPO 订单？[​](/docs/zh-CN/binance-spot-api-docs/faqs/opo#哪些交易对支持-opo-订单 "哪些交易对支持 OPO 订单？的直接链接")

订单类型| Exchange Information 中需要包含  
---|---  
OPO| `otoAllowed` 和 `opoAllowed`  
OPOCO| `otoAllowed`、`opoAllowed` 和 `ocoAllowed`