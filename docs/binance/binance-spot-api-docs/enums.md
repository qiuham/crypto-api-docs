---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/enums
api_type: REST
updated_at: 2026-01-15T23:35:52.439314
---

# ENUM Definitions

This will apply for both REST API and WebSocket API.

## Symbol status (status)[​](/docs/binance-spot-api-docs/enums#symbol-status-status "Direct link to Symbol status \(status\)")

  * `TRADING`
  * `END_OF_DAY`
  * `HALT`
  * `BREAK`



## Account and Symbol Permissions (permissions)[​](/docs/binance-spot-api-docs/enums#account-and-symbol-permissions-permissions "Direct link to Account and Symbol Permissions \(permissions\)")

  * `SPOT`
  * `MARGIN`
  * `LEVERAGED`
  * `TRD_GRP_002`
  * `TRD_GRP_003`
  * `TRD_GRP_004`
  * `TRD_GRP_005`
  * `TRD_GRP_006`
  * `TRD_GRP_007`
  * `TRD_GRP_008`
  * `TRD_GRP_009`
  * `TRD_GRP_010`
  * `TRD_GRP_011`
  * `TRD_GRP_012`
  * `TRD_GRP_013`
  * `TRD_GRP_014`
  * `TRD_GRP_015`
  * `TRD_GRP_016`
  * `TRD_GRP_017`
  * `TRD_GRP_018`
  * `TRD_GRP_019`
  * `TRD_GRP_020`
  * `TRD_GRP_021`
  * `TRD_GRP_022`
  * `TRD_GRP_023`
  * `TRD_GRP_024`
  * `TRD_GRP_025`



## Order status (status)[​](/docs/binance-spot-api-docs/enums#order-status-status "Direct link to Order status \(status\)")

Status| Description  
---|---  
`NEW`| The order has been accepted by the engine.  
`PENDING_NEW`| The order is in a pending phase until the working order of an order list has been fully filled.  
`PARTIALLY_FILLED`| A part of the order has been filled.  
`FILLED`| The order has been completed.  
`CANCELED`| The order has been canceled by the user.  
`PENDING_CANCEL`| Currently unused  
`REJECTED`| The order was not accepted by the engine and not processed.  
`EXPIRED`| The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill)   
or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance)  
`EXPIRED_IN_MATCH`| The order was expired by the exchange due to STP. (e.g. an order with `EXPIRE_TAKER` will match with existing orders on the book with the same account or same `tradeGroupId`)  
  
## Order List Status (listStatusType)[​](/docs/binance-spot-api-docs/enums#order-list-status-liststatustype "Direct link to Order List Status \(listStatusType\)")

Status| Description  
---|---  
`RESPONSE`| This is used when the ListStatus is responding to a failed action. (E.g. order list placement or cancellation)  
`EXEC_STARTED`| The order list has been placed or there is an update to the order list status.  
`UPDATED`| The clientOrderId of an order in the order list has been changed.  
`ALL_DONE`| The order list has finished executing and thus is no longer active.  
  
## Order List Order Status (listOrderStatus)[​](/docs/binance-spot-api-docs/enums#order-list-order-status-listorderstatus "Direct link to Order List Order Status \(listOrderStatus\)")

Status| Description  
---|---  
`EXECUTING`| Either an order list has been placed or there is an update to the status of the list.  
`ALL_DONE`| An order list has completed execution and thus no longer active.  
`REJECT`| The List Status is responding to a failed action either during order placement or order canceled.  
  
## ContingencyType[​](/docs/binance-spot-api-docs/enums#contingencytype "Direct link to ContingencyType")

  * `OCO`
  * `OTO`



## AllocationType[​](/docs/binance-spot-api-docs/enums#allocationtype "Direct link to AllocationType")

  * `SOR`



## Order types (orderTypes, type)[​](/docs/binance-spot-api-docs/enums#order-types-ordertypes-type "Direct link to Order types \(orderTypes, type\)")

  * `LIMIT`
  * `MARKET`
  * `STOP_LOSS`
  * `STOP_LOSS_LIMIT`
  * `TAKE_PROFIT`
  * `TAKE_PROFIT_LIMIT`
  * `LIMIT_MAKER`



## Order Response Type (newOrderRespType)[​](/docs/binance-spot-api-docs/enums#order-response-type-neworderresptype "Direct link to Order Response Type \(newOrderRespType\)")

  * `ACK`
  * `RESULT`
  * `FULL`



## Working Floor[​](/docs/binance-spot-api-docs/enums#working-floor "Direct link to Working Floor")

  * `EXCHANGE`
  * `SOR`



## Order side (side)[​](/docs/binance-spot-api-docs/enums#order-side-side "Direct link to Order side \(side\)")

  * `BUY`
  * `SELL`



## Time in force (timeInForce)[​](/docs/binance-spot-api-docs/enums#time-in-force-timeinforce "Direct link to Time in force \(timeInForce\)")

This sets how long an order will be active before expiration.

Status| Description  
---|---  
`GTC`| Good Til Canceled   
An order will be on the book unless the order is canceled.  
`IOC`| Immediate Or Cancel   
An order will try to fill the order as much as it can before the order expires.  
`FOK`| Fill or Kill   
An order will expire if the full order cannot be filled upon execution.  
  
## Rate limiters (rateLimitType)[​](/docs/binance-spot-api-docs/enums#rate-limiters-ratelimittype "Direct link to Rate limiters \(rateLimitType\)")

  * REQUEST_WEIGHT


    
    
    {  
        "rateLimitType": "REQUEST_WEIGHT",  
        "interval": "MINUTE",  
        "intervalNum": 1,  
        "limit": 6000  
    }  
    

  * ORDERS


    
    
    {  
        "rateLimitType": "ORDERS",  
        "interval": "SECOND",  
        "intervalNum": 1,  
        "limit": 10  
    }  
    

  * RAW_REQUESTS


    
    
    {  
        "rateLimitType": "RAW_REQUESTS",  
        "interval": "MINUTE",  
        "intervalNum": 5,  
        "limit": 61000  
    }  
    

## Rate limit intervals (interval)[​](/docs/binance-spot-api-docs/enums#rate-limit-intervals-interval "Direct link to Rate limit intervals \(interval\)")

  * SECOND
  * MINUTE
  * DAY



## STP Modes[​](/docs/binance-spot-api-docs/enums#stp-modes "Direct link to STP Modes")

Read [Self Trade Prevention (STP) FAQ](/docs/binance-spot-api-docs/faqs/stp_faq) to learn more.

  * `NONE`
  * `EXPIRE_MAKER`
  * `EXPIRE_TAKER`
  * `EXPIRE_BOTH`
  * `DECREMENT`
  * `TRANSFER`

---

# 枚举定义

这将适用于 REST API 和 WebSocket API。

## 交易对的状态（status）[​](/docs/zh-CN/binance-spot-api-docs/enums#交易对的状态status "交易对的状态（status）的直接链接")

  * `TRADING` \- 正常交易中
  * `END_OF_DAY` \- 收盘
  * `HALT` \- 交易终止(该交易对已下线)
  * `BREAK` \- 交易暂停



## 账户与交易对权限（permissions）[​](/docs/zh-CN/binance-spot-api-docs/enums#账户与交易对权限permissions "账户与交易对权限（permissions）的直接链接")

  * `SPOT` \- 现货
  * `MARGIN` \- 杠杆
  * `LEVERAGED` \- 杠杆代币
  * `TRD_GRP_002` \- 交易组 002
  * `TRD_GRP_003` \- 交易组 003
  * `TRD_GRP_004` \- 交易组 004
  * `TRD_GRP_005` \- 交易组 005
  * `TRD_GRP_006` \- 交易组 006
  * `TRD_GRP_007` \- 交易组 007
  * `TRD_GRP_008` \- 交易组 008
  * `TRD_GRP_009` \- 交易组 009
  * `TRD_GRP_010` \- 交易组 010
  * `TRD_GRP_011` \- 交易组 011
  * `TRD_GRP_012` \- 交易组 012
  * `TRD_GRP_013` \- 交易组 013
  * `TRD_GRP_014` \- 交易组 014
  * `TRD_GRP_015` \- 交易组 015
  * `TRD_GRP_016` \- 交易组 016
  * `TRD_GRP_017` \- 交易组 017
  * `TRD_GRP_018` \- 交易组 018
  * `TRD_GRP_019` \- 交易组 019
  * `TRD_GRP_020` \- 交易组 020
  * `TRD_GRP_021` \- 交易组 021
  * `TRD_GRP_022` \- 交易组 022
  * `TRD_GRP_023` \- 交易组 023
  * `TRD_GRP_024` \- 交易组 024
  * `TRD_GRP_025` \- 交易组 025



## 订单状态（status）[​](/docs/zh-CN/binance-spot-api-docs/enums#订单状态status "订单状态（status）的直接链接")

状态| 描述  
---|---  
`NEW`| 该订单被交易引擎接受。  
`PENDING_NEW`| 该订单处于待处理 (`PENDING`) 阶段，直到其所属订单组（order list） 中的 `working order` 完全成交。  
`PARTIALLY_FILLED`| 部分订单已被成交。  
`FILLED`| 订单已完全成交。  
`CANCELED`| 用户撤销了订单。  
`PENDING_CANCEL`| 撤销中(目前并未使用)  
`REJECTED`| 订单没有被交易引擎接受，也没被处理。  
`EXPIRED`| 该订单根据订单类型的规则被取消（例如，没有成交的 LIMIT FOK 订单, LIMIT IOC 或部分成交的 MARKET 订单）  
或者被交易引擎取消（例如，在强平期间被取消的订单，在交易所维护期间被取消的订单）  
`EXPIRED_IN_MATCH`| 表示订单由于 STP 而过期。（例如，带有 `EXPIRE_TAKER` 的订单与账簿上同属相同帐户或相同 `tradeGroupId` 的现有订单匹配）  
  
## 订单组（order list）状态 （状态类型集 listStatusType）[​](/docs/zh-CN/binance-spot-api-docs/enums#订单组order-list状态-状态类型集-liststatustype "订单组（order list）状态 �（状态类型集 listStatusType）的直接链接")

状态| 描述  
---|---  
`RESPONSE`| 在 ListStatus 用于响应失败的操作时会被使用。（例如，下订单组或取消订单组）  
`EXEC_STARTED`| 订单组已被下达或订单组状态有更新。  
`UPDATED`| 订单组里的某个订单的 clientOrderId 被改变。  
`ALL_DONE`| 订单组执行结束，因此不再处于活动状态。  
  
## 订单组（order list）中的订单状态 （订单状态集 listOrderStatus）[​](/docs/zh-CN/binance-spot-api-docs/enums#订单组order-list中的订单状态-订单状态集-listorderstatus "订单组（order list）中的订单状态 （订单状态集 listOrderStatus）的直接链接")

状态| 描述  
---|---  
`EXECUTING`| 订单组已被下达或订单组状态有更新。  
`ALL_DONE`| 订单组执行结束，因此不再处于活动状态。  
`REJECT`| 在 ListStatus 用于响应在下单阶段或取消订单组期间的失败操作时会被使用，  
  
## 订单组的类型[​](/docs/zh-CN/binance-spot-api-docs/enums#订单组的类型 "订单组的类型的直接链接")

  * `OCO`
  * `OTO`



## 分配类型[​](/docs/zh-CN/binance-spot-api-docs/enums#分配类型 "分配类型的直接链接")

  * `SOR`



## 订单类型（orderTypes, type）[​](/docs/zh-CN/binance-spot-api-docs/enums#订单类型ordertypes-type "订单类型（orderTypes, type）的直接链接")

  * `LIMIT` \- 限价单
  * `MARKET` \- 市价单
  * `STOP_LOSS` \- 止损单
  * `STOP_LOSS_LIMIT` \- 限价止损单
  * `TAKE_PROFIT` \- 止盈单
  * `TAKE_PROFIT_LIMIT` \- 限价止盈单
  * `LIMIT_MAKER` \- 限价做市单



## 订单返回类型 （newOrderRespType）[​](/docs/zh-CN/binance-spot-api-docs/enums#订单返回类型-neworderresptype "订单返回类型 （newOrderRespType）的直接链接")

  * `ACK`
  * `RESULT`
  * `FULL`



## 工作平台[​](/docs/zh-CN/binance-spot-api-docs/enums#工作平台 "工作平台的直接链接")

  * `EXCHANGE` \- 常规交易
  * `SOR` \- 智能订单路由



## 订单方向 (side)[​](/docs/zh-CN/binance-spot-api-docs/enums#订单方向-side "订单方向 \(side\)的直接链接")

  * `BUY` \- 买入
  * `SELL` \- 卖出



## 生效时间 （timeInForce）[​](/docs/zh-CN/binance-spot-api-docs/enums#生效时间-timeinforce "生效时间 （timeInForce）的直接链接")

这里定义了订单在失效前的有效时间。

状态| 描述  
---|---  
`GTC`| 成交为止   
订单会一直有效，直到被成交或者取消。  
`IOC`| 无法立即成交的部分就撤销   
订单在失效前会尽量多的成交。  
`FOK`| 无法全部立即成交就撤销   
如果无法全部成交，订单会失效。  
  
## 速率限制种类（rateLimitType）[​](/docs/zh-CN/binance-spot-api-docs/enums#速率限制种类ratelimittype "速率限制种类（rateLimitType）的直接链接")

  * REQUESTS_WEIGHT - 单位时间请求权重之和上限


    
    
    {  
        "rateLimitType": "REQUEST_WEIGHT",  
        "interval": "MINUTE",  
        "intervalNum": 1,  
        "limit": 6000  
    }  
    

  * ORDERS - 单位时间下单(撤单)次数上限


    
    
    {  
        "rateLimitType": "ORDERS",  
        "interval": "SECOND",  
        "intervalNum": 1,  
        "limit": 10  
    }  
    

  * RAW_REQUESTS - 单位时间请求次数上限


    
    
    {  
        "rateLimitType": "RAW_REQUESTS",  
        "interval": "MINUTE",  
        "intervalNum": 5,  
        "limit": 61000  
    }  
    

## 速率限制间隔 （interval）[​](/docs/zh-CN/binance-spot-api-docs/enums#速率限制间隔-interval "速率限制间隔 （interval）的直接链接")

  * SECOND
  * MINUTE
  * DAY



## STP 模式[​](/docs/zh-CN/binance-spot-api-docs/enums#stp-模式 "STP 模式的直接链接")

请参阅 [自我交易预防 (Self Trade Prevention - STP) 常见问题](/docs/zh-CN/binance-spot-api-docs/faqs/stp_faq)。

  * `NONE`
  * `EXPIRE_MAKER`
  * `EXPIRE_TAKER`
  * `EXPIRE_BOTH`
  * `DECREMENT`
  * `TRANSFER`