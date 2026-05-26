---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-credit-lines
api_type: REST
updated_at: 2026-05-26 14:52:55.039186
---

# Get Credit Lines

**POST** `https://api.kraken.com/0/private/CreditLines`

Retrieve all credit line details for VIPs with this functionality.

**API Key Permissions Required:** `Funds permissions - Query`

## Request​

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**rebase_multiplier** `rebase_multiplier (string)nullable`

Optional parameter for viewing xstocks data.
* `rebased`: Display in terms of underlying equity.
* `base`: Display in terms of SPV tokens.

**Possible values:** [`rebased`, `base`]

**Default value:**`rebased`

## Responses​

  * 200

Credit line details retrieved.

  * application/json
* Schema

**Schema**

**result** `objectnullable`

Credit Line Details

    ↳ **asset_details** `object`

Balances by asset

**property name*** CreditLinesAsset

Credit line details for a specific asset

        ↳ **balance** `string`

Current balance for the asset

**Example:**`1000.5000`

        ↳ **credit_limit** `string`

Credit limit for the asset

**Example:**`50000.0000`

        ↳ **credit_used** `string`

Currently used credit for the asset

**Example:**`12500.0000`

        ↳ **available_credit** `string`

Available credit for the asset

**Example:**`37500.0000`

        ↳ **limits_monitor** `object`

Credit monitor

            ↳ **total_credit_usd** `stringnullable`

Total credit across all assets represented in USD

**Example:**`100000.0000`

            ↳ **total_credit_used_usd** `stringnullable`

Total credit used across all assets represented in USD

**Example:**`25000.0000`

            ↳ **total_collateral_value_usd** `stringnullable`

Sum of asset balance in USD * collateral

**Example:**`150000.0000`

            ↳ **equity_usd** `stringnullable`

Total collateral - total credit (in USD)

**Example:**`125000.0000`

            ↳ **ongoing_balance** `stringnullable`

Total collateral / total credit (in USD)

**Example:**`1.5000`

            ↳ **debt_to_equity** `stringnullable`

Total credit used / equity (in USD)

**Example:**`0.2000`

**error** `string[]`
* curl
  * python
  * go
  * nodejs
  * php
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/CreditLines' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 0,  
      "rebase_multiplier": "rebased"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 0,
      "rebase_multiplier": "rebased"
    }