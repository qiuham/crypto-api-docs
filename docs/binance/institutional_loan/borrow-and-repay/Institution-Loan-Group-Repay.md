---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay
api_type: REST
updated_at: 2026-01-15T23:50:29.703796
---

# Risk Unit Repay(TRADE)

## API Description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#api-description "Direct link to API Description")

This endpoint is used to perform full or partial repayment of the specified risk unit. This endpoint is accessible only with the credit account API key.

## HTTP Request[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#http-request "Direct link to HTTP Request")

POST /sapi/v1/margin/loan-group/repay

## Request Weight[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#request-weight "Direct link to Request Weight")

3000(UID)

## Request Parameters[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| YES| Risk unit unique identifier  
assetName| STRING| YES| Asset Name , USDT or USDC  
amount| DECIMAL| YES| The real repaid amount = min(available amount in account, input repay amount)  
  
## Response Example[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#response-example "Direct link to Response Example")
    
    
    {  
      
    "transactionId": 12317283617,  
      
    "amount": 123456.78  
      
    }  
    

## Response detail description[​](/docs/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#response-detail-description "Direct link to Response detail description")

Parameter| Type| Description  
---|---|---  
transactionId| STRING| Transaction ID  
amount| DECIMAL| The amount that has been repaid

---

# 风险单位还款 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#接口描述 "接口描述的直接链接")

机构贷风险单位全部或部分还款，仅支持放贷账户调用该接口。

## HTTP 请求[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#http-请求 "HTTP 请求的直接链接")

POST /sapi/v1/margin/loan-group/repay

## 请求权重[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#请求权重 "请求权重的直接链接")

3000(UID)

## 请求参数[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
groupId| LONG| YES| 唯一风险单位标识符  
assetName| STRING| YES| 资产名称，如 USDT 或 USDC  
amount| DECIMAL| YES| 最终还款金额取值于： min(账户实际可还款金额, 输入的金额)，两者取小。  
  
## 响应示例[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#响应示例 "响应示例的直接链接")
    
    
    {  
      
    "transactionId": 12317283617,  
      
    "amount": 123456.78    
    }  
    

## 响应信息详解：[​](/docs/zh-CN/institutional_loan/borrow-and-repay/Institution-Loan-Group-Repay#响应信息详解 "响应信息详解：的直接链接")

参数| 类型| 描述  
---|---|---  
transactionId| STRING| 交易 ID  
amount| DECIMAL| 确切的偿还金额