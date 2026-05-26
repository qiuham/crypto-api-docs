---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/new-crypto-loan/fixed/repay-collateral
api_type: REST
updated_at: 2026-01-16T09:39:50.184807
---

# Collateral Repayment

> Permission: "Spot trade"  
>  UID rate limit: 1 req / second

info

**fixed currency offset logic**

  *     1. From Currency Perspective 
       * Orders with the closest maturity date will be sorted in descending order.
       * If the maturity date is the same, the order with the higher interest rate will be prioritized.
       * If the interest rates are the same, the order will be processed randomly.Orders will be processed sequentially. Within an order, interest will be repaid first, followed by principal.
  *     2. From Order Perspective 
       * Interest will be repaid first, followed by principal.



### HTTP Request

POST `/v5/crypto-loan-fixed/repay-collateral`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
loanId| false| string| Loan contract ID. If not passed, the fixed currency offset logic will apply.  
loanCurrency| **true**|  string| Loan coin name  
collateralCoin| **true**|  string| Collateral currencies: Use commas to separate multiple collateral currencies  
amount| **true**|  string| Repay amount  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
  
None

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/repay-collateral HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752656296791  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 50  
    {  
      "loanCurrency": "ETH",  
      "amount": "0.1",  
      "collateralCoin":"USDT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.collateral_repayment_fixed_crypto_loan(  
        loanCurrency="ETH",  
        amount="0.1",  
        collateralCoin="USDT",  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1756973819393  
    }

---

# 抵押品還款

> 權限: "現貨"  
>  頻率: 1次/秒

信息

**定期幣種沖銷邏輯**

  *     1. 幣種緯度 
       * 按到期日由近及遠的借款訂單.
       * 如果到期日相同，則優先還借款利率高的訂單.
       * 如果借款利率相同，則隨機處理。依訂單逐步處理，訂單內，優先還利息，再還本金.
  *     2. 訂單緯度 
       * 優先還款利息，再還款本金.



### HTTP 請求

POST `/v5/crypto-loan-fixed/repay-collateral`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
loanId| false| string| 借款合同ID.如果不輸入，則按定期幣種沖銷邏輯來  
loanCurrency| **true**|  string| 借款幣種  
collateralCoin| **true**|  string| 抵押品幣種: 多個抵押品幣種使用英文逗號分開  
amount| **true**|  string| 還款數量  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
  
無

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/crypto-loan-fixed/repay-collateral HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: XXXXXX  
    X-BAPI-TIMESTAMP: 1752656296791  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 50  
    {  
      "loanCurrency": "ETH",  
      "amount": "0.1",  
      "collateralCoin":"USDT"  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.collateral_repayment_fixed_crypto_loan(  
        loanCurrency="ETH",  
        amount="0.1",  
        collateralCoin="USDT",  
    ))  
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "ok",  
        "result": {},  
        "retExtInfo": {},  
        "time": 1756973819393  
    }