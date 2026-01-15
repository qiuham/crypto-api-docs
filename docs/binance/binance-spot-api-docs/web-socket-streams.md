---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams
api_type: WebSocket
updated_at: 2026-01-15T23:37:08.328524
---

# WebSocket Streams for Binance

## General WSS information[​](/docs/binance-spot-api-docs/web-socket-streams#general-wss-information "Direct link to General WSS information")

  * The base endpoint is: **wss://stream.binance.com:9443** or **wss://stream.binance.com:443**.
  * Streams can be accessed either in a single raw stream or in a combined stream.
  * Raw streams are accessed at **/ws/ <streamName>**
  * Combined streams are accessed at **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
  * Combined stream events are wrapped as follows: **{"stream":" <streamName>","data":<rawPayload>}**
  * All symbols for streams are **lowercase**
  * A single connection to **stream.binance.com** is only valid for 24 hours; expect to be disconnected at the 24 hour mark
  * The WebSocket server will send a `ping frame` every 20 seconds. 
    * If the WebSocket server does not receive a `pong frame` back from the connection within a minute the connection will be disconnected.
    * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
    * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**
  * The base endpoint **wss://data-stream.binance.vision** can be subscribed to receive **only** market data messages.   
User data stream is **NOT** available from this URL.
  * All time and timestamp related fields are **milliseconds by default**. To receive the information in microseconds, please add the parameter `timeUnit=MICROSECOND or timeUnit=microsecond` in the URL. 
    * For example: `/stream?streams=btcusdt@trade&timeUnit=MICROSECOND`
  * If your request contains a symbol name containing non-ASCII characters, then the stream events may contain non-ASCII characters encoded in UTF-8.
  * [All Market Mini Tickers Stream](#all-market-mini-tickers-stream and [All Market Rolling Window Statistics Streams](/docs/binance-spot-api-docs/web-socket-streams#all-market-rolling-window-statistics-streams) events may contain non-ASCII characters encoded in UTF-8.



## WebSocket Limits[​](/docs/binance-spot-api-docs/web-socket-streams#websocket-limits "Direct link to WebSocket Limits")

  * WebSocket connections have a limit of 5 incoming messages per second. A message is considered: 
    * A PING frame
    * A PONG frame
    * A JSON controlled message (e.g. subscribe, unsubscribe)
  * A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
  * A single connection can listen to a maximum of 1024 streams.
  * There is a limit of **300 connections per attempt every 5 minutes per IP**.



## Live Subscribing/Unsubscribing to streams[​](/docs/binance-spot-api-docs/web-socket-streams#live-subscribingunsubscribing-to-streams "Direct link to Live Subscribing/Unsubscribing to streams")

  * The following data can be sent through the WebSocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
  * The `id` is used as an identifier to uniquely identify the messages going back and forth. The following formats are accepted: 
    * 64-bit signed integer
    * alphanumeric strings; max length 36
    * `null`
  * In the response, if the `result` received is `null` this means the request sent was a success for non-query requests (e.g. Subscribing/Unsubscribing).



### Subscribe to a stream[​](/docs/binance-spot-api-docs/web-socket-streams#subscribe-to-a-stream "Direct link to Subscribe to a stream")

  * Request
        
        {  
            "method": "SUBSCRIBE",  
            "params": ["btcusdt@aggTrade", "btcusdt@depth"],  
            "id": 1  
        }  
        

  * Response
        
        {  
            "result": null,  
            "id": 1  
        }  
        




### Unsubscribe to a stream[​](/docs/binance-spot-api-docs/web-socket-streams#unsubscribe-to-a-stream "Direct link to Unsubscribe to a stream")

  * Request
        
        {  
            "method": "UNSUBSCRIBE",  
            "params": ["btcusdt@depth"],  
            "id": 312  
        }  
        

  * Response
        
        {  
            "result": null,  
            "id": 312  
        }  
        




### Listing Subscriptions[​](/docs/binance-spot-api-docs/web-socket-streams#listing-subscriptions "Direct link to Listing Subscriptions")

  * Request
        
        {  
            "method": "LIST_SUBSCRIPTIONS",  
            "id": 3  
        }  
        

  * Response
        
        {  
            "result": ["btcusdt@aggTrade"],  
            "id": 3  
        }  
        




### Setting Properties[​](/docs/binance-spot-api-docs/web-socket-streams#setting-properties "Direct link to Setting Properties")

Currently, the only property that can be set is whether `combined` stream payloads are enabled or not. The combined property is set to `false` when connecting using `/ws/` ("raw streams") and `true` when connecting using `/stream/`.

  * Request
        
        {  
            "method": "SET_PROPERTY",  
            "params": ["combined", true],  
            "id": 5  
        }  
        

  * Response
        
        {  
            "result": null,  
            "id": 5  
        }  
        




### Retrieving Properties[​](/docs/binance-spot-api-docs/web-socket-streams#retrieving-properties "Direct link to Retrieving Properties")

  * Request
        
        {  
            "method": "GET_PROPERTY",  
            "params": ["combined"],  
            "id": 2  
        }  
        

  * Response
        
        {  
            "result": true, // Indicates that combined is set to true.  
            "id": 2  
        }  
        




### Error Messages[​](/docs/binance-spot-api-docs/web-socket-streams#error-messages "Direct link to Error Messages")

Error Message| Description  
---|---  
{"code": 0, "msg": "Unknown property","id": %s}| Parameter used in the `SET_PROPERTY` or `GET_PROPERTY` was invalid  
{"code": 1, "msg": "Invalid value type: expected Boolean"}| Value should only be `true` or `false`  
{"code": 2, "msg": "Invalid request: property name must be a string"}| Property name provided was invalid  
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}| Parameter `id` had to be provided or the value provided in the `id` parameter is an unsupported type  
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one of `SUBSCRIBE`, `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, `GET_PROPERTY` at line 1 column 28"}| Possible typo in the provided method or provided method was neither of the expected values  
{"code": 2, "msg": "Invalid request: too many parameters"}| Unnecessary parameters provided in the data  
{"code": 2, "msg": "Invalid request: property name must be a string"}| Property name was not provided  
{"code": 2, "msg": "Invalid request: missing field `method` at line 1 column 73"}| `method` was not provided in the data  
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"}| JSON data sent has incorrect syntax.  
  
# Detailed Stream information

## Aggregate Trade Streams[​](/docs/binance-spot-api-docs/web-socket-streams#aggregate-trade-streams "Direct link to Aggregate Trade Streams")

The Aggregate Trade Streams push trade information that is aggregated for a single taker order.

**Stream Name:** <symbol>@aggTrade

**Update Speed:** Real-time

**Payload:**
    
    
    {  
        "e": "aggTrade",        // Event type  
        "E": 1672515782136,     // Event time  
        "s": "BNBBTC",          // Symbol  
        "a": 12345,             // Aggregate trade ID  
        "p": "0.001",           // Price  
        "q": "100",             // Quantity  
        "f": 100,               // First trade ID  
        "l": 105,               // Last trade ID  
        "T": 1672515782136,     // Trade time  
        "m": true,              // Is the buyer the market maker?  
        "M": true               // Ignore  
    }  
    

## Trade Streams[​](/docs/binance-spot-api-docs/web-socket-streams#trade-streams "Direct link to Trade Streams")

The Trade Streams push raw trade information; each trade has a unique buyer and seller.

**Stream Name:** <symbol>@trade

**Update Speed:** Real-time

**Payload:**
    
    
    {  
        "e": "trade",           // Event type  
        "E": 1672515782136,     // Event time  
        "s": "BNBBTC",          // Symbol  
        "t": 12345,             // Trade ID  
        "p": "0.001",           // Price  
        "q": "100",             // Quantity  
        "T": 1672515782136,     // Trade time  
        "m": true,              // Is the buyer the market maker?  
        "M": true               // Ignore  
    }  
    

## Kline/Candlestick Streams for UTC[​](/docs/binance-spot-api-docs/web-socket-streams#klinecandlestick-streams-for-utc "Direct link to Kline/Candlestick Streams for UTC")

The Kline/Candlestick Stream push updates to the current klines/candlestick every second in `UTC+0` timezone

**Kline/Candlestick chart intervals:**

s-> seconds; m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

  * 1s
  * 1m
  * 3m
  * 5m
  * 15m
  * 30m
  * 1h
  * 2h
  * 4h
  * 6h
  * 8h
  * 12h
  * 1d
  * 3d
  * 1w
  * 1M



**Stream Name:** <symbol>@kline_<interval>

**Update Speed:** 1000ms for `1s`, 2000ms for the other intervals

**Payload:**
    
    
    {  
        "e": "kline",               // Event type  
        "E": 1672515782136,         // Event time  
        "s": "BNBBTC",              // Symbol  
        "k": {  
            "t": 1672515780000,     // Kline start time  
            "T": 1672515839999,     // Kline close time  
            "s": "BNBBTC",          // Symbol  
            "i": "1m",              // Interval  
            "f": 100,               // First trade ID  
            "L": 200,               // Last trade ID  
            "o": "0.0010",          // Open price  
            "c": "0.0020",          // Close price  
            "h": "0.0025",          // High price  
            "l": "0.0015",          // Low price  
            "v": "1000",            // Base asset volume  
            "n": 100,               // Number of trades  
            "x": false,             // Is this kline closed?  
            "q": "1.0000",          // Quote asset volume  
            "V": "500",             // Taker buy base asset volume  
            "Q": "0.500",           // Taker buy quote asset volume  
            "B": "123456"           // Ignore  
        }  
    }  
    

## Kline/Candlestick Streams with timezone offset[​](/docs/binance-spot-api-docs/web-socket-streams#klinecandlestick-streams-with-timezone-offset "Direct link to Kline/Candlestick Streams with timezone offset")

The Kline/Candlestick Stream push updates to the current klines/candlestick every second in `UTC+8` timezone

**Kline/Candlestick chart intervals:**

Supported intervals: See [`Kline/Candlestick chart intervals`](/docs/binance-spot-api-docs/web-socket-streams#kline-intervals)

**UTC+8 timezone offset:**

  * Kline intervals open and close in the `UTC+8` timezone. For example the `1d` klines will open at the beginning of the `UTC+8` day, and close at the end of the `UTC+8` day.
  * Note that `E` (event time), `t` (start time) and `T` (close time) in the payload are Unix timestamps, which are always interpreted in UTC.



**Stream Name:** <symbol>@kline_<interval>@+08:00

**Update Speed:** 1000ms for `1s`, 2000ms for the other intervals

**Payload:**
    
    
    {  
        "e": "kline",               // Event type  
        "E": 1672515782136,         // Event time  
        "s": "BNBBTC",              // Symbol  
        "k": {  
            "t": 1672515780000,     // Kline start time  
            "T": 1672515839999,     // Kline close time  
            "s": "BNBBTC",          // Symbol  
            "i": "1m",              // Interval  
            "f": 100,               // First trade ID  
            "L": 200,               // Last trade ID  
            "o": "0.0010",          // Open price  
            "c": "0.0020",          // Close price  
            "h": "0.0025",          // High price  
            "l": "0.0015",          // Low price  
            "v": "1000",            // Base asset volume  
            "n": 100,               // Number of trades  
            "x": false,             // Is this kline closed?  
            "q": "1.0000",          // Quote asset volume  
            "V": "500",             // Taker buy base asset volume  
            "Q": "0.500",           // Taker buy quote asset volume  
            "B": "123456"           // Ignore  
        }  
    }  
    

## Individual Symbol Mini Ticker Stream[​](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream "Direct link to Individual Symbol Mini Ticker Stream")

24hr rolling window mini-ticker statistics. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

**Stream Name:** <symbol>@miniTicker

**Update Speed:** 1000ms

**Payload:**
    
    
    {  
        "e": "24hrMiniTicker",     // Event type  
        "E": 1672515782136,        // Event time  
        "s": "BNBBTC",             // Symbol  
        "c": "0.0025",             // Close price  
        "o": "0.0010",             // Open price  
        "h": "0.0025",             // High price  
        "l": "0.0010",             // Low price  
        "v": "10000",              // Total traded base asset volume  
        "q": "18"                  // Total traded quote asset volume  
    }  
    

## All Market Mini Tickers Stream[​](/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream "Direct link to All Market Mini Tickers Stream")

24hr rolling window mini-ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

**Stream Name:** !miniTicker@arr

**Update Speed:** 1000ms

**Payload:**
    
    
    [  
        {  
            // Same as <symbol>@miniTicker payload  
        }  
    ]  
    

## Individual Symbol Ticker Streams[​](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-ticker-streams "Direct link to Individual Symbol Ticker Streams")

24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

**Stream Name:** <symbol>@ticker

**Update Speed:** 1000ms

**Payload:**
    
    
    {  
        "e": "24hrTicker",      // Event type  
        "E": 1672515782136,     // Event time  
        "s": "BNBBTC",          // Symbol  
        "p": "0.0015",          // Price change  
        "P": "250.00",          // Price change percent  
        "w": "0.0018",          // Weighted average price  
        "x": "0.0009",          // First trade(F)-1 price (first trade before the 24hr rolling window)  
        "c": "0.0025",          // Last price  
        "Q": "10",              // Last quantity  
        "b": "0.0024",          // Best bid price  
        "B": "10",              // Best bid quantity  
        "a": "0.0026",          // Best ask price  
        "A": "100",             // Best ask quantity  
        "o": "0.0010",          // Open price  
        "h": "0.0025",          // High price  
        "l": "0.0010",          // Low price  
        "v": "10000",           // Total traded base asset volume  
        "q": "18",              // Total traded quote asset volume  
        "O": 0,                 // Statistics open time  
        "C": 86400000,          // Statistics close time  
        "F": 0,                 // First trade ID  
        "L": 18150,             // Last trade Id  
        "n": 18151              // Total number of trades  
    }  
    

## Individual Symbol Rolling Window Statistics Streams[​](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-rolling-window-statistics-streams "Direct link to Individual Symbol Rolling Window Statistics Streams")

Rolling window ticker statistics for a single symbol, computed over multiple windows.

**Stream Name:** <symbol>@ticker_<window_size>

**Window Sizes:** 1h,4h,1d

**Update Speed:** 1000ms

**Note** : This stream is different from the <symbol>@ticker stream. The open time `"O"` always starts on a minute, while the closing time `"C"` is the current time of the update. As such, the effective window might be up to 59999ms wider than <window_size>.

**Payload:**
    
    
    {  
        "e": "1hTicker",        // Event type  
        "E": 1672515782136,     // Event time  
        "s": "BNBBTC",          // Symbol  
        "p": "0.0015",          // Price change  
        "P": "250.00",          // Price change percent  
        "o": "0.0010",          // Open price  
        "h": "0.0025",          // High price  
        "l": "0.0010",          // Low price  
        "c": "0.0025",          // Last price  
        "w": "0.0018",          // Weighted average price  
        "v": "10000",           // Total traded base asset volume  
        "q": "18",              // Total traded quote asset volume  
        "O": 0,                 // Statistics open time  
        "C": 1675216573749,     // Statistics close time  
        "F": 0,                 // First trade ID  
        "L": 18150,             // Last trade Id  
        "n": 18151              // Total number of trades  
    }  
    

## All Market Rolling Window Statistics Streams[​](/docs/binance-spot-api-docs/web-socket-streams#all-market-rolling-window-statistics-streams "Direct link to All Market Rolling Window Statistics Streams")

Rolling window ticker statistics for all market symbols, computed over multiple windows. Note that only tickers that have changed will be present in the array.

**Stream Name:** !ticker_<window-size>@arr

**Window Size:** 1h,4h,1d

**Update Speed:** 1000ms

**Payload:**
    
    
    [  
        {  
            // Same as <symbol>@ticker_<window_size> payload,  
            // one for each symbol updated within the interval.  
        }  
    ]  
    

## Individual Symbol Book Ticker Streams[​](/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-book-ticker-streams "Direct link to Individual Symbol Book Ticker Streams")

Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol. Multiple `<symbol>@bookTicker` streams can be subscribed to over one connection.

**Stream Name:** <symbol>@bookTicker

**Update Speed:** Real-time

**Payload:**
    
    
    {  
        "u": 400900217,         // order book updateId  
        "s": "BNBUSDT",         // symbol  
        "b": "25.35190000",     // best bid price  
        "B": "31.21000000",     // best bid qty  
        "a": "25.36520000",     // best ask price  
        "A": "40.66000000"      // best ask qty  
    }  
    

## Average Price[​](/docs/binance-spot-api-docs/web-socket-streams#average-price "Direct link to Average Price")

Average price streams push changes in the average price over a fixed time interval.

**Stream Name:** <symbol>@avgPrice

**Update Speed:** 1000ms

**Payload:**
    
    
    {  
        "e": "avgPrice",           // Event type  
        "E": 1693907033000,        // Event time  
        "s": "BTCUSDT",            // Symbol  
        "i": "5m",                 // Average price interval  
        "w": "25776.86000000",     // Average price  
        "T": 1693907032213         // Last trade time  
    }  
    

## Partial Book Depth Streams[​](/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams "Direct link to Partial Book Depth Streams")

Top **< levels>** bids and asks, pushed every second. Valid **< levels>** are 5, 10, or 20.

**Stream Names:** <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms

**Update Speed:** 1000ms or 100ms

**Payload:**
    
    
    {  
        "lastUpdateId": 160,     // Last update ID  
        "bids": [                // Bids to be updated  
            [  
                "0.0024",        // Price level to be updated  
                "10"             // Quantity  
            ]  
        ],  
        "asks": [                // Asks to be updated  
            [  
                "0.0026",        // Price level to be updated  
                "100"            // Quantity  
            ]  
        ]  
    }  
    

## Diff. Depth Stream[​](/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream "Direct link to Diff. Depth Stream")

Order book price and quantity depth updates used to locally manage an order book.

**Stream Name:** <symbol>@depth OR <symbol>@depth@100ms

**Update Speed:** 1000ms or 100ms

**Payload:**
    
    
    {  
        "e": "depthUpdate",     // Event type  
        "E": 1672515782136,     // Event time  
        "s": "BNBBTC",          // Symbol  
        "U": 157,               // First update ID in event  
        "u": 160,               // Final update ID in event  
        "b": [                  // Bids to be updated  
            [  
                "0.0024",       // Price level to be updated  
                "10"            // Quantity  
            ]  
        ],  
        "a": [                  // Asks to be updated  
            [  
                "0.0026",       // Price level to be updated  
                "100"           // Quantity  
            ]  
        ]  
    }  
    

## How to manage a local order book correctly[​](/docs/binance-spot-api-docs/web-socket-streams#how-to-manage-a-local-order-book-correctly "Direct link to How to manage a local order book correctly")

  1. Open a WebSocket connection to `wss://stream.binance.com:9443/ws/bnbbtc@depth`.
  2. Buffer the events received from the stream. Note the `U` of the first event you received.
  3. Get a depth snapshot from `https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=5000`.
  4. If the `lastUpdateId` from the snapshot is strictly less than the `U` from step 2, go back to step 3.
  5. In the buffered events, discard any event where `u` is <= `lastUpdateId` of the snapshot. The first buffered event should now have `lastUpdateId` within its `[U;u]` range.
  6. Set your local order book to the snapshot. Its update ID is `lastUpdateId`.
  7. Apply the update procedure below to all buffered events, and then to all subsequent events received.



To apply an event to your local order book, follow this update procedure:

  1. Decide whether the update event can be applied: 
     * If the event last update ID (`u`) is less than the update ID of your local order book, ignore the event.
     * If the event first update ID (`U`) is greater than the update ID of your local order book + 1, you have missed some events.   
Discard your local order book and restart the process from the beginning.
     * Normally, `U` of the next event is equal to `u + 1` of the previous event.
  2. For each price level in bids (`b`) and asks (`a`), set the new quantity in the order book: 
     * If the price level does not exist in the order book, insert it with new quantity.
     * If the quantity is zero, remove the price level from the order book.
  3. Set the order book update ID to the last update ID (`u`) in the processed event.



> [!NOTE] Since depth snapshots retrieved from the API have a limit on the number of price levels (5000 on each side maximum), you won't learn the quantities for the levels outside of the initial snapshot unless they change.   
>  So be careful when using the information for those levels, since they might not reflect the full view of the order book.   
>  However, for most use cases, seeing 5000 levels on each side is enough to understand the market and trade effectively.

---

# WebSocket 行情接口

## 基本信息[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#基本信息 "基本信息的直接链接")

  * 本篇所列出的所有wss接口的baseurl为: **wss://stream.binance.com:9443** 或者 **wss://stream.binance.com:443**
  * 所有stream均可以直接访问，或者作为组合streams的一部分。
  * 直接访问时URL格式为 **/ws/ <streamName>**
  * 组合streams的URL格式为 **/stream?streams= <streamName1>/<streamName2>/<streamName3>**
  * 订阅组合streams时，事件payload会以这样的格式封装 **{"stream":" <streamName>","data":<rawPayload>}**
  * stream名称中所有交易对均为**小写**
  * 每个到**stream.binance.com** 的链接有效期不超过24小时，请妥善处理断线重连。
  * WebSocket 服务器**每20秒** 发送 PING 消息。 
    * 如果 WebSocket 服务器没有在一分钟之内收到PONG 消息应答，连接会被断开。
    * 当客户收到PING消息，必须尽快回复PONG消息，同时payload需要和PING消息一致。
    * 服务器允许未经请求的PONG消息，但这不会保证连接不断开。**对于这些PONG 消息，建议payload为空。**
  * **wss://data-stream.binance.vision** 可以用来订阅仅有市场信息的数据流。账户信息**无法** 从此URL获得。
  * 所有时间和时间戳相关字段均以**毫秒为默认单位** 。 要以微秒为单位接收信息，请在 URL 中添加参数 `timeUnit=MICROSECOND` 或 `timeUnit=microsecond`。 
    * 例如： `/stream?streams=btcusdt@trade&timeUnit=MICROSECOND`
  * 如果您的请求包含非 ASCII 字符的交易对名称，那么数据流事件中可能包含以 UTF-8 编码的非 ASCII 字符。
  * [全市场所有 Symbol 的精简 Ticker](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#all-markets-mini-ticker) 和 [全市场滚动窗口统计](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#all-market-rolling-window-ticker) 事件可能包含以 UTF-8 编码的非 ASCII 字符。



## WebSocket 连接限制[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#websocket-连接限制 "WebSocket 连接限制的直接链接")

  * WebSocket服务器每秒最多接受5个消息。消息包括: 
    * PING帧
    * PONG帧
    * JSON格式的消息, 比如订阅, 断开订阅.
  * 如果用户发送的消息超过限制，连接会被断开连接。反复被断开连接的IP有可能被服务器屏蔽。
  * 单个连接最多可以订阅1024个Streams。
  * 每IP地址、每5分钟最多可以发送300次连接请求。



## 实时订阅/取消数据流[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#实时订阅取消数据流 "实时订阅/取消数据流的直接链接")

  * 以下数据可以通过 WebSocket 发送以实现订阅或取消订阅数据流。示例如下.
  * 请求中的`id`被用作唯一标识来区分来回传递的消息。以下格式被接受: 
    * 64位有符号整数
    * 字母数字字符串；最大长度36
    * `null`
  * 如果相应内容中的`result` 为 `null`，表示请求发送成功。



### 订阅一个信息流[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#订阅一个信息流 "订阅一个信息流的直接链接")

  * 请求
        
        {  
            "method": "SUBSCRIBE",  
            "params": ["btcusdt@aggTrade", "btcusdt@depth"],  
            "id": 1  
        }  
        

  * 响应
        
        {  
            "result": null,  
            "id": 1  
        }  
        




### 取消订阅一个信息流[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#取消订阅一个信息流 "取消订阅一个信息流的直接链接")

  * 请求
        
        {  
            "method": "UNSUBSCRIBE",  
            "params": ["btcusdt@depth"],  
            "id": 312  
        }  
        

  * 响应
        
        {  
            "result": null,  
            "id": 312  
        }  
        




### 已订阅信息流[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#已订阅信息流 "已订阅信息流的直接链接")

  * 请求
        
        {  
            "method": "LIST_SUBSCRIPTIONS",  
            "id": 3  
        }  
        

  * 响应
        
        {  
            "result": ["btcusdt@aggTrade"],  
            "id": 3  
        }  
        




### 设定属性[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#设定属性 "设定属性的直接链接")

当前，唯一可以设置的属性是设置是否启用`combined`("组合")信息流。 当使用`/ws/`("原始信息流")进行连接时，combined属性设置为`false`，而使用 `/stream/`进行连接时则将属性设置为`true`。

  * 请求
        
        {  
            "method": "SET_PROPERTY",  
            "params": ["combined", true],  
            "id": 5  
        }  
        

  * 响应
        
        {  
            "result": null,  
            "id": 5  
        }  
        




### 检索属性[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#检索属性 "检索属性的直接链接")

  * 请求
        
        {  
            "method": "GET_PROPERTY",  
            "params": ["combined"],  
            "id": 2  
        }  
        

  * 响应
        
        {  
            "result": true, // Indicates that combined is set to true.  
            "id": 2  
        }  
        




### 错误信息[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#错误信息 "错误信息的直接链接")

错误信息| 描述  
---|---  
{"code": 0, "msg": "Unknown property","id": %s}| `SET_PROPERTY` 或 `GET_PROPERTY`中应用的参数无效  
{"code": 1, "msg": "Invalid value type: expected Boolean"}| 仅接受`true`或`false`  
{"code": 2, "msg": "Invalid request: property name must be a string"}| 提供的属性名无效  
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}| 参数`id`未提供或`id`值是无效类型  
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one of `SUBSCRIBE`, `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, `GET_PROPERTY` at line 1 column 28"}| 错字提醒，或提供的值不是预期类型  
{"code": 2, "msg": "Invalid request: too many parameters"}| 数据中提供了不必要参数  
{"code": 2, "msg": "Invalid request: property name must be a string"}| 未提供属性名  
{"code": 2, "msg": "Invalid request: missing field `method` at line 1 column 73"}| 数据未提供`method`  
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"}| JSON 语法有误.  
  
# Stream 详细定义

## 归集交易[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#归集交易 "归集交易的直接链接")

归集交易与逐笔交易的区别在于，同一个taker在同一价格与多个maker成交时，会被归集为一笔成交。

**Stream 名称:** <symbol>@aggTrade

**更新速度:** 实时

**Payload:**
    
    
    {  
        "e": "aggTrade",        // 事件类型  
        "E": 1672515782136,     // 事件时间  
        "s": "BNBBTC",          // 交易对  
        "a": 12345,             // 归集交易ID  
        "p": "0.001",           // 成交价格  
        "q": "100",             // 成交数量  
        "f": 100,               // 被归集的首个交易ID  
        "l": 105,               // 被归集的末次交易ID  
        "T": 1672515782136,     // 成交时间  
        "m": true,              // 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。  
        "M": true               // 请忽略该字段  
    }  
    

## 逐笔交易[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#逐笔交易 "逐笔交易的直接链接")

逐笔交易推送每一笔成交的信息。**成交** ，或者说交易的定义是仅有一个吃单者与一个挂单者相互交易。

**Stream 名称:** <symbol>@trade

**更新速度:** 实时

**Payload:**
    
    
    {  
        "e": "trade",           // 事件类型  
        "E": 1672515782136,     // 事件时间  
        "s": "BNBBTC",          // 交易对  
        "t": 12345,             // 交易ID  
        "p": "0.001",           // 成交价格  
        "q": "100",             // 成交数量  
        "T": 1672515782136,     // 成交时间  
        "m": true,              // 买方是否是做市方。如true，则此次成交是一个主动卖出单，否则是一个主动买入单。  
        "M": true               // 请忽略该字段  
    }  
    

## UTC K线[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#utc-k��线 "UTC K线的直接链接")

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。此更新是基于 `UTC+0` 时区的。

**订阅Kline需要提供间隔参数，最短为分钟线，最长为月线。支持以下间隔:**

m -> 分钟; h -> 小时; d -> 天; w -> 周; M -> 月

  * 1m
  * 3m
  * 5m
  * 15m
  * 30m
  * 1h
  * 2h
  * 4h
  * 6h
  * 8h
  * 12h
  * 1d
  * 3d
  * 1w
  * 1M



**Stream 名称:** <symbol>@kline_<interval>

**更新速度:** `1s` 1000ms，其它间隔 2000ms

**Payload:**
    
    
    {  
        "e": "kline",               // 事件类型  
        "E": 1672515782136,         // 事件时间  
        "s": "BNBBTC",              // 交易对  
        "k": {  
            "t": 1672515780000,     // 这根K线的起始时间  
            "T": 1672515839999,     // 这根K线的结束时间  
            "s": "BNBBTC",          // 交易对  
            "i": "1m",              // K线间隔  
            "f": 100,               // 这根K线期间第一笔成交ID  
            "L": 200,               // 这根K线期间末一笔成交ID  
            "o": "0.0010",          // 这根K线期间第一笔成交价  
            "c": "0.0020",          // 这根K线期间末一笔成交价  
            "h": "0.0025",          // 这根K线期间最高成交价  
            "l": "0.0015",          // 这根K线期间最低成交价  
            "v": "1000",            // 这根K线期间成交量  
            "n": 100,               // 这根K线期间成交数量  
            "x": false,             // 这根K线是否完结（是否已经开始下一根K线）  
            "q": "1.0000",          // 这根K线期间成交额  
            "V": "500",             // 主动买入的成交量  
            "Q": "0.500",           // 主动买入的成交额  
            "B": "123456"           // 忽略此参数  
        }  
    }  
    

## 带有时区偏移量的K线[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#带有时区偏移量的k线 "带有时区偏移量的K线的直接链接")

K线stream逐秒推送所请求的K线种类(最新一根K线)的更新。此更新是基于 `UTC+8` 时区的。

**订阅Kline需要提供的间隔参数:**

参考 [`Kline所支持的间隔参数`](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#kline-intervals)

**UTC+8 时区偏移量：**

  * K线间隔的开始和结束时间会基于 `UTC+8` 时区。例如， `1d` K线将在 `UTC+8` 当天开始，并在 `UTC+8` 当日完结时随之结束。
  * 请注意，Payload中的 `E`（event time），`t`（start time）和 `T`（close time）是 Unix 时间戳，它们始终以 UTC 格式解释。



**Stream 名称:** <symbol>@kline_<interval>@+08:00

**更新速度:** `1s` 1000ms，其它间隔 2000ms

**Payload:**
    
    
    {  
        "e": "kline",               // Event type  
        "E": 1672515782136,         // Event time  
        "s": "BNBBTC",              // Symbol  
        "k": {  
            "t": 1672515780000,     // Kline start time  
            "T": 1672515839999,     // Kline close time  
            "s": "BNBBTC",          // Symbol  
            "i": "1m",              // Interval  
            "f": 100,               // First trade ID  
            "L": 200,               // Last trade ID  
            "o": "0.0010",          // Open price  
            "c": "0.0020",          // Close price  
            "h": "0.0025",          // High price  
            "l": "0.0015",          // Low price  
            "v": "1000",            // Base asset volume  
            "n": 100,               // Number of trades  
            "x": false,             // Is this kline closed?  
            "q": "1.0000",          // Quote asset volume  
            "V": "500",             // Taker buy base asset volume  
            "Q": "0.500",           // Taker buy quote asset volume  
            "B": "123456"           // Ignore  
        }  
    }  
    

## 按Symbol的精简Ticker[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#按symbol的精简ticker "按Symbol的精简Ticker的直接链接")

按Symbol逐秒刷新的24小时精简ticker信息

**Stream 名称:** <symbol>@miniTicker

**更新速度:** 1000ms

**Payload:**
    
    
    {  
        "e": "24hrMiniTicker",     // 事件类型  
        "E": 1672515782136,        // 事件时间  
        "s": "BNBBTC",             // 交易对  
        "c": "0.0025",             // 最新成交价格  
        "o": "0.0010",             // 24小时前开始第一笔成交价格  
        "h": "0.0025",             // 24小时内最高成交价  
        "l": "0.0010",             // 24小时内最低成交加  
        "v": "10000",              // 成交量  
        "q": "18"                  // 成交额  
    }  
    

## 全市场所有Symbol的精简Ticker[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#全市场所有symbol的精简ticker "全市场所有Symbol的精简Ticker的直接链接")

同上，只是推送所有交易对

**Stream名称:** !miniTicker@arr

**更新速度:** 1000ms

**Payload:**
    
    
    [  
        {  
            // 数组每一个元素对应一个交易对，内容与 \<symbol\>@miniTicker相同  
        }  
    ]  
    

## 按Symbol的完整Ticker[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#按symbol的完整ticker "按Symbol的完整Ticker的直接链接")

按Symbol逐秒刷新的24小时完整ticker信息

**Stream 名称:** <symbol>@ticker

**更新速度:** 1000ms

**Payload:**
    
    
    {  
        "e": "24hrTicker",      // 事件类型  
        "E": 1672515782136,     // 事件时间  
        "s": "BNBBTC",          // 交易对  
        "p": "0.0015",          // 24小时价格变化  
        "P": "250.00",          // 24小时价格变化（百分比）  
        "w": "0.0018",          // 平均价格  
        "x": "0.0009",          // 整整24小时之前，向前数的最后一次成交价格  
        "c": "0.0025",          // 最新成交价格  
        "Q": "10",              // 最新成交交易的成交量  
        "b": "0.0024",          // 目前最高买单价  
        "B": "10",              // 目前最高买单价的挂单量  
        "a": "0.0026",          // 目前最低卖单价  
        "A": "100",             // 目前最低卖单价的挂单量  
        "o": "0.0010",          // 整整24小时前，向后数的第一次成交价格  
        "h": "0.0025",          // 24小时内最高成交价  
        "l": "0.0010",          // 24小时内最低成交加  
        "v": "10000",           // 24小时内成交量  
        "q": "18",              // 24小时内成交额  
        "O": 0,                 // 统计开始时间  
        "C": 1675216573749,     // 统计结束时间  
        "F": 0,                 // 24小时内第一笔成交交易ID  
        "L": 18150,             // 24小时内最后一笔成交交易ID  
        "n": 18151              // 24小时内成交数  
    }  
    

## 按Symbol的最优挂单信息[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#按symbol的最优挂单信息 "按Symbol的最优挂单信息的直接链接")

实时推送指定交易对最优挂单信息 多个 `<symbol>@bookTicker` 可以订阅在一个WebSocket连接上

**Stream 名称:** <symbol>@bookTicker

**更新速度:** 实时

**Payload:**
    
    
    {  
        "u": 400900217,         // order book updateId  
        "s": "BNBUSDT",         // 交易对  
        "b": "25.35190000",     // 买单最优挂单价格  
        "B": "31.21000000",     // 买单最优挂单数量  
        "a": "25.36520000",     // 卖单最优挂单价格  
        "A": "40.66000000"      // 卖单最优挂单数量  
    }  
    

## 平均价格[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#平均价格 "平均价格的直接链接")

平均价格流推送在固定时间间隔内的平均价格变动。

**Stream 名称:** <symbol>@avgPrice

**更新速度:** 1000ms

**Payload:**
    
    
    {  
        "e": "avgPrice",           // Event type  
        "E": 1693907033000,        // Event time  
        "s": "BTCUSDT",            // Symbol  
        "i": "5m",                 // Average price interval  
        "w": "25776.86000000",     // Average price  
        "T": 1693907032213         // Last trade time  
    }  
    

## 有限档深度信息[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#有限档深度信息 "有限档深度信息的直接链接")

每秒推送有限档深度信息。levels 表示几档买卖单信息, 可选 5/10/20档

**Stream 名称:** <symbol>@depth<levels> 或者 <symbol>@depth<levels>@100ms

**更新速度:** 1000ms 或者 100ms

**Payload:**
    
    
    {  
        "lastUpdateId": 160,     // 末次更新ID  
        "bids": [                // 买单  
            [  
                "0.0024",        // 价  
                "10",            // 量  
                []               // 忽略  
            ]  
        ],  
        "asks": [                // 卖单  
            [  
                "0.0026",        // 价  
                "100",           // 量  
                []               // 忽略  
            ]  
        ]  
    }  
    

## 增量深度信息stream[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#增量深度信息stream "增量�深度信息stream的直接链接")

每秒推送orderbook的变化部分（如果有）

**Stream 名称:** <symbol>@depth 或者 <symbol>@depth@100ms

**更新速度:** 1000ms 或者 100ms

**Payload:**
    
    
    {  
        "e": "depthUpdate",     // 事件类型  
        "E": 1672515782136,     // 事件时间  
        "s": "BNBBTC",          // 交易对  
        "U": 157,               // 从上次推送至今新增的第一个 update Id  
        "u": 160,               // 从上次推送至今新增的最后一个 update Id  
        "b": [                  // 变动的买单深度  
            [  
                "0.0024",       // 价  
                "10",           // 量  
                []              // Ignore  
            ]  
        ],  
        "a": [                  // 变动的卖单深度  
            [  
                "0.0026",       // 价  
                "100",          // 量  
                []              // Ignore  
            ]  
        ]  
    }  
    

## 按Symbol的滚动窗口统计[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#按symbol的滚动窗口统计 "按Symbol的滚动窗口统计的直接链接")

单个symbol的滚动窗口统计, 支持多个时间窗口。

**Stream 名称:** <symbol>@ticker_<window_size>

**Window Sizes:** 1h, 4h, 1d

**更新速度:** 1000ms

_注意_ :   


  * 该数据流和 <symbol>@ticker 不一样。
  * `O` (`open time`) 会在每分钟整点开始, 而 `C` (`closing time`)是当前更新时间。
  * 实际统计的时间范围会比<window_size>多不超过59999ms。



**Payload:**
    
    
    {  
        "e": "1hTicker",        // Event type  
        "E": 1672515782136,     // Event time  
        "s": "BNBBTC",          // Symbol  
        "p": "0.0015",          // Price change  
        "P": "250.00",          // Price change percent  
        "o": "0.0010",          // Open price  
        "h": "0.0025",          // High price  
        "l": "0.0010",          // Low price  
        "c": "0.0025",          // Last price  
        "w": "0.0018",          // Weighted average price  
        "v": "10000",           // Total traded base asset volume  
        "q": "18",              // Total traded quote asset volume  
        "O": 0,                 // Statistics open time  
        "C": 86400000,          // Statistics close time  
        "F": 0,                 // First trade ID  
        "L": 18150,             // Last trade Id  
        "n": 18151              // Total number of trades  
    }  
    

## 全市场滚动窗口统计[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#全市场滚动窗口统计 "全市场滚动窗口统计的直接链接")

全市场symbols的滚动窗口ticker统计，计算于多个窗口。  


注意：有变动的ticker才会推送。

**Stream 名称:** !ticker_<window-size>@arr

**Window Size:** 1h, 4h, 1d

**更新速度:** 1000ms

> **Payload:**
    
    
    [  
        {  
            // 同 <symbol>@ticker_<window-size> payload,  
            // 间隔内更新的每个symbol。  
        }  
    ]  
    

## 如何正确在本地维护一个order book副本[​](/docs/zh-CN/binance-spot-api-docs/web-socket-streams#如何正确在本地维护一个order-book��副本 "如何正确在本地维护一个order book副本的直接链接")

  1. 打开与 `wss://stream.binance.com:9443/ws/bnbbtc@depth` 的 WebSocket 连接。
  2. 开始缓存收到的event。请记录您收到的第一个event的 `U`值。
  3. 访问 `https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=5000` 获取深度快照。
  4. 如果快照中的 `lastUpdateId` 小于等于步骤 2 中的 `U` 值，请返回步骤 3。
  5. 在收到的event中，丢弃快照中 `u` <= `lastUpdateId` 的所有event。现在第一个event的 `lastUpdateId` 应该在 `[U;u]` 范围以内。
  6. 将本地order book设置为快照。它的更新ID 为 `lastUpdateId`。
  7. 更新所有缓存的event，以及后续的所有event。



要将一个event应用于您的本地order book，请遵循以下更新过程：

  1. 判断是否需要处理event： 
     * 如果event的最后一次更新ID（`u`）小于本地order book的更新ID，忽略该event。
     * 如果event的首次更新ID（`U`）大于本地order book的更新ID加1，说明你错过了一些events。  
请丢弃您的本地order book并从头开始重新同步。
     * 通常，下一event的`U`等于上一event的`u + 1`。
  2. 对买价（`b`）和卖价（`a`）中的每个价位，设置order book中的新数量： 
     * 如果该价位在order book中不存在，则插入该价位及其数量。
     * 如果数量为零，则从order book中删除此价位。
  3. 将order book的更新ID设置为已处理event的最后一次更新ID（`u`）。



> [!NOTE] 由于从 API 检索的深度快照对价位的数量有限制（每侧最多 5000 个），因此除非它们发生变化，否则您将无法了解初始快照之外的价位数量。  
>  因此，在使用这些级别的信息时要小心，因为它们可能无法反映订单簿的完整视图。  
>  但是，对于大多数场景，可以每侧看到 5000 个价位就足以了解市场并进行有效交易。