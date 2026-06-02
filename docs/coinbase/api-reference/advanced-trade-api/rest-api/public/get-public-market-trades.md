---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-market-trades
api_type: Market Data
updated_at: 2026-06-02 19:15:08.421405
---

# Get Public Market Trades

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/ticker`

PublicGet Public Market TradesGet snapshot information by product ID about the last trades (ticks) and best bid/ask.GET/api/v3/brokerage/market/products/{product_id}/tickerGet Public Market Trades
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/ticker \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "trades": [
        {
          "trade_id": "34b080bf-fcfd-445a-832b-46b5ddc65601",
          "product_id": "BTC-USD",
          "price": "140.91",
          "size": "4",
          "time": "2021-05-31T09:59:59.000Z",
          "side": "",
          "exchange": "<string>"
        }
      ],
      "best_bid": "291.13",
      "best_ask": "292.40"
    }

AuthorizationsAuthorizationstringheaderrequiredA JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.Path Parametersproduct_idstringrequiredThe trading pair (e.g. 'BTC-USD').Query Parameterslimitinteger<int32>requiredThe number of trades to be returned.startstringThe UNIX timestamp indicating the start of the time interval.endstringThe UNIX timestamp indicating the end of the time interval.ResponseA successful response.tradesobject[]Show child attributesbest_bidstringThe best bid for the `product_id`, in quote currency.Example:`"291.13"`best_askstringThe best ask for the `product_id`, in quote currency.Example:`"292.40"`