---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rfq/trade/quote-list
api_type: Trading
updated_at: 2026-06-20 19:07:31.712670
---

# Get RFQs (real-time)

Obtain real-time inquiry information. **Up to 50 requests per second**

info

  * Obtain RFQs in real-time.
  * If both rfqId and rfqLinkId are passed, only rfqId is considered.
  * Sorted in descending order by createdAt.
  * During periods of extreme market volatility, this interface may experience increased latency or temporary delays in data delivery



### HTTP Request

GET`/v5/rfq/rfq-realtime`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
rfqId|  _false_|  string| Inquiry ID  
rfqLinkId|  _false_|  string| Custom inquiry ID, traderType is quote, this field is invalid  
traderType| false| string| Trader type, `quote` , `request`. Default: `quote`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| An array of RFQs  
> rfqId| string| Inquiry ID  
> rfqLinkId| string| Custom RFQ ID. Not publicly disclosed.  
>counterparties| array of srings| List of bidders  
> expiresAt| string| The inquiry's expiration time (ms)  
> strategyType| string| Inquiry label  
> status| string| Status of the RFQ: `Active` `PendingFill` `Canceled` `Filled` `Expired` `Failed`  
> acceptOtherQuoteStatus| string| Whether to accept non-LP quotes. The default value is `false`: `false`: Default value, do not accept non-LP quotes. `true`: Accept non-LP quotes  
> deskCode| string| The unique identification code of the inquiring party, which is not visible when anonymous was set to `true` when the RFQ was created  
> createdAt| string| Time (ms) when the trade is created in epoch, such as 1650380963  
> updatedAt| string| Time (ms) when the trade is updated in epoch, such as 1650380964  
> legs| array of objects| Combination transaction  
>> category| string| category. Valid values include: "linear", "option" and "spot"  
>> symbol| string| The unique instrument ID  
>> side| string| Inquiry direction: Valid values are `Buy` and `Sell` .  
>> qty| string| Order quantity of the instrument.  
  
### Request Example

  * HTTP
  * Python


    
    
    GET /v5/rfq/rfq-realtime HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_rfq_realtime())  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "rfqLinkId": "",  
                    "rfqId": "1756885055799241492396882271696580",  
                    "counterparties": [  
                        "hashwave2"  
                    ],  
                    "strategyType": "custom",  
                    "expiresAt": "1756885655801",  
                    "status": "Active",  
                    "acceptOtherQuoteStatus":"false",  
                    "deskCode": "1nu9d1",  
                    "createdAt": "1756885055801",  
                    "updatedAt": "1756885055801",  
                    "legs": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "side": "Buy",  
                            "qty": "1"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756885059062  
    }

---

# 獲取實时的詢價單資訊

獲取實时的詢價單資訊。**每秒最多 50 次請求**

信息

  * 獲取使用者發送或接收的詢價資訊，從 rfq-engine 即時查詢，無延遲
  * 同時傳遞 rfqId 和 rfqLinkId 時，以 rfqId 為準
  * 根據詢價單的創建時間倒序排列並返回。
  * 在極端市場波動期間, 此介面可能會出現延遲增加或資料傳遞暫時延遲的情況



### HTTP 請求

GET`/v5/rfq/rfq-realtime`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
rfqId| **false**|  string| 詢價單 ID  
rfqLinkId| **false**|  string| 詢價單自定義 ID，當 traderType 為 quote 時，此字段無效  
traderType| **false**|  string| 交易者類型，`quote` 或 `request`，默認為 `request`

  * `Request`：詢價方，查詢自己發出的詢價單
  * `Quote`：報價方，查詢自己接收到的詢價單

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| Array| 詢價單數據陣列  
> rfqId| string| 詢價單 ID  
> rfqLinkId| string| 自定義詢價單 ID，客戶敏感資訊不會公開，僅返回給報價方。  
> counterparties| Array of strings| 報價方列表  
> expiresAt| string| 詢價單的過期時間，Unix 時間戳的毫秒格式  
> strategyType| string| 詢價標籤  
> status| string| 詢價單狀態：`Active`、`PendingFill`、`Canceled`、`Filled`、`Expired`、`Failed`  
> acceptOtherQuoteStatus| string| 是否接受非 LP 報價. 預設值是 `false`.`false`: 不接受非 LP 報價. `true`: 接受非 LP 報價  
> deskCode| string| 詢價方的唯一識別代碼，若詢價時設置匿名為 `true` 則不可見  
> createdAt| string| 交易創建的時間（毫秒），例如 1650380963  
> updatedAt| string| 交易更新的時間（毫秒），例如 1650380964  
> legs| Array of objects| 組合交易  
>> category| string| 類型，有效值包括：`linear`、`option` 和 `spot`  
>> symbol| string| 唯一的交易品種 ID  
>> side| string| 詢價方向，有效值包括 `Buy` 和 `Sell`  
>> qty| string| 交易品種的訂單數量  
  
### 請求示例
    
    
    GET /v5/rfq/rfq-realtime HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676430842094  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "rfqLinkId": "",  
                    "rfqId": "1756885055799241492396882271696580",  
                    "counterparties": [  
                        "hashwave2"  
                    ],  
                    "strategyType": "custom",  
                    "expiresAt": "1756885655801",  
                    "status": "Active",  
                    "acceptOtherQuoteStatus":"false",  
                    "deskCode": "1nu9d1",  
                    "createdAt": "1756885055801",  
                    "updatedAt": "1756885055801",  
                    "legs": [  
                        {  
                            "category": "linear",  
                            "symbol": "BTCUSDT",  
                            "side": "Buy",  
                            "qty": "1"  
                        }  
                    ]  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1756885059062  
    }