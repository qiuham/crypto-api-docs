---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-withdrawal-addresses
api_type: REST
updated_at: 2026-06-04 19:46:52.347481
---

# Get Withdrawal Information

**POST** `https://api.kraken.com/0/private/WithdrawInfo`

Retrieve fee information about potential withdrawals for a particular asset, key and amount.

**API Key Permissions Required:** `Funds permissions - Query` and `Funds permissions - Withdraw`

## Request

  * application/json

### Body**required**

**nonce** `integer<int64>` *required*

Nonce used in construction of `API-Sign` header

**asset** `string` *required*

Asset being withdrawn

**key** `string` *required*

Withdrawal key name, as set up on your account

**amount** `string` *required*

Amount to be withdrawn

## Responses

  * 200

Withdrawal information retrieved.

  * application/json
* Schema

**Schema**

**result** `object`

Withdrawal Info

**method** `string`

Name of the withdrawal method that will be used

**limit** `string`

Maximum net amount that can be withdrawn right now

**amount** `string`

Net amount that will be sent, after fees

**fee** `string`

Amount of fees that will be paid

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/private/WithdrawInfo' \  
    -H 'Content-Type: application/json' \  
    -H 'Accept: application/json' \  
    -H 'API-Key: <API-Key>' \  
    -H 'API-Sign: <API-Sign>' \  
    -d '{  
      "nonce": 1695828271,  
      "asset": "XBT",  
      "key": "btc_testnet",  
      "amount": "0.725"  
    }'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

Auth

API-Key

API-Sign

Body required
    
    
    {
      "nonce": 1695828271,
      "asset": "XBT",
      "key": "btc_testnet",
      "amount": "0.725"
    }