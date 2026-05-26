---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/account/repay-liability
api_type: Account
updated_at: 2026-01-16T09:38:01.274053
---

# Repay Liability

You can manually repay the liabilities of Unified account

> **Permission** : USDC Contracts  
> 

info

  1. BYUSDT will not be used for repayment.
  2. MNT will temporarily not be used for repayment, and repaying MNT liabilities through convert-repay is not supported. However, you may still use [Manual Repay Without Asset Conversion](/docs/v5/account/no-convert-repay) to repay MNT using your existing balance.



### HTTP Request

POST `/v5/account/quick-repayment`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
coin| false| string| The coin with liability, uppercase only 

  * Input the specific coin: repay the liability of this coin in particular
  * No coin specified: repay the liability of all coins

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> coin| string| Coin used for repayment 

  * The order of currencies used to repay liability is based on `liquidationOrder` from [this endpoint](/docs/v5/spot-margin-uta/vip-margin)

  
> repaymentQty| string| Repayment qty  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/quick-repayment HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1701848610019  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 22  
      
    {  
        "coin": "USDT"  
    }  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .repayLiability({  
        coin: 'USDT',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "SUCCESS",  
        "result": {  
            "list": [  
                {  
                    "coin": "BTC",  
                    "repaymentQty": "0.10549670"  
                },  
                {  
                    "coin": "ETH",  
                    "repaymentQty": "2.27768114"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1701848610941  
    }

---

# 一鍵還款

您可以通過該接口手動還清統一帳戶中的借款

> 權限: USDC合約

信息

  1. BYUSDT 不會被用於還款
  2. MNT 暫時不會被用於還款, 亦不支援通過貨幣轉換還款(convert-repay)來償還 MNT 負債. 不過, 您仍可使用 [無損手工還款](/docs/zh-TW/v5/account/no-convert-repay)以現有餘額償還 MNT 借款



### HTTP 請求

POST `/v5/account/quick-repayment`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
coin| false| string| 有負債的幣種

  * 指定幣種: 則僅還清指定幣種的負債
  * 不指定: 還清所有有負債的幣種

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> coin| string| 用於償還借款的兌出幣種

  * 用於還款的幣種是基於這個[接口](/docs/zh-TW/v5/spot-margin-uta/vip-margin)中的`liquidationOrder`字段 

  
> repaymentQty| string| 兌出幣種數量  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/account/quick-repayment HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN: XXXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1701848610019  
    X-BAPI-RECV-WINDOW: 5000  
    Content-Type: application/json  
    Content-Length: 22  
      
    {  
        "coin": "USDT"  
    }  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .repayLiability({  
        coin: 'USDT',  
      })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "SUCCESS",  
        "result": {  
            "list": [  
                {  
                    "coin": "BTC",  
                    "repaymentQty": "0.10549670"  
                },  
                {  
                    "coin": "ETH",  
                    "repaymentQty": "2.27768114"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1701848610941  
    }