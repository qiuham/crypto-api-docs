---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-orders-info
api_type: REST
updated_at: 2026-06-06 19:27:27.168392
---

# Post-Trade Data

**GET** `https://api.kraken.com/0/public/PostTrade`

Returns a list of trades on the spot exchange. If no filter parameters are specified, the last 1000 trades for all pairs are received.

## Request

### Query Parameters

**symbol** `string`

Filter the results to the currency pair.

**Example:** BTC/USD

**from_ts** `ISO 8601`

Filter the results to include the trades _after_ this timestamp.

**Example:** 2024-05-30T12:34:56.123456789Z

**to_ts** `ISO 8601`

Filter the results to include the trades _before or at_ this timestamp.

**Example:** 2024-05-30T12:34:56.123456789Z

**count** `integer`

**Possible values:** `>= 1` and `<= 1000`

The maximum number of trades to return.

**Default value:**`1000`

## Responses

  * 200
* application/json
* Schema

**Schema**

**result** `object`

    ↳ **last_ts** `string<ISO 8601>`

Timestamp of the latest trade in the list. This field can be used as the `from_ts` parameter when requesting the next batch of trades.

**Example:**`2024-05-30T12:34:56.123456789Z`

    ↳ **count** `int`

The number of trades returned.

**Possible values:** `>= 0` and `<= 1000`

    ↳ **trades** `object<Trade>[]`

A list of trades in ascending timestamp order.

**Possible values:** `<= 1000`

  * Array [

        ↳ **trade_id** `string`

Kraken unique trade identifier.

**Possible values:** `<= 19 characters`

**Example:**`TGBB7L-HT5LX-J3BZ4A`

        ↳ **price** `string`

Trade price excluding fees and commissions.

**Example:**`102002.1`

        ↳ **quantity** `string`

Unconsolidated trade quantity from execution.

**Example:**`1.24`

        ↳ **symbol** `string`

The symbol of the currency pair.

**Possible values:** `<= 32 characters`

**Example:**`BTC/USD`

        ↳ **description** `string`

The full description of the currency pair.

**Possible values:** `<= 350 characters`

**Example:**`Bitcoin / US Dollars`

        ↳ **base_asset** `string<ISO 4217>`

Currency code for the base asset.

**Example:**`BTC`

        ↳ **base_notation** `string`

Indicates that the quantity is expressed in nominal value.

**Possible values:** [`UNIT`]

        ↳ **quote_asset** `string<ISO 4217>`

Currency in which the trading price is expressed.

**Example:**`USD`

        ↳ **quote_notation** `string`

Indicates that the price is expressed in monetary value.

**Possible values:** [`MONE`]

        ↳ **trade_venue** `string<ISO 10383>`

Market Identifier Code (MIC) of the trading platform where the trade was executed.

**Possible values:** `<= 12 characters`

**Example:**`PGSL`

        ↳ **trade_ts** `string<ISO 8601>`

Timestamp the trade was matched in the engine to microsecond precision.

**Example:**`2024-05-30T12:34:56.123456789Z`

        ↳ **publication_venue** `string<ISO 10383>`

Market Identifier Code (MIC) of the trading platform where the trade was published.

**Possible values:** `<= 12 characters`

**Example:**`PGSL`

        ↳ **publication_ts** `string<ISO 8601>`

Timestamp the trade was published to market data streams.

**Example:**`2024-05-30T12:34:56.123456789Z`

  * ]

**error** `string[]`
* curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/PostTrade' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Parameters

symbol — query

from_ts — query

to_ts — query

count — query

ResponseClear

Click the `Send API Request` button above and see the response here!