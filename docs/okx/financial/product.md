---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product
anchor_id: financial-product
api_type: API
updated_at: 2026-01-15T23:28:04.521360
---

# Financial Product

## On-chain earn  
  
Only the assets in the funding account can be used for purchase. [More details](/earn/onchain-earn)

### GET / Offers

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/offers`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/offers
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_offers(ccy="USDT")
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | No | Product ID  
protocolType | String | No | Protocol type  
`defi`: on-chain earn  
ccy | String | No | Investment currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "DOT",
                "productId": "101",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1767",
                "earlyRedeem": false,
                "state": "purchasable",
                "investData": [
                    {
                        "bal": "0",
                        "ccy": "DOT",
                        "maxAmt": "0",
                        "minAmt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0"
                    }
                ],
                "fastRedemptionDailyLimit": "",
                "redeemPeriod": [
                    "28D",
                    "28D"
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency type, e.g. `BTC`  
productId | String | Product ID  
protocol | String | Protocol  
protocolType | String | Protocol type  
`defi`: on-chain earn  
term | String | Protocol term  
It will return the days of fixed term and will return `0` for flexible product  
apy | String | Estimated annualization  
If the annualization is 7% , this field is 0.07  
earlyRedeem | Boolean | Whether the protocol supports early redemption  
investData | Array of objects | Current target currency information available for investment  
> ccy | String | Investment currency, e.g. `BTC`  
> bal | String | Available balance to invest  
> minAmt | String | Minimum subscription amount  
> maxAmt | String | Maximum available subscription amount  
earningData | Array of objects | Earning data  
> ccy | String | Earning currency, e.g. `BTC`  
> earningType | String | Earning type  
`0`: Estimated earning  
`1`: Cumulative earning  
state | String | Product state  
`purchasable`: Purchasable  
`sold_out`: Sold out  
`Stop`: Suspension of subscription  
redeemPeriod | Array of strings | Redemption Period, format in [min time,max time]  
`H`: Hour, `D`: Day  
e.g. ["1H","24H"] represents redemption period is between 1 Hour and 24 Hours.  
["14D","14D"] represents redemption period is 14 days.  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
If fast redemption is not supported, it will return ''.  
  
### POST / Purchase

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/purchase`

> Request Example
    
    
    # Invest 100ZIL 30-day staking protocol
    POST /api/v5/finance/staking-defi/purchase
    body 
    {
        "productId":"1234",
        "investData":[
          {
            "ccy":"ZIL",
            "amt":"100"
          }
        ],
        "term":"30"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.purchase(
                productId = "4005", 
                investData = [{
                    "ccy":"USDT",
                    "amt":"100"
                }]
            )
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | Yes | Product ID  
investData | Array of objects | Yes | Investment data  
> ccy | String | Yes | Investment currency, e.g. `BTC`  
> amt | String | Yes | Investment amount  
term | String | Conditional | Investment term  
Investment term must be specified for fixed-term product  
tag | String | No | Order tag  
A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 16 characters.  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
tag | String | Order tag  
  
### POST / Redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/redeem`

> Request Example
    
    
    # Early redemption of investment
    POST /api/v5/finance/staking-defi/redeem
    body 
    {
        "ordId":"754147",
        "protocolType":"defi",
        "allowEarlyRedeem":true
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    
    result = StakingAPI.redeem(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
protocolType | String | Yes | Protocol type  
`defi`: on-chain earn  
allowEarlyRedeem | Boolean | No | Whether allows early redemption  
Default is `false`  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
tag | String | Order tag  
  
### POST / Cancel purchases/redemptions

After cancelling, returning funds will go to the funding account. 

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/cancel`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/cancel
    body 
    {
        "ordId":"754147",
        "protocolType":"defi"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.cancel(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
protocolType | String | Yes | Protocol type  
`defi`: on-chain earn  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
tag | String | Order tag  
  
### GET / Active orders

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/orders-active`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/orders-active
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_activity_orders()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | No | Product ID  
protocolType | String | No | Protocol type  
`defi`: on-chain earn  
ccy | String | No | Investment currency, e.g. `BTC`  
state | String | No | Order state  
`8`: Pending   
`13`: Cancelling   
`9`: Onchain   
`1`: Earning   
`2`: Redeeming  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "2413499",
                "ccy": "DOT",
                "productId": "101",
                "state": "1",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1014",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "earnings": "0.10615025"
                    }
                ],
                "purchasedTime": "1729839328000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2213257",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02886582"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000627"
                    }
                ],
                "purchasedTime": "1725345790000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2210943",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02891823"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000632"
                    }
                ],
                "purchasedTime": "1725280801000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
ordId | String | Order ID  
productId | String | Product ID  
state | String | Order state  
`8`: Pending   
`13`: Cancelling   
`9`: Onchain   
`1`: Earning   
`2`: Redeeming  
protocol | String | Protocol  
protocolType | String | Protocol type  
`defi`: on-chain earn  
term | String | Protocol term  
It will return the days of fixed term and will return `0` for flexible product  
apy | String | Estimated APY  
If the estimated APY is 7% , this field is 0.07  
Retain to 4 decimal places (truncated)  
investData | Array of objects | Investment data  
> ccy | String | Investment currency, e.g. `BTC`  
> amt | String | Invested amount  
earningData | Array of objects | Earning data  
> ccy | String | Earning currency, e.g. `BTC`  
> earningType | String | Earning type  
`0`: Estimated earning  
`1`: Cumulative earning  
> earnings | String | Earning amount  
fastRedemptionData | Array of objects | Fast redemption data  
> ccy | String | Currency, e.g. `BTC`  
> redeemingAmt | String | Redeeming amount  
purchasedTime | String | Order purchased time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estSettlementTime | String | Estimated redemption settlement time  
cancelRedemptionDeadline | String | Deadline for cancellation of redemption application  
tag | String | Order tag  
  
### GET / Order history

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/orders-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/orders-history
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_orders_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
productId | String | No | Product ID  
protocolType | String | No | Protocol type  
`defi`: on-chain earn  
ccy | String | No | Investment currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested ID. The value passed is the corresponding `ordId`  
before | String | No | Pagination of data to return records newer than the requested ID. The value passed is the corresponding `ordId`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
           {
                "ordId": "1579252",
                "ccy": "DOT",
                "productId": "101",
                "state": "3",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1704",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "realizedEarnings": "0"
                    }
                ],
                "purchasedTime": "1712908001000",
                "redeemedTime": "1712914294000",
                "tag": ""
           }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
ordId | String | Order ID  
productId | String | Product ID  
state | String | Order state  
`3`: Completed (including canceled and redeemed)  
protocol | String | Protocol  
protocolType | String | Protocol type  
`defi`: on-chain earn  
term | String | Protocol term  
It will return the days of fixed term and will return `0` for flexible product  
apy | String | Estimated APY  
If the estimated APY is 7% , this field is `0.07`  
Retain to 4 decimal places (truncated)  
investData | Array of objects | Investment data  
> ccy | String | Investment currency, e.g. `BTC`  
> amt | String | Invested amount  
earningData | Array of objects | Earning data  
> ccy | String | Earning currency, e.g. `BTC`  
> earningType | String | Earning type  
`0`: Estimated earning  
`1`: Cumulative earning  
> realizedEarnings | String | Cumulative earning of redeemed orders  
This field is just valid when the order is in redemption state  
purchasedTime | String | Order purchased time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
redeemedTime | String | Order redeemed time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
tag | String | Order tag  
  
## ETH staking

ETH Staking, also known as Ethereum Staking, is the process of participating in the Ethereum blockchain's Proof-of-Stake (PoS) consensus mechanism.  
Stake to receive BETH for liquidity at 1:1 ratio and earn daily BETH rewards  
[Learn more about ETH Staking](https://www.okx.com/earn/ethereum-staking)

### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
  
### POST / Purchase

Staking ETH for BETH  
Only the assets in the funding account can be used.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/purchase`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Investment amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Redeem

Only the assets in the funding account can be used. If your BETH is in your trading account, you can make funding transfer first.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/redeem
    body 
    {
        "amt": "10"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_redeem(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Redeeming amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Cancel redeem

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ordId | String | Yes | Order ID  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ordId | String | Order ID  
  
### GET / Balance

The balance is a snapshot summarized all BETH assets (including assets in redeeming) in account.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BETH`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual  
ts | String | Query data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/purchase-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/purchase-redeem-history
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase_redeem_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Type  
`purchase`  
`redeem`  
status | String | No | Status  
`pending`  
`success`  
`failed`  
`cancelled`  
after | String | No | Pagination of data to return records earlier than the `requestTime`. The value passed is the corresponding `timestamp`  
before | String | No | Pagination of data to return records newer than the `requestTime`. The value passed is the corresponding `timestamp`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`purchase`  
`redeem`  
amt | String | Purchase/Redeem amount  
redeemingAmt | String | Redeeming amount  
status | String | Status  
`pending`  
`success`  
`failed`  
`cancelled`  
ordId | String | Order ID  
requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085`  
completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/eth/apy-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/eth/apy-history?days=2
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = EthStaking.EthStakingAPI(flag=flag)
    
    result = StackingAPI.eth_apy_history(days="7")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
days | String | Yes | Get the days of APY(Annual percentage yield) history record in the past  
No more than 365 days  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.02690000",
                "ts": "1734195600000"
            },
            {
                "rate": "0.02840000",
                "ts": "1734109200000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
rate | String | APY(Annual percentage yield), e.g. `0.01` represents `1%`  
ts | String | Data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## SOL staking

By staking SOL tokens and delegating them to validators on the Solana network, you can receive equivalent OKSOL and earn extra OKSOL rewards.  
Stake SOL on Solana to receive OKSOL at a 1:1 ratio for liquidity  
[Learn more about OKSOL Staking](/earn/solana-staking#from=finance_crypto)

### GET / Product info

#### Rate Limit: 3 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/product-info`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> Response Example
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240"
        },
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fastRedemptionDailyLimit | String | Fast redemption daily limit  
The master account and sub-accounts share the same limit  
fastRedemptionAvail | String | Currently fast redemption max available amount  
  
### POST / Purchase

Staking SOL for OKSOL  
Only the assets in the funding account can be used.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/purchase`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/sol/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Investment amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### POST / Redeem

Only the assets in the funding account can be used. If your OKSOL is in your trading account, you can make funding transfer first.  

#### Rate Limit: 2 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/staking-defi/sol/redeem`

> Request Example
    
    
    POST /api/v5/finance/staking-defi/sol/redeem
    body 
    {
        "amt": "10"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_redeem(amt="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
amt | String | Yes | Redeeming amount  
  
> Response Example
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### Response Parameters

code = `0` means your request has been successfully handled.

### GET / Balance

The balance is summarized all OKSOL assets (including assets in redeeming) in account.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `OKSOL`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual  
  
### GET / Purchase&Redeem history

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
type | String | No | Type  
`purchase`  
`redeem`  
status | String | No | Status  
`pending`  
`success`  
`failed`  
after | String | No | Pagination of data to return records earlier than the `requestTime`. The value passed is the corresponding `timestamp`  
before | String | No | Pagination of data to return records newer than the `requestTime`. The value passed is the corresponding `timestamp`  
limit | String | No | Number of results per request. The default is `100`. The maximum is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
type | String | Type  
`purchase`  
`redeem`  
amt | String | Purchase/Redeem amount  
redeemingAmt | String | Redeeming amount  
status | String | Status  
`pending`  
`success`  
`failed`  
requestTime | String | Request time of make purchase/redeem, Unix timestamp format in milliseconds, e.g. `1597026383085`  
completedTime | String | Completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
estCompletedTime | String | Estimated completed time of redeem settlement, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / APY history (Public)

Public endpoints don't need authorization.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/apy-history`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
days | String | Yes | Get the days of APY(Annual percentage yield) history record in the past  
No more than 365 days  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
rate | String | APY(Annual percentage yield), e.g. `0.01` represents `1%`  
ts | String | Data time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## Simple earn flexible

Simple earn flexible (saving) is earned by lending to leveraged trading users in the lending market. [learn more](/earn/simple-earn)

### GET / Saving balance

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/savings/balance`

> Request Example
    
    
    GET /api/v5/finance/savings/balance?ccy=USDT
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_saving_balance(ccy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg":"",
        "data": [
            {
                "earnings": "0.0010737388791526",
                "redemptAmt": "",
                "rate": "0.0100000000000000",
                "ccy": "USDT",
                "amt": "11.0010737453457821",
                "loanAmt": "11.0010630707982819",
                "pendingAmt": "0.0000106745475002"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
amt | String | Currency amount  
earnings | String | Currency earnings  
rate | String | Minimum annual lending rate configured by users  
loanAmt | String | Lending amount  
pendingAmt | String | Pending amount  
redemptAmt | String | ~~Redempting amount~~ (Deprecated)  
  
### POST / Savings purchase/redemption

Only the assets in the funding account can be used for saving.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/savings/purchase-redempt`

> Request Example
    
    
    POST /api/v5/finance/savings/purchase-redempt
    body
    {
        "ccy":"BTC",
        "amt":"1",
        "side":"purchase",
        "rate":"0.01"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.savings_purchase_redemption(ccy='USDT',amt="0.1",side="purchase",rate="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
amt | String | Yes | Purchase/redemption amount  
side | String | Yes | Action type.   
`purchase`: purchase saving shares   
`redempt`: redeem saving shares  
rate | String | Conditional | Annual purchase rate, e.g. `0.1` represents `10%`  
Only applicable to purchase saving shares  
The interest rate of the new subscription will cover the interest rate of the last subscription  
The rate value range is between 1% and 365%  
  
> Response Example
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "amt":"1",
                "side":"purchase",
                "rate": "0.01"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency  
amt | String | Purchase/Redemption amount  
side | String | Action type  
rate | String | Annual purchase rate, e.g. `0.1` represents `10%`  
  
### POST / Set lending rate

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/savings/set-lending-rate`

> Request Example
    
    
    POST /api/v5/finance/savings/set-lending-rate
    body
    {
        "ccy":"BTC",
        "rate":"0.02"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.set_lending_rate(ccy='USDT',rate="1")
    print(result)
    

#### Request Parameters

Parameter | Type | Required | Description  
---|---|---|---  
ccy | String | Yes | Currency, e.g. `BTC`  
rate | String | Yes | Annual lending rate  
The rate value range is between 1% and 365%  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "rate": "0.02"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
rate | String | Annual lending rate  
  
### GET / Lending history

Return data in the past month.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/savings/lending-history`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_lending_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "amt": "0.01",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            },
            {
                "ccy": "ETH",
                "amt": "0.2",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            }
        ]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
amt | String | Lending amount  
earnings | String | Currency earnings  
rate | String | Lending annual interest rate  
ts | String | Lending time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Public borrow info (public)

Authentication is not required for this public endpoint.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-summary`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-rate-summary
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_info()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "avgAmt": "10000",
            "avgAmtUsd": "10000000000",
            "avgRate": "0.03",
            "preRate": "0.02",
            "estRate": "0.01"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
avgAmt | String | ~~24H average borrowing amount~~(deprecated)  
avgAmtUsd | String | ~~24H average borrowing amount in`USD` value~~(deprecated)  
avgRate | String | 24-hours average annual borrowing rate  
preRate | String | Last annual borrowing interest rate  
estRate | String | Next estimate annual borrowing interest rate  
  
### GET / Public borrow history (public)

Authentication is not required for this public endpoint.  
Only returned records after December 14, 2021.

#### Rate Limit: 6 requests per second

#### Rate limit rule: IP

#### HTTP Request

`GET /api/v5/finance/savings/lending-rate-history`

> Request Example
    
    
    GET /api/v5/finance/savings/lending-rate-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
before | String | No | Pagination of data to return records newer than the requested `ts`, Unix timestamp format in milliseconds, e.g. `1597026383085`  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
If `ccy` is not specified, all data under the same `ts` will be returned, not limited by `limit`  
  
> Response Example
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "amt": "0.01",
            "rate": "0.001",
            "ts": "1597026383085"
        }]
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `BTC`  
amt | String | ~~Lending amount~~(deprecated)  
rate | String | Annual borrowing interest rate  
ts | String | Time, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
## Flexible loan

OKX Flexible Loan is a high-end loan product that allows users to increase cash flow without selling off their crypto. [More details](/loan)

### GET / Borrowable currencies

Get borrowable currencies

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/borrow-currencies`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/borrow-currencies
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.borrow_currencies()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT"
            },
            {
                "borrowCcy": "USDC"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
borrowCcy | String | Borrowable currency, e.g. `BTC`  
  
### GET / Collateral assets

Get collateral assets in funding account.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/collateral-assets`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Collateral currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
assets | Array of objects | Collateral assets data  
> ccy | String | Currency, e.g. `BTC`  
> amt | String | Available amount  
> notionalUsd | String | Notional value in `USD`  
  
### POST / Maximum loan amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`POST /api/v5/finance/flexible-loan/max-loan`

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/max-loan
    body
    {
        "borrowCcy": "USDT"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_loan(borrowCcy="USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
borrowCcy | String | Yes | Currency to borrow, e.g. `USDT`  
supCollateral | Array of objects | No | Supplementary collateral assets  
> ccy | String | Yes | Currency, e.g. `BTC`  
> amt | String | Yes | Amount  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT",
                "maxLoan": "0.01113",
                "notionalUsd": "0.01113356",
                "remainingQuota": "3395000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
borrowCcy | String | Currency to borrow, e.g. `USDT`  
maxLoan | String | Maximum available loan  
notionalUsd | String | Maximum available loan notional value, unit in `USD`  
remainingQuota | String | Remaining quota, unit in `borrowCcy`  
  
### GET / Maximum collateral redeem amount

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount("USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Collateral currency, e.g. `USDT`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Collateral currency, e.g. `USDT`  
maxRedeemAmt | String | Maximum collateral redeem amount  
  
### POST / Adjust collateral

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | Yes | Operation type  
`add`: Add collateral  
`reduce`: Reduce collateral  
collateralCcy | String | Yes | Collateral currency, e.g. `BTC`  
collateralAmt | String | Yes | Collateral amount  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### Response Parameters

code = `0` means your request has been accepted (It doesn't mean the request has been successfully handled.)

### GET / Loan info

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-info`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
loanNotionalUsd | String | Loan value in `USD`  
loanData | Array of objects | Loan data  
> ccy | String | Loan currency, e.g. `USDT`  
> amt | String | Loan amount  
collateralNotionalUsd | String | Collateral value in `USD`  
collateralData | Array of objects | Collateral data  
> ccy | String | Collateral currency, e.g. `BTC`  
> amt | String | Collateral amount  
riskWarningData | Object | Risk warning data  
> instId | String | Liquidation instrument ID, e.g. `BTC-USDT`  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
> liqPx | String | Liquidation price  
The unit of the liquidation price is the quote currency of the instrument, e.g. `USDT` in `BTC-USDT`.  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
curLTV | String | Current LTV, e.g. `0.1` represents `10%`  
Note: LTV = Loan to Value  
marginCallLTV | String | Margin call LTV, e.g. `0.1` represents `10%`  
If your loan hits the margin call LTV, our system will automatically warn you that your loan is getting close to forced liquidation.  
liqLTV | String | Liquidation LTV, e.g. `0.1` represents `10%`  
If your loan reaches liquidation LTV, it'll trigger forced liquidation. When this happens, you'll lose access to your collateral and any repayments made.  
  
### GET / Loan history

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-history`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | No | Action type  
`borrowed`  
`repaid`  
`collateral_locked`  
`collateral_released`  
`forced_repayment_buy`  
`forced_repayment_sell`  
`forced_liquidation`  
`partial_liquidation`  
`sell_collateral`  
`buy_transition_coin`  
`sell_transition_coin`  
`buy_borrowed_coin`  
after | String | No | Pagination of data to return records earlier than the requested `refId`(not include)  
before | String | No | Pagination of data to return records newer than the requested `refId`(not include)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
refId | String | Reference ID  
type | String | Action type  
ccy | String | Currency, e.g. `BTC`  
amt | String | Amount  
ts | String | Timestamp for the action, Unix timestamp format in milliseconds, e.g. `1597026383085`  
  
### GET / Accrued interest

Retrieves the interest accrual history for flexible loans over the past 30 days.

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/interest-accrued`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/interest-accrued
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.interest_accrued()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Loan currency, e.g. `BTC`  
after | String | No | Pagination of data to return records earlier than the requested `refId`(not include)  
before | String | No | Pagination of data to return records newer than the requested `refId`(not include)  
limit | String | No | Number of results per request. The maximum is `100`. The default is `100`.  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDC",
                "interest": "0.00004054",
                "interestRate": "0.41",
                "loan": "0.86599309",
                "refId": "17319133035195744",
                "ts": "1731913200000"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
refId | String | Reference ID  
ccy | String | Loan currency, e.g. `BTC`  
loan | String | Loan when calculated interest  
interest | String | Interest  
interestRate | String | APY, e.g. `0.01` represents `1%`  
ts | String | Timestamp to calculated interest, Unix timestamp format in milliseconds, e.g. `1597026383085`

---

# 金融产品

## 链上赚币   
  
仅资金账户中的资产支持申购。[了解更多](/cn/earn/onchain-earn)

### GET / 查看项目 

#### 限速：3次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/offers`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/offers
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0" # 实盘:0 , 模拟盘:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_offers(ccy="USDT")
    print(result)
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 否 | 项目ID  
protocolType | String | 否 | 项目类型  
`defi`：链上赚币  
ccy | String | 否 | 投资币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "DOT",
                "productId": "101",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1767",
                "earlyRedeem": false,
                "state": "purchasable",
                "investData": [
                    {
                        "bal": "0",
                        "ccy": "DOT",
                        "maxAmt": "0",
                        "minAmt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0"
                    }
                ],
                "fastRedemptionDailyLimit": "",
                "redeemPeriod": [
                    "28D",
                    "28D"
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
productId | String | 项目ID  
protocol | String | 项目名称  
protocolType | String | 项目类型  
`defi`：链上赚币  
term | String | 项目期限  
活期为0，其他则显示定期天数  
apy | String | 预估年化  
如果年化为`7%` ，则该字段为`0.07`  
earlyRedeem | Boolean | 项目是否支持提前赎回  
investData | Array of objects | 目前用户可用来投资的目标币种信息  
> ccy | String | 投资币种，如`BTC`  
> bal | String | 可投数量  
> minAmt | String | 最小申购量  
> maxAmt | String | 最大可申购量  
earningData | Array of objects | 收益信息  
> ccy | String | 收益币种，如`BTC`  
> earningType | String | 收益类型  
`0`：预估收益  
`1`：累计发放收益  
state | String | 项目状态  
`purchasable`：可申购  
`sold_out`：售罄  
`stop`：暂停申购  
redeemPeriod | Array of strings | 赎回期，形式为 [最小赎回时间,最大赎回时间]  
`H`：小时，`D`：天  
例 ["1H","24H"] 表示赎回期时1小时到24小时。  
["14D","14D"] 表示赎回期为14天。  
fastRedemptionDailyLimit | String | 快速赎回每日最高限额  
如果不支持快速赎回，则返回""  
  

### POST / 申购项目 

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/purchase`

> 请求示例
    
    
    # 投资100ZIL30天的锁仓挖矿项目
    POST /api/v5/finance/staking-defi/purchase
    body 
    {
        "productId":"1234",
        "investData":[
          {
            "ccy":"ZIL",
            "amt":"100"
          }
        ],
        "term":"30"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0" # 实盘:0 , 模拟盘:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.purchase(
                productId = "4005", 
                investData = [{
                    "ccy":"USDT",
                    "amt":"100"
                }]
            )
    print(result)
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 是 | 项目ID  
investData | Array of objects | 是 | 投资信息  
> ccy | String | 是 | 投资币种，如 `BTC`  
> amt | String | 是 | 投资数量  
term | String | 可选 | 投资期限  
定期项目必须指定投资期限  
tag | String | 否 | 订单标签  
字母（区分大小写）与数字的组合，可以是纯字母、纯数字，且长度在1-16位之间  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
tag | String | 订单标签  
  
### POST / 赎回项目 

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/redeem`

> 请求示例
    
    
    # 提前赎回项目投资
    POST /api/v5/finance/staking-defi/redeem
    body 
    {
        "ordId":"754147",
        "protocolType":"defi",
        "allowEarlyRedeem":true
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    
    result = StakingAPI.redeem(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
protocolType | String | 是 | 项目类型  
`defi`：链上赚币  
allowEarlyRedeem | Boolean | 否 | 是否提前赎回  
默认为`false`  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
tag | String | 订单标签  
  
### POST / 撤销项目申购/赎回 

撤销申购后的资金返回资金账户。 

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/cancel`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/cancel
    body 
    {
        "ordId":"754147",
        "protocolType":"defi"
    }
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘:0 , 模拟盘:1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.cancel(
               ordId = "1234",
               protocolType = "defi"
            )
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
protocolType | String | 是 | 项目类型  
`defi`：链上赚币  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
        {
          "ordId": "754147",
          "tag": ""
        }
      ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
tag | String | 订单标签  
  
### GET / 查看活跃订单 

#### 限速：3次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/orders-active`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/orders-active
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_activity_orders()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 否 | 项目ID  
protocolType | String | 否 | 项目类型  
`defi`：链上赚币  
ccy | String | 否 | 投资币种，如 `BTC`  
state | String | 否 | 订单状态  
`8`: 待上车（预约中）  
`13`: 订单取消中  
`9`: 上链中  
`1`: 收益中  
`2`: 赎回中  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "2413499",
                "ccy": "DOT",
                "productId": "101",
                "state": "1",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1014",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "earnings": "0.10615025"
                    }
                ],
                "purchasedTime": "1729839328000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2213257",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02886582"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000627"
                    }
                ],
                "purchasedTime": "1725345790000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            },
            {
                "ordId": "2210943",
                "ccy": "USDT",
                "productId": "4005",
                "state": "1",
                "protocol": "On-Chain Defi",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.0323",
                "investData": [
                    {
                        "ccy": "USDT",
                        "amt": "1"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "USDT",
                        "earningType": "0",
                        "earnings": "0.02891823"
                    },
                    {
                        "ccy": "COMP",
                        "earningType": "1",
                        "earnings": "0.0000632"
                    }
                ],
                "purchasedTime": "1725280801000",
                "tag": "",
                "estSettlementTime": "",
                "cancelRedemptionDeadline": "",
                "fastRedemptionData": []
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
ordId | String | 订单ID  
productId | String | 项目ID  
state | String | 订单状态  
`8`：待上车（预约中）  
`13`：订单取消中  
`9`：上链中  
`1`：收益中  
`2`：赎回中  
protocol | String | 项目名称  
protocolType | String | 项目类型  
`defi`：链上赚币  
term | String | 项目期限  
活期为0，其他则显示定期天数  
apy | String | 预估年化  
如果年化为7% ，则该字段为0.07  
保留到小数点后4位（截位）  
investData | Array of objects | 用户投资信息  
> ccy | String | 投资币种，如 `BTC`  
> amt | String | 已投资数量  
earningData | Array of objects | 收益信息  
> ccy | String | 收益币种，如 `BTC`  
> earningType | String | 收益类型  
`0`：预估收益  
`1`：实际到账收益  
> earnings | String | 收益数量  
fastRedemptionData | Array of objects | 快速赎回信息  
> ccy | String | 快速赎回币种，如 `BTC`  
> redeemingAmt | String | 赎回中的数量  
purchasedTime | String | 用户订单创建时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estSettlementTime | String | 预估赎回到账时间  
cancelRedemptionDeadline | String | 撤销赎回申请截止时间  
tag | String | 订单标签  
  
### GET / 查看历史订单 

#### 限速：3次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/orders-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/orders-history
    
    
    
    
    import okx.Finance.StakingDefi as StakingDefi
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StakingAPI = StakingDefi.StakingDefiAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StakingAPI.get_orders_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
productId | String | 否 | 项目ID  
protocolType | String | 否 | 项目类型  
`defi`：链上赚币  
ccy | String | 否 | 投资币种，如 `BTC`  
after | String | 否 | 请求此ID之前（更旧的数据）的分页内容，传的值为对应接口的`ordId`  
before | String | 否 | 请求此ID之后（更新的数据）的分页内容，传的值为对应接口的`ordId`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [
           {
                "ordId": "1579252",
                "ccy": "DOT",
                "productId": "101",
                "state": "3",
                "protocol": "Polkadot",
                "protocolType": "defi",
                "term": "0",
                "apy": "0.1704",
                "investData": [
                    {
                        "ccy": "DOT",
                        "amt": "2"
                    }
                ],
                "earningData": [
                    {
                        "ccy": "DOT",
                        "earningType": "0",
                        "realizedEarnings": "0"
                    }
                ],
                "purchasedTime": "1712908001000",
                "redeemedTime": "1712914294000",
                "tag": ""
           }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
ordId | String | 订单ID  
productId | String | 项目ID  
state | String | 订单状态  
3: 订单已完成（包含撤销和已赎回两种状态）  
protocol | String | 项目名称  
protocolType | String | 项目类型  
`defi`：链上赚币  
term | String | 项目期限  
活期为0，其他则显示定期天数  
apy | String | 预估年化  
如果年化为7% ，则该字段为0.07  
保留到小数点后4位（截位）  
investData | Array of objects | 用户投资信息  
> ccy | String | 投资币种，如`BTC`  
> amt | String | 已投资数量  
earningData | Array of objects | 收益信息  
> ccy | String | 收益币种，如`BTC`  
> earningType | String | 收益类型  
`0`：预估收益  
`1`：实际到账收益  
> realizedEarnings | String | 已赎回订单累计收益  
该字段仅在订单处于赎回状态时有效  
purchasedTime | String | 用户订单创建时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
redeemedTime | String | 用户订单赎回时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
tag | String | 订单标签  
  
## ETH质押 

ETH 质押，也称为以太坊质押，是参与以太坊区块链权益证明 (Proof of Stake, PoS) 共识机制的过程。  
质押 ETH 即获 1:1 BETH 并赚取每日奖励，享受更高流动性  
[了解更多](https://www.okx.com/zh-hans/earn/ethereum-staking)

### GET / 获取产品信息 

#### 限速：3 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/product-info
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_product_info()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "fastRedemptionDailyLimit": "100"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
  
### POST / 申购 

质押ETH获取BETH  
仅资金账户中的资产支持ETH质押。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/purchase`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 投资数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### POST / 赎回 

只能赎回资金账户中的 BETH 资产，交易账户中的 BETH 资产需要您先做资金划转到资金账户后赎回。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/redeem
    body 
    {
        "amt":"10"
    }
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_redeem(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 赎回数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### POST / 撤销赎回 

#### 限速：2 次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/eth/cancel-redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/eth/cancel-redeem
    body
    {
        "ordId": "1234567890"
    }
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ordId | String | 是 | 订单ID  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ordId": "1234567890"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ordId | String | 订单ID  
  
### GET / 获取余额 

该余额是一个汇总账户BETH资产（含赎回中）的快照数据。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/balance
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
          {
            "amt": "0.63926191",
            "ccy": "BETH",
            "latestInterestAccrual": "0.00006549",
            "totalInterestAccrual": "0.01490596",
            "ts": "1699257600000"
          }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BETH`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益  
ts | String | 快照时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取申购赎回记录 

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/purchase-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/purchase-redeem-history
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.eth_purchase_redeem_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 类型  
`purchase`：申购  
`redeem`：赎回  
status | String | 否 | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
`cancelled`：已取消  
after | String | 否 | 请求此`requestTime`之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此`requestTime`之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 类型  
`purchase`：申购  
`redeem`：赎回  
amt | String | 申购/赎回 的数量  
redeemingAmt | String | 赎回中的数量  
status | String | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
`cancelled`：已取消  
ordId | String | 订单ID  
requestTime | String | 发起 申购/赎回 请求的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
completedTime | String | 赎回请求处理完成的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estCompletedTime | String | 预估完成赎回的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取历史收益率(公共) 

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/staking-defi/eth/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/eth/apy-history?days=2
    
    
    
    
    import okx.Finance.EthStaking as EthStaking
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = EthStaking.EthStakingAPI(flag=flag)
    
    result = StackingAPI.eth_apy_history(days="7")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
days | String | 是 | 查询最近多少天内的数据，不超过365天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.02690000",
                "ts": "1734195600000"
            },
            {
                "rate": "0.02840000",
                "ts": "1734109200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
rate | String | 年化收益率，如 `0.01`代表`1%`  
ts | String | 时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
## SOL质押 

通过质押 SOL 代币并将其委托给 Solana 网络上的验证者，您可以收到等值的 OKSOL 并获得每日 OKSOL 奖励。  
在 Solana 上质押 SOL，即获 1:1 OKSOL，享受更高流动性  
[了解更多](/zh-hans/earn/solana-staking#from=finance_crypto)

### GET / 获取产品信息 

#### 限速：3 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/product-info`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/product-info
    
    
    
    
    

> 返回结果
    
    
    {
        "code": "0",
        "data": {
            "fastRedemptionAvail": "240",
            "fastRedemptionDailyLimit": "240"
        },
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fastRedemptionDailyLimit | String | 快速赎回每日最高份额  
母账户和子账户共享同一个限额  
fastRedemptionAvail | String | 当前剩余最大可赎回数量  
  
### POST / 申购 

质押 SOL 获取 OKSOL  
仅资金账户中的资产支持 SOL 质押。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/sol/purchase`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/sol/purchase
    body 
    {
        "amt":"100"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 投资数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### POST / 赎回 

只能赎回资金账户中的 OKSOL 资产，交易账户中的 OKSOL 资产需要您先做资金划转到资金账户后赎回。

#### 限速：2次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP 请求

`POST /api/v5/finance/staking-defi/sol/redeem`

> 请求示例
    
    
    POST /api/v5/finance/staking-defi/sol/redeem
    body 
    {
        "amt":"10"
    }
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_redeem(amt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
amt | String | 是 | 赎回数量  
  
> 返回结果
    
    
    {
      "code": "0",
      "msg": "",
      "data": [
      ]
    }
    

#### 返回参数

code = `0`代表请求已被成功处理

### GET / 获取余额 

该余额是一个汇总账户OKSOL资产（含赎回中）的实时数据。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `OKSOL`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益  
  
### GET / 获取申购赎回记录 

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/purchase-redeem-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/purchase-redeem-history
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_purchase_redeem_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 类型  
`purchase`：申购  
`redeem`：赎回  
status | String | 否 | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
after | String | 否 | 请求此`requestTime`之前（更旧的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 请求此`requestTime`之后（更新的数据）的分页内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 返回结果的数量，默认100条，最大值为100条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.62666630",
                "completedTime": "1683413171000",
                "estCompletedTime": "",
                "redeemingAmt": "",
                "requestTime": "1683413171000",
                "status": "success",
                "type": "purchase"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
type | String | 类型  
`purchase`：申购  
`redeem`：赎回  
amt | String | 申购/赎回 的数量  
redeemingAmt | String | 赎回中的数量  
status | String | 状态  
`pending`：处理中  
`success`：成功处理  
`failed`：处理失败  
requestTime | String | 发起 申购/赎回 请求的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
completedTime | String | 赎回请求处理完成的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
estCompletedTime | String | 预估完成赎回的时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 获取历史收益率(公共) 

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/apy-history`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/apy-history?days=2
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(flag=flag)
    
    result = StackingAPI.sol_apy_history(days="7")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
days | String | 是 | 查询最近多少天内的数据，不超过365天  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "rate": "0.11280000",
                "ts": "1734192000000"
            },
            {
                "rate": "0.11270000",
                "ts": "1734105600000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
rate | String | 年化收益率，如 `0.01`代表`1%`  
ts | String | 时间，值为时间戳，Unix时间戳为毫秒数格式，如 `1597026383085`  
  
## 活期简单赚币 

活期简单赚币通过在借贷市场出借给杠杆交易用户获取收益。[了解更多](/cn/earn/simple-earn)

### GET / 获取活期简单赚币余额 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/savings/balance`

> 请求示例
    
    
    GET /api/v5/finance/savings/balance?ccy=BTC
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_saving_balance(ccy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg":"",
        "data": [
            {
                "earnings": "0.0010737388791526",
                "redemptAmt": "",
                "rate": "0.0100000000000000",
                "ccy": "USDT",
                "amt": "11.0010737453457821",
                "loanAmt": "11.0010630707982819",
                "pendingAmt": "0.0000106745475002"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | 币种数量  
earnings | String | 币种持仓收益  
rate | String | 用户配置的最低年化出借利率  
loanAmt | String | 已出借数量  
pendingAmt | String | 未出借数量  
redemptAmt | String | ~~赎回中的数量~~ （已废弃）  
  
### POST / 活期简单赚币申购/赎回 

仅资金账户中的资产支持活期简单赚币申购。

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/savings/purchase-redempt`

> 请求示例
    
    
    POST /api/v5/finance/savings/purchase-redempt
    body
    {
        "ccy":"BTC",
        "amt":"1",
        "side":"purchase",
        "rate":"0.01"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.savings_purchase_redemption(ccy='USDT',amt="0.1",side="purchase",rate="1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种名称，如 `BTC`  
amt | String | 是 | 申购/赎回 数量  
side | String | 是 | 操作类型  
`purchase`：申购 `redempt`：赎回  
rate | String | 可选 | 申购年利率，如 `0.1`代表`10%`  
仅适用于申购，新申购的利率会覆盖上次申购的利率  
参数取值范围在1%到365%之间  
  
> 返回结果
    
    
    {
        "code":"0",
        "msg":"",
        "data":[
            {
                "ccy":"BTC",
                "amt":"1",
                "side":"purchase",
                "rate":"0.01"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称  
amt | String | 申购/赎回 数量  
side | String | 操作类型  
rate | String | 申购年利率，如 `0.1`代表`10%`  
  
### POST / 设置活期简单赚币借贷利率 

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/savings/set-lending-rate`

> 请求示例
    
    
    POST /api/v5/finance/savings/set-lending-rate
    body
    {
        "ccy":"BTC",
        "rate":"0.02"
    }
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.set_lending_rate(ccy='USDT',rate="1")
    print(result)
    

#### 请求参数

参数名 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 币种名称，如 `BTC`  
rate | String | 是 | 贷出年利率  
参数取值范围在1%到365%之间  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "rate": "0.02"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `BTC`  
rate | String | 贷出年利率  
  
### GET / 获取活期简单赚币出借明细 

返回最近一个月的数据

#### 限速：6次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/savings/lending-history`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(apikey, secretkey, passphrase, False, flag)
    
    result = SavingsAPI.get_lending_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为 100，不填默认返回 100 条  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
                "ccy": "BTC",
                "amt": "0.01",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            },
            {
                "ccy": "ETH",
                "amt": "0.2",
                "earnings": "0.001",
                "rate": "0.01",
                "ts": "1597026383085"
            }
        ]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | 出借数量  
earnings | String | 已赚取利息  
rate | String | 出借年利率  
ts | String | 出借时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
### GET / 获取市场借贷信息（公共）

公共接口无须鉴权

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/finance/savings/lending-rate-summary`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-rate-summary
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_info()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "avgAmt": "10000",
            "avgAmtUsd": "10000000000",
            "avgRate": "0.03",
            "preRate": "0.02",
            "estRate": "0.01"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
avgAmt | String | ~~过去24小时平均借贷量~~(已弃用)  
avgAmtUsd | String | ~~过去24小时平均借贷美元价值~~(已弃用)  
avgRate | String | 过去24小时平均借入年利率  
preRate | String | 上一次借入年利率  
estRate | String | 下一次预估借入年利率  
  
### GET / 获取市场借贷历史（公共） 

公共接口无须鉴权  
返回2021年12月14日后的记录  

#### 限速：6次/s

#### 限速规则：IP

#### HTTP请求

`GET /api/v5/finance/savings/lending-rate-history`

> 请求示例
    
    
    GET /api/v5/finance/savings/lending-rate-history
    
    
    
    
    import okx.Finance.Savings as Savings
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    SavingsAPI = Savings.SavingsAPI(flag=flag)
    
    result = SavingsAPI.get_public_borrow_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
after | String | 否 | 查询在此之前的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
before | String | 否 | 查询在此之后的内容，值为时间戳，Unix 时间戳为毫秒数格式，如 `1597026383085`  
limit | String | 否 | 分页返回的结果集数量，最大为100，不填默认返回100条  
如果不指定`ccy`,会返回同一个`ts`下的全部数据，不受`limit`限制  
  
> 返回结果
    
    
    {
        "code": "0",
        "msg": "",
        "data": [{
            "ccy": "BTC",
            "amt": "0.01",
            "rate": "0.001",
            "ts": "1597026383085"
        }]
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种，如 `BTC`  
amt | String | ~~市场总出借数量~~ （已弃用）  
rate | String | 出借年利率  
ts | String | 时间，Unix时间戳的毫秒数格式，如 `1597026383085`  
  
## 活期借币 

欧易活期借币是一款高端借贷产品，用户无需变卖数字货币即可增加现金流。[了解更多](/loan)

### GET / 可借币种列表 

获取可借币种列表

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/borrow-currencies`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/borrow-currencies
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.borrow_currencies()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT"
            },
            {
                "borrowCcy": "USDC"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
borrowCcy | String | 可借币种，如 `BTC`  
  
### GET / 可抵押资产 

获取可抵押资产信息（仅支持资金账户中的资产）

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/collateral-assets`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
assets | Array of objects | 可抵押资产信息  
> ccy | String | 币种，如 `BTC`  
> amt | String | 可用数量  
> notionalUsd | String | 可抵押资产的美金价值  
  
### POST / 最大可借 

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`POST /api/v5/finance/flexible-loan/max-loan`

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/max-loan
    body
    {
        "borrowCcy": "USDT"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_loan(borrowCcy="USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
borrowCcy | String | 是 | 借币币种，如 `USDT`  
supCollateral | Array of objects | 否 | 补充抵押资产信息  
> ccy | String | 是 | 币种，如 `BTC`  
> amt | String | 是 | 数量  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "borrowCcy": "USDT",
                "maxLoan": "0.01113",
                "notionalUsd": "0.01113356",
                "remainingQuota": "3395000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
borrowCcy | String | 借币币种，如 `USDT`  
maxLoan | String | 最大可借数量  
notionalUsd | String | 最大可借美元价值  
remainingQuota | String | 剩余可借额度，单位为`borrowCcy`  
  
### GET / 抵押物最大可赎回数量 

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount("USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 抵押物币种，如 `USDT`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 抵押物币种，如 `USDT`  
maxRedeemAmt | String | 抵押物最大可赎回数量  
  
### POST / 调整抵押物 

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 是 | 操作类型  
`add`：补充抵押物  
`reduce`：减少抵押物  
collateralCcy | String | 是 | 抵押物币种，如 `BTC`  
collateralAmt | String | 是 | 抵押物数量  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### 返回参数

code = `0` 代表请求已被接受(不代表处理成功)

### GET / 借贷信息 

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-info`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
loanNotionalUsd | String | 借币资产美金价值  
loanData | Array of objects | 借币数据  
> ccy | String | 借贷币种  
> amt | String | 借贷数量  
collateralNotionalUsd | String | 抵押物美金价值  
collateralData | Array of objects | 抵押资产数据  
> ccy | String | 抵押币种  
> amt | String | 抵押数量  
riskWarningData | Object | 风险预警信息  
> instId | String | 清算交易产品，如 `BTC-USDT`  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
> liqPx | String | 清算价格  
清算价格的单位为交易产品的计价币，如 `BTC-USDT`中的`USDT`。  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
curLTV | String | 当前质押率，如 `0.1`代表`10%`  
注：LTV(Loan-to-Value，贷款价值比)  
marginCallLTV | String | 预警质押率，如 `0.1`代表`10%`  
您的质押率达到预警质押率时，系统将会提示您当前质押率过高，即将触发强平。  
liqLTV | String | 强平质押率，如 `0.1`代表`10%`  
若您的借贷达到强平质押率并被强平，您将损失质押物及已完成的还款。  
  
### GET / 借贷历史 

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-history`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-history
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_history()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 否 | 操作类型  
`borrowed`：借入  
`repaid`：还币  
`collateral_locked`：锁定质押物  
`collateral_released`：释放质押物  
`forced_repayment_buy`：自动换币买入  
`forced_repayment_sell`：自动换币卖出  
`forced_liquidation`：强制平仓  
`partial_liquidation`：强制减仓  
`sell_collateral`：卖出质押资产  
`buy_transition_coin`：购买中介币种  
`sell_transition_coin`：卖出中介币种  
`buy_borrowed_coin`：购买借币币种  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
limit | String | 否 | 返回结果的数量，最大为`100`，默认`100`条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "-0.001",
                "ccy": "DOT",
                "refId": "17316594851045086",
                "ts": "1731659485000",
                "type": "collateral_locked"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
refId | String | 对应记录ID  
type | String | 操作类型  
ccy | String | 币种，如 `BTC`  
amt | String | 数量  
ts | String | 操作发生时间，Unix 时间戳为毫秒数格式，如 `1597026383085`  
  
### GET / 计息记录 

获取最近30天的计息记录。

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/interest-accrued`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/interest-accrued
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.interest_accrued()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 借贷币种，如 `BTC`  
after | String | 否 | 请求此 ID 之前（更旧的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
before | String | 否 | 请求此 ID 之后（更新的数据）的分页内容，传的值为对应接口的`refId`（不包含）  
limit | String | 否 | 返回结果的数量，最大为`100`，默认`100`条  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDC",
                "interest": "0.00004054",
                "interestRate": "0.41",
                "loan": "0.86599309",
                "refId": "17319133035195744",
                "ts": "1731913200000"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
refId | String | 对应记录ID  
ccy | String | 币种，如 `BTC`  
loan | String | 计息时负债  
interest | String | 利息  
interestRate | String | 年化利率，如 `0.01`代表`1%`  
ts | String | 计息时间，Unix 时间戳为毫秒数格式，如 `1597026383085`