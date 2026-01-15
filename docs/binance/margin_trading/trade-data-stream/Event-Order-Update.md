---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade-data-stream/Event-Order-Update
api_type: Trading
updated_at: 2026-01-15T23:48:39.890424
---

# Payload: Order update

## Event Description[​](/docs/margin_trading/trade-data-stream/Event-Order-Update#event-description "Direct link to Event Description")

Orders are updated with the `executionReport` event.

**Execution types:**

  * NEW - The order has been accepted into the engine.
  * CANCELED - The order has been canceled by the user.
  * REPLACED (currently unused)
  * REJECTED - The order has been rejected and was not processed (This message appears only with Cancel Replace Orders wherein the new order placement is rejected but the request to cancel request succeeds.)
  * TRADE - Part of the order or all of the order's quantity has filled.
  * EXPIRED - The order was canceled according to the order type's rules (e.g. LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill) or by the exchange, (e.g. orders canceled during liquidation, orders canceled during maintenance).
  * TRADE_PREVENTION - The order has expired due to STP trigger.



Check the [Public API Definitions](/docs/margin_trading/trade-data-stream/Event-Order-Update#public-api-definitions) for more relevant enum definitions.

These are fields that appear in the payload only if certain conditions are met.

Field | Name | Description | Examples  
---|---|---|---  
`d` | Trailing Delta | Appears only for trailing stop orders. | `"d": 4`  
`D` | Trailing Time | `"D": 1668680518494`  
`j` | Strategy Id | Appears only if the `strategyId` parameter was provided upon order placement. | `"j": 1`  
`J` | Strategy Type | Appears only if the `strategyType` parameter was provided upon order placement. | `"J": 1000000`  
`v` | Prevented Match Id | Appears only for orders that expired due to STP. | `"v": 3`  
`A` | Prevented Quantity | `"A":"3.000000"`  
`B` | Last Prevented Quantity | `"B":"3.000000"`  
`u` | Trade Group Id | `"u":1`  
`U` | Counter Order Id | `"U":37`  
`Cs` | Counter Symbol | `"Cs": "BTCUSDT"`  
`pl` | Prevented Execution Quantity | `"pl":"2.123456"`  
`pL` | Prevented Execution Price | `"pL":"0.10000001"`  
`pY` | Prevented Execution Quote Qty | `"pY":"0.21234562"`  
`W` | Working Time | Appears when the order is working on the book | `"W": 1668683798379`  
`b` | Match Type | Appears for orders that have allocations | `"b":"ONE_PARTY_TRADE_REPORT"`  
`a` | Allocation ID | `"a":1234`  
`k` | Working Floor | Appears for orders that could potentially have allocations | `"k":"SOR"`  
`uS` | UsedSor | Appears for orders that used SOR | `"uS":true`  
  
## Event Name[​](/docs/margin_trading/trade-data-stream/Event-Order-Update#event-name "Direct link to Event Name")

`executionReport`

## Response Example[​](/docs/margin_trading/trade-data-stream/Event-Order-Update#response-example "Direct link to Response Example")

> **Payload:**
    
    
    {  
      "e": "executionReport",        // Event type  
      "E": 1499405658658,            // Event time  
      "s": "ETHBTC",                 // Symbol  
      "c": "mUvoqJxFIILMdfAW5iGSOW", // Client order ID  
      "S": "BUY",                    // Side  
      "o": "LIMIT",                  // Order type  
      "f": "GTC",                    // Time in force  
      "q": "1.00000000",             // Order quantity  
      "p": "0.10264410",             // Order price  
      "P": "0.00000000",             // Stop price  
      "F": "0.00000000",             // Iceberg quantity  
      "g": -1,                       // OrderListId  
      "C": "",                       // Original client order ID; This is the ID of the order being canceled  
      "x": "NEW",                    // Current execution type  
      "X": "NEW",                    // Current order status  
      "r": "NONE",                   // Order reject reason; will be an error code.  
      "i": 4293153,                  // Order ID  
      "l": "0.00000000",             // Last executed quantity  
      "z": "0.00000000",             // Cumulative filled quantity  
      "L": "0.00000000",             // Last executed price  
      "n": "0",                      // Commission amount  
      "N": null,                     // Commission asset  
      "T": 1499405658657,            // Transaction time  
      "t": -1,                       // Trade ID  
      "I": 8641984,                  // Ignore  
      "w": true,                     // Is the order on the book?  
      "m": false,                    // Is this trade the maker side?  
      "M": false,                    // Ignore  
      "O": 1499405658657,            // Order creation time  
      "Z": "0.00000000",             // Cumulative quote asset transacted quantity  
      "Y": "0.00000000",             // Last quote asset transacted quantity (i.e. lastPrice * lastQty)  
      "Q": "0.00000000",             // Quote Order Quantity  
      "W": 1499405658657,            // Working Time; This is only visible if the order has been placed on the book.  
      "V": "NONE"                    // selfTradePreventionMode  
    }  
    

If the order is an OCO, an event will be displayed named `ListStatus` in addition to the `executionReport` event.
    
    
    {  
      "e": "listStatus",                //Event Type  
      "E": 1564035303637,               //Event Time  
      "s": "ETHBTC",                    //Symbol  
      "g": 2,                           //OrderListId  
      "c": "OCO",                       //Contingency Type  
      "l": "EXEC_STARTED",              //List Status Type  
      "L": "EXECUTING",                 //List Order Status  
      "r": "NONE",                      //List Reject Reason  
      "C": "F4QN4G8DlFATFlIUQ0cjdD",    //List Client Order ID  
      "T": 1564035303625,               //Transaction Time  
      "O": [                            //An array of objects  
        {  
          "s": "ETHBTC",                //Symbol  
          "i": 17,                      // orderId  
          "c": "AJYsMjErWJesZvqlJCTUgL" //ClientOrderId  
        },  
        {  
          "s": "ETHBTC",  
          "i": 18,  
          "c": "bfYPSQdLoqAJeNrOr9adzq"  
        }  
      ]  
    }

---

# 订单更新

## 事件描述[​](/docs/zh-CN/margin_trading/trade-data-stream/Event-Order-Update#事件描述 "事件描述的直接链接")

订单通过`executionReport`事件进行更新。

**执行类型:**

  * NEW - 新订单已被引擎接受。
  * CANCELED - 订单被用户取消。
  * REPLACED - (保留字段，当前未使用)
  * REJECTED - 新订单被拒绝 （这信息只会在撤消挂单再下单中发生，下新订单被拒绝但撤消挂单请求成功）。
  * TRADE - 订单有新成交。
  * EXPIRED - 订单已根据 Time In Force 参数的规则取消（e.g. 没有成交的 LIMIT FOK 订单或部分成交的 LIMIT IOC 订单）或者被交易所取消（e.g. 强平或维护期间取消的订单）。
  * TRADE_PREVENTION - 订单因 STP 触发而过期。



请查阅[公开API参数](/docs/zh-CN/margin_trading/trade-data-stream/Event-Order-Update#public-api-definitions)文档获取更多枚举定义。

**备注:** 通过将`Z`除以`z`可以找到平均价格。

如果订单是OCO，则除了显示`executionReport`事件外，还将显示一个名为`ListStatus`的事件。

### `executionReport` 中的仅在满足特定条件时才会出现的字段：[​](/docs/zh-CN/margin_trading/trade-data-stream/Event-Order-Update#executionreport-中的仅在满足特定条件时才会出现的字段 "executionreport-中的仅在满足特定条件时才会出现的字段的直接链接")

字段 | 名称 | 描述 | 示例  
---|---|---|---  
`d` | Trailing Delta | 出现在追踪止损订单中。 | `"d": 4`  
`D` | Trailing Time | `"D": 1668680518494`  
`j` | Strategy Id | 如果在请求中添加了`strategyId`参数，则会出现。 | `"j": 1`  
`J` | Strategy Type | 如果在请求中添加了`strategyType`参数，则会出现。 | `"J": 1000000`  
`v` | Prevented Match Id | 只有在因为 STP 导致订单失效时可见。 | `"v": 3`  
`A` | Prevented Quantity | `"A":"3.000000"`  
`B` | Last Prevented Quantity | `"B":"3.000000"`  
`u` | Trade Group Id | `"u":1`  
`U` | Counter Order Id | `"U":37`  
`Cs` | Counter Symbol | `"Cs": "BTCUSDT"`  
`pl` | Prevented Execution Quantity | `"pl":"2.123456"`  
`pL` | Prevented Execution Price | `"pL":"0.10000001"`  
`pY` | Prevented Execution Quote Qty | `"pY":"0.21234562"`  
`W` | Working Time | 只有在订单在订单簿上时可见 | `"W": 1668683798379`  
`b` | Match Type | 只有在订单有分配时可见 | `"b":"ONE_PARTY_TRADE_REPORT"`  
`a` | Allocation ID | `"a":1234`  
`k` | Working Floor | 只有在订单可能有分配时可见 | `"k":"SOR"`  
`uS` | UsedSor | 只有在订单使用 SOR 时可见 | `"uS":true`  
  
## 事件类型[​](/docs/zh-CN/margin_trading/trade-data-stream/Event-Order-Update#事件类型 "事件类型的直接链接")

`executionReport`

## 响应示例[​](/docs/zh-CN/margin_trading/trade-data-stream/Event-Order-Update#响应示例 "响应示例的直接链接")
    
    
    {  
      "e": "executionReport",        // 事件类型  
      "E": 1499405658658,            // 事件时间  
      "s": "ETHBTC",                 // 交易对  
      "c": "mUvoqJxFIILMdfAW5iGSOW", // clientOrderId  
      "S": "BUY",                    // 订单方向  
      "o": "LIMIT",                  // 订单类型  
      "f": "GTC",                    // 有效方式  
      "q": "1.00000000",             // 订单原始数量  
      "p": "0.10264410",             // 订单原始价格  
      "P": "0.00000000",             // 止盈止损单触发价格  
      "F": "0.00000000",             // 冰山订单数量  
      "g": -1,                       // OCO订单 OrderListId  
      "C": "",                       // 原始订单自定义ID(原始订单，指撤单操作的对象。撤单本身被视为另一个订单)  
      "x": "NEW",                    // 本次事件的具体执行类型  
      "X": "NEW",                    // 订单的当前状态  
      "r": "NONE",                   // 订单被拒绝的原因  
      "i": 4293153,                  // orderId  
      "l": "0.00000000",             // 订单末次成交量  
      "z": "0.00000000",             // 订单累计已成交量  
      "L": "0.00000000",             // 订单末次成交价格  
      "n": "0",                      // 手续费数量  
      "N": null,                     // 手续费资产类别  
      "T": 1499405658657,            // 成交时间  
      "t": -1,                       // 成交ID  
      "v": 3,                        // 被阻止撮合交易的ID; 这仅在订单因 STP 触发而过期时可见  
      "I": 8641984,                  // 请忽略  
      "w": true,                     // 订单是否在订单簿上？  
      "m": false,                    // 该成交是作为挂单成交吗？  
      "M": false,                    // 请忽略  
      "O": 1499405658657,            // 订单创建时间  
      "Z": "0.00000000",             // 订单累计已成交金额  
      "Y": "0.00000000",             // 订单末次成交金额  
      "Q": "0.00000000",             // Quote Order Quantity  
      "W": 1499405658657,            // Working Time; 订单被添加到 order book 的时间  
      "V": "NONE"                    // SelfTradePreventionMode  
    }  
    

如果订单是OCO，则除了显示`executionReport`事件外，还将显示一个名为`ListStatus`的事件。
    
    
    {  
      "e": "listStatus",                // 事件类型  
      "E": 1564035303637,               // 事件时间  
      "s": "ETHBTC",                    // 交易对  
      "g": 2,                           // OrderListId  
      "c": "OCO",                       // Contingency Type  
      "l": "EXEC_STARTED",              // List Status Type  
      "L": "EXECUTING",                 // List Order Status  
      "r": "NONE",                      // List 被拒绝的原因  
      "C": "F4QN4G8DlFATFlIUQ0cjdD",    // List Client Order ID  
      "T": 1564035303625,               // 成交时间  
      "O": [                             
        {  
          "s": "ETHBTC",                // 交易对  
          "i": 17,                      // orderId  
          "c": "AJYsMjErWJesZvqlJCTUgL" // clientOrderId  
        },  
        {  
          "s": "ETHBTC",  
          "i": 18,  
          "c": "bfYPSQdLoqAJeNrOr9adzq"  
        }  
      ]  
    }