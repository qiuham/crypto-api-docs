---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/no-convert-repay
api_type: Account
updated_at: 2026-01-16T09:38:01.148168
---

# Manual Repay Without Asset Conversion

info

  * If `coin` is passed in input parameter and `amount` is not, the coin will be repaid in full.



important

  1. When repaying, system will only use the spot available balance of the debt currency. Users can perform a manual repay without converting their other assets.
  2. To check the spot available amount to repay, you can call this API: [Get Available Amount to Repay](/docs/v5/spot-margin-uta/repayment-available-amount)
  3. Repayment is prohibited between 04:00 and 05:30 per hour. Interest is calculated based on the BorrowAmount at 05:00 per hour.
  4. System repays floating-rate liabilities first, followed by fixed-rate
  5. BYUSDT will not be used for repayment.



### HTTP Request

POST `/v5/account/no-convert-repay`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| **true**|  string| coin name, uppercase only  
amount| false| string| Repay amount. If `coin` is not passed in input parameter, `amount` can not be passed in input parameter  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
result| array| Object  
> resultStatus| string| 

  * `P`: Processing
  * `SU`: Success
  * `FA`: Failed

  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/no-convert-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin":"BTC",  
        "amount":"0.01"  
    }  
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "resultStatus": "P"  
        },  
        "retExtInfo": {},  
        "time": 1756295680801  
    }

---

# 無損手工還款

信息

  * 如果輸入參數中傳遞了 `coin`，而未傳遞 `amount`，則將全額償還該幣。



重要

  1. 還款時，只使用負債幣種的現貨可用餘額. 用戶不會轉換其他資產進行手動還款。
  2. 若要查看可用於還款的現貨可用餘額，您可以調用此 API：[查詢負債幣種可還款金額](/docs/zh-TW/v5/spot-margin-uta/repayment-available-amount)
  3. 每小時04分-05分30秒，禁止還款。計息是按每小時05分那一刻的borrowAmount來進行計息。
  4. 系統先償還浮動利率債務，然後償還固定利率債務。
  5. BYUSDT 不會被用於還款



### HTTP 請求

POST `/v5/account/no-convert-repay`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| **true**|  string| 幣名稱，僅限大寫  
amount| false| string| 還款金額，若未使用 `coin` 作為輸入參數，則 `amount` 不作為輸入參數  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
result| array| Object  
> resultStatus| string| 

  * `P`: 處理中
  * `SU`: 成功
  * `FA`: 失敗

  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/no-convert-repay HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1675842997277  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
      
    {  
        "coin":"BTC",  
        "amount":"0.01"  
    }  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "resultStatus": "P"  
        },  
        "retExtInfo": {},  
        "time": 1756295680801  
    }