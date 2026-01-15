---
exchange: binance
source_url: https://developers.binance.com/docs/institutional_loan/account
api_type: Account
updated_at: 2026-01-15T23:50:26.586341
---

# Query Risk Unit Details (USER_DATA)

## API Description[​](/docs/institutional_loan/account#api-description "Direct link to API Description")

Retrieve Institutional loan risk unit details. This endpoint can be accessed using the API key from either the parent or the credit accounts.

Parent Account:

  * If no groupId is provided, you will query all risk units
  * If the groupId is provided, it will only query that single risk unit.



Credit Account:

  * Only the risk unit connected to that credit account will be queried



Other Accounts:

  * LTV details cannot be queried, no results were returned.



## HTTP Request[​](/docs/institutional_loan/account#http-request "Direct link to HTTP Request")

**GET** `/sapi/v1/margin/loan-group/ltv-details`

## Request Weight[​](/docs/institutional_loan/account#request-weight "Direct link to Request Weight")

**200(IP)**

## Request Parameters[​](/docs/institutional_loan/account#request-parameters "Direct link to Request Parameters")

**Name**| **Type**| **Mandatory**| **Description**  
---|---|---|---  
**groupId**| **LONG**| **NO**|   
  
## Response Example[​](/docs/institutional_loan/account#response-example "Direct link to Response Example")
    
    
    [ {  
        "groupId": 1,  
        "parentEmail": "andrew.kemmer001@test.com",  
        "creditEmail": "tst20241120@test.com",  
        "updateTime": 1752137105623,  
        "ltv": "0.592",  
        "totalNetEquity": "26.35196946",  
        "totalMaintenanceMargin": "0.50106177",  
        "totalLiability": "15.30718771",  
        "parentAccountFrozenAmount": "8.18753688",  
        "maxTransferOutAmount": "0",  
        "maxAllowedBorrowLimit": "16.32397222",  
        "liabilities": [  
          {  
            "assetName": "USDT",  
            "principal": "15.30718771",  
            "interest": "0"  
          } ],  
        "collateralAccounts": [  
          {  
            "email": "collateral001@test.com",  
            "type": "COLLATERAL",  
            "wallets": [  
              {  
                "accountType": "SPOT",  
                "netEquity": "5",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "CROSS_MARGIN",  
                "netEquity": "4.98938226",  
                "maintainMargin": "0.50106177"  
              } ] },  
          {  
            "email": "collateral003@test.com",  
            "type": "COLLATERAL",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "5.4284319",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "CROSS_MARGIN",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              } ] },  
          {  
            "email": "CREDIT20241120@test.com",  
            "type": "CREDIT",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "PORTFOLIO_MARGIN",  
                "netEquity": "4.93362203",  
                "maintainMargin": "0"  
              }] },  
          {  
            "email": "collateral004l@test.com",  
            "type": "COLLATERAL",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "PORTFOLIO_MARGIN",  
                "netEquity": "1.00053327",  
                "maintainMargin": "0"  
              } ] },  
          {  
            "email": "collatera005@test.com",  
            "type": "COLLATERAL",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "5",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "CROSS_MARGIN",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              } ] }  ] }   
    ]  
    

## Response detail description:[​](/docs/institutional_loan/account#response-detail-description "Direct link to Response detail description:")

Parameter| Type| Description  
---|---|---  
groupId| Long| Risk unit unique identifier  
parentEmail| String| Parent account registered email  
creditEmail| String| Credit account registered email  
updateTime| Long| Last update timestamp (milliseconds)  
ltv| String| Loan-to-Value Ratio  
  
*_The LTV ratio is calculated using real-time parameters captured at the moment the API is called.. Depending on market volatility, LTV ratio may fluctuate, It is recommended that users re-query the API endpoint or perform manual LTV recalculation to ensure accuracy._  
totalNetEquity| String| ∑Equity in all PM sub account + ( ∑Collateral Value - ∑(Liability + Interest) in all Cross Margin account + Free accepted tokens in spot  
totalMaintenanceMargin| String| Aggregated Maintenance Margin  
totalLiability| String| Outstanding Loan Principal + Outstanding Loan Interest  
liabilities| Object Array| Liabilities details  
→ assetName| String| Asset name  
→ principal| String| Outstanding loan principal amount  
→ interest| String| Outstanding loan interest  
collateralAccounts| Object Array| Risk group sub account details  
→ email| String| Collateral account registered email  
→ type| String| Credit or Collateral Account  
→ wallets| Object Array| Wallet details  
→ → accountType| String| Wallet type  
→ → netEquity| String| Net equity in wallet  
→ → maintainMargin| String| Maintenance margin required

---

# 查询风险单元详情(USER_DATA)

## 接口描述[​](/docs/zh-CN/institutional_loan/account#接口描述 "接口描述的直接链接")

查询机构贷风险单位详情，母账户和借贷账户均可调用该接口。

  * 母账户：

    * 当未提供 groupId 时，可以查询所有风险单位详情。
    * 当提供特定 groupId 时，可以查询单个风险单位详情。
  * 信用账户：

    * 仅支持查询与该借贷账户绑定的风险单位详情。
  * 其他账户：

    * 无法查询LTV详情，无结果返回。



## HTTP请求[​](/docs/zh-CN/institutional_loan/account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/loan-group/ltv-details`

## 请求权重[​](/docs/zh-CN/institutional_loan/account#请求权重 "请求权重的直接链接")

**200(IP)**

## 请求参数[​](/docs/zh-CN/institutional_loan/account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
groupId| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/institutional_loan/account#响应示例 "响应示例的直接链接")
    
    
    [ {  
        "groupId": 1,  
        "parentEmail": "andrew.kemmer001@test.com",  
        "creditEmail": "tst20241120@test.com",  
        "updateTime": 1752137105623,  
        "ltv": "0.592",  
        "totalNetEquity": "26.35196946",  
        "totalMaintenanceMargin": "0.50106177",  
        "totalLiability": "15.30718771",  
        "parentAccountFrozenAmount": "8.18753688",  
        "maxTransferOutAmount": "0",  
        "maxAllowedBorrowLimit": "16.32397222",  
        "liabilities": [  
          {  
            "assetName": "USDT",  
            "principal": "15.30718771",  
            "interest": "0"  
          } ],  
        "collateralAccounts": [  
          {  
            "email": "collateral001@test.com",  
            "type": "COLLATERAL",  
            "wallets": [  
              {  
                "accountType": "SPOT",  
                "netEquity": "5",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "CROSS_MARGIN",  
                "netEquity": "4.98938226",  
                "maintainMargin": "0.50106177"  
              } ] },  
          {  
            "email": "collateral003@test.com",  
            "type": "COLLATERAL",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "5.4284319",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "CROSS_MARGIN",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              } ] },  
          {  
            "email": "CREDIT20241120@test.com",  
            "type": "CREDIT",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "PORTFOLIO_MARGIN",  
                "netEquity": "4.93362203",  
                "maintainMargin": "0"  
              }] },  
          {  
            "email": "collateral004l@test.com",  
            "type": "COLLATERAL",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "PORTFOLIO_MARGIN",  
                "netEquity": "1.00053327",  
                "maintainMargin": "0"  
              } ] },  
          {  
            "email": "collatera005@test.com",  
            "type": "COLLATERAL",  
            "wallets": [ {  
                "accountType": "SPOT",  
                "netEquity": "5",  
                "maintainMargin": "0"  
              },  
              {  
                "accountType": "CROSS_MARGIN",  
                "netEquity": "0",  
                "maintainMargin": "0"  
              } ] }  ] }   
    ]  
    

响应信息详解：

参数| 类型| 描述  
---|---|---  
groupId| Long| 唯一风险单位标识符  
parentEmail| String| 母账户注册邮箱  
creditEmail| String| 机构贷子账户注册邮箱  
updateTime| Long| 最后更新时间戳（毫秒）  
ltv| String| 贷款价值比 (Loan-to-Value Ratio)  
  
*_LTV 比率使用 API 调用时刻捕获的实时参数计算得出。根据市场波动情况，LTV 比率可能会波动，建议用户重新查询或手动重新计算 LTV 以确保准确性。_  
totalNetEquity| String| Σ所有统一账户子账户抵押品权益 + Σ 抵押品价值 - Σ 全仓杠杆账户（负债 + 利息） + 现货可用资产  
totalMaintenanceMargin| String| 维持保证金总额  
totalLiability| String| 未偿还贷款本金 + 未偿还贷款利息  
liabilities| Object Array| 负债详情  
→ assetName| String| 币种名称  
→ principal| String| 未偿还贷款本金  
→ interest| String| 未偿还利息  
collateralAccounts| Object Array| 风险单位子账户详情  
→ email| String| 抵押子账户绑定邮箱  
→ type| String| 类型，枚举 放贷子账户/抵押子账户  
→ wallets| Object Array| 账户详情  
→ → accountType| String| 账户类型  
→ → netEquity| String| 账户净资产  
→ → maintainMargin| String| 维持保证金