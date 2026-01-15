---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay
api_type: REST
updated_at: 2026-01-15T23:48:24.638415
---

# Query borrow/repay records in Margin account(USER_DATA)

## API Description[​](/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay#api-description "Direct link to API Description")

Query borrow/repay records in Margin account

## HTTP Request[​](/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/borrow-repay`

## Request Weight[​](/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
isolatedSymbol| STRING| NO| Symbol in Isolated Margin  
txId| LONG| NO| `tranId` in `POST /sapi/v1/margin/loan`  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| Current querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
type| STRING| YES| `BORROW` or `REPAY`  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * `txId` or `startTime` must be sent. `txId` takes precedence. Response in descending order
>   * If an asset is sent, data within 30 days before `endTime`; If an asset is not sent, data within 7 days before `endTime`
>   * If neither `startTime` nor `endTime` is sent, the recent 7-day data will be returned.
>   * `startTime` set as `endTime` \- 7days by default, `endTime` set as current time by default
> 


## Response Example[​](/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay#response-example "Direct link to Response Example")
    
    
    {  
      "rows": [  
          {  
            "type": "AUTO", // AUTO,MANUAL for Cross Margin Borrow; MANUAL，AUTO，BNB_AUTO_REPAY，POINT_AUTO_REPAY for Cross Margin Repay; AUTO，MANUAL for Isolated Margin Borrow/Repay;  
            "isolatedSymbol": "BNBUSDT",     // isolated symbol, will not be returned for crossed margin  
            "amount": "14.00000000",   // Total amount borrowed/repaid  
            "asset": "BNB",     
            "interest": "0.01866667",    // Interest repaid  
            "principal": "13.98133333",   // Principal repaid  
            "status": "CONFIRMED",   //one of PENDING (pending execution), CONFIRMED (successfully execution), FAILED (execution failed, nothing happened to your account);  
            "timestamp": 1563438204000,  
            "txId": 2970933056  
          }  
      ],  
      "total": 1  
    }

---

# 查询借贷/还款记录(USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Borrow-Repay#接口描述 "接口描述的直接链接")

查询借贷/还款记录

## HTTP请求[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Borrow-Repay#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/borrow-repay`

## 请求权重[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Borrow-Repay#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Borrow-Repay#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
isolatedSymbol| STRING| NO| 逐仓symbol  
txId| LONG| NO| `POST /sapi/v1/margin/loan`中的`tranId`  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| 当前查询页。 开始值 1。 默认:1  
size| LONG| NO| 默认:10 最大:100  
type| STRING| YES| 操作类型：BORROW、REPAY  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
>   * 必须发送`txId`或`startTime`，`txId`优先
>   * 响应返回为降序排列。
>   * 传了`asset`参数，最大查询时间范围为`endTime`往前30天；不传`asset`参数，最大查询时间范围为`endTime`往前7天。
>   * 若`startTime`和`endTime`没传，则默认返回最近7天数据
>   * `startTime`不传，默认`endTime`-7天；结束时间不传，默认当前时间
> 


## 响应示例[​](/docs/zh-CN/margin_trading/borrow-and-repay/Query-Borrow-Repay#响应示例 "响应示例的直接链接")
    
    
    {  
      "rows": [  
          {  
            "type": "AUTO", // 全仓借贷可返回：AUTO,MANUAL ; 全仓还款可返回：MANUAL，AUTO，BNB_AUTO_REPAY，POINT_AUTO_REPAY; 逐仓借贷或还款可返回：AUTO，MANUAL  
            "isolatedSymbol": "BNBUSDT",     // 逐仓还款 返回逐仓symbol; 若是全仓不会返回此字段  
            "amount": "14.00000000",   // 还款总额  
            "asset": "BNB",     
            "interest": "0.01866667",    // 支付的利息  
            "principal": "13.98133333",   // 支付的本金  
            "status": "CONFIRMED",   //状态: PENDING (等待执行), CONFIRMED (成功还款), FAILED (执行失败);  
            "timestamp": 1563438204000,  
            "txId": 2970933056  
          }  
      ],  
      "total": 1  
    }