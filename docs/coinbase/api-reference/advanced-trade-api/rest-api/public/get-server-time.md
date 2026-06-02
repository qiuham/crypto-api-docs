---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-server-time
api_type: REST
updated_at: 2026-06-02 19:15:08.586765
---

# Get Server Time

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/time`

PublicGet Server TimeGet the current time from the Coinbase Advanced API.GET/api/v3/brokerage/timeGet Server Time
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/time \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "iso": "<string>",
      "epochSeconds": "<string>",
      "epochMillis": "<string>"
    }

AuthorizationsAuthorizationstringheaderrequiredA JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.ResponseA successful response.isostringAn ISO-8601 representation of the timestampepochSecondsstring<int64>A second-precision representation of the timestampepochMillisstring<int64>A millisecond-precision representation of the timestamp