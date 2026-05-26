---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/rate-limit
api_type: REST
updated_at: 2026-01-16T09:40:36.575739
---

# Rate Limit Rules

## IP Limit

### HTTP IP limit

You are allowed to send **600 requests within a 5-second window per IP** by default. This limit applies to all traffic directed to `api.bybit.com`, `api.bybick.com`, and local site hostnames such as `api.bybit.kz`. If you encounter the error **"403, access too frequent"** , it indicates that your IP has exceeded the allowed request frequency. In this case, you should terminate all HTTP sessions and wait for at least 10 minutes. The ban will be lifted automatically.

We do not recommend running your application at the very edge of these limits in case abnormal network activity results in an unexpected violation.

### Websocket IP limit

  * Do not establish more than 500 connections within a 5-minute window. This limit applies to all connections directed to `stream.bybit.com` as well as local site hostnames such as `stream.bybit.kz`.
  * Do not frequently connect and disconnect the connection
  * Do not establish more than 1,000 connections per IP for market data. The connection limits are counted separately for Spot, Linear, Inverse, and Options markets



## API Rate Limit

caution

If you receive `"retCode": 10006, "retMsg": "Too many visits!"` in the JSON response, you have hit the API rate limit.

The API rate limit is based on the **rolling time window per second and UID**. In other words, it is per second per UID. Every request to the API returns response header shown in the code panel:

  * `X-Bapi-Limit-Status` \- your remaining requests for current endpoint
  * `X-Bapi-Limit` \- your current limit for current endpoint
  * `X-Bapi-Limit-Reset-Timestamp` \- the timestamp indicating when your request limit resets if you have exceeded your rate_limit. Otherwise, this is just the current timestamp (it may not exactly match `timeNow`).



> Http Response Header Example
    
    
    ▶Response Headers  
    Content-Type: application/json; charset=utf-8  
    Content-Length: 141  
    X-Bapi-Limit: 100  
    X-Bapi-Limit-Status: 99  
    X-Bapi-Limit-Reset-Timestamp: 1672738134824  
    

### API Rate Limit Table

#### Trade

Method| Path| UTA2.0 Pro| upgradable  
---|---|---|---  
inverse| linear| option| spot  
POST| /v5/order/create| 10/s| 10/s| 20/s| Y  
/v5/order/amend| 10/s| 10/s| 10/s| Y  
/v5/order/cancel| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-all| 10/s| 1/s| 20/s| Y  
/v5/order/create-batch| 10/s| 10/s| 20/s| Y  
/v5/order/amend-batch| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-batch| 10/s| 10/s| 20/s| Y  
/v5/order/disconnected-cancel-all| 5/s| N  
GET| /v5/order/realtime| 50/s| N  
/v5/order/history| 50/s| N  
/v5/execution/list| 50/s| N  
/v5/order/spot-borrow-check| -| 50/s| N  
  
#### Position

Method| Path| UTA2.0 Pro| upgradable  
---|---|---|---  
inverse| linear| option| spot  
GET| /v5/position/list| 50/s| -| N  
/v5/position/closed-pnl| 50/s| -| -| N  
POST| /v5/position/set-leverage| 10/s| 10/s| -| -| N  
  
#### Account

Method| Path| | Limit| upgradable  
---|---|---|---|---  
GET| /v5/account/wallet-balance| accountType=UNIFIED| 50/s| N  
/v5/account/withdrawal| | 50/s| N  
/v5/account/borrow-history| | 50/s| N  
/v5/account/borrow| | 1/s| N  
/v5/account/repay| | 1/s| N  
/v5/account/no-convert-repay| | 1/s| N  
/v5/account/collateral-info| | 50/s| N  
/v5/asset/coin-greeks| | 50/s| N  
/v5/account/transaction-log| accountType=UNIFIED| 50/s| N  
/v5/account/fee-rate| category=linear| 10/s| N  
category=spot| 5/s| N  
category=option| 5/s| N  
category=inverse| 10/s| N  
  
#### Asset

Method| Path| Limit| upgradable  
---|---|---|---  
GET| /v5/asset/transfer/query-asset-info| 60 req/min| N  
/v5/asset/transfer/query-transfer-coin-list| 60 req/min| N  
/v5/asset/transfer/query-inter-transfer-list| 60 req/min| N  
/v5/asset/transfer/query-sub-member-list| 60 req/min| N  
/v5/asset/transfer/query-universal-transfer-list| 5 req/s| N  
/v5/asset/transfer/query-account-coins-balance| 5 req/s| N  
/v5/asset/deposit/query-record| 100 req/min| N  
/v5/asset/deposit/query-sub-member-record| 300 req/min| N  
/v5/asset/deposit/query-address| 300 req/min| N  
/v5/asset/deposit/query-sub-member-address| 300 req/min| N  
/v5/asset/withdraw/query-record| 300 req/min| N  
/v5/asset/coin/query-info| 5 req/s| N  
/v5/asset/exchange/order-record| 600 req/min| N  
POST| /v5/asset/transfer/inter-transfer| 60 req/min| N  
/v5/asset/transfer/save-transfer-sub-member| 20 req/s| N  
/v5/asset/transfer/universal-transfer| 5 req/s| N  
/v5/asset/withdraw/create| 5 req/s| N  
/v5/asset/withdraw/cancel| 60 req/min| N  
  
#### User

Method| Path| Limit| upgradable  
---|---|---|---  
POST| v5/user/create-sub-member| 1 req/s| N  
/v5/user/create-sub-api| 1 req/s| N  
/v5/user/frozen-sub-member| 5 req/s| N  
/v5/user/update-api| 5 req/s| N  
/v5/user/update-sub-api| 5 req/s| N  
/v5/user/delete-api| 5 req/s| N  
/v5/user/delete-sub-api| 5 req/s| N  
GET| /v5/user/query-sub-members| 10 req/s| N  
/v5/user/query-api| 10 req/s| N  
/v5/user/aff-customer-info| 10 req/s| N  
  
#### Spot Margin Trade (UTA)

For now, there is no limit for endpoints under this category  
---  
  
#### Spread Trading

Method| Path| Limit| Upgradable  
---|---|---|---  
POST| [Create Spread Order](/docs/v5/spread/trade/create-order)| 20 req/s| N  
POST| [Amend Spread Order](/docs/v5/spread/trade/amend-order)| 20 req/s| N  
POST| [Cancel Spread Order](/docs/v5/spread/trade/cancel-order)| 20 req/s| N  
POST| [Cancel All Spread Orders](/docs/v5/spread/trade/cancel-all)| 5 req/s| N  
GET| [Get Spread Open Orders](/docs/v5/spread/trade/open-order)| 50 req/s| N  
GET| [Get Spread Order History](/docs/v5/spread/trade/order-history)| 50 req/s| N  
GET| [Get Spread Trade History](/docs/v5/spread/trade/trade-history)| 50 req/s| N  
  
## Instructions for batch endpoints

tip

The batch order endpoint, which includes operations for creating, amending, and canceling, has its own rate limit and does not share it with single requests, _e.g., let's say the rate limit of single create order endpoint is 100/s, and batch create order endpoint is 100/s, so in this case, I can place 200 linear orders in one second if I use both endpoints to place orders_

### When category = linear spot or inverse

  * API for batch create/amend/cancel order, the frequency of the API will be consistent with the current configuration, but the counting consumption will be consumed according to the actual number of orders. (Number of consumption = number of requests * number of orders included in a single request), and the configuration of business lines is independent of each other.

  * The batch APIs allows 1-10 orders/request. For example, if a batch order request is made once and contains 5 orders, then the request limit will consume 5.

  * If part of the last batch of orders requested within 1s exceeds the limit, the part that exceeds the limit will fail, and the part that does not exceed the limit will succeed. For example, in the 1 second, the remaining limit is 5, but a batch request containing 8 orders is placed at this time, then the first 5 orders will be successfully placed, and the 6-8th orders will report an error exceeding the limit, and these orders will fail.

---

# 基礎頻率限制

## IP限頻

### HTTP IP限頻

默認情況下, 每個IP允許在每5秒的時間窗口內發送最多600次請求。這個速率限制將統計所有打到`api.bybit.com`, `api.bybick.com`, 以及本地站`api.bybit.kz`等域名的請求數量。 如果您遇到了**“403, access too frequent”** 這樣的報錯, 它表示您的IP已經超過了限定的頻率, 這種情況下, 您應當斷開所有來自這個IP的活著的HTTP會話, 然後休息至少10分鐘。IP將會自動解除限制。

我們不建議您在這些限制的邊緣運行您的應用程序，以防異常的網絡活動導致意外違規。

### Websocket IP 限頻

  * 不要在5分鐘內構建超過500個連接, 這個限頻適用於所有發往`stream.bybit.com` 以及本地站域名, 比如 `stream.bybit.kz`的連接請求;
  * 不要嘗試頻繁地構建連接與斷開連接;
  * 訂閱行情數據時, 每個IP不要構建超過1,000個連接, 現貨、U本位期貨、幣本位期貨以及期權分開計算。



## 賬戶頻率限製

警告

如果您收到這樣的響應`"retCode": 10006, "retMsg": "Too many visits!"`, 則表示您觸發了帳戶頻率限制, 請等到頻率限制重置以後, 再繼續發送請求。

Bybit基於**每秒鍾** 的滾動時間窗口來做頻率限製，並且是按**賬戶** （uid）來做劃分限製，每次請求API響應頭(response header)中都會包含如下字段：

  * `X-Bapi-Limit-Status` \- 該接口當前時間窗口剩余可用請求數
  * `X-Bapi-Limit` \- 該接口當前頻率限製上限
  * `X-Bapi-Limit-Reset-Timestamp` \- 如果您已超過該接口當前窗口頻率限製，該字段表示下個可用時間窗口的時間戳（毫秒），即什麽時候可以恢復訪問；如果您未超過該接口當前窗口頻率限製，該字段表示返回的是當前服務器時間（毫秒).



> Http 響應頭示例
    
    
    ▶Response Headers  
    Content-Type: application/json; charset=utf-8  
    Content-Length: 141  
    X-Bapi-Limit: 100  
    X-Bapi-Limit-Status: 99  
    X-Bapi-Limit-Reset-Timestamp: 1672738134824  
    

### 接口頻率限制表

#### 交易

請求方式| 路徑| 統一帳戶| 是否可提頻  
---|---|---|---  
inverse| linear| option| spot  
POST| /v5/order/create| 10/s| 10/s| 20/s| Y  
/v5/order/amend| 10/s| 10/s| 10/s| Y  
/v5/order/cancel| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-all| 10/s| 1/s| 20/s| Y  
/v5/order/create-batch| 10/s| 10/s| 20/s| Y  
/v5/order/amend-batch| 10/s| 10/s| 20/s| Y  
/v5/order/cancel-batch| 10/s| 10/s| 20/s| Y  
/v5/order/disconnected-cancel-all| 5/s| N  
GET| /v5/order/realtime| 50/s| N  
/v5/order/history| 50/s| N  
/v5/execution/list| 50/s| N  
/v5/order/spot-borrow-check| -| 50/s| N  
  
#### 持倉

請求方式| 路徑| 統一帳戶| 是否可提頻  
---|---|---|---  
inverse| linear| option| spot  
GET| /v5/position/list| 50/s| -| N  
/v5/position/closed-pnl| 50/s| -| -| N  
POST| /v5/position/set-leverage| 10/s| 10/s| -| -| N  
  
#### 账户

請求方式| 路徑| | 頻率| 是否可提頻  
---|---|---|---|---  
GET| /v5/account/wallet-balance| accountType=UNIFIED| 50/s| N  
/v5/account/withdrawal| | 50/s| N  
/v5/account/borrow-history| | 50/s| N  
/v5/account/borrow| | 1/s| N  
/v5/account/repay| | 1/s| N  
/v5/account/no-convert-repay| | 1/s| N  
/v5/account/collateral-info| | 50/s| N  
/v5/asset/coin-greeks| | 50/s| N  
/v5/account/transaction-log| accountType=UNIFIED| 50/s| N  
/v5/account/fee-rate| category=linear| 10/s| N  
category=spot| 5/s| N  
category=option| 5/s| N  
category=inverse| 10/s| N  
  
#### 資產

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
GET| /v5/asset/transfer/query-asset-info| 60 req/min| N  
/v5/asset/transfer/query-transfer-coin-list| 60 req/min| N  
/v5/asset/transfer/query-inter-transfer-list| 60 req/min| N  
/v5/asset/transfer/query-sub-member-list| 60 req/min| N  
/v5/asset/transfer/query-universal-transfer-list| 5 req/s| N  
/v5/asset/transfer/query-account-coins-balance| 5 req/s| N  
/v5/asset/deposit/query-record| 100 req/min| N  
/v5/asset/deposit/query-sub-member-record| 300 req/min| N  
/v5/asset/deposit/query-address| 300 req/min| N  
/v5/asset/deposit/query-sub-member-address| 300 req/min| N  
/v5/asset/withdraw/query-record| 300 req/min| N  
/v5/asset/coin/query-info| 5 req/s| N  
/v5/asset/exchange/order-record| 600 req/min| N  
POST| /v5/asset/transfer/inter-transfer| 60 req/min| N  
/v5/asset/transfer/save-transfer-sub-member| 20 req/s| N  
/v5/asset/transfer/universal-transfer| 5 req/s| N  
/v5/asset/withdraw/create| 5 req/s| N  
/v5/asset/withdraw/cancel| 60 req/min| N  
  
#### 用戶

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
POST| v5/user/create-sub-member| 1 req/s| N  
/v5/user/create-sub-api| 1 req/s| N  
/v5/user/frozen-sub-member| 5 req/s| N  
/v5/user/update-api| 5 req/s| N  
/v5/user/update-sub-api| 5 req/s| N  
/v5/user/delete-api| 5 req/s| N  
/v5/user/delete-sub-api| 5 req/s| N  
GET| /v5/user/query-sub-members| 10 req/s| N  
/v5/user/query-api| 10 req/s| N  
/v5/user/aff-customer-info| 10 req/s| N  
  
#### 槓桿代幣

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
GET| /v5/spot-lever-token/order-record| 50 req/s| N  
POST| /v5/spot-lever-token/purchase| 20 req/s| N  
POST| /v5/spot-lever-token/redeem| 20 req/s| N  
  
#### 全倉槓桿 (統一帳戶)

目前，該目錄下的接口沒有頻率限制  
---  
  
#### 價差交易

請求方式| 路徑| 頻率| 是否可提頻  
---|---|---|---  
POST| [創建價差委托單](/docs/zh-TW/v5/spread/trade/create-order)| 20 req/s| N  
POST| [修改價差委託單](/docs/zh-TW/v5/spread/trade/amend-order)| 20 req/s| N  
POST| [撤銷價差委託單](/docs/zh-TW/v5/spread/trade/cancel-order)| 20 req/s| N  
POST| [價差-全部撤單](/docs/zh-TW/v5/spread/trade/cancel-all)| 5 req/s| N  
GET| [查詢價差活動單](/docs/zh-TW/v5/spread/trade/open-order)| 50 req/s| N  
GET| [查詢價差訂單歷史](/docs/zh-TW/v5/spread/trade/order-history)| 50 req/s| N  
GET| [查詢價差成交歷史](/docs/zh-TW/v5/spread/trade/trade-history)| 50 req/s| N  
  
## 批量接口限頻說明

提示

批次訂單接口（包括創建、修改和取消）的速率限制不會與單一的下改撤請求共享。 _例如，單一下單接口頻率是100/秒, 批量下單接口是100/秒,，那麼當結合兩個接口一起下單時， 就擁有200單每秒的能力_ 。

#### 僅category=linear, inverse或spot時

  * 批量下單的接口，api rate limit：接口的頻次，還是統一沿用當前配置，但是計數消耗會根據實際的訂單數來消耗。（消耗數 = 請求數 * 請求中包含的訂單數），業務線配置相互獨立。

  * 批量接口允許1-10orders/request，例如，批量下單請求一次，包含5個orders，則本次請求limit數量消耗5。

  * 若1s內的最後一次請求的批量訂單，部分超限，則超過的部分會失敗（報錯超過上限），未超過的部分會成功。例如，這1s中，limit還剩5，但是此時下了一個包含8個orders的批量請求， 那麼前5個orders會下單成功，第6-8的orders，會報錯超過上限，下單失敗。