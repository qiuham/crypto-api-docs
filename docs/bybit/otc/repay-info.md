---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/otc/repay-info
api_type: REST
updated_at: 2026-01-16T09:40:21.408941
---

# Get Repayment Orders

Get a list of your loan repayment orders (orders which repaid the loan).

tip

  * Get the past 2 years data by default
  * Get up to the past 2 years of data



### HTTP Request

GET `/v5/ins-loan/repaid-history`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
startTime| false| integer| The start timestamp (ms)  
endTime| false| integer| The end timestamp (ms)  
limit| false| integer| Limit for data size. [`1`, `100`]. Default: `100`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
repayInfo| array| Object  
> repayOrderId| string| Repaid order ID  
> repaidTime| string| Repaid timestamp (ms)  
> token| string| Repaid coin  
> quantity| string| Repaid principle  
> interest| string| Repaid interest  
> businessType| string| Repaid type. `1`：normal repayment; `2`：repaid by liquidation  
> status| string| `1`：success; `2`：fail  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/repaid-history HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1678687944725  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_repayment_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingRepayOrders({  
        limit: 100,  
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
        "retMsg": "",  
        "result": {  
            "repayInfo": [  
                {  
                    "repayOrderId": "8189",  
                    "repaidTime": "1663126393000",  
                    "token": "USDT",  
                    "quantity": "30000",  
                    "interest": "0",  
                    "businessType": "1",  
                    "status": "1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1669366648366  
    }

---

# 查詢還款信息

提示

  * 默認查詢過去2年的數據
  * 最多支持查詢過去2年的數據



### HTTP 請求

GET `/v5/ins-loan/repaid-history`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
startTime| false| integer| 開始時間戳 (毫秒)  
endTime| false| integer| 結束時間戳 (毫秒)  
limit| false| integer| 返回數量限制. [`1`, `100`]. 默認: `100`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
repayInfo| array| Object  
> repayOrderId| string| 還款訂單號  
> repaidTime| string| 還款時間（毫秒）  
> token| string| 還款幣種  
> quantity| string| 還款本金  
> interest| string| 還款利息  
> businessType| string| 還款類型. `1`：正常還款; `2`：系統強平還款  
> status| string| `1`：還款成功; `2`：還款失敗  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/ins-loan/repaid-history HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-SIGN-TYPE: 2  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1678687944725  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_repayment_info())  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getInstitutionalLendingRepayOrders({  
        limit: 100,  
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
        "retMsg": "",  
        "result": {  
            "repayInfo": [  
                {  
                    "repayOrderId": "8189",  
                    "repaidTime": "1663126393000",  
                    "token": "USDT",  
                    "quantity": "30000",  
                    "interest": "0",  
                    "businessType": "1",  
                    "status": "1"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1669366648366  
    }