---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/borrow-and-repay
api_type: REST
updated_at: 2026-01-15T23:50:29.502602
---

# Risk Unit Borrow(TRADE)

## API Description[​](/docs/institutional_loan/borrow-and-repay#api-description "Direct link to API Description")

This endpoint is used to perform a borrow request for that specified risk unit. This endpoint is accessible only with the credit account API key.

## HTTP Request[​](/docs/institutional_loan/borrow-and-repay#http-request "Direct link to HTTP Request")

POST /sapi/v1/margin/loan-group/borrow

## Request Weight[​](/docs/institutional_loan/borrow-and-repay#request-weight "Direct link to Request Weight")

3000(UID)

## Request Parameters[​](/docs/institutional_loan/borrow-and-repay#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| YES| Risk unit unique identifier  
assetName| STRING| YES| Asset Name , USDT or USDC  
amount| DECIMAL| YES|   
  
## Response Example[​](/docs/institutional_loan/borrow-and-repay#response-example "Direct link to Response Example")
    
    
    {   
      
    "transactionId":12317283617,   
      
    "amount":123456.78,    
      
    "status":success  
      
    }   
    

## Response detail description[​](/docs/institutional_loan/borrow-and-repay#response-detail-description "Direct link to Response detail description")

Parameter| Type| Description  
---|---|---  
transactionId| String| Transaction ID  
amount| DECIMAL| The amount borrowed  
status| String| success: Borrow Successfully  
  
**Error Code**

  * -27009: The requested borrow amount exceeds the maximum allowed limit.

---

# 风险单位借款 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/borrow-and-repay#接口描述 "接口描述的直接链接")

机构贷风险单位借款。仅支持放贷账户调用该接口。

## HTTP 请求[​](/docs/zh-CN/institutional_loan/borrow-and-repay#http-请求 "HTTP 请求的直接链接")

POST /sapi/v1/margin/loan-group/borrow

## 请求权重[​](/docs/zh-CN/institutional_loan/borrow-and-repay#请求权重 "请求权重的直接链接")

3000(UID)

## 请求参数[​](/docs/zh-CN/institutional_loan/borrow-and-repay#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
groupId| LONG| YES|   
assetName| STRING| YES| 资产名称，如 USDT 或 USDC  
amount| DECIMAL| YES|   
  
## 响应示例[​](/docs/zh-CN/institutional_loan/borrow-and-repay#响应示例 "响应示例的直接链接")
    
    
    {  
      
     "transactionId":12317283617,   
      
    "amount":123456.78,    
      
    "status":success  
      
    }   
    

## 响应信息详解：[​](/docs/zh-CN/institutional_loan/borrow-and-repay#响应信息详解 "响应信息详解：的直接链接")

参数| 类型| 描述  
---|---|---  
transactionId| String| 交易 ID  
amount| DECIMAL| 借款金额  
status| String| sucess: 借款成功  
  
**Error Code**

  * -27009: .请求的借贷额度超过最大可借额度。