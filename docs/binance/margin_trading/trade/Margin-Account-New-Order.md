---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Margin-Account-New-Order
api_type: Trading
updated_at: 2026-06-19 18:50:49.575588
---

# Query Liquidation Loan Repay History (USER_DATA)

## Description[​](/docs/margin_trading/trade/Query-Liquidation-Loan-Repay-History#description "Direct link to Description")

Query the repayment history of cross-margin liquidation loans (deficit caused by bankruptcy during liquidation). Supports time-range filtering and pagination.

## HTTP Request[​](/docs/margin_trading/trade/Query-Liquidation-Loan-Repay-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/liquidation-loan/repay-history`

## Request Weight[​](/docs/margin_trading/trade/Query-Liquidation-Loan-Repay-History#request-weight "Direct link to Request Weight")

**100(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Liquidation-Loan-Repay-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| NO| Start time in Unix timestamp (milliseconds). Defaults to 7 days ago if not specified  
endTime| LONG| NO| End time in Unix timestamp (milliseconds). Defaults to now if not specified  
current| LONG| NO| Current page number, default `1`  
size| LONG| NO| Page size, default `50`  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * The maximum query range is 90 days. If `startTime` is earlier than 90 days ago, it will be clamped to 90 days ago.
  * Only records with status `SUCCESS` or `PENDING` are returned. Failed repayment records are excluded.



## Response Example[​](/docs/margin_trading/trade/Query-Liquidation-Loan-Repay-History#response-example "Direct link to Response Example")
    
    
    {  
        "total": 2,  
        "rows": [  
            {  
                "repayId": 12345678,  
                "asset": "USDC",  
                "amount": "300.00000000",  
                "status": "SUCCESS",  
                "createTime": 1714492800000  
            },  
            {  
                "repayId": 12345679,  
                "asset": "USDC",  
                "amount": "200.00000000",  
                "status": "SUCCESS",  
                "createTime": 1714579200000  
            }  
        ]  
    }  
    

## Response Parameters[​](/docs/margin_trading/trade/Query-Liquidation-Loan-Repay-History#response-parameters "Direct link to Response Parameters")

Name| Type| Description  
---|---|---  
total| LONG| Total number of repayment records  
rows| ARRAY| List of repayment records  
rows[].repayId| LONG| Unique identifier for the repayment transaction  
rows[].asset| STRING| Asset used for repayment  
rows[].amount| DECIMAL| The repayment amount  
rows[].status| STRING| Repayment status: `SUCCESS` (completed) or `PENDING` (processing)  
rows[].createTime| LONG| Unix timestamp (milliseconds) when the repayment was created

---

# 查询强平欠款还款历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan-Repay-History#接口描述 "接口描述的直接链接")

查询全仓杠杆强平穿仓欠款（强平穿仓产生的负债）的还款历史记录，支持按时间范围过滤和分页查询。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan-Repay-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/liquidation-loan/repay-history`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan-Repay-History#请求权重 "请求权重的直接链接")

**100(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan-Repay-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
startTime| LONG| NO| 起始时间，Unix 时间戳（毫秒）。未指定时默认为 7 天前  
endTime| LONG| NO| 结束时间，Unix 时间戳（毫秒）。未指定时默认为当前时间  
current| LONG| NO| 当前页码，默认 `1`  
size| LONG| NO| 每页数量，默认 `50`  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 最大查询范围为 90 天。如果 `startTime` 早于 90 天前，将被截断为 90 天前。
  * 仅返回状态为 `SUCCESS`（成功）或 `PENDING`（处理中）的记录，失败的还款记录不会返回。



## 响应示例[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan-Repay-History#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 2,  
        "rows": [  
            {  
                "repayId": 12345678,  
                "asset": "USDC",  
                "amount": "300.00000000",  
                "status": "SUCCESS",  
                "createTime": 1714492800000  
            },  
            {  
                "repayId": 12345679,  
                "asset": "USDC",  
                "amount": "200.00000000",  
                "status": "PENDING",  
                "createTime": 1714579200000  
            }  
        ]  
    }  
    

## 响应参数[​](/docs/zh-CN/margin_trading/trade/Query-Liquidation-Loan-Repay-History#响应参数 "响应参数的直接链接")

名称| 类型| 描述  
---|---|---  
total| LONG| 还款记录总数  
rows| ARRAY| 还款记录列表  
rows[].repayId| LONG| 还款交易唯一标识  
rows[].asset| STRING| 还款资产  
rows[].amount| DECIMAL| 还款金额  
rows[].status| STRING| 还款状态：`SUCCESS`（成功）或 `PENDING`（处理中）  
rows[].createTime| LONG| 还款创建时间，Unix 时间戳（毫秒）