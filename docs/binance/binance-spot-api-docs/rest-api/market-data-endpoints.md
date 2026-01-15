---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
api_type: Market Data
updated_at: 2026-01-15T23:36:19.345117
---

# Market Data endpoints

### Order book[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#order-book "Direct link to Order book")
    
    
    GET /api/v3/depth  
    

**Weight:** Adjusted based on the limit:

Limit| Request Weight  
---|---  
1-100| 5  
101-500| 25  
501-1000| 50  
1001-5000| 250  
  
**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default: 100; Maximum: 5000.   
If limit > 5000, only 5000 entries will be returned.  
symbolStatus| ENUM| NO| Filters for symbols that have this `tradingStatus`.   
A status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "lastUpdateId": 1027024,  
        "bids": [  
            [  
                "4.00000000",      // PRICE  
                "431.00000000"     // QTY  
            ]  
        ],  
        "asks": [["4.00000200", "12.00000000"]]  
    }  
    

### Recent trades list[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#recent-trades-list "Direct link to Recent trades list")
    
    
    GET /api/v3/trades  
    

Get recent trades.

**Weight:** 25

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default: 500; Maximum: 1000.  
  
**Data Source:** Memory

**Response:**
    
    
    [  
        {  
            "id": 28457,  
            "price": "4.00000100",  
            "qty": "12.00000000",  
            "quoteQty": "48.000012",  
            "time": 1499865549590,  
            "isBuyerMaker": true,  
            "isBestMatch": true  
        }  
    ]  
    

### Old trade lookup[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#old-trade-lookup "Direct link to Old trade lookup")
    
    
    GET /api/v3/historicalTrades  
    

Get older trades.

**Weight:** 25

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| Default: 500; Maximum: 1000.  
fromId| LONG| NO| TradeId to fetch from. Default gets most recent trades.  
  
**Data Source:** Database

**Response:**
    
    
    [  
        {  
            "id": 28457,  
            "price": "4.00000100",  
            "qty": "12.00000000",  
            "quoteQty": "48.000012",  
            "time": 1499865549590,  
            "isBuyerMaker": true,  
            "isBestMatch": true  
        }  
    ]  
    

### Compressed/Aggregate trades list[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#compressedaggregate-trades-list "Direct link to Compressed/Aggregate trades list")
    
    
    GET /api/v3/aggTrades  
    

Get compressed, aggregate trades. Trades that fill at the time, from the same taker order, with the same price will have the quantity aggregated.

**Weight:** 4

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
fromId| LONG| NO| ID to get aggregate trades from INCLUSIVE.  
startTime| LONG| NO| Timestamp in ms to get aggregate trades from INCLUSIVE.  
endTime| LONG| NO| Timestamp in ms to get aggregate trades until INCLUSIVE.  
limit| INT| NO| Default: 500; Maximum: 1000.  
  
  * If fromId, startTime, and endTime are not sent, the most recent aggregate trades will be returned.



**Data Source:** Database

**Response:**
    
    
    [  
        {  
            "a": 26129,             // Aggregate tradeId  
            "p": "0.01633102",      // Price  
            "q": "4.70443515",      // Quantity  
            "f": 27781,             // First tradeId  
            "l": 27781,             // Last tradeId  
            "T": 1498793709153,     // Timestamp  
            "m": true,              // Was the buyer the maker?  
            "M": true               // Was the trade the best price match?  
        }  
    ]  
    

### Kline/Candlestick data[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data "Direct link to Kline/Candlestick data")
    
    
    GET /api/v3/klines  
    

Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.

**Weight:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
interval| ENUM| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
timeZone| STRING| NO| Default: 0 (UTC)  
limit| INT| NO| Default: 500; Maximum: 1000.  
  
Supported kline intervals (case-sensitive):

Interval| `interval` value  
---|---  
seconds| `1s`  
minutes| `1m`, `3m`, `5m`, `15m`, `30m`  
hours| `1h`, `2h`, `4h`, `6h`, `8h`, `12h`  
days| `1d`, `3d`  
weeks| `1w`  
months| `1M`  
  
**Notes:**

  * If `startTime` and `endTime` are not sent, the most recent klines are returned.
  * Supported values for `timeZone`: 
    * Hours and minutes (e.g. `-1:00`, `05:45`)
    * Only hours (e.g. `0`, `8`, `4`)
    * Accepted range is strictly [-12:00 to +14:00] inclusive
  * If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
  * Note that `startTime` and `endTime` are always interpreted in UTC, regardless of `timeZone`.



**Data Source:** Database

**Response:**
    
    
    [  
        [  
            1499040000000,         // Kline open time  
            "0.01634790",          // Open price  
            "0.80000000",          // High price  
            "0.01575800",          // Low price  
            "0.01577100",          // Close price  
            "148976.11427815",     // Volume  
            1499644799999,         // Kline Close time  
            "2434.19055334",       // Quote asset volume  
            308,                   // Number of trades  
            "1756.87402397",       // Taker buy base asset volume  
            "28.46694368",         // Taker buy quote asset volume  
            "0"                    // Unused field, ignore.  
        ]  
    ]  
    

### UIKlines[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#uiklines "Direct link to UIKlines")
    
    
    GET /api/v3/uiKlines  
    

The request is similar to klines having the same parameters and response.

`uiKlines` return modified kline data, optimized for presentation of candlestick charts.

**Weight:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
interval| ENUM| YES| See [`klines`](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#kline-intervals)  
startTime| LONG| NO|   
endTime| LONG| NO|   
timeZone| STRING| NO| Default: 0 (UTC)  
limit| INT| NO| Default: 500; Maximum: 1000.  
  
  * If `startTime` and `endTime` are not sent, the most recent klines are returned.
  * Supported values for `timeZone`: 
    * Hours and minutes (e.g. `-1:00`, `05:45`)
    * Only hours (e.g. `0`, `8`, `4`)
    * Accepted range is strictly [-12:00 to +14:00] inclusive
  * If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
  * Note that `startTime` and `endTime` are always interpreted in UTC, regardless of `timeZone`.



**Data Source:** Database

**Response:**
    
    
    [  
        [  
            1499040000000,         // Kline open time  
            "0.01634790",          // Open price  
            "0.80000000",          // High price  
            "0.01575800",          // Low price  
            "0.01577100",          // Close price  
            "148976.11427815",     // Volume  
            1499644799999,         // Kline close time  
            "2434.19055334",       // Quote asset volume  
            308,                   // Number of trades  
            "1756.87402397",       // Taker buy base asset volume  
            "28.46694368",         // Taker buy quote asset volume  
            "0"                    // Unused field. Ignore.  
        ]  
    ]  
    

### Current average price[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#current-average-price "Direct link to Current average price")
    
    
    GET /api/v3/avgPrice  
    

Current average price for a symbol.

**Weight:** 2

**Parameters:**

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "mins": 5,                     // Average price interval (in minutes)  
        "price": "9.35751834",         // Average price  
        "closeTime": 1694061154503     // Last trade time  
    }  
    

### 24hr ticker price change statistics[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#24hr-ticker-price-change-statistics "Direct link to 24hr ticker price change statistics")
    
    
    GET /api/v3/ticker/24hr  
    

24 hour rolling window price change statistics. **Careful** when accessing this with no symbol.

**Weight:**

Parameter | Symbols Provided | Weight  
---|---|---  
symbol | 1 | 2  
symbol parameter is omitted | 80  
symbols | 1-20 | 2  
21-100 | 40  
101 or more | 80  
symbols parameter is omitted | 80  
  
**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
symbol | STRING | NO | Parameter symbol and symbols cannot be used in combination.   
If neither parameter is sent, tickers for all symbols will be returned in an array.   
  
Examples of accepted format for the symbols parameter: ["BTCUSDT","BNBUSDT"]   
or   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
symbols | STRING | NO  
type | ENUM | NO | Supported values: `FULL` or `MINI`.   
If none provided, the default is `FULL`  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.   
For multiple or all symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Data Source:** Memory

**Response - FULL:**
    
    
    {  
        "symbol": "BNBBTC",  
        "priceChange": "-94.99999800",  
        "priceChangePercent": "-95.960",  
        "weightedAvgPrice": "0.29628482",  
        "prevClosePrice": "0.10002000",  
        "lastPrice": "4.00000200",  
        "lastQty": "200.00000000",  
        "bidPrice": "4.00000000",  
        "bidQty": "100.00000000",  
        "askPrice": "4.00000200",  
        "askQty": "100.00000000",  
        "openPrice": "99.00000000",  
        "highPrice": "100.00000000",  
        "lowPrice": "0.10000000",  
        "volume": "8913.30000000",  
        "quoteVolume": "15.30000000",  
        "openTime": 1499783499040,  
        "closeTime": 1499869899040,  
        "firstId": 28385,     // First tradeId  
        "lastId": 28460,      // Last tradeId  
        "count": 76           // Trade count  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "BNBBTC",  
            "priceChange": "-94.99999800",  
            "priceChangePercent": "-95.960",  
            "weightedAvgPrice": "0.29628482",  
            "prevClosePrice": "0.10002000",  
            "lastPrice": "4.00000200",  
            "lastQty": "200.00000000",  
            "bidPrice": "4.00000000",  
            "bidQty": "100.00000000",  
            "askPrice": "4.00000200",  
            "askQty": "100.00000000",  
            "openPrice": "99.00000000",  
            "highPrice": "100.00000000",  
            "lowPrice": "0.10000000",  
            "volume": "8913.30000000",  
            "quoteVolume": "15.30000000",  
            "openTime": 1499783499040,  
            "closeTime": 1499869899040,  
            "firstId": 28385,     // First tradeId  
            "lastId": 28460,      // Last tradeId  
            "count": 76           // Trade count  
        }  
    ]  
    

**Response - MINI:**
    
    
    {  
        "symbol": "BNBBTC",               // Symbol Name  
        "openPrice": "99.00000000",       // Opening price of the Interval  
        "highPrice": "100.00000000",      // Highest price in the interval  
        "lowPrice": "0.10000000",         // Lowest  price in the interval  
        "lastPrice": "4.00000200",        // Closing price of the interval  
        "volume": "8913.30000000",        // Total trade volume (in base asset)  
        "quoteVolume": "15.30000000",     // Total trade volume (in quote asset)  
        "openTime": 1499783499040,        // Start of the ticker interval  
        "closeTime": 1499869899040,       // End of the ticker interval  
        "firstId": 28385,                 // First tradeId considered  
        "lastId": 28460,                  // Last tradeId considered  
        "count": 76                       // Total trade count  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "BNBBTC",  
            "openPrice": "99.00000000",  
            "highPrice": "100.00000000",  
            "lowPrice": "0.10000000",  
            "lastPrice": "4.00000200",  
            "volume": "8913.30000000",  
            "quoteVolume": "15.30000000",  
            "openTime": 1499783499040,  
            "closeTime": 1499869899040,  
            "firstId": 28385,  
            "lastId": 28460,  
            "count": 76  
        },  
        {  
            "symbol": "LTCBTC",  
            "openPrice": "0.07000000",  
            "highPrice": "0.07000000",  
            "lowPrice": "0.07000000",  
            "lastPrice": "0.07000000",  
            "volume": "11.00000000",  
            "quoteVolume": "0.77000000",  
            "openTime": 1656908192899,  
            "closeTime": 1656994592899,  
            "firstId": 0,  
            "lastId": 10,  
            "count": 11  
        }  
    ]  
    

### Trading Day Ticker[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#trading-day-ticker "Direct link to Trading Day Ticker")
    
    
    GET /api/v3/ticker/tradingDay  
    

Price change statistics for a trading day.

**Weight:**

4 for each requested `symbol`.   
  
The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.

**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
symbol | STRING | YES | Either `symbol` or `symbols` must be provided   
  
Examples of accepted format for the `symbols` parameter:   
["BTCUSDT","BNBUSDT"]   
or   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
  
The maximum number of `symbols` allowed in a request is 100.   
symbols  
timeZone | STRING | NO | Default: 0 (UTC)  
type | ENUM | NO | Supported values: `FULL` or `MINI`.   
If none provided, the default is `FULL`  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.   
For multiple symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Notes:**

  * Supported values for `timeZone`: 
    * Hours and minutes (e.g. `-1:00`, `05:45`)
    * Only hours (e.g. `0`, `8`, `4`)



**Data Source:** Database

**Response - FULL:**

With `symbol`:
    
    
    {  
        "symbol": "BTCUSDT",  
        "priceChange": "-83.13000000",            // Absolute price change  
        "priceChangePercent": "-0.317",           // Relative price change in percent  
        "weightedAvgPrice": "26234.58803036",     // quoteVolume / volume  
        "openPrice": "26304.80000000",  
        "highPrice": "26397.46000000",  
        "lowPrice": "26088.34000000",  
        "lastPrice": "26221.67000000",  
        "volume": "18495.35066000",               // Volume in base asset  
        "quoteVolume": "485217905.04210480",      // Volume in quote asset  
        "openTime": 1695686400000,  
        "closeTime": 1695772799999,  
        "firstId": 3220151555,                    // Trade ID of the first trade in the interval  
        "lastId": 3220849281,                     // Trade ID of the last trade in the interval  
        "count": 697727                           // Number of trades in the interval  
    }  
    

With `symbols`:
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "priceChange": "-83.13000000",  
            "priceChangePercent": "-0.317",  
            "weightedAvgPrice": "26234.58803036",  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",  
            "quoteVolume": "485217905.04210480",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,  
            "lastId": 3220849281,  
            "count": 697727  
        },  
        {  
            "symbol": "BNBUSDT",  
            "priceChange": "2.60000000",  
            "priceChangePercent": "1.238",  
            "weightedAvgPrice": "211.92276958",  
            "openPrice": "210.00000000",  
            "highPrice": "213.70000000",  
            "lowPrice": "209.70000000",  
            "lastPrice": "212.60000000",  
            "volume": "280709.58900000",  
            "quoteVolume": "59488753.54750000",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 672397461,  
            "lastId": 672496158,  
            "count": 98698  
        }  
    ]  
    

**Response - MINI:**

With `symbol`:
    
    
    {  
        "symbol": "BTCUSDT",  
        "openPrice": "26304.80000000",  
        "highPrice": "26397.46000000",  
        "lowPrice": "26088.34000000",  
        "lastPrice": "26221.67000000",  
        "volume": "18495.35066000",              // Volume in base asset  
        "quoteVolume": "485217905.04210480",     // Volume in quote asset  
        "openTime": 1695686400000,  
        "closeTime": 1695772799999,  
        "firstId": 3220151555,                   // Trade ID of the first trade in the interval  
        "lastId": 3220849281,                    // Trade ID of the last trade in the interval  
        "count": 697727                          // Number of trades in the interval  
    }  
    

With `symbols`:
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",  
            "quoteVolume": "485217905.04210480",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,  
            "lastId": 3220849281,  
            "count": 697727  
        },  
        {  
            "symbol": "BNBUSDT",  
            "openPrice": "210.00000000",  
            "highPrice": "213.70000000",  
            "lowPrice": "209.70000000",  
            "lastPrice": "212.60000000",  
            "volume": "280709.58900000",  
            "quoteVolume": "59488753.54750000",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 672397461,  
            "lastId": 672496158,  
            "count": 98698  
        }  
    ]  
    

### Symbol price ticker[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-price-ticker "Direct link to Symbol price ticker")
    
    
    GET /api/v3/ticker/price  
    

Latest price for a symbol or symbols.

**Weight:**

Parameter | Symbols Provided | Weight  
---|---|---  
symbol | 1 | 2  
symbol parameter is omitted | 4  
symbols | Any | 4  
  
**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
symbol | STRING | NO |  Parameter symbol and symbols cannot be used in combination.   
If neither parameter is sent, prices for all symbols will be returned in an array.   
  
Examples of accepted format for the symbols parameter: ["BTCUSDT","BNBUSDT"]   
or   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D  
symbols | STRING | NO  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.   
For multiple or all symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "symbol": "LTCBTC",  
        "price": "4.00000200"  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "LTCBTC",  
            "price": "4.00000200"  
        },  
        {  
            "symbol": "ETHBTC",  
            "price": "0.07946600"  
        }  
    ]  
    

### Symbol order book ticker[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#symbol-order-book-ticker "Direct link to Symbol order book ticker")
    
    
    GET /api/v3/ticker/bookTicker  
    

Best price/qty on the order book for a symbol or symbols.

**Weight:**

Parameter | Symbols Provided | Weight  
---|---|---  
symbol | 1 | 2  
symbol parameter is omitted | 4  
symbols | Any | 4  
  
**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
symbol | STRING | NO |  Parameter symbol and symbols cannot be used in combination.   
If neither parameter is sent, bookTickers for all symbols will be returned in an array.   
  
Examples of accepted format for the symbols parameter: ["BTCUSDT","BNBUSDT"]   
or   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D  
symbols | STRING | NO  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.   
For multiple or all symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Data Source:** Memory

**Response:**
    
    
    {  
        "symbol": "LTCBTC",  
        "bidPrice": "4.00000000",  
        "bidQty": "431.00000000",  
        "askPrice": "4.00000200",  
        "askQty": "9.00000000"  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "LTCBTC",  
            "bidPrice": "4.00000000",  
            "bidQty": "431.00000000",  
            "askPrice": "4.00000200",  
            "askQty": "9.00000000"  
        },  
        {  
            "symbol": "ETHBTC",  
            "bidPrice": "0.07946700",  
            "bidQty": "9.00000000",  
            "askPrice": "100000.00000000",  
            "askQty": "1000.00000000"  
        }  
    ]  
    

### Rolling window price change statistics[​](/docs/binance-spot-api-docs/rest-api/market-data-endpoints#rolling-window-price-change-statistics "Direct link to Rolling window price change statistics")
    
    
    GET /api/v3/ticker  
    

**Note:** This endpoint is different from the `GET /api/v3/ticker/24hr` endpoint.

The window used to compute statistics will be no more than 59999ms from the requested `windowSize`.

`openTime` for `/api/v3/ticker` always starts on a minute, while the `closeTime` is the current time of the request. As such, the effective window will be up to 59999ms wider than `windowSize`.

E.g. If the `closeTime` is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the `windowSize` is `1d`. the `openTime` will be: 1641201420000 (January 3, 2022, 09:17:00)

**Weight:**

4 for each requested `symbol` regardless of `windowSize`.   
  
The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.

**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
symbol | STRING | YES | Either `symbol` or `symbols` must be provided   
  
Examples of accepted format for the `symbols` parameter:   
["BTCUSDT","BNBUSDT"]   
or   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
  
The maximum number of `symbols` allowed in a request is 100.   
symbols  
windowSize | ENUM | NO | Defaults to `1d` if no parameter provided   
Supported `windowSize` values:   
`1m`,`2m`....`59m` for minutes   
`1h`, `2h`....`23h` \- for hours   
`1d`...`7d` \- for days   
  
Units cannot be combined (e.g. `1d2h` is not allowed)  
type | ENUM | NO | Supported values: `FULL` or `MINI`.   
If none provided, the default is `FULL`  
symbolStatus | ENUM | NO | Filters for symbols that have this `tradingStatus`.  
For a single symbol, a status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.  
For multiple symbols, non-matching ones are simply excluded from the response.  
Valid values: `TRADING`, `HALT`, `BREAK`  
  
**Data Source:** Database

**Response - FULL:**

When using `symbol`:
    
    
    {  
        "symbol": "BNBBTC",  
        "priceChange": "-8.00000000",         // Absolute price change  
        "priceChangePercent": "-88.889",      // Relative price change in percent  
        "weightedAvgPrice": "2.60427807",     // QuoteVolume / Volume  
        "openPrice": "9.00000000",  
        "highPrice": "9.00000000",  
        "lowPrice": "1.00000000",  
        "lastPrice": "1.00000000",  
        "volume": "187.00000000",  
        "quoteVolume": "487.00000000",        // Sum of (price * volume) for all trades  
        "openTime": 1641859200000,            // Open time for ticker window  
        "closeTime": 1642031999999,           // Close time for ticker window  
        "firstId": 0,                         // Trade IDs  
        "lastId": 60,  
        "count": 61                           // Number of trades in the interval  
    }  
    

or

When using `symbols`:
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "priceChange": "-154.13000000",           // Absolute price change  
            "priceChangePercent": "-0.740",           // Relative price change in percent  
            "weightedAvgPrice": "20677.46305250",     // QuoteVolume / Volume  
            "openPrice": "20825.27000000",  
            "highPrice": "20972.46000000",  
            "lowPrice": "20327.92000000",  
            "lastPrice": "20671.14000000",  
            "volume": "72.65112300",  
            "quoteVolume": "1502240.91155513",        // Sum of (price * volume) for all trades  
            "openTime": 1655432400000,                // Open time for ticker window  
            "closeTime": 1655446835460,               // Close time for ticker window  
            "firstId": 11147809,                      // Trade IDs  
            "lastId": 11149775,  
            "count": 1967                             // Number of trades in the interval  
        },  
        {  
            "symbol": "BNBBTC",  
            "priceChange": "0.00008530",  
            "priceChangePercent": "0.823",  
            "weightedAvgPrice": "0.01043129",  
            "openPrice": "0.01036170",  
            "highPrice": "0.01049850",  
            "lowPrice": "0.01033870",  
            "lastPrice": "0.01044700",  
            "volume": "166.67000000",  
            "quoteVolume": "1.73858301",  
            "openTime": 1655432400000,  
            "closeTime": 1655446835460,  
            "firstId": 2351674,  
            "lastId": 2352034,  
            "count": 361  
        }  
    ]  
    

**Response - MINI:**

When using `symbol`:
    
    
    {  
        "symbol": "LTCBTC",  
        "openPrice": "0.10000000",  
        "highPrice": "2.00000000",  
        "lowPrice": "0.10000000",  
        "lastPrice": "2.00000000",  
        "volume": "39.00000000",  
        "quoteVolume": "13.40000000",     // Sum of (price * volume) for all trades  
        "openTime": 1656986580000,        // Open time for ticker window  
        "closeTime": 1657001016795,       // Close time for ticker window  
        "firstId": 0,                     // Trade IDs  
        "lastId": 34,  
        "count": 35                       // Number of trades in the interval  
    }  
    

OR

When using `symbols`:
    
    
    [  
        {  
            "symbol": "BNBBTC",  
            "openPrice": "0.10000000",  
            "highPrice": "2.00000000",  
            "lowPrice": "0.10000000",  
            "lastPrice": "2.00000000",  
            "volume": "39.00000000",  
            "quoteVolume": "13.40000000",     // Sum of (price * volume) for all trades  
            "openTime": 1656986880000,        // Open time for ticker window  
            "closeTime": 1657001297799,       // Close time for ticker window  
            "firstId": 0,                     // Trade IDs  
            "lastId": 34,  
            "count": 35                       // Number of trades in the interval  
        },  
        {  
            "symbol": "LTCBTC",  
            "openPrice": "0.07000000",  
            "highPrice": "0.07000000",  
            "lowPrice": "0.07000000",  
            "lastPrice": "0.07000000",  
            "volume": "33.00000000",  
            "quoteVolume": "2.31000000",  
            "openTime": 1656986880000,  
            "closeTime": 1657001297799,  
            "firstId": 0,  
            "lastId": 32,  
            "count": 33  
        }  
    ]

---

# 行情接口

### 深度信息[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#深度信息 "深度信息的直接链接")
    
    
    GET /api/v3/depth  
    

**权重:**

限制| 权重  
---|---  
1-100| 5  
101-500| 25  
501-1000| 50  
1001-5000| 250  
  
**参数:**

名称| 类型| 是否必须| 描述  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| 默认： 100; 最大： 5000。   
如果 limit > 5000, 最多返回5000条数据。  
symbolStatus| ENUM| NO| 过滤具有此 `tradingStatus` 的交易对。  
如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`  
有效值： `TRADING`, `HALT`, `BREAK`  
  
**数据源:** 缓存

**响应:**
    
    
    {  
        "lastUpdateId": 1027024,  
        "bids": [  
            [  
                "4.00000000",      // 价位  
                "431.00000000"     // 挂单量  
            ]  
        ],  
        "asks": [["4.00000200", "12.00000000"]]  
    }  
    

### 近期成交[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#近期成交 "近期成交的直接链接")
    
    
    GET /api/v3/trades  
    

获取近期成交

**权重:** 25

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| 默认值： 500； 最大值： 1000。  
  
**数据源:** 缓存

**响应:**
    
    
    [  
        {  
            "id": 28457,  
            "price": "4.00000100",  
            "qty": "12.00000000",  
            "quoteQty": "48.000012",  
            "time": 1499865549590,  
            "isBuyerMaker": true,  
            "isBestMatch": true  
        }  
    ]  
    

### 查询历史成交[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#查询历史成交 "查询历史成交的直接链接")
    
    
    GET /api/v3/historicalTrades  
    

**权重:** 25

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
limit| INT| NO| 默认值： 500； 最大值： 1000。  
fromId| LONG| NO| 从哪一条成交id开始返回，缺省返回最近的成交记录  
  
**数据源:** 数据库

**响应:**
    
    
    [  
        {  
            "id": 28457,  
            "price": "4.00000100",  
            "qty": "12.00000000",  
            "quoteQty": "48.000012",  
            "time": 1499865549590,  
            "isBuyerMaker": true,  
            "isBestMatch": true  
        }  
    ]  
    

### 近期成交(归集)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#近期成交归集 "近期成交\(归集\)的直接链接")
    
    
    GET /api/v3/aggTrades  
    

与trades的区别是，同一个taker在同一时间同一价格与多个maker的成交会被合并为一条记录

**权重:** 4

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
fromId| LONG| NO| 从包含fromID的成交开始返回结果  
startTime| LONG| NO| 从该时刻之后的成交记录开始返回结果  
endTime| LONG| NO| 返回该时刻为止的成交记录  
limit| INT| NO| 默认值： 500； 最大值： 1000。  
  
  * 如果没有发送任何筛选参数(fromId, startTime, endTime)，默认返回最近的成交记录



**数据源:** 数据库

**响应:**
    
    
    [  
        {  
            "a": 26129,             // 归集成交ID  
            "p": "0.01633102",      // 成交价  
            "q": "4.70443515",      // 成交量  
            "f": 27781,             // 被归集的首个成交ID  
            "l": 27781,             // 被归集的末个成交ID  
            "T": 1498793709153,     // 成交时间  
            "m": true,              // 是否为主动卖出单  
            "M": true               // 是否为最优撮合单(可忽略，目前总为最优撮合)  
        }  
    ]  
    

### K线数据[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#k线数据 "K线数据的直接链接")
    
    
    GET /api/v3/klines  
    

每根K线的开盘时间可视为唯一ID

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
interval| ENUM| YES| 请参考 [`K线间隔`](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#kline-intervals)  
startTime| LONG| NO|   
endTime| LONG| NO|   
timeZone| STRING| NO| 默认值： 0 (UTC)  
limit| INT| NO| 默认值： 500； 最大值： 1000。  
  
支持的K线间隔 （区分大小写）：

间隔| `间隔` 值  
---|---  
seconds -> 秒| `1s`  
minutes -> 分钟| `1m`， `3m`， `5m`， `15m`， `30m`  
hours -> 小时| `1h`， `2h`， `4h`， `6h`， `8h`， `12h`  
days -> 天| `1d`， `3d`  
weeks -> 周| `1w`  
months -> 月| `1M`  
  
**请注意：**

  * 如果未发送`startTime`和`endTime`，将返回最近的K线数据。
  * `timeZone`支持的值包括： 
    * 小时和分钟（例如 `-1:00`，`05:45`）
    * 仅小时（例如 `0`，`8`，`4`）
    * 接受的值范围严格为 [-12:00 到 +14:00]（包括边界）
  * 如果提供了`timeZone`，K线间隔将在该时区中解释，而不是在UTC中。
  * 请注意，无论`timeZone`如何，`startTime`和`endTime`始终以UTC时区解释。



**数据源:** 数据库

**响应:**
    
    
    [  
        [  
            1499040000000,          // 开盘时间  
            "0.01634790",           // 开盘价  
            "0.80000000",           // 最高价  
            "0.01575800",           // 最低价  
            "0.01577100",           // 收盘价(当前K线未结束的即为最新价)  
            "148976.11427815",      // 成交量  
            1499644799999,          // 收盘时间  
            "2434.19055334",        // 成交额  
            308,                    // 成交笔数  
            "1756.87402397",        // 主动买入成交量  
            "28.46694368",          // 主动买入成交额  
            "17928899.62484339"     // 请忽略该参数  
        ]  
    ]  
    

### UIK线数据[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#uik线数据 "UIK线数据的直接链接")
    
    
    GET /api/v3/uiKlines  
    

请求参数与响应和k线接口相同。

`uiKlines` 返回修改后的k线数据，针对k线图的呈现进行了优化。

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
interval| ENUM| YES| 请参考 [`K线间隔`](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#kline-intervals)  
startTime| LONG| NO|   
endTime| LONG| NO|   
timeZone| STRING| NO| 默认值： 0 (UTC)  
limit| INT| NO| 默认值： 500； 最大值： 1000。  
  
  * 如果未发送 `startTime` 和 `endTime`，默认返回最近的交易。
  * `timeZone`支持的值包括： 
    * 小时和分钟（例如 `-1:00`，`05:45`）
    * 仅小时（例如 `0`，`8`，`4`）
    * 接受的值范围严格为 [-12:00 到 +14:00]（包括边界）
  * 如果提供了`timeZone`，K线间隔将在该时区中解释，而不是在UTC中。
  * 请注意，无论`timeZone`如何，`startTime`和`endTime`始终以UTC时区解释。



**数据源:** 数据库

**响应:**
    
    
    [  
        [  
            1499040000000,         // k线开盘时间  
            "0.01634790",          // 开盘价  
            "0.80000000",          // 最高价  
            "0.01575800",          // 最低价  
            "0.01577100",          // 收盘价(当前K线未结束的即为最新价)  
            "148976.11427815",     // 成交量  
            1499644799999,         // k线收盘时间  
            "2434.19055334",       // 成交额  
            308,                   // 成交笔数  
            "1756.87402397",       // 主动买入成交量  
            "28.46694368",         // 主动买入成交额  
            "0"                    // 请忽略该参数  
        ]  
    ]  
    

### 当前平均价格[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#当前平均价格 "当前平均价格的直接链接")
    
    
    GET /api/v3/avgPrice  
    

**权重:** 2

**参数:**

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
  
**数据源:** 缓存

**响应:**
    
    
    {  
        "mins": 5,  
        "price": "9.35751834",  
        "closeTime": 1694061154503  
    }  
    

### 24hr价格变动情况[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#24hr价格变动情况 "24hr价格变动情况的直接链接")
    
    
    GET /api/v3/ticker/24hr  
    

请注意，不携带symbol参数会返回全部交易对数据，不仅数据庞大，而且权重极高

**权重:**

参数 | 提供Symbol数量 | 权重  
---|---|---  
symbol | 1 | 2  
不提供symbol | 80  
symbols | 1-20 | 2  
21-100 | 40  
>= 101 | 80  
不提供symbol | 80  
  
**参数:**

名称 | 类型 | 是否强制要求 | 详情  
---|---|---|---  
symbol | STRING | NO | 参数 `symbol` 和 `symbols` 不可以一起使用   
如果都不提供, 所有symbol的ticker数据都会返回.   
  
symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"]   
或   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
symbols | STRING | NO  
type | ENUM | NO | 可接受的参数: `FULL` or `MINI`.   
如果不提供, 默认值为 `FULL`  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
**数据源:** 缓存

**响应 - FULL:**
    
    
    {  
        "symbol": "BNBBTC",  
        "priceChange": "-94.99999800",  
        "priceChangePercent": "-95.960",  
        "weightedAvgPrice": "0.29628482",  
        "prevClosePrice": "0.10002000",  
        "lastPrice": "4.00000200",  
        "lastQty": "200.00000000",  
        "bidPrice": "4.00000000",  
        "bidQty": "100.00000000",  
        "askPrice": "4.00000200",  
        "askQty": "100.00000000",  
        "openPrice": "99.00000000",  
        "highPrice": "100.00000000",  
        "lowPrice": "0.10000000",  
        "volume": "8913.30000000",  
        "quoteVolume": "15.30000000",  
        "openTime": 1499783499040,  
        "closeTime": 1499869899040,  
        "firstId": 28385,     // 首笔成交id  
        "lastId": 28460,      // 末笔成交id  
        "count": 76           // 成交笔数  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "BNBBTC",  
            "priceChange": "-94.99999800",  
            "priceChangePercent": "-95.960",  
            "weightedAvgPrice": "0.29628482",  
            "prevClosePrice": "0.10002000",  
            "lastPrice": "4.00000200",  
            "lastQty": "200.00000000",  
            "bidPrice": "4.00000000",  
            "bidQty": "100.00000000",  
            "askPrice": "4.00000200",  
            "askQty": "100.00000000",  
            "openPrice": "99.00000000",  
            "highPrice": "100.00000000",  
            "lowPrice": "0.10000000",  
            "volume": "8913.30000000",  
            "quoteVolume": "15.30000000",  
            "openTime": 1499783499040,  
            "closeTime": 1499869899040,  
            "firstId": 28385,     // 首笔成交id  
            "lastId": 28460,      // 末笔成交id  
            "count": 76           // 成交笔数  
        }  
    ]  
    

**响应 - MINI**
    
    
    {  
        "symbol": "BNBBTC",               // 交易对  
        "openPrice": "99.00000000",       // 间隔开盘价  
        "highPrice": "100.00000000",      // 间隔最高价  
        "lowPrice": "0.10000000",         // 间隔最低价  
        "lastPrice": "4.00000200",        // 间隔收盘价  
        "volume": "8913.30000000",        // 总交易量 (base asset)  
        "quoteVolume": "15.30000000",     // 总交易量 (quote asset)  
        "openTime": 1499783499040,        // ticker间隔的开始时间  
        "closeTime": 1499869899040,       // ticker间隔的结束时间  
        "firstId": 28385,                 // 统计时间内的第一笔trade id  
        "lastId": 28460,                  // 统计时间内的最后一笔trade id  
        "count": 76                       // 统计时间内交易笔数  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "BNBBTC",  
            "openPrice": "99.00000000",  
            "highPrice": "100.00000000",  
            "lowPrice": "0.10000000",  
            "lastPrice": "4.00000200",  
            "volume": "8913.30000000",  
            "quoteVolume": "15.30000000",  
            "openTime": 1499783499040,  
            "closeTime": 1499869899040,  
            "firstId": 28385,  
            "lastId": 28460,  
            "count": 76  
        },  
        {  
            "symbol": "LTCBTC",  
            "openPrice": "0.07000000",  
            "highPrice": "0.07000000",  
            "lowPrice": "0.07000000",  
            "lastPrice": "0.07000000",  
            "volume": "11.00000000",  
            "quoteVolume": "0.77000000",  
            "openTime": 1656908192899,  
            "closeTime": 1656994592899,  
            "firstId": 0,  
            "lastId": 10,  
            "count": 11  
        }  
    ]  
    

### 交易日行情(Ticker)[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#交易日行情ticker "交易日行情\(Ticker\)的直接链接")
    
    
    GET /api/v3/ticker/tradingDay  
    

交易日价格变动统计。

**权重:**

每个`交易对`占用4个权重.   
  
当请求中的交易对数量超过50，此请求的权重将限制在200。

**参数:**

参数名 | 类型 | 是否必需 | 描述  
---|---|---|---  
symbol | STRING | YES |  `symbol` 或者 `symbols` 必须提供之一   
  
`symbols` 可以接受的格式:   
["BTCUSDT","BNBUSDT"]   
或者   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
  
`symbols` 最多可以发送100个.   
symbols  
timeZone | STRING | NO | Default: 0 (UTC)  
type | ENUM | NO | 可接受值: `FULL` or `MINI`.   
默认值: `FULL`  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
**注意:**

  * `timeZone`支持的值包括： 
    * 小时和分钟（例如 `-1:00`，`05:45`）
    * 仅小时（例如 `0`，`8`，`4`）



**数据源:** 数据库

**响应 - FULL**

有 `symbol`:
    
    
    {  
        "symbol": "BTCUSDT",  
        "priceChange": "-83.13000000",            // 绝对价格变动  
        "priceChangePercent": "-0.317",           // 相对价格变动百分比  
        "weightedAvgPrice": "26234.58803036",     // 报价成交量 / 成交量  
        "openPrice": "26304.80000000",  
        "highPrice": "26397.46000000",  
        "lowPrice": "26088.34000000",  
        "lastPrice": "26221.67000000",  
        "volume": "18495.35066000",               // 基础资产的成交量  
        "quoteVolume": "485217905.04210480",      // 报价资产的成交量  
        "openTime": 1695686400000,  
        "closeTime": 1695772799999,  
        "firstId": 3220151555,                    // 区间内的第一个交易的交易ID  
        "lastId": 3220849281,                     // 区间内的最后一个交易的交易ID  
        "count": 697727                           // 区间内的交易数量  
    }  
    

有 `symbols`:
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "priceChange": "-83.13000000",  
            "priceChangePercent": "-0.317",  
            "weightedAvgPrice": "26234.58803036",  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",  
            "quoteVolume": "485217905.04210480",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,  
            "lastId": 3220849281,  
            "count": 697727  
        },  
        {  
            "symbol": "BNBUSDT",  
            "priceChange": "2.60000000",  
            "priceChangePercent": "1.238",  
            "weightedAvgPrice": "211.92276958",  
            "openPrice": "210.00000000",  
            "highPrice": "213.70000000",  
            "lowPrice": "209.70000000",  
            "lastPrice": "212.60000000",  
            "volume": "280709.58900000",  
            "quoteVolume": "59488753.54750000",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 672397461,  
            "lastId": 672496158,  
            "count": 98698  
        }  
    ]  
    

**响应: - MINI**

有 `symbol`:
    
    
    {  
        "symbol": "BTCUSDT",  
        "openPrice": "26304.80000000",  
        "highPrice": "26397.46000000",  
        "lowPrice": "26088.34000000",  
        "lastPrice": "26221.67000000",  
        "volume": "18495.35066000",              // 基础资产的成交量  
        "quoteVolume": "485217905.04210480",     // 报价资产的成交量  
        "openTime": 1695686400000,  
        "closeTime": 1695772799999,  
        "firstId": 3220151555,                   // 区间内的第一个交易的交易ID  
        "lastId": 3220849281,                    // 区间内的最后一个交易的交易ID  
        "count": 697727                          // 区间内的交易数量  
    }  
    

有 `symbols`:
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "openPrice": "26304.80000000",  
            "highPrice": "26397.46000000",  
            "lowPrice": "26088.34000000",  
            "lastPrice": "26221.67000000",  
            "volume": "18495.35066000",  
            "quoteVolume": "485217905.04210480",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 3220151555,  
            "lastId": 3220849281,  
            "count": 697727  
        },  
        {  
            "symbol": "BNBUSDT",  
            "openPrice": "210.00000000",  
            "highPrice": "213.70000000",  
            "lowPrice": "209.70000000",  
            "lastPrice": "212.60000000",  
            "volume": "280709.58900000",  
            "quoteVolume": "59488753.54750000",  
            "openTime": 1695686400000,  
            "closeTime": 1695772799999,  
            "firstId": 672397461,  
            "lastId": 672496158,  
            "count": 98698  
        }  
    ]  
    

### 最新价格接口[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#最新价格接口 "最新价格接口的直接链接")
    
    
    GET /api/v3/ticker/price  
    

返回最近价格

**权重:**

参数 | Symbols数量 | 权重  
---|---|---  
symbol | 1 | 2  
不提供symbol | 4  
symbols | 不限 | 4  
  
**参数:**

参数名 | 类型 | 是否强制 | 详情  
---|---|---|---  
symbol | STRING | NO |  参数 `symbol` 和 `symbols` 不可以一起使用   
如果都不提供, 所有symbol的价格数据都会返回.   
  
symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"]   
或   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
symbols | STRING | NO  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
  * 不发送交易对参数，则会返回所有交易对信息



**数据源:** 缓存

**响应:**
    
    
    {  
        "symbol": "LTCBTC",  
        "price": "4.00000200"  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "LTCBTC",  
            "price": "4.00000200"  
        },  
        {  
            "symbol": "ETHBTC",  
            "price": "0.07946600"  
        }  
    ]  
    

### 最优挂单接口[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#最优挂单接口 "最优挂单接口的直接链接")
    
    
    GET /api/v3/ticker/bookTicker  
    

返回当前最优的挂单(最高买单，最低卖单)

**权重:**

参数 | Symbols数量 | 权重  
---|---|---  
symbol | 1 | 2  
不提供symbol | 4  
symbols | 不限 | 4  
  
**参数:**

参数名 | 类型 | 是否强制 | 详情  
---|---|---|---  
symbol | STRING | NO |  参数 `symbol` 和 `symbols` 不可以一起使用   
如果都不提供, 所有symbol的bookTicker数据都会返回.   
  
symbols参数可接受的格式： ["BTCUSDT","BNBUSDT"]   
或   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
symbols | STRING | NO  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个或者全部交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
  * 不发送交易对参数，则会返回所有交易对信息



**数据源:** 缓存

**响应:**
    
    
    {  
        "symbol": "LTCBTC",  
        "bidPrice": "4.00000000",     // 最优买单价  
        "bidQty": "431.00000000",     // 挂单量  
        "askPrice": "4.00000200",     // 最优卖单价  
        "askQty": "9.00000000"        // 挂单量  
    }  
    

OR
    
    
    [  
        {  
            "symbol": "LTCBTC",  
            "bidPrice": "4.00000000",  
            "bidQty": "431.00000000",  
            "askPrice": "4.00000200",  
            "askQty": "9.00000000"  
        },  
        {  
            "symbol": "ETHBTC",  
            "bidPrice": "0.07946700",  
            "bidQty": "9.00000000",  
            "askPrice": "100000.00000000",  
            "askQty": "1000.00000000"  
        }  
    ]  
    

### 滚动窗口价格变动统计[​](/docs/zh-CN/binance-spot-api-docs/rest-api/market-data-endpoints#滚动窗口价格变动统计 "滚动窗口价格变动统计的直接链接")
    
    
    GET /api/v3/ticker  
    

**注意:** 此接口和 `GET /api/v3/ticker/24hr` 有所不同.

此接口统计的时间范围比请求的`windowSize`多不超过59999ms.

接口的 `openTime` 是某一分钟的起始，而结束是当前的时间. 所以实际的统计区间会比请求的时间窗口多不超过59999ms.

比如, 结束时间 `closeTime` 是 1641287867099 (January 04, 2022 09:17:47:099 UTC) , `windowSize` 为 `1d`. 那么开始时间 `openTime` 则为 1641201420000 (January 3, 2022, 09:17:00 UTC)

**权重:** 4/交易对.   
  
如果`symbols`请求的交易对超过50, 上限是200.

**参数:**

Name | Type | Mandatory | Description  
---|---|---|---  
symbol | STRING | YES |  提供 symbol或者symbols 其中之一   
`symbols` 可以传入的格式:   
["BTCUSDT","BNBUSDT"]   
or   
%5B%22BTCUSDT%22,%22BNBUSDT%22%5D   
  
`symbols` 允许最多100个交易对   
symbols  
windowSize | ENUM | NO | 默认为 `1d`   
`windowSize` 支持的值:   
如果是分钟: `1m`,`2m`....`59m`   
如果是小时: `1h`, `2h`....`23h`   
如果是天: `1d`...`7d`   
  
不可以组合使用, 比如`1d2h`  
type | ENUM | NO | 可接受的参数: `FULL` or `MINI`.   
如果不提供, 默认值为 `FULL`  
symbolStatus | ENUM | NO | 过滤具有此 `tradingStatus` 的交易对。  
对于单个交易对，如果状态不匹配，将返回错误 `-1220 交易对与状态不匹配`。  
对于多个交易对， 响应中不会包括状态不匹配的交易对。  
有效值： `TRADING`, `HALT`, `BREAK`  
  
**数据源:** 数据库

**响应 - FULL**

使用参数 `symbol` 返回:
    
    
    {  
        "symbol": "BNBBTC",  
        "priceChange": "-8.00000000",        // 价格变化  
        "priceChangePercent": "-88.889",     // 价格变化百分比  
        "weightedAvgPrice": "2.60427807",  
        "openPrice": "9.00000000",  
        "highPrice": "9.00000000",  
        "lowPrice": "1.00000000",  
        "lastPrice": "1.00000000",  
        "volume": "187.00000000",  
        "quoteVolume": "487.00000000",  
        "openTime": 1641859200000,           // ticker的开始时间  
        "closeTime": 1642031999999,          // ticker的结束时间  
        "firstId": 0,                        // 统计时间内的第一笔trade id  
        "lastId": 60,  
        "count": 61                          // 统计时间内交易笔数  
    }  
    

使用参数 `symbols` 返回:
    
    
    [  
        {  
            "symbol": "BTCUSDT",  
            "priceChange": "-154.13000000",  
            "priceChangePercent": "-0.740",  
            "weightedAvgPrice": "20677.46305250",  
            "openPrice": "20825.27000000",  
            "highPrice": "20972.46000000",  
            "lowPrice": "20327.92000000",  
            "lastPrice": "20671.14000000",  
            "volume": "72.65112300",  
            "quoteVolume": "1502240.91155513",  
            "openTime": 1655432400000,  
            "closeTime": 1655446835460,  
            "firstId": 11147809,  
            "lastId": 11149775,  
            "count": 1967  
        },  
        {  
            "symbol": "BNBBTC",  
            "priceChange": "0.00008530",  
            "priceChangePercent": "0.823",  
            "weightedAvgPrice": "0.01043129",  
            "openPrice": "0.01036170",  
            "highPrice": "0.01049850",  
            "lowPrice": "0.01033870",  
            "lastPrice": "0.01044700",  
            "volume": "166.67000000",  
            "quoteVolume": "1.73858301",  
            "openTime": 1655432400000,  
            "closeTime": 1655446835460,  
            "firstId": 2351674,  
            "lastId": 2352034,  
            "count": 361  
        }  
    ]  
    

**响应 - MINI**

使用参数 `symbol` 返回:
    
    
    {  
        "symbol": "LTCBTC",  
        "openPrice": "0.10000000",  
        "highPrice": "2.00000000",  
        "lowPrice": "0.10000000",  
        "lastPrice": "2.00000000",  
        "volume": "39.00000000",  
        "quoteVolume": "13.40000000",     // 此k线内所有交易的price(价格) x volume(交易量)的总和  
        "openTime": 1656986580000,        // ticker窗口的开始时间  
        "closeTime": 1657001016795,       // ticker窗口的结束时间  
        "firstId": 0,                     // 首笔成交id  
        "lastId": 34,  
        "count": 35                       // 统计时间内交易笔数  
    }  
    

使用参数 `symbols` 返回:
    
    
    [  
        {  
            "symbol": "BNBBTC",  
            "openPrice": "0.10000000",  
            "highPrice": "2.00000000",  
            "lowPrice": "0.10000000",  
            "lastPrice": "2.00000000",  
            "volume": "39.00000000",  
            "quoteVolume": "13.40000000",     // 此k线内所有交易的price(价格) x volume(交易量)的总和  
            "openTime": 1656986880000,        // ticker窗口的开始时间  
            "closeTime": 1657001297799,       // ticker窗口的结束时间  
            "firstId": 0,                     // 首笔成交id  
            "lastId": 34,  
            "count": 35                       // 统计时间内交易笔数  
        },  
        {  
            "symbol": "LTCBTC",  
            "openPrice": "0.07000000",  
            "highPrice": "0.07000000",  
            "lowPrice": "0.07000000",  
            "lastPrice": "0.07000000",  
            "volume": "33.00000000",  
            "quoteVolume": "2.31000000",  
            "openTime": 1656986880000,  
            "closeTime": 1657001297799,  
            "firstId": 0,  
            "lastId": 32,  
            "count": 33  
        }  
    ]