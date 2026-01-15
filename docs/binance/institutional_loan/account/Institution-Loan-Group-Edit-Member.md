---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/account/Institution-Loan-Group-Edit-Member
api_type: Account
updated_at: 2026-01-15T23:50:26.708049
---

# Add Collateral Accounts  (TRADE)

## API Description[​](/docs/institutional_loan/account/Institution-Loan-Group-Edit-Member#api-description "Direct link to API Description")

Add new collateral accounts for the Risk Unit. This endpoint is accessible only with the parent account API key.

## HTTP Request[​](/docs/institutional_loan/account/Institution-Loan-Group-Edit-Member#http-request "Direct link to HTTP Request")

POST /sapi/v1/margin/loan-group/edit-member

## Request Weight[​](/docs/institutional_loan/account/Institution-Loan-Group-Edit-Member#request-weight "Direct link to Request Weight")

1000(UID)

## Request Parameters[​](/docs/institutional_loan/account/Institution-Loan-Group-Edit-Member#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
groupId| LONG| YES|   
subEmail| STRING| YES|   
enableSpot| BOOLEAN| YES| TRUE, FALSE  
enableMargin| BOOLEAN| YES| TRUE, FALSE  
  
  * For the credit account, the enableMargin should always be TRUE.

  * Collateral sub-accounts can be added to the Risk Unit but cannot be removed. Therefore, the enableSpot or enableMargin parameters cannot be switched from TRUE to FALSE once the sub-account is activated in the Risk Unit. If you need to remove credit or collateral sub-accounts from the Risk Unit, please contact the Binance Margin team for support.




## Response Example[​](/docs/institutional_loan/account/Institution-Loan-Group-Edit-Member#response-example "Direct link to Response Example")
    
    
    {  
      "status": 0  
    }

---

# 添加抵押子账户 (USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Edit-Member#接口描述 "接口描述的直接链接")

添加风险单位的抵押子账户，仅支持母账户调用该接口。

## HTTP 请求[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Edit-Member#http-请求 "HTTP 请求的直接链接")

POST /sapi/v1/margin/loan-group/edit-member

## 请求权重[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Edit-Member#请求权重 "请求权重的直接链接")

1000(UID)

## 请求参数[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Edit-Member#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
groupId| LONG| YES|   
  
subEmail| STRING| YES|   
  
enableSpot| BOOLEAN| YES| TRUE, FALSE  
enableMargin| BOOLEAN| YES| TRUE, FALSE  
  
  * 如果参数subEmail 为信用贷账号，则参数enableMargin必须设置为TRUE，不能设置为FALSE。

  * 参数enableSpot 和 enableMargin 只能从FALSE变更到TRUE，不能从TRUE变更到FALSE。即不能通过该接口移除抵押子账户，若想要移除抵押子账户，需联系杠杆团队。




## 响应示例[​](/docs/zh-CN/institutional_loan/account/Institution-Loan-Group-Edit-Member#响应示例 "响应示例的直接链接")
    
    
    {  
      "status": 0  
    }