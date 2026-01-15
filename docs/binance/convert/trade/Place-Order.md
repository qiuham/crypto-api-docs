---
exchange: binance
source_url: https://developers.binance.com/docs/convert/trade/Place-Order
api_type: Trading
updated_at: 2026-01-15T23:50:19.868577
---

# Place limit order (USER_DATA)

## API Description[​](/docs/convert/trade/Place-Order#api-description "Direct link to API Description")

Enable users to place a limit order

## HTTP Request[​](/docs/convert/trade/Place-Order#http-request "Direct link to HTTP Request")

POST `/sapi/v1/convert/limit/placeOrder`

## Request Weight[​](/docs/convert/trade/Place-Order#request-weight "Direct link to Request Weight")

**500(UID)**

## Request Parameters[​](/docs/convert/trade/Place-Order#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
baseAsset| STRING| YES| base asset (use the response `fromIsBase` from `GET /sapi/v1/convert/exchangeInfo` api to check which one is baseAsset )  
quoteAsset| STRING| YES| quote asset  
limitPrice| DECIMAL| YES| Symbol limit price (from baseAsset to quoteAsset)  
baseAmount| DECIMAL| NO| Base asset amount. (One of `baseAmount` or `quoteAmount` is required)  
quoteAmount| DECIMAL| NO| Quote asset amount. (One of `baseAmount` or `quoteAmount` is required)  
side| ENUM| YES| `BUY` or `SELL`  
walletType| ENUM| NO| It is to choose which wallet of assets. The wallet selection is `SPOT`, `FUNDING` and `EARN`. Combination of wallet is supported i.e. `SPOT_FUNDING`, `FUNDING_EARN`, `SPOT_FUNDING_EARN` or `SPOT_EARN` Default is `SPOT`.  
expiredType| ENUM| YES| 1_D, 3_D, 7_D, 30_D (D means day)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `baseAsset` or `quoteAsset` can be determined via `exchangeInfo` endpoint.
>   * Limit price is defined from `baseAsset` to `quoteAsset`.
>   * Either `baseAmount` or `quoteAmount` is used.
> 


## Response Example[​](/docs/convert/trade/Place-Order#response-example "Direct link to Response Example")
    
    
    {  
       "quoteId":"12415572564",  
       "ratio":"38163.7",  
       "inverseRatio":"0.0000262",  
       "validTimestamp":1623319461670,  
       "toAmount":"3816.37",  
       "fromAmount":"0.1"  
    }

---

# 创建闪兑限价单(USER_DATA)

## 接口描述[​](/docs/zh-CN/convert/trade/Place-Order#接口描述 "接口描述的直接链接")

用户创建闪兑限价单

## HTTP请求[​](/docs/zh-CN/convert/trade/Place-Order#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/convert/limit/placeOrder`

## 请求权重[​](/docs/zh-CN/convert/trade/Place-Order#请求权重 "请求权重的直接链接")

**500(UID)**

## 请求参数[​](/docs/zh-CN/convert/trade/Place-Order#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
baseAsset| STRING| YES| 先使用`GET /sapi/v1/convert/exchangeInfo` API接口去查询币对中的quoteAsset  
quoteAsset| STRING| YES| 先使用`GET /sapi/v1/convert/exchangeInfo`API接口去查询币对中的quoteAsset  
limitPrice| DECIMAL| YES| 币对限价 (从`baseAsset` 到 `quoteAsset`)  
baseAmount| DECIMAL| NO| Base asset 金额 (baseAmount 或 quoteAmount 需且仅需填写一个)  
quoteAmount| DECIMAL| NO| Quote asset 金额 (baseAmount 或 quoteAmount 需且仅需填写一个)  
side| ENUM| YES| `BUY` 或者`SELL`  
walletType| ENUM| NO| 这里可以选择支付钱包，可支持的钱包的选择有`SPOT`，`FUNDING`和`EARN`。组合钱包选择也可支持，如`SPOT_FUNDING`，`FUNDING_EARN`，`SPOT_FUNDING_EARN`或者`SPOT_EARN`。默认选择为`SPOT`。  
expiredType| ENUM| YES| 1_D, 3_D, 7_D, 30_D (D 指天)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `baseAsset` 或 `quoteAsset` 可以通过`GET /sapi/v1/convert/exchangeInfo`API 接口判别.
>   * 限价的方向是从`baseAsset`到`quoteAsset`.
>   * `baseAmount`或`quoteAmount`需且仅需一个.
> 


## 响应示例[​](/docs/zh-CN/convert/trade/Place-Order#响应示例 "响应示例的直接链接")
    
    
    {  
        "orderId": 1603680255057330400,   
        "status": "PROCESS"  
    }