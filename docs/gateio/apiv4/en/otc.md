---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/otc
api_type: REST
updated_at: 2026-06-01 20:42:27.973209
---

# OTC

* Python 
  * Shell 


OTC Trading

##  Fiat and stablecoin quote🔒 Authenticated

POST`/otc/quote`

POST `/otc/quote`

_Fiat and stablecoin quote_

Create fiat and stablecoin quotes, supporting both PAY and GET directions

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcQuoteRequest | Required | none  
↳ side | body | string | Required | PAY/GET quote direction. PAY means user inputs pay amount, GET means user inputs get amount. If PAY, pay_amount is required. If GET, get_amount is required  
↳ pay_coin | body | string | Required | Currency the user pays. Supported currencies can be found on the OTC web quote page.  
↳ get_coin | body | string | Required | Currency the user receives. Supported currencies can be found on the OTC web quote page.  
↳ pay_amount | body | string | Optional | User payment currency amount  
↳ get_amount | body | string | Optional | Amount of currency received by the user  
↳ create_quote_token | body | string | Optional | Create quote token: 0: quote preview only; 1: generate quote token for order placement.  
↳ promotion_code | body | string | Optional | Promotion code (optional)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Quote retrieved successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Quote retrieved successfully | OtcQuoteResponse  
  
### Response Schema

Status Code **200**

_OtcQuoteResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» type | string | BUY (on-ramp) or SELL (off-ramp)  
»» pay_coin | string | Payment currency  
»» get_coin | string | Currency  
»» pay_amount | string | Payment amount  
»» get_amount | string | Redemption Amount  
»» rate | string | Exchange rate  
»» rate_reci | string | Reciprocal of the exchange rate  
»» promotion_code | string | Promotion code  
»» side | string | Quote method  
»» order_type | string | Order type: FIAT (fiat) / STABLE (stablecoin)  
»» quote_token | string | Quote token required when placing an order  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/quote'
    query_param = ''
    body='{"side":"PAY","pay_coin":"USDT","get_coin":"USD","pay_amount":"30000","get_amount":"30000","create_quote_token":"0","promotion_code":""}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/quote"
    query_param=""
    body_param='{"side":"PAY","pay_coin":"USDT","get_coin":"USD","pay_amount":"30000","get_amount":"30000","create_quote_token":"0","promotion_code":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "url": "",
        "memo": "",
        "type": "BUY",
        "pay_coin": "USD",
        "get_coin": "USDT",
        "pay_amount": "30000.00",
        "get_amount": "29891.00",
        "rate": "1.0036",
        "rate_reci": "0.9964",
        "promotion_code": "",
        "side": "PAY",
        "has_signature": "0",
        "validity_period": "300",
        "ex_rate": "0.9967",
        "usdc_rate": "0.99990000",
        "is_need_file": "0",
        "gate_bank_id": "1",
        "gate_bank_name": "",
        "order_type": "FIAT",
        "quote_token": "",
        "refresh_limit": 20,
        "refresh_limit_msg": ""
      },
      "timestamp": 1752051076
    }
    

##  Create fiat order🔒 Authenticated

POST`/otc/order/create`

POST `/otc/order/create`

_Create fiat order_

Create a fiat order, supporting BUY for on-ramp and SELL for off-ramp

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcOrderRequest | Required | none  
↳ type | body | string | Required | BUY (on-ramp) or SELL (off-ramp)  
↳ side | body | string | Required | Quote direction returned by the quote API (used for order validation)  
↳ crypto_currency | body | string | Required | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page)  
↳ fiat_currency | body | string | Required | Fiat currency (supported currencies can be queried from the OTC web fiat quote page)  
↳ crypto_amount | body | string | Required | Amount of cryptocurrency  
↳ fiat_amount | body | string | Required | Fiat amount  
↳ promotion_code | body | string | Optional | Promotion code  
↳ quote_token | body | string | Required | Parameter returned by the quote API  
↳ bank_id | body | string | Required | The bank card ID used for placing the order; select it from the list returned by `GET /otc/bank_list` (or `GET /otc/bank/list`); the default card has `is_default=1`  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order created successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/order/create'
    query_param = ''
    body='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/order/create"
    query_param=""
    body_param='{"type":"BUY","side":"FIAT","crypto_currency":"USDT","fiat_currency":"USD","crypto_amount":"30000","fiat_amount":"30000","promotion_code":"","quote_token":"","bank_id":"2"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "timestamp": 1752051076
    }
    

##  Create stablecoin order🔒 Authenticated

POST`/otc/stable_coin/order/create`

POST `/otc/stable_coin/order/create`

_Create stablecoin order_

Create stablecoin order

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcStableCoinOrderRequest | Required | none  
↳ pay_coin | body | string | Optional | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
↳ get_coin | body | string | Optional | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
↳ pay_amount | body | string | Optional | User payment currency amount  
↳ get_amount | body | string | Optional | Amount of currency received by the user  
↳ side | body | string | Optional | Quote direction returned by the quote API (used for order validation)  
↳ promotion_code | body | string | Optional | promotion code  
↳ quote_token | body | string | Optional | Parameter returned by the quote API  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Stablecoin order created successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Stablecoin order created successfully | OtcStableCoinOrderCreateResponse  
  
### Response Schema

Status Code **200**

_OtcStableCoinOrderCreateResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/stable_coin/order/create'
    query_param = ''
    body='{"pay_coin":"USDC","get_coin":"USDT","pay_amount":"30000","get_amount":"20000","side":"PAY","promotion_code":"","quote_token":"dsafjkdshfjdsjkfah"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/stable_coin/order/create"
    query_param=""
    body_param='{"pay_coin":"USDC","get_coin":"USDT","pay_amount":"30000","get_amount":"20000","side":"PAY","promotion_code":"","quote_token":"dsafjkdshfjdsjkfah"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string"
    }
    

##  Get user bank card list🔒 Authenticated

GET`/otc/bank_list`

GET `/otc/bank_list`

Get `user bank card list`

Retrieve the user's bank card list, used to select a bank card when placing an order. **Default card** : refer to the list item field `is_default` (1=default); there is no need to call the deprecated standalone "default bank card" endpoint. Corresponding Inner: `GET /bank_list` or `GET /bank/list`.

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcBankListResponse  
  
### Response Schema

Status Code **200**

_OtcBankListResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» lists | array | Bank card list  
»»» OtcBankListItem | object | none  
»»»» id | string | Bank ID (required for order placement)  
»»»» bank_account_name | string | Bank account name  
»»»» bank_name | string | Bank name  
»»»» bank_country | string | Bank country  
»»»» bank_address | string | Bank address  
»»»» bank_code | string | Bank code  
»»»» branch_code | string | Branch code  
»»»» iban | string | IBAN number  
»»»» swift | string | SWIFT code  
»»»» remittance_line_number | string | Remittance routing number  
»»»» agent_bank_name | string | Correspondent bank name  
»»»» agent_bank_swift | string | Correspondent bank SWIFT code  
»»»» submit_time | string | Submission time  
»»»» update_time | string | Update time  
»»»» status | string | Status  
»»»» documentation_file_type | string | Document file type  
»»»» memo | string | Remark  
»»»» is_default | integer | Whether it is the default bank card. 1 - Yes, 0 - No  
»»»» bank_id | string | Bank ID  
»»»» documentation_file_key_url | string | Document file URL  
»»» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank_list'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/otc/bank_list"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "lists": [
          {
            "id": "762",
            "bank_account_name": "hshsbshhh",
            "bank_name": "jjjsjhs",
            "bank_country": "Anguilla",
            "bank_address": "jshhtestaddress879hao",
            "bank_code": "",
            "branch_code": "",
            "iban": "1554 **** 8756",
            "swift": "455876663",
            "remittance_line_number": "4867645497945",
            "agent_bank_name": "",
            "agent_bank_swift": "",
            "submit_time": "2026-01-21 05:56:49",
            "update_time": "2026-01-21 05:57:09",
            "status": "1",
            "documentation_file_type": "",
            "memo": "",
            "is_default": 1,
            "bank_id": "762",
            "documentation_file_key_url": ""
          }
        ]
      },
      "timestamp": 1769998217
    }
    

##  Get the user's bank card list (a path synonymous with bank_list)🔒 Authenticated

GET`/otc/bank/list`

GET `/otc/bank/list`

Get `the user's bank card list (a path synonymous with bank_list)`

Semantically identical to `GET /otc/bank_list`. Corresponding Inner: `GET /bank/list`. For the default card, refer to the `is_default` field.

### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcBankListResponse  
  
### Response Schema

Status Code **200**

_OtcBankListResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» lists | array | Bank card list  
»»» OtcBankListItem | object | none  
»»»» id | string | Bank ID (required for order placement)  
»»»» bank_account_name | string | Bank account name  
»»»» bank_name | string | Bank name  
»»»» bank_country | string | Bank country  
»»»» bank_address | string | Bank address  
»»»» bank_code | string | Bank code  
»»»» branch_code | string | Branch code  
»»»» iban | string | IBAN number  
»»»» swift | string | SWIFT code  
»»»» remittance_line_number | string | Remittance routing number  
»»»» agent_bank_name | string | Correspondent bank name  
»»»» agent_bank_swift | string | Correspondent bank SWIFT code  
»»»» submit_time | string | Submission time  
»»»» update_time | string | Update time  
»»»» status | string | Status  
»»»» documentation_file_type | string | Document file type  
»»»» memo | string | Remark  
»»»» is_default | integer | Whether it is the default bank card. 1 - Yes, 0 - No  
»»»» bank_id | string | Bank ID  
»»»» documentation_file_key_url | string | Document file URL  
»»» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank/list'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/otc/bank/list"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "timestamp": 0
    }
    

##  Create bank card🔒 Authenticated

POST`/otc/bank/create`

POST `/otc/bank/create`

_Create bank card_

Bind a bank card. Under the Global entity, an account with a non-matching name may enter manual review (`status` pending) and require subsequent supplementary materials. Corresponding Inner: `POST /bank/create`. Fields and protocol are subject to the production form/gateway; in some environments `bank_account_name` is passed Base64-encoded, see the integration notes for details.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankCreateMultipartRequest | Required | none  
↳ bank_account_name | body | string | Required | none  
↳ bank_name | body | string | Required | none  
↳ bank_country | body | string | Required | none  
↳ bank_address | body | string | Required | none  
↳ iban | body | string | Required | none  
↳ swift | body | string | Required | none  
↳ remittance_line_number | body | string | Optional | none  
↳ agent_bank_name | body | string | Optional | none  
↳ agent_bank_swift | body | string | Optional | none  
↳ documentation_file | body | string(binary) | Required | Account-opening proof file (jpg/jpeg/png/pdf, etc.; single file ≤4MB — subject to production environment).  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Accepted successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Accepted successfully | OtcBankCreateResponse  
  
### Response Schema

Status Code **200**

_Bank card created successfully (Inner returns bank_id and status)._

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» bank_id | integer | Bank card primary key in otc_rds.  
»» status | integer | Review status (e.g., pending review).  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank/create'
    query_param = ''
    body='{"bank_account_name":"string","bank_name":"string","bank_country":"string","bank_address":"string","iban":"string","swift":"string","remittance_line_number":"string","agent_bank_name":"string","agent_bank_swift":"string","documentation_file":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/bank/create"
    query_param=""
    body_param='{"bank_account_name":"string","bank_name":"string","bank_country":"string","bank_address":"string","iban":"string","swift":"string","remittance_line_number":"string","agent_bank_name":"string","agent_bank_swift":"string","documentation_file":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    bank_account_name: string
    bank_name: string
    bank_country: string
    bank_address: string
    iban: string
    swift: string
    remittance_line_number: string
    agent_bank_name: string
    agent_bank_swift: string
    documentation_file: string
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "bank_id": 0,
        "status": 0
      },
      "timestamp": 0
    }
    

##  Delete bank card🔒 Authenticated

POST`/otc/bank/delete`

POST `/otc/bank/delete`

Delete `bank card`

Delete `the specified bank card. Corresponds to Inner: POST /bank/delete.`

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankIdRequest | Required | none  
↳ bank_id | body | string | Required | Bank card ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Deleted successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Deleted successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank/delete'
    query_param = ''
    body='{"bank_id":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/bank/delete"
    query_param=""
    body_param='{"bank_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "bank_id": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Set default bank card🔒 Authenticated

POST`/otc/bank/set_default`

POST `/otc/bank/set_default`

_Set default bank card_

Set the specified bank card as default. Corresponds to Inner: `POST /bank/set_default`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankIdRequest | Required | none  
↳ bank_id | body | string | Required | Bank card ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Set successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Set successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank/set_default'
    query_param = ''
    body='{"bank_id":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/bank/set_default"
    query_param=""
    body_param='{"bank_id":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "bank_id": "string"
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Query the checklist of materials to supplement for a bank card🔒 Authenticated

GET`/otc/bank/bank_supplement_checklist`

GET `/otc/bank/bank_supplement_checklist`

_Query the checklist of materials to supplement for a bank card_

**①** `bank_id` must be specified: after verifying that the card belongs to the current user and its status allows supplementation, returns the items to be supplemented and whether each sub-item is required, based on the user's **passed professional verification type** (personal/enterprise). Corresponding Inner: `GET /bank/bank_supplement_checklist`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
bank_id | query | string | Required | Bank card ID (otc_rds / the id returned by the list endpoint).  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcBankSupplementChecklistResponse  
  
### Response Schema

Status Code **200**

_OtcBankSupplementChecklistResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» user_type | string | personal or enterprise  
»» items | array | none  
»»» code | string | Material item code, corresponding to the top-level key of `relationship_proof`  
»»» zh | string | none  
»»» en | string | none  
»»» required | boolean | Whether required  
»» timestamp | integer | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
user_type | personal  
user_type | enterprise  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank/bank_supplement_checklist'
    query_param = 'bank_id=string'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/otc/bank/bank_supplement_checklist"
    query_param="bank_id=string"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "user_type": "personal",
        "items": [
          {}
        ]
      },
      "timestamp": 0
    }
    

##  Submit Bank Card Supplement Materials (Personal)🔒 Authenticated

POST`/otc/bank/personal/bank_supplement`

POST `/otc/bank/personal/bank_supplement`

_Submit Bank Card Supplement Materials (Personal)_

**Personal professional verification (type=1)** users submit non-same-person/supplementary materials. Must match `user_type=personal` returned by `GET /otc/bank/bank_supplement_checklist?bank_id=`, otherwise the request is rejected. **multipart/form-data** is recommended: each material item is a separate file field, with field names matching the checklist `code` (`id_document_front`, `id_document_back`, `address_proof`).

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankPersonalSupplementMultipartRequest | Required | none  
↳ bank_id | body | string | Required | none  
↳ id_document_front | body | string(binary) | Required | none  
↳ id_document_back | body | string(binary) | Required | none  
↳ address_proof | body | string(binary) | Required | none  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Accepted successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Accepted successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank/personal/bank_supplement'
    query_param = ''
    body='{"bank_id":"string","id_document_front":"string","id_document_back":"string","address_proof":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/bank/personal/bank_supplement"
    query_param=""
    body_param='{"bank_id":"string","id_document_front":"string","id_document_back":"string","address_proof":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    bank_id: string
    id_document_front: string
    id_document_back: string
    address_proof: string
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Submit Bank Card Supplement Materials (Enterprise)🔒 Authenticated

POST`/otc/bank/enterprise/bank_supplement`

POST `/otc/bank/enterprise/bank_supplement`

_Submit Bank Card Supplement Materials (Enterprise)_

**Enterprise professional verification (type=2)** users submit supplementary materials. Must match `user_type=enterprise` returned by the checklist. **multipart** file field names: `certificate`, `share_holders`, `passport`, `share_holding_structure`.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcBankEnterpriseSupplementMultipartRequest | Required | none  
↳ uid | body | string | Optional | none  
↳ bank_id | body | string | Required | none  
↳ certificate | body | string(binary) | Required | none  
↳ share_holders | body | string(binary) | Required | none  
↳ passport | body | string(binary) | Required | none  
↳ share_holding_structure | body | string(binary) | Required | none  
↳ funds_statement | body | string(binary) | Optional | none  
↳ additional | body | string(binary) | Optional | none  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Accepted successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Accepted successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/bank/enterprise/bank_supplement'
    query_param = ''
    body='{"uid":"string","bank_id":"string","certificate":"string","share_holders":"string","passport":"string","share_holding_structure":"string","funds_statement":"string","additional":"string"}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/bank/enterprise/bank_supplement"
    query_param=""
    body_param='{"uid":"string","bank_id":"string","certificate":"string","share_holders":"string","passport":"string","share_holding_structure":"string","funds_statement":"string","additional":"string"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    uid: string
    bank_id: string
    certificate: string
    share_holders: string
    passport: string
    share_holding_structure: string
    funds_statement: string
    additional: string
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    

##  Mark fiat order as paid (deposit confirmation)🔒 Authenticated

POST`/otc/order/paid`

POST `/otc/order/paid`

_Mark fiat order as paid (deposit confirmation)_

Mark a fiat buy order as paid (deposit confirmation). **The user's payment receipt must be uploaded** : `payment_receipt_file_key` is required; file format jpg / jpeg / png / pdf, single file no larger than 4MB (jointly validated by the server and gateway). The compatible field name `payment_receipt` is subject to the gateway/production environment. For the persisted field, see `otc_trade_record.payment_receipt_file_key`. The Pay Inner path is `POST .../pay/order_set_paid` (orders are usually associated via `client_order_id`); this OpenAPI path maps to Inner `POST /order/paid` and still uses `order_id` as the primary key—if the gateway unifies it to the merchant order number, the gateway documentation prevails.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | OtcMarkOrderPaidRequest | Required | none  
↳ order_id | body | string | Required | Order ID  
↳ client_order_id | body | string | Optional | Client order ID (used by some gateway/Inner Pay paths, optional)  
↳ payment_receipt_file_key | body | string | Required | User payment receipt: **required**. Stored as a file_key. Single file; jpg/jpeg/png/pdf; ≤4MB.  
↳ payment_receipt | body | string | Optional | Alias compatible with `payment_receipt_file_key` (depends on the gateway's external field name)  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)The order has been marked as paid

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | The order has been marked as paid | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/order/paid'
    query_param = ''
    body='{"order_id":"203","client_order_id":"","payment_receipt_file_key":"BASE64_ENCODED_FILE_KEY","payment_receipt":""}'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/order/paid"
    query_param=""
    body_param='{"order_id":"203","client_order_id":"","payment_receipt_file_key":"BASE64_ENCODED_FILE_KEY","payment_receipt":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "order_id": "203",
      "client_order_id": "",
      "payment_receipt_file_key": "BASE64_ENCODED_FILE_KEY",
      "payment_receipt": ""
    }
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "timestamp": 1752051076
    }
    

##  Fiat order cancellation🔒 Authenticated

POST`/otc/order/cancel`

POST `/otc/order/cancel`

_Fiat order cancellation_

Cancel fiat order

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | query | string | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Order cancelled successfully

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Order cancelled successfully | OtcActionResponse  
  
### Response Schema

Status Code **200**

_OtcActionResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» timestamp | integer | none  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/order/cancel'
    query_param = 'order_id=string'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('POST', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="POST"
    url="/otc/order/cancel"
    query_param="order_id=string"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "timestamp": 1752051076
    }
    

##  Fiat order list🔒 Authenticated

GET`/otc/order/list`

GET `/otc/order/list`

_Fiat order list_

Query the fiat order list with filters such as type, currency, time range, and status

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
type | query | string | Optional | BUY (on-ramp) or SELL (off-ramp)  
fiat_currency | query | string | Optional | Fiat currency  
crypto_currency | query | string | Optional | Digital currency  
start_time | query | string | Optional | Start Time  
end_time | query | string | Optional | End time  
status | query | string | Optional | DONE ：Completed  
pn | query | string | Optional | Page number  
ps | query | string | Optional | Number of items per page  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcOrderListResponse  
  
### Response Schema

Status Code **200**

_OtcOrderListResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» pn | integer | none  
»» ps | integer | none  
»» total_pn | integer | none  
»» count | integer | none  
»» list | array | none  
»»» OtcOrderListItem | object | none  
»»»» time | string | Current time  
»»»» timestamp | integer | Current timestamp  
»»»» order_id | string | orderId  
»»»» trade_no | string | Trade number  
»»»» type | string | Quote direction buy/sell/all  
»»»» status | string | Order Status  
»»»» db_status | string | none  
»»»» fiat_currency | string | Fiat type  
»»»» fiat_currency_info | object | none  
»»»»» name | string | Name  
»»»»» icon | string | Image  
»»»» fiat_amount | string | Fiat amount  
»»»» crypto_currency | string | Stablecoin  
»»»» crypto_currency_info | object | none  
»»»»» name | string | none  
»»»»» icon | string | none  
»»»» crypto_amount | string | Stablecoin amount  
»»»» rate | string | Exchange rate  
»»»» transfer_remark | string | Remark  
»»»» gate_bank_account_iban | string | Bank account  
»»»» promotion_code | string | Promotion code  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/order/list'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/otc/order/list"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "Success",
      "data": {
        "pn": 1,
        "ps": 10,
        "total_pn": 1,
        "count": 2,
        "list": [
          {
            "time": "2025-02-11 07:45:06",
            "timestamp": 1739000013,
            "order_id": "41",
            "trade_no": "20250207043457590939",
            "type": "SELL",
            "status": "PROCESSIONG",
            "db_status": "PAID",
            "fiat_currency": "USD",
            "fiat_currency_info": {
              "name": "USD",
              "icon": "http://icon.url"
            },
            "fiat_amount": "199600",
            "ceypto_currency": "USDT",
            "crypto_currency_info": {
              "name": "USDT",
              "icon": "http://icon.url"
            },
            "crypto_amount": "200000",
            "rate": "0.998000",
            "transfer_remark": "",
            "gate_bank_account_iban": "89b9b9b9b",
            "promotion_code": ""
          }
        ]
      }
    }
    

##  Stablecoin order list🔒 Authenticated

GET`/otc/stable_coin/order/list`

GET `/otc/stable_coin/order/list`

_Stablecoin order list_

Query stablecoin order list with filtering by currency, time range, status, etc.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
page_size | query | string | Optional | Number of records per page  
page_number | query | string | Optional | Page number  
coin_name | query | string | Optional | ordercurrency  
start_time | query | string | Optional | Start Time  
end_time | query | string | Optional | End time  
status | query | string | Optional | Status: PROCESSING: in progress / DONE：completed / FAILED: failed  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcStableCoinOrderListResponse  
  
### Response Schema

Status Code **200**

_OtcStableCoinOrderListResponse_

Name | Type | Description  
---|---|---  
» code | integer | none  
» message | string | none  
» data | object | none  
»» total | integer | none  
»» page_size | integer | none  
»» page_number | integer | none  
»» total_page | integer | none  
»» list | array | none  
»»» OtcStableCoinOrderListItem | object | none  
»»»» id | integer | Order ID  
»»»» trade_no | string | Transaction reference number  
»»»» pay_coin | string | Payment currency  
»»»» pay_amount | string | Payment amount  
»»»» get_coin | string | Received currency  
»»»» get_amount | string | Received amount  
»»»» rate | string | Exchange rate  
»»»» rate_reci | string | Reciprocal of the exchange rate  
»»»» status | string | PROCESSING: in progress / DONE: completed / FAILED: failed  
»»»» create_timest | integer | timetimestamp  
»»»» create_time | string | Created time  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/stable_coin/order/list'
    query_param = ''
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/otc/stable_coin/order/list"
    query_param=""
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "code": 0,
      "message": "success",
      "data": {
        "total": 20,
        "page_size": 10,
        "page_number": 1,
        "total_page": 10,
        "list": [
          {
            "id": 1,
            "trade_no": "89875324974",
            "pay_coin": "USDT",
            "pay_icon": "https://icon.com",
            "pay_amount": "30000.00",
            "get_coin": "JDUSD",
            "get_icon": "https://icon.com",
            "get_amount": "20000.00",
            "rate": "1.5",
            "rate_reci": "0.6667",
            "status": "PROCESSING",
            "create_timest": 17878979789,
            "create_time": "2025-09-09 10:00:00"
          }
        ]
      }
    }
    

##  Fiat order details🔒 Authenticated

GET`/otc/order/detail`

GET `/otc/order/detail`

_Fiat order details_

Query fiat order details

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
order_id | query | string | Required | Order ID  
  
### Responses

  * 200[OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1)Query successful

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | Query successful | OtcOrderDetailResponse  
  
### Response Schema

Status Code **200**

_OtcOrderDetailResponse_

Name | Type | Description  
---|---|---  
» message | string | none  
» code | integer | none  
» data | object | none  
»» order_id | string | Order ID  
»» uid | string | User ID  
»» type | string | Order Type  
»» fiat_currency | string | Fiat type  
»» fiat_amount | string | Fiat amount  
»» crypto_currency | string | Stablecoin  
»» crypto_amount | string | Stablecoin amount  
»» rate | string | Exchange rate  
»» transfer_remark | string | Remark  
»» status | string | Status  
»» db_status | string | none  
»» create_time | string | Created time  
»» memo | string | Cancellation or rejection reason  
»» side | string | Quote direction  
»» promotion_code | string | Promotion code  
»» trade_no | string | Trade number  
  
WARNING

To perform this operation, you must be authenticated by API key and secret

Code samples
    
    
    # coding: utf-8
    import requests
    import time
    import hashlib
    import hmac
    
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    url = '/otc/order/detail'
    query_param = 'order_id=string'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())
    
    
    
    
    key="YOUR_API_KEY"
    secret="YOUR_API_SECRET"
    host="https://api.gateio.ws"
    prefix="/api/v4"
    method="GET"
    url="/otc/order/detail"
    query_param="order_id=string"
    body_param=''
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url?$query_param"
    curl -X $method $full_url \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Example responses

> 200 Response
    
    
    {
      "message": "成功",
      "code": 0,
      "data": {
        "order_id": "265",
        "uid": "2124269088",
        "type": "BUY",
        "fiat_currency": "USD",
        "fiat_amount": "300000",
        "crypto_currency": "USDT",
        "crypto_amount": "299700",
        "rate": "1.001001",
        "transfer_remark": "Bank Code: 016, Branch Code: 478",
        "status": "PROCESSIONG",
        "db_status": "PAID",
        "create_time": "2025-03-07 07:51:52",
        "memo": "",
        "side": "FIAT",
        "promotion_code": "",
        "trade_no": "20250307075152206853"
      }
    }
    

#  Schemas

##  OtcStableCoinOrderRequest

_Stablecoin Order Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
pay_coin | string | Optional | none | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
get_coin | string | Optional | none | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page.  
pay_amount | string | Optional | none | User payment currency amount  
get_amount | string | Optional | none | Amount of currency received by the user  
side | string | Optional | none | Quote direction returned by the quote API (used for order validation)  
promotion_code | string | Optional | none | promotion code  
quote_token | string | Optional | none | Parameter returned by the quote API  
      
    
    {
      "pay_coin": "USDC",
      "get_coin": "USDT",
      "pay_amount": "30000",
      "get_amount": "20000",
      "side": "PAY",
      "promotion_code": "",
      "quote_token": "dsafjkdshfjdsjkfah"
    }
    
    

##  OtcStableCoinOrderListResponse

_OtcStableCoinOrderListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ total | integer | Required | none | none  
↳ page_size | integer | Required | none | none  
↳ page_number | integer | Required | none | none  
↳ total_page | integer | Required | none | none  
↳ list | array | Required | none | none  
↳ OtcStableCoinOrderListItem | object | Optional | none | none  
↳ id | integer | Optional | none | Order ID  
↳ trade_no | string | Optional | none | Transaction reference number  
↳ pay_coin | string | Optional | none | Payment currency  
↳ pay_amount | string | Optional | none | Payment amount  
↳ get_coin | string | Optional | none | Received currency  
↳ get_amount | string | Optional | none | Received amount  
↳ rate | string | Optional | none | Exchange rate  
↳ rate_reci | string | Optional | none | Reciprocal of the exchange rate  
↳ status | string | Optional | none | PROCESSING: in progress / DONE: completed / FAILED: failed  
↳ create_timest | integer | Optional | none | timetimestamp  
↳ create_time | string | Optional | none | Created time  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "total": 0,
        "page_size": 0,
        "page_number": 0,
        "total_page": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  OtcBankListResponse

_OtcBankListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ lists | array | Required | none | Bank card list  
↳ OtcBankListItem | object | Optional | none | none  
↳ id | string | Required | none | Bank ID (required for order placement)  
↳ bank_account_name | string | Required | none | Bank account name  
↳ bank_name | string | Required | none | Bank name  
↳ bank_country | string | Optional | none | Bank country  
↳ bank_address | string | Optional | none | Bank address  
↳ bank_code | string | Optional | none | Bank code  
↳ branch_code | string | Optional | none | Branch code  
↳ iban | string | Optional | none | IBAN number  
↳ swift | string | Optional | none | SWIFT code  
↳ remittance_line_number | string | Optional | none | Remittance routing number  
↳ agent_bank_name | string | Optional | none | Correspondent bank name  
↳ agent_bank_swift | string | Optional | none | Correspondent bank SWIFT code  
↳ submit_time | string | Optional | none | Submission time  
↳ update_time | string | Optional | none | Update time  
↳ status | string | Optional | none | Status  
↳ documentation_file_type | string | Optional | none | Document file type  
↳ memo | string | Optional | none | Remark  
↳ is_default | integer | Optional | none | Whether it is the default bank card. 1 - Yes, 0 - No  
↳ bank_id | string | Optional | none | Bank ID  
↳ documentation_file_key_url | string | Optional | none | Document file URL  
↳ timestamp | integer | Required | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  OtcMarkOrderPaidRequest

_Request body for marking a fiat order as paid (deposit confirmation). Must include the user's payment receipt (consistent with §3.2).  
**`payment_receipt_file_key` is required**; the order primary key on this path is `order_id`. When accessed via the Pay gateway using `client_order_id`, the gateway's rewritten field takes precedence._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
order_id | string | Required | none | Order ID  
client_order_id | string | Optional | none | Client order ID (used by some gateway/Inner Pay paths, optional)  
payment_receipt_file_key | string | Required | none | User payment receipt: **required**. Stored as a file_key. Single file; jpg/jpeg/png/pdf; ≤4MB.  
payment_receipt | string | Optional | none | Alias compatible with `payment_receipt_file_key` (depends on the gateway's external field name)  
      
    
    {
      "order_id": "203",
      "client_order_id": "",
      "payment_receipt_file_key": "BASE64_ENCODED_FILE_KEY",
      "payment_receipt": ""
    }
    
    

##  OtcOrderRequest

_Fiat Order Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
type | string | Required | none | BUY (on-ramp) or SELL (off-ramp)  
side | string | Required | none | Quote direction returned by the quote API (used for order validation)  
crypto_currency | string | Required | none | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page)  
fiat_currency | string | Required | none | Fiat currency (supported currencies can be queried from the OTC web fiat quote page)  
crypto_amount | string | Required | none | Amount of cryptocurrency  
fiat_amount | string | Required | none | Fiat amount  
promotion_code | string | Optional | none | Promotion code  
quote_token | string | Required | none | Parameter returned by the quote API  
bank_id | string | Required | none | The bank card ID used for placing the order; select it from the list returned by `GET /otc/bank_list` (or `GET /otc/bank/list`); the default card has `is_default=1`  
      
    
    {
      "type": "BUY",
      "side": "FIAT",
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "crypto_amount": "30000",
      "fiat_amount": "30000",
      "promotion_code": "",
      "quote_token": "",
      "bank_id": "2"
    }
    
    

##  OtcOrderDetailResponse

_OtcOrderDetailResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
message | string | Required | none | none  
code | integer | Required | none | none  
data | object | Required | none | none  
↳ order_id | string | Required | none | Order ID  
↳ uid | string | Required | none | User ID  
↳ type | string | Required | none | Order Type  
↳ fiat_currency | string | Required | none | Fiat type  
↳ fiat_amount | string | Required | none | Fiat amount  
↳ crypto_currency | string | Required | none | Stablecoin  
↳ crypto_amount | string | Required | none | Stablecoin amount  
↳ rate | string | Required | none | Exchange rate  
↳ transfer_remark | string | Required | none | Remark  
↳ status | string | Required | none | Status  
↳ db_status | string | Required | none | none  
↳ create_time | string | Required | none | Created time  
↳ memo | string | Required | none | Cancellation or rejection reason  
↳ side | string | Required | none | Quote direction  
↳ promotion_code | string | Required | none | Promotion code  
↳ trade_no | string | Required | none | Trade number  
      
    
    {
      "message": "string",
      "code": 0,
      "data": {
        "order_id": "string",
        "uid": "string",
        "type": "string",
        "fiat_currency": "string",
        "fiat_amount": "string",
        "crypto_currency": "string",
        "crypto_amount": "string",
        "rate": "string",
        "transfer_remark": "string",
        "status": "string",
        "db_status": "string",
        "create_time": "string",
        "memo": "string",
        "side": "string",
        "promotion_code": "string",
        "trade_no": "string"
      }
    }
    
    

##  OtcQuoteResponse

_OtcQuoteResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ type | string | Required | none | BUY (on-ramp) or SELL (off-ramp)  
↳ pay_coin | string | Required | none | Payment currency  
↳ get_coin | string | Required | none | Currency  
↳ pay_amount | string | Required | none | Payment amount  
↳ get_amount | string | Required | none | Redemption Amount  
↳ rate | string | Required | none | Exchange rate  
↳ rate_reci | string | Required | none | Reciprocal of the exchange rate  
↳ promotion_code | string | Required | none | Promotion code  
↳ side | string | Required | none | Quote method  
↳ order_type | string | Required | none | Order type: FIAT (fiat) / STABLE (stablecoin)  
↳ quote_token | string | Required | none | Quote token required when placing an order  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "type": "string",
        "pay_coin": "string",
        "get_coin": "string",
        "pay_amount": "string",
        "get_amount": "string",
        "rate": "string",
        "rate_reci": "string",
        "promotion_code": "string",
        "side": "string",
        "order_type": "string",
        "quote_token": "string"
      }
    }
    
    

##  OtcBankPersonalSupplementMultipartRequest

_Personal supplement`multipart/form-data`. File field names are fixed: `id_document_front`, `id_document_back`, `address_proof` (aligned with the checklist `code`); the optional string field `relationship_proof` (JSON text) is merged with the upload result._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
bank_id | string | Required | none | none  
id_document_front | string(binary) | Required | none | none  
id_document_back | string(binary) | Required | none | none  
address_proof | string(binary) | Required | none | none  
      
    
    {
      "bank_id": "string",
      "id_document_front": "string",
      "id_document_back": "string",
      "address_proof": "string"
    }
    
    

##  OtcActionResponse

_OtcActionResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
timestamp | integer | Required | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "timestamp": 0
    }
    
    

##  OtcBankCreateResponse

_Bank card created successfully (Inner returns bank_id and status)._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ bank_id | integer | Required | none | Bank card primary key in otc_rds.  
↳ status | integer | Required | none | Review status (e.g., pending review).  
timestamp | integer | Optional | none | none  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "bank_id": 0,
        "status": 0
      },
      "timestamp": 0
    }
    
    

##  OtcBankIdRequest

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
bank_id | string | Required | none | Bank card ID  
      
    
    {
      "bank_id": "string"
    }
    
    

##  OtcQuoteRequest

_Fiat and Stablecoin Quote Request Body_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
side | string | Required | none | PAY/GET quote direction. PAY means user inputs pay amount, GET means user inputs get amount. If PAY, pay_amount is required. If GET, get_amount is required  
pay_coin | string | Required | none | Currency the user pays. Supported currencies can be found on the OTC web quote page.  
get_coin | string | Required | none | Currency the user receives. Supported currencies can be found on the OTC web quote page.  
pay_amount | string | Optional | none | User payment currency amount  
get_amount | string | Optional | none | Amount of currency received by the user  
create_quote_token | string | Optional | none | Create quote token: 0: quote preview only; 1: generate quote token for order placement.  
promotion_code | string | Optional | none | Promotion code (optional)  
      
    
    {
      "side": "PAY",
      "pay_coin": "USDT",
      "get_coin": "USD",
      "pay_amount": "30000",
      "get_amount": "30000",
      "create_quote_token": "0",
      "promotion_code": ""
    }
    
    

##  OtcStableCoinOrderCreateResponse

_OtcStableCoinOrderCreateResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
      
    
    {
      "code": 0,
      "message": "string"
    }
    
    

##  OtcBankSupplementChecklistResponse

_OtcBankSupplementChecklistResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ user_type | string | Required | none | personal or enterprise  
↳ items | [OtcBankSupplementChecklistItem] | Required | none | none  
timestamp | integer | Optional | none | none  
  
####  Enumerated Values

Enumerated ValuesProperty | Value  
---|---  
user_type | personal  
user_type | enterprise  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "user_type": "personal",
        "items": [
          {}
        ]
      },
      "timestamp": 0
    }
    
    

##  OtcBankCreateMultipartRequest

_Inner create-bank-card`multipart/form-data`. Use the form field `documentation_file` to upload the account-opening proof._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
bank_account_name | string | Required | none | none  
bank_name | string | Required | none | none  
bank_country | string | Required | none | none  
bank_address | string | Required | none | none  
iban | string | Required | none | none  
swift | string | Required | none | none  
remittance_line_number | string | Optional | none | none  
agent_bank_name | string | Optional | none | none  
agent_bank_swift | string | Optional | none | none  
documentation_file | string(binary) | Required | none | Account-opening proof file (jpg/jpeg/png/pdf, etc.; single file ≤4MB — subject to production environment).  
      
    
    {
      "bank_account_name": "string",
      "bank_name": "string",
      "bank_country": "string",
      "bank_address": "string",
      "iban": "string",
      "swift": "string",
      "remittance_line_number": "string",
      "agent_bank_name": "string",
      "agent_bank_swift": "string",
      "documentation_file": "string"
    }
    
    

##  OtcBankEnterpriseSupplementMultipartRequest

_Enterprise supplement`multipart/form-data`. File field names: `certificate`, `share_holders`, `passport`, `share_holding_structure`; optional `funds_statement`, `additional`. Optional string field `relationship_proof` (JSON) is merged into the request._

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
uid | string | Optional | none | none  
bank_id | string | Required | none | none  
certificate | string(binary) | Required | none | none  
share_holders | string(binary) | Required | none | none  
passport | string(binary) | Required | none | none  
share_holding_structure | string(binary) | Required | none | none  
funds_statement | string(binary) | Optional | none | none  
additional | string(binary) | Optional | none | none  
      
    
    {
      "uid": "string",
      "bank_id": "string",
      "certificate": "string",
      "share_holders": "string",
      "passport": "string",
      "share_holding_structure": "string",
      "funds_statement": "string",
      "additional": "string"
    }
    
    

##  OtcOrderListResponse

_OtcOrderListResponse_

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | integer | Required | none | none  
message | string | Required | none | none  
data | object | Required | none | none  
↳ pn | integer | Required | none | none  
↳ ps | integer | Required | none | none  
↳ total_pn | integer | Required | none | none  
↳ count | integer | Required | none | none  
↳ list | array | Required | none | none  
↳ OtcOrderListItem | object | Optional | none | none  
↳ time | string | Optional | none | Current time  
↳ timestamp | integer | Optional | none | Current timestamp  
↳ order_id | string | Optional | none | orderId  
↳ trade_no | string | Optional | none | Trade number  
↳ type | string | Optional | none | Quote direction buy/sell/all  
↳ status | string | Optional | none | Order Status  
↳ db_status | string | Optional | none | none  
↳ fiat_currency | string | Optional | none | Fiat type  
↳ fiat_currency_info | object | Optional | none | none  
↳ name | string | Required | none | Name  
↳ icon | string | Required | none | Image  
↳ fiat_amount | string | Optional | none | Fiat amount  
↳ crypto_currency | string | Optional | none | Stablecoin  
↳ crypto_currency_info | object | Optional | none | none  
↳ name | string | Required | none | none  
↳ icon | string | Required | none | none  
↳ crypto_amount | string | Optional | none | Stablecoin amount  
↳ rate | string | Optional | none | Exchange rate  
↳ transfer_remark | string | Optional | none | Remark  
↳ gate_bank_account_iban | string | Optional | none | Bank account  
↳ promotion_code | string | Optional | none | Promotion code  
      
    
    {
      "code": 0,
      "message": "string",
      "data": {
        "pn": 0,
        "ps": 0,
        "total_pn": 0,
        "count": 0,
        "list": [
          {}
        ]
      }
    }
    
    

##  OtcBankSupplementChecklistItem

###  Properties

PropertiesName | Type | Required | Restrictions | Description  
---|---|---|---|---  
code | string | Required | none | Material item code, corresponding to the top-level key of `relationship_proof`  
zh | string | Optional | none | none  
en | string | Optional | none | none  
required | boolean | Required | none | Whether required  
      
    
    {
      "code": "string",
      "zh": "string",
      "en": "string",
      "required": true
    }