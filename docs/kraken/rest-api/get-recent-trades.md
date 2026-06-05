---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/get-recent-trades
api_type: REST
updated_at: 2026-06-05 19:37:02.350488
---

# Get Server Time

**GET** `https://api.kraken.com/0/public/Time`

Get the server's time.

## Responses

  * 200

Success response

  * application/json
* Schema

**Schema**

**result** `object`

    ↳ **unixtime** `integer`

Unix timestamp

**rfc1123** string

RFC 1123 time format

**error** `string[]`
* curl
  * python
  * go
  * nodejs
* CURL

    
    
    curl -L 'https://api.kraken.com/0/public/Time' \  
    -H 'Accept: application/json'  
    

Request Collapse all

Base URL

https://api.kraken.com/0

ResponseClear

Click the `Send API Request` button above and see the response here!