---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/repay
api_type: Account
updated_at: 2026-01-16T09:38:01.210365
---

# Manual Repay

info

  * If neither `coin` nor `amount` is passed in input parameter, then repay all the liabilities.
  * If `coin` is passed in input parameter and `amount` is not, the coin will be repaid in full.



important

  1. When repaying, the system will first use the spot available balance of the debt currency. If that’s not enough, the remaining amount will be repaid by converting other assets according to the [liquidation order](https://www.bybit.com/en/announcement-info/fullstock-leverage-uta/).
  2. If you only want to repay using your spot balance and don't want to trigger currency convert repayment, please refer to [Manual Repay Without Asset Conversion](/docs/v5/account/no-convert-repay)
  3. Repayment is prohibited between 04:00 and 05:30 per hour. Interest is calculated based on the BorrowAmount at 05:00 per hour.
  4. System repays floating-rate liabilities first, followed by fixed-rate
  5. BYUSDT will not be used for repayment.
  6. MNT will temporarily not be used for repayment, and repaying MNT liabilities through convert-repay is not supported. However, you may still use [Manual Repay Without Asset Conversion](/docs/v5/account/no-convert-repay) to repay MNT using your existing balance.



### HTTP Request

POST `/v5/account/repay`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| coin name, uppercase only  
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


    
    
    POST /v5/account/repay HTTP/1.1  
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

# 手工還款

信息

  * 如果輸入參數中未傳遞 `coin` 或 `amount`，則償還所有債務。
  * 如果輸入參數中傳遞了 `coin`，而未傳遞 `amount`，則將全額償還該幣。



重要

  1. 還款時，優先使用負債幣種的現貨可用餘額，不足的部分，將會按照[清算順序](https://www.bybit.com/zh-TW/announcement-info/fullstock-leverage-uta/)兌幣還款
  2. 如果您只想使用現貨可用餘額還款，而不想觸發貨幣轉換還款，請參閱 [無損手工還款](/docs/zh-TW/v5/account/no-convert-repay)
  3. 每小時04分-05分30秒，禁止還款。計息是按每小時05分那一刻的borrowAmount來進行計息。
  4. 系統先償還浮動利率債務，然後償還固定利率債務。
  5. BYUSDT 不會被用於還款
  6. MNT 暫時不會被用於還款, 亦不支援通過貨幣轉換還款(convert-repay)來償還 MNT 負債. 不過, 您仍可使用 [無損手工還款](/docs/zh-TW/v5/account/no-convert-repay)以現有餘額償還 MNT 借款



### HTTP 請求

POST `/v5/account/repay`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 幣名稱，僅限大寫  
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


    
    
    POST /v5/account/repay HTTP/1.1  
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