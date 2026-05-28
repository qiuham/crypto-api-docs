---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/spot-margin-uta/fixedborrow
api_type: REST
updated_at: 2026-05-28 19:25:57.679701
---

# Get Fixed-Rate Borrow Order Info

info

  * Results are returned in descending order by `orderTime`.



### HTTP Request

GET`/v5/spot-margin-trade/fixedborrow-order-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
orderId| false| string| Loan order ID  
orderCurrency| false| string| Loan coin name  
state| false| string| Borrow order status. `1`: Matching; `2`: Partially filled and cancelled; `3`: Fully filled; `4`: Cancelled  
term| false| string| Fixed term. `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
limit| false| string| Limit for data size per page. [1, 100]. Default: `10`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> annualRate| string| Annual rate for the borrowing  
> orderId| long| Loan order ID  
> orderTime| string| Order created time  
> filledQty| string| Filled quantity  
> orderQty| string| Order quantity  
> orderCurrency| string| Coin name  
> state| integer| Borrow order status. `1`: Matching; `2`: Partially filled and cancelled; `3`: Fully filled; `4`: Cancelled; `5`: Failed  
> term| integer| Fixed term. `7`: 7 days; `14`: 14 days; `30`: 30 days; `90`: 90 days; `180`: 180 days  
> repayType| string| `1`: Auto Repayment; `2`: Transfer to flexible loan  
> strategyType| string| `PARTIAL`: Allow partial fill; `FULL`: Full fill only  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixedborrow-order-info?orderCurrency=ETH&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.spot_margin_trade_get_fixed_borrow_order_info(  
        orderCurrency="ETH",  
        limit="10"  
    ))  
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.070000000000000000",  
                    "orderId": "FIXED_BORROW_4563567182f746ec9f73e4357264d8c7187",  
                    "orderTime": "1775616125000",  
                    "filledQty": "0.000000000000000000",  
                    "orderQty": "1.000000000000000000",  
                    "orderCurrency": "ETH",  
                    "state": 1,  
                    "term": 7,  
                    "repayType": "1",  
                    "strategyType": "FULL"  
                },  
                {  
                    "annualRate": "1.000000000000000000",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "orderTime": "1764120783000",  
                    "filledQty": "1000.000000000000000000",  
                    "orderQty": "1000.000000000000000000",  
                    "orderCurrency": "USDT",  
                    "state": 3,  
                    "term": 1,  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                }  
            ],  
            "nextPageCursor": "30"  
        },  
        "retExtInfo": {},  
        "time": 1775616669348  
    }

---

# 查詢固定利率借款訂單信息

信息

  * 結果按 `orderTime` 時間倒序返回。



### HTTP 請求

GET`/v5/spot-margin-trade/fixedborrow-order-info`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
orderId| false| string| 借款訂單 ID  
orderCurrency| false| string| 借款幣種  
state| false| string| 借款訂單狀態。`1`：撮合中；`2`：部分成交後取消；`3`：全部成交；`4`：已取消  
term| false| string| 借款期限。`7`：7天；`14`：14天；`30`：30天；`90`：90天；`180`：180天  
limit| false| string| 每頁返回數量，[1, 100]，默認：`10`  
cursor| false| string| 翻頁游標，使用上一次響應中的 `nextPageCursor` 獲取下一頁數據  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> annualRate| string| 借款年化利率  
> orderId| long| 借款訂單 ID  
> orderTime| string| 訂單創建時間  
> filledQty| string| 已成交數量  
> orderQty| string| 訂單數量  
> orderCurrency| string| 幣種名稱  
> state| integer| 借款訂單狀態。`1`：撮合中；`2`：部分成交後取消；`3`：全部成交；`4`：已取消；`5`：失敗  
> term| integer| 借款期限。`7`：7天；`14`：14天；`30`：30天；`90`：90天；`180`：180天  
> repayType| string| `1`：自動還款；`2`：轉為活期借款  
> strategyType| string| `PARTIAL`：允許部分成交；`FULL`：僅允許全部成交  
nextPageCursor| string| 參考請求參數 `cursor`  
  
* * *

### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/spot-margin-trade/fixedborrow-order-info?orderCurrency=ETH&limit=10 HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-SIGN: XXXXX  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1692696840996  
    X-BAPI-RECV-WINDOW: 5000  
    
    
    
      
    
    
    
      
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "success",  
        "result": {  
            "list": [  
                {  
                    "annualRate": "0.070000000000000000",  
                    "orderId": "FIXED_BORROW_4563567182f746ec9f73e4357264d8c7187",  
                    "orderTime": "1775616125000",  
                    "filledQty": "0.000000000000000000",  
                    "orderQty": "1.000000000000000000",  
                    "orderCurrency": "ETH",  
                    "state": 1,  
                    "term": 7,  
                    "repayType": "1",  
                    "strategyType": "FULL"  
                },  
                {  
                    "annualRate": "1.000000000000000000",  
                    "orderId": "FIXED_BORROW_a17089fc526441faa52eb99b0b9feb69185",  
                    "orderTime": "1764120783000",  
                    "filledQty": "1000.000000000000000000",  
                    "orderQty": "1000.000000000000000000",  
                    "orderCurrency": "USDT",  
                    "state": 3,  
                    "term": 1,  
                    "repayType": "1",  
                    "strategyType": "PARTIAL"  
                }  
            ],  
            "nextPageCursor": "30"  
        },  
        "retExtInfo": {},  
        "time": 1775616669348  
    }