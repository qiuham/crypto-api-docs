---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/affiliate/affiliate-info
api_type: REST
updated_at: 2026-01-16T09:38:15.138032
---

# Get Affiliate User Info

To use this endpoint, you should have an affiliate account and only tick "affiliate" permission while creating the API key.  
Affiliate site: <https://affiliates.bybit.com>

tip

  * Use master UID only
  * The api key can only have "Affiliate" permission
  * The transaction volume and deposit amount are the total amount of the user done on Bybit, and have nothing to do with commission settlement. Any transaction volume data related to commission settlement is subject to the Affiliate Portal.



### HTTP Request

GET `/v5/user/aff-customer-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
uid| **true**|  string| The master account UID of affiliate's client  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
uid| string| UID  
vipLevel| string| VIP level  
takerVol30Day| string| Taker volume in last 30 days (USDT). All volume related attributes below includes Derivatives, Option, Spot volume  
makerVol30Day| string| Maker volume in last 30 days (USDT)  
tradeVol30Day| string| Total trading volume in last 30 days (USDT)  
depositAmount30Day| string| Deposit amount in last 30 days (USDT), update in 5 mins  
takerVol365Day| string| Taker volume in the past year (USDT)  
makerVol365Day| string| Maker volume in the past year (USDT)  
tradeVol365Day| string| Total trading volume in the past year (USDT)  
depositAmount365Day| string| Total deposit amount in the past year (USDT), update in 5 mins  
totalWalletBalance| string| Wallet balance range 

  * `1`: less than 100 USDT value
  * `2`: [100, 250) USDT value
  * `3`: [250, 500) USDT value
  * `4`: greater than 500 USDT value

  
depositUpdateTime| string| The update date time (UTC) of deposit data  
volUpdateTime| string| The update date of volume data time (UTC)  
KycLevel| integer| KYC level. `1`, `2`, `0`  
[](/docs/api-explorer/v5/user/affiliate-info)

* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/aff-customer-info?uid=1513500 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1685596324209  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAffiliateUserInfo({ uid: '1513500' })  
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
            "uid": "1513500",  
            "takerVol30Day": "10",  
            "makerVol30Day": "20",  
            "tradeVol30Day": "30",  
            "depositAmount30Day": "90",  
            "takerVol365Day": "100",  
            "makerVol365Day": "500",  
            "tradeVol365Day": "600",  
            "depositAmount365Day": "1300",  
            "totalWalletBalance": "4",  
            "depositUpdateTime": "2023-06-01 05:12:04",  
            "vipLevel": "99",  
            "volUpdateTime": "2023-06-02 00:00:00",  
            "KycLevel": 1  
        },  
        "retExtInfo": {},  
        "time": 1685596324508  
    }

---

# 查詢代理用戶信息

要使用此接口，您应该有一个代理商账户，并且在创建 API 密钥时仅勾选“代理商”权限。  
代理商网站: <https://affiliates.bybit.com>

提示

  * 僅支持使用母帳戶uid
  * 若要查詢該接口, api key僅能擁有代理商權限, 若擁有任何其他權限項, 請移除
  * 交易量和入金金額為用戶在Bybit上的總量，與結傭無關，任何結傭相關的交易量數據，以Affiliate Portal為準。



### HTTP 請求

GET `/v5/user/aff-customer-info`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
uid| **true**|  string| 被代理用戶的母帳戶uid  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
uid| string| 帳戶uid  
vipLevel| string| VIP等級  
takerVol30Day| string| 過去30天的吃單交易量. 單位: USDT. 所有下方交易量相關的字段, 包含了期貨、期權和現貨的交易量  
makerVol30Day| string| 過去30天的掛單交易量. 單位: USDT  
tradeVol30Day| string| 過去30天的總交易量. 單位: USDT  
depositAmount30Day| string| 過去30天的入金金額, 5分鐘內更新. 單位: USDT  
takerVol365Day| string| 過去一年的吃單交易量. 單位: USDT  
makerVol365Day| string| 過去一年的掛單交易量. 單位: USDT  
tradeVol365Day| string| 過去一年的總交易量. 單位: USDT  
depositAmount365Day| string| 過去一年的總入金金額, 5分鐘內更新. 單位: USDT  
totalWalletBalance| string| 資產餘額區間

  * `1`: 少於100 USDT的價值
  * `2`: 100(含) ~ 250 USDT的價值
  * `3`: 250(含) ~ 500 USDT的價值
  * `4`: 大於 500USDT的價值

  
depositUpdateTime| string| 入金數據更新時間. UTC時間  
volUpdateTime| string| 交易量數據更新時間. UTC時間  
KycLevel| integer| KYC等級. `0`, `1`, `2`  
[](/docs/zh-TW/api-explorer/v5/user/affiliate-info)

* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/user/aff-customer-info?uid=1513500 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1685596324209  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
      
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAffiliateUserInfo({ uid: '1513500' })  
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
            "uid": "1513500",  
            "takerVol30Day": "10",  
            "makerVol30Day": "20",  
            "tradeVol30Day": "30",  
            "depositAmount30Day": "90",  
            "takerVol365Day": "100",  
            "makerVol365Day": "500",  
            "tradeVol365Day": "600",  
            "depositAmount365Day": "1300",  
            "totalWalletBalance": "4",  
            "depositUpdateTime": "2023-06-01 05:12:04",  
            "vipLevel": "99",  
            "volUpdateTime": "2023-06-02 00:00:00",  
            "KycLevel": 1  
        },  
        "retExtInfo": {},  
        "time": 1685596324508  
    }