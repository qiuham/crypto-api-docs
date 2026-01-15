---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records
api_type: REST
updated_at: 2026-01-15T23:50:29.572060
---

# Risk Unit borrow/repay records(TRADE)

#### API Description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#api-description "Direct link to API Description")

Get borrow/repay records in the Institution Loan Risk Unit. This endpoint is accessible only with the credit account API key.

#### HTTP Request[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#http-request "Direct link to HTTP Request")

GET /sapi/v1/margin/loan-group/borrow-repay

#### Request Weight[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#request-weight "Direct link to Request Weight")

10(IP)

#### RequestParameters[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#requestparameters "Direct link to RequestParameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| NO| Risk unit unique identifier  
type| STRING| YES| BORROW or REPAY  
asset| STRING| NO| Asset Name , USDT or USDC  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| The currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
recvWindow| LONG| NO| The value cannot be greater than 60000  
timestamp| LONG| YES|   
  
  * Credit account can query either activated risk unit or closed risk unit with the specific groupId. The current activated risk unit will be returned if the parameter of groupId is not input.
  * Response in descending order
  * If the asset parameter is provided, the maximum query time range is 30 days ahead of endTime; if the asset parameter is not provided the maximum query time range is 7 days ahead of endTime
  * If neither startTime nor endTime is sent, the recent 7-day data will be returned.
  * startTime set as endTime - 7days by default, endTime set as current time by default
  * The length of startTime and endTime cannot exceed 100 days, otherwise an error is reported and no record is returned.



#### Response Example[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#response-example "Direct link to Response Example")
    
    
    {  
    "total": 1,  
    "rows": [  
    {  
    "tranId": 1648963682,  
    "assetName": "USDT",  
    "amount": 300,  
    "status": "CONFIRM",  
    "type": "BORROW",//BORROW, NORMAL_REPAY, FORCE_REPAY  
    "timestamp": 1750420899036 // Create Time  
    },  
    {  
    "tranId": 1648963682,  
    "assetName": "USDT",  
    "amount": 300,  
    "status": "FAILED",  
    "type": "BORROW", //BORROW, NORMAL_REPAY, FORCE_REPAY  
    "timestamp": 1750420899036 // Create Time  
    },  
    {  
    "tranId": 1648963682,  
    "assetName": "USDT",  
    "amount": 300,  
    "principal": 298,  
    "interest": 2,  
    "status": "CONFIRM",  
    "type": "REPAY", //BORROW, NORMAL_REPAY, FORCE_REPAY  
    "timestamp": 1750420899036 // Create Time  
    }  
    ]}

---

# 查询风险单元借贷/还款记录 (USER_DATA)

#### 接口描述[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#接口描述 "接口描述的直接链接")

查询风险单位借贷/还款记录，仅支持放贷账户调用该接口。

#### HTTP请求[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#http请求 "HTTP请求的直接链接")

GET /sapi/v1/margin/loan-group/borrow-repay

#### 请求权重[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#请求权重 "请求权重的直接链接")

10(IP)

#### 请求参数[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
groupId| LONG| NO| 唯一风险单位标识符  
type| STRING| YES| 操作类型：BORROW、REPAY  
asset| STRING| NO| 资产名称， 如 USDT 或 USDC  
startTime| LONG| NO| 开始时间  
endTime| LONG| NO| 结束时间  
current| LONG| NO| 当前查询页。 开始值 1。 默认:1  
size| LONG| NO| 默认:10 最大:100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * 放贷账户可根据参数groupId查询当前生效状态 风险单位和已经关闭的风险单位，若groupId为空，则返回当前生效状态 的风险单位。
  * 响应返回为降序排列。
  * 若传了asset参数，最大查询时间范围为endTime往前30天；不传asset参数，最大查询时间范围为endTime往前7天。
  * 若startTime和endTime没传，则默认返回最近7天数据。
  * startTime不传，默认endTime-7天；结束时间不传，默认当前时间。
  * startTime和endTime时间长度不能超过100天，否则报错，无返回记录。



#### 响应示例[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Borrow-Repay-Records#响应示例 "响应示例的直接链接")
    
    
    {  
    "total": 1,  
    "rows": [  
    {  
    "tranId": 1648963682,  
    "assetName": "USDT",  
    "amount": 300,  
    "status": "CONFIRM",  
    "type": "BORROW", //BORROW, NORMAL_REPAY, FORCE_REPAY  
    "timestamp": 1750420899036 // Create Time  
    },  
    {  
    "tranId": 1648963682,  
    "assetName": "USDT",  
    "amount": 300,  
    "status": "FAILED",  
    "type": "BORROW", //BORROW, NORMAL_REPAY, FORCE_REPAY  
    "timestamp": 1750420899036 // Create Time  
    },  
    {  
    "tranId": 1648963682,  
    "assetName": "USDT",  
    "amount": 300,  
    "principal": 298,  
    "interest": 2,  
    "status": "CONFIRM",  
    "type": "REPAY", //BORROW, NORMAL_REPAY, FORCE_REPAY  
    "timestamp": 1750420899036 // Create Time  
    }  
    ]}