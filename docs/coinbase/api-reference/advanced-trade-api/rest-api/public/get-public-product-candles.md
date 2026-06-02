---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-product-candles
api_type: Market Data
updated_at: 2026-06-02 19:15:08.540654
---

# Get Public Product Candles

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles`

PublicGet Public Product CandlesGet rates for a single product by product ID, grouped in buckets.GET/api/v3/brokerage/market/products/{product_id}/candlesGet Public Product Candles
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/market/products/{product_id}/candles \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "candles": [
        {
          "start": "1639508050",
          "low": "140.21",
          "high": "140.21",
          "open": "140.21",
          "close": "140.21",
          "volume": "56437345"
        }
      ]
    }

AuthorizationsAuthorizationstringheaderrequiredA JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.Path Parametersproduct_idstringrequiredThe trading pair (e.g. 'BTC-USD').Query ParametersstartstringrequiredThe UNIX timestamp indicating the start of the time interval.endstringrequiredThe UNIX timestamp indicating the end of the time interval.granularityenum<string>default:UNKNOWN_GRANULARITYrequiredThe timeframe each candle represents.Available options: `UNKNOWN_GRANULARITY`, `ONE_MINUTE`, `FIVE_MINUTE`, `FIFTEEN_MINUTE`, `THIRTY_MINUTE`, `ONE_HOUR`, `TWO_HOUR`, `FOUR_HOUR`, `SIX_HOUR`, `ONE_DAY` limitinteger<int32>The number of candle buckets to be returned. By default, returns 350 (max 350).ResponseA successful response.candlesobject[]Show child attributes