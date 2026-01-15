---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/testnet/enums
api_type: REST
updated_at: 2026-01-15T23:36:24.867468
---

# ENUM Definitions

This will apply for both REST API and WebSocket API.

## Symbol status (status):[​](/docs/binance-spot-api-docs/testnet/enums#symbol-status-status "Direct link to Symbol status \(status\):")

  * `TRADING`
  * `END_OF_DAY`
  * `HALT`
  * `BREAK`



## Account and Symbol Permissions (permissions)[​](/docs/binance-spot-api-docs/testnet/enums#account-and-symbol-permissions-permissions "Direct link to Account and Symbol Permissions \(permissions\)")

  * `SPOT`



## Order status (status)[​](/docs/binance-spot-api-docs/testnet/enums#order-status-status "Direct link to Order status \(status\)")

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
  
## Order List Status (listStatusType)[​](/docs/binance-spot-api-docs/testnet/enums#order-list-status-liststatustype "Direct link to Order List Status \(listStatusType\)")

Status| Description  
---|---  
`RESPONSE`| This is used when the ListStatus is responding to a failed action. (E.g. order list placement or cancellation)  
`EXEC_STARTED`| The order list has been placed or there is an update to the order list status.  
`UPDATED`| The clientOrderId of an order in the order list has been changed.  
`ALL_DONE`| The order list has finished executing and thus is no longer active.  
  
## Order List Order Status (listOrderStatus)[​](/docs/binance-spot-api-docs/testnet/enums#order-list-order-status-listorderstatus "Direct link to Order List Order Status \(listOrderStatus\)")

Status| Description  
---|---  
`EXECUTING`| Either an order list has been placed or there is an update to the status of the list.  
`ALL_DONE`| An order list has completed execution and thus no longer active.  
`REJECT`| The List Status is responding to a failed action either during order placement or order canceled.  
  
## ContingencyType[​](/docs/binance-spot-api-docs/testnet/enums#contingencytype "Direct link to ContingencyType")

  * `OCO`
  * `OTO`



## AllocationType[​](/docs/binance-spot-api-docs/testnet/enums#allocationtype "Direct link to AllocationType")

  * `SOR`



## Order types (orderTypes, type)[​](/docs/binance-spot-api-docs/testnet/enums#order-types-ordertypes-type "Direct link to Order types \(orderTypes, type\)")

  * `LIMIT`
  * `MARKET`
  * `STOP_LOSS`
  * `STOP_LOSS_LIMIT`
  * `TAKE_PROFIT`
  * `TAKE_PROFIT_LIMIT`
  * `LIMIT_MAKER`



## Order Response Type (newOrderRespType)[​](/docs/binance-spot-api-docs/testnet/enums#order-response-type-neworderresptype "Direct link to Order Response Type \(newOrderRespType\)")

  * `ACK`
  * `RESULT`
  * `FULL`



## Working Floor[​](/docs/binance-spot-api-docs/testnet/enums#working-floor "Direct link to Working Floor")

  * `EXCHANGE`
  * `SOR`



## Order side (side)[​](/docs/binance-spot-api-docs/testnet/enums#order-side-side "Direct link to Order side \(side\)")

  * `BUY`
  * `SELL`



## Time in force (timeInForce)[​](/docs/binance-spot-api-docs/testnet/enums#time-in-force-timeinforce "Direct link to Time in force \(timeInForce\)")

This sets how long an order will be active before expiration.

Status| Description  
---|---  
`GTC`| Good Til Canceled   
An order will be on the book unless the order is canceled.  
`IOC`| Immediate Or Cancel   
An order will try to fill the order as much as it can before the order expires.  
`FOK`| Fill or Kill   
An order will expire if the full order cannot be filled upon execution.  
  
## Rate limiters (rateLimitType)[​](/docs/binance-spot-api-docs/testnet/enums#rate-limiters-ratelimittype "Direct link to Rate limiters \(rateLimitType\)")

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
    

## Rate limit intervals (interval)[​](/docs/binance-spot-api-docs/testnet/enums#rate-limit-intervals-interval "Direct link to Rate limit intervals \(interval\)")

  * SECOND
  * MINUTE
  * DAY



## STP Modes[​](/docs/binance-spot-api-docs/testnet/enums#stp-modes "Direct link to STP Modes")

Read [Self Trade Prevention (STP) FAQ](/docs/binance-spot-api-docs/faqs/stp_faq) to learn more.

  * `NONE`
  * `EXPIRE_MAKER`
  * `EXPIRE_TAKER`
  * `EXPIRE_BOTH`
  * `DECREMENT`
  * `TRANSFER`

---

# ENUM Definitions

This will apply for both REST API and WebSocket API.

## Symbol status (status):[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#symbol-status-status "Symbol status \(status\):的直接链接")

  * `TRADING`
  * `END_OF_DAY`
  * `HALT`
  * `BREAK`



## Account and Symbol Permissions (permissions)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#account-and-symbol-permissions-permissions "Account and Symbol Permissions \(permissions\)的直接链接")

  * `SPOT`



## Order status (status)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#order-status-status "Order status \(status\)的直接链接")

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
  
## Order List Status (listStatusType)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#order-list-status-liststatustype "Order List Status \(listStatusType\)的直接链接")

Status| Description  
---|---  
`RESPONSE`| This is used when the ListStatus is responding to a failed action. (E.g. order list placement or cancellation)  
`EXEC_STARTED`| The order list has been placed or there is an update to the order list status.  
`UPDATED`| The clientOrderId of an order in the order list has been changed.  
`ALL_DONE`| The order list has finished executing and thus is no longer active.  
  
## Order List Order Status (listOrderStatus)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#order-list-order-status-listorderstatus "Order List Order Status \(listOrderStatus\)的直接链接")

Status| Description  
---|---  
`EXECUTING`| Either an order list has been placed or there is an update to the status of the list.  
`ALL_DONE`| An order list has completed execution and thus no longer active.  
`REJECT`| The List Status is responding to a failed action either during order placement or order canceled.  
  
## ContingencyType[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#contingencytype "ContingencyType的直接链接")

  * `OCO`
  * `OTO`



## AllocationType[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#allocationtype "AllocationType的直接链接")

  * `SOR`



## Order types (orderTypes, type)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#order-types-ordertypes-type "Order types \(orderTypes, type\)的直接链接")

  * `LIMIT`
  * `MARKET`
  * `STOP_LOSS`
  * `STOP_LOSS_LIMIT`
  * `TAKE_PROFIT`
  * `TAKE_PROFIT_LIMIT`
  * `LIMIT_MAKER`



## Order Response Type (newOrderRespType)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#order-response-type-neworderresptype "Order Response Type \(newOrderRespType\)的直接链接")

  * `ACK`
  * `RESULT`
  * `FULL`



## Working Floor[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#working-floor "Working Floor的直接链接")

  * `EXCHANGE`
  * `SOR`



## Order side (side)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#order-side-side "Order side \(side\)的直接链接")

  * `BUY`
  * `SELL`



## Time in force (timeInForce)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#time-in-force-timeinforce "Time in force \(timeInForce\)的直接链接")

This sets how long an order will be active before expiration.

Status| Description  
---|---  
`GTC`| Good Til Canceled   
An order will be on the book unless the order is canceled.  
`IOC`| Immediate Or Cancel   
An order will try to fill the order as much as it can before the order expires.  
`FOK`| Fill or Kill   
An order will expire if the full order cannot be filled upon execution.  
  
## Rate limiters (rateLimitType)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#rate-limiters-ratelimittype "Rate limiters \(rateLimitType\)的直接链接")

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
    

## Rate limit intervals (interval)[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#rate-limit-intervals-interval "Rate limit intervals \(interval\)的直接链接")

  * SECOND
  * MINUTE
  * DAY



## STP Modes[​](/docs/zh-CN/binance-spot-api-docs/testnet/enums#stp-modes "STP Modes的直接链接")

Read [Self Trade Prevention (STP) FAQ](/docs/zh-CN/binance-spot-api-docs/faqs/stp_faq.md) to learn more.

  * `NONE`
  * `EXPIRE_MAKER`
  * `EXPIRE_TAKER`
  * `EXPIRE_BOTH`
  * `DECREMENT`
  * `TRANSFER`