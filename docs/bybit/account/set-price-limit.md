---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/set-price-limit
api_type: Account
updated_at: 2026-01-16T09:38:07.005575
---

# Set Limit Price Behaviour

You can configure how the system behaves when your limit order price exceeds the highest bid or lowest ask price. You can query configuration by [Get Trade Behaviour Setting](/docs/v5/account/get-user-setting-config).

Spot

  * **Maximum Buy Price** : _Min[Max(Index, Index × (1 + y%) + 2-Minute Average Premium), Index × (1 + z%)]_
  * **Lowest price for Sell** : _Max[Min(Index, Index × (1 – y%) + 2-Minute Average Premium), Index × (1 – z%)]_



Futures

  * **Maximum Buy Price** : _min( max( index , markprice_ ( 1 + x% ）), markprice _( 1 + y%) )_
  * **Lowest price for Sell** : _max ( min( index , markprice_ ( 1 - x% )) , markprice ( 1 - y%) )



Default Setting

  * Spot: **modifyEnable = false.** If the order price exceeds the boundary, the system rejects the request.   
Corresponding to [Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config) that **lpaSpot = false , lpaPerp = true**

  * Futures: **modifyEnable = true.** If the order price exceeds the boundary, the system will automatically adjust the price to the nearest allowed boundary (i.e., highest bid or lowest ask).  
Corresponding to [Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config) that **lpaSpot = true , lpaPerp = false**

  * Setting either `linear` or `inverse` will set behaviour for **all futures**.




### HTTP Request

POST `/v5/account/set-limit-px-action`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
category| **true**|  string| `linear`, `inverse`, `spot`  
modifyEnable| **true**|  boolean| `true`: allow the syetem to modify the order price  
`false`: reject your order request  
  
### Response Parameters

None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-limit-px-action HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "category": "spot",  
        "modifyEnable": true  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1753255927952  
    }

---

# 設置限價單行為

您可以設定當限價單價格超過最高買價或最低賣價時，系統的行為方式。 您可以使用[查詢交易行為設置](/docs/zh-TW/v5/account/get-user-setting-config)接口查詢限價單行為

現貨

  * **最高買入價格** : _Min[Max(指數價格, 指數價格 × (1 + y%) + 2分鐘平均溢價), 指數價格 × (1 + z%)]_
  * **最低賣出價格** : _Max[Min(指數價格, 指數價格 × (1 - y%) + 2分鐘平均溢價), 指數價格 × (1 - z%)]_



合約

  * **最高買入價格** : _min( max( 指數價格 , 標記價格 × (1 + x%) ), 標記價格 × (1 + y%) )_
  * **最低賣出價格** : *max( min( 指數價格 , 標記價格 × (1 - x%) ), 標記價格 × (1 - y%) )



預設設定

  * 現貨: **modifyEnable = false.** 若下單價格超出限制範圍，系統將拒絕該請求   
對應[Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config)接口返回值：**lpaSpot = false , lpaPerp = true**

  * 合約: **modifyEnable = true.** 若下單價格超出限制範圍，系統會自動將價格調整至允許的最近邊界（即最高買價或最低賣價）。   
對應[Get Limit Price Behaviour](https://bybit-exchange.github.io/docs/v5/account/get-user-setting-config)接口返回值：**lpaSpot = true , lpaPerp = false**

  * 設定 `linear` 或 `inverse` 會對整個**合約** 生效  





### HTTP 請求

POST `/v5/account/set-limit-px-action`

### 請求參數

參數| 類型| 說明| 默認值  
---|---|---|---  
category| **true**|  string| `linear`, `inverse`, `spot`  
modifyEnable| **true**|  boolean| `true`: 允許系統自動修改價格  
`false`: 拒絕請求  
  
### 響應參數

無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/set-limit-px-action HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1753255927950  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 52  
      
    {  
        "category": "spot",  
        "modifyEnable": true  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1753255927952  
    }