---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/futures-api/history/get-execution-events
api_type: REST
updated_at: 2026-05-26 14:50:29.738272
---

# Get execution events

**GET** `https://futures.kraken.com/api/history/v3/executions`

Lists executions/trades for authenticated account.

## Request​

### Query Parameters

**since** `timestamp-milliseconds`

Timestamp in milliseconds.

**before** `timestamp-milliseconds`

Timestamp in milliseconds.

**sort** `string`

**Possible values:** [`asc`, `desc`]

Determines the order of events in response(s).
* `asc` = chronological
* `desc` = reverse-chronological

**Default value:**`desc`

**continuation_token** `base64`

Opaque token from the `Next-Continuation-Token` header used to continue listing events. The `sort` parameter must be the same as in the previous request to continue listing in the same direction.

**count** `int64`

**Possible values:** `>= 1`

The maximum number of results to return. The upper bound is determined by a global limit.

**tradeable** `string`

If present events of other tradeables are filtered out.

## Responses​

  * 200
* application/json
* Schema

**Schema**

**accountUid** string<uuid>required

**len** `integer<uint64>` *required*

**serverTime** string<date-time>

**elements** `object[]` *required*

  * Array [

    ↳ **uid** `string` *required*

    ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

    ↳ **event** `object` *required*

**Execution** objectrequired

        ↳ **execution** `object` *required*

            ↳ **uid** `string<uuid>` *required*

            ↳ **order** `object` *required*

                ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

                ↳ **tradeable** `string` *required*

                ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

                ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

                ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

                ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

                ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

                ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

                ↳ **price** `string<decimal>` *required*

**Example:**`1234.56789`

**markPrice** string<decimal>required

**Example:**`1234.56789`

**executionType** executionType (string)

**Possible values:** [`maker`, `taker`]

**limitFilled** booleanrequired

**oldTakerOrder** object

                ↳ **uid** `string<uuid>` *required*

**accountUid** string<uuid>required

                ↳ **tradeable** `string` *required*

                ↳ **direction** `string` *required*

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Buy`, `Sell`, `Unknown`]

                ↳ **quantity** `string<decimal>` *required*

**Example:**`1234.56789`

                ↳ **filled** `string<decimal>` *required*

**Example:**`1234.56789`

                ↳ **timestamp** `integer<timestamp-milliseconds>` *required*

**Example:**`1604937694000`

**limitPrice** string<decimal>required

**Example:**`1234.56789`

**orderType** stringrequired

`Unknown` is returned when the source value couldn't be decoded; this will be replaced with a real value as soon as possible.

**Possible values:** [`Limit`, `IoC`, `Post`, `Market`, `Liquidation`, `Assignment`, `Unwind`, `Unknown`]

**clientId** stringrequired

**reduceOnly** booleanrequired

**lastUpdateTimestamp** integer<timestamp-milliseconds>required

**Example:**`1604937694000`

**spotData** string | nullnullablerequired

**regulatoryExternalUid** string<uuid>

**usdValue** string<decimal>required

**Example:**`1234.56789`

**orderData** objectnullablerequired

                ↳ **fee** `string<decimal>` *required*

**Example:**`1234.56789`

**positionSize** string<decimal>required

**Example:**`1234.56789`

**feeCalculationInfo** object[]required

  * Array [

**percentageFee** string<decimal>required

**Example:**`1234.56789`

**userFeeDiscountApplied** objectrequired

oneOf
* Decimal
* MOD2

****string

**Example:**`1234.56789`

**marketShareRebateCredited** objectrequired

oneOf
* Decimal
* MOD2

****string

**Example:**`1234.56789`

  * ]

**regulatoryData** object

                ↳ **venue** `string`

                ↳ **counterparty** `string`

**externalUid** string<uuid>

**takerReducedQuantity** stringrequired

sometimes empty string

  * ]

**continuationToken** string<base64>

Opaque token to pass to the next request to continue listing events. The `sort` parameter must be the same as in the previous request to continue listing in the same direction.

#### Authorization: APIKey
    
    
    **name:** [APIKey](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** General API key with at least **read-only** access**in:** header**x-inlineDescription:** true
    
    
    **name:** [Authent](/api/docs/futures-api/history/history#authentication)**type:** apiKey**description:** Authentication string**in:** header**x-inlineDescription:** true

  * curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://futures.kraken.com/api/history/v3/executions' \  
    -H 'Accept: application/json' \  
    -H 'APIKey: <APIKey>' \  
    -H 'Authent: <Authent>'  
    

Request Collapse all

Base URL

https://futures.kraken.com/api/history/v3

Auth

general-api-key-read-only

authent

Parameters

since — query

before — query

sort — query

\---ascdesc

continuation_token — query

count — query

tradeable — query