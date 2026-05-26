---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config
api_type: Account
updated_at: 2026-01-16T09:38:01.014531
---

# Get Trade Behaviour Setting

You can get configuration how the system behaves when your limit order price exceeds the highest bid or lowest ask price.

Spot

  * **Maximum Buy Price** : _Min[Max(Index, Index × (1 + y%) + 2-Minute Average Premium), Index × (1 + z%)]_
  * **Lowest price for Sell** : _Max[Min(Index, Index × (1 – y%) + 2-Minute Average Premium), Index × (1 – z%)]_



Futures

  * **Maximum Buy Price** : _min( max( index , markprice_ ( 1 + x% ）), markprice _( 1 + y%) )_
  * **Lowest price for Sell** : _max ( min( index , markprice_ ( 1 - x% )) , markprice ( 1 - y%) )



Default Setting

  * Spot: **lpaSpot = false.** If the order price exceeds the boundary, the system rejects the request.

  * Futures: **lpaPerp = false.** If the order price exceeds the boundary, the system will automatically adjust the price to the nearest allowed boundary (i.e., highest bid or lowest ask).




### HTTP Request

GET `/v5/account/user-setting-config`

### Request Parameters

None

### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> lpaSpot| boolean| 

  * `true`: If the order price exceeds the boundary, the system will automatically adjust the price to the nearest allowed boundary
  * `false`: If the order price exceeds the boundary, the system rejects the request.

  
> lpaPerp| boolean| 

  * `true`: If the order price exceeds the boundary, the system rejects the request.
  * `false`: If the order price exceeds the boundary, the system will automatically adjust the price to the nearest allowed boundary

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/user-setting-config HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "lpaSpot": true,  
            "lpaPerp": false  
        },  
        "retExtInfo": {},  
        "time": 1756794317787  
    }

---

# 查詢交易行為設置

您可以查詢當限價單價格超過最高買價或最低賣價時，系統的行為方式。

現貨

  * **最高買入價格** : _Min[Max(指數價格, 指數價格 × (1 + y%) + 2分鐘平均溢價), 指數價格 × (1 + z%)]_
  * **最低賣出價格** : _Max[Min(指數價格, 指數價格 × (1 - y%) + 2分鐘平均溢價), 指數價格 × (1 - z%)]_



合約

  * **最高買入價格** : _min( max( 指數價格 , 標記價格 × (1 + x%) ), 標記價格 × (1 + y%) )_
  * **最低賣出價格** : *max( min( 指數價格 , 標記價格 × (1 - x%) ), 標記價格 × (1 - y%) )



預設設定

  * 現貨: **lpaSpot = false.** 若下單價格超出限制範圍，系統將拒絕該請求

  * 合約: **lpaPerp = false.** 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界（即最高買價或最低賣價）。




### HTTP 請求

GET `/v5/account/user-setting-config`

### 請求參數

無

### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> lpaSpot| boolean| 

  * `true`: 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界
  * `false`: 若下單價格超出限制範圍，系統將拒絕該請求

  
> lpaPerp| boolean| 

  * `true`: 若下單價格超出限制範圍，系統將拒絕該請求 
  * `false`: 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/account/user-setting-config HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "lpaSpot": true,  
            "lpaPerp": false  
        },  
        "retExtInfo": {},  
        "time": 1756794317787  
    }