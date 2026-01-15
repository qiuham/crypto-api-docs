---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-get-loan-info
anchor_id: financial-product-flexible-loan-get-loan-info
api_type: API
updated_at: 2026-01-15T23:28:05.659989
---

# GET / Loan info

#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/loan-info`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
loanNotionalUsd | String | Loan value in `USD`  
loanData | Array of objects | Loan data  
> ccy | String | Loan currency, e.g. `USDT`  
> amt | String | Loan amount  
collateralNotionalUsd | String | Collateral value in `USD`  
collateralData | Array of objects | Collateral data  
> ccy | String | Collateral currency, e.g. `BTC`  
> amt | String | Collateral amount  
riskWarningData | Object | Risk warning data  
> instId | String | Liquidation instrument ID, e.g. `BTC-USDT`  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
> liqPx | String | Liquidation price  
The unit of the liquidation price is the quote currency of the instrument, e.g. `USDT` in `BTC-USDT`.  
This field is only valid when there is only one type of collateral and one type of borrowed currency. In other cases, it returns "".  
curLTV | String | Current LTV, e.g. `0.1` represents `10%`  
Note: LTV = Loan to Value  
marginCallLTV | String | Margin call LTV, e.g. `0.1` represents `10%`  
If your loan hits the margin call LTV, our system will automatically warn you that your loan is getting close to forced liquidation.  
liqLTV | String | Liquidation LTV, e.g. `0.1` represents `10%`  
If your loan reaches liquidation LTV, it'll trigger forced liquidation. When this happens, you'll lose access to your collateral and any repayments made.

---

# GET / 借贷信息

#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/loan-info`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/loan-info
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.loan_info()
    print(result)
    

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "collateralData": [
                    {
                        "amt": "0.0000097",
                        "ccy": "COMP"
                    },
                    {
                        "amt": "0.78",
                        "ccy": "STX"
                    },
                    {
                        "amt": "0.001",
                        "ccy": "DOT"
                    },
                    {
                        "amt": "0.05357864",
                        "ccy": "LUNA"
                    }
                ],
                "collateralNotionalUsd": "1.5078763",
                "curLTV": "0.5742",
                "liqLTV": "0.8374",
                "loanData": [
                    {
                        "amt": "0.86590608",
                        "ccy": "USDC"
                    }
                ],
                "loanNotionalUsd": "0.8661285",
                "marginCallLTV": "0.7374",
                "riskWarningData": {
                    "instId": "",
                    "liqPx": ""
                }
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
loanNotionalUsd | String | 借币资产美金价值  
loanData | Array of objects | 借币数据  
> ccy | String | 借贷币种  
> amt | String | 借贷数量  
collateralNotionalUsd | String | 抵押物美金价值  
collateralData | Array of objects | 抵押资产数据  
> ccy | String | 抵押币种  
> amt | String | 抵押数量  
riskWarningData | Object | 风险预警信息  
> instId | String | 清算交易产品，如 `BTC-USDT`  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
> liqPx | String | 清算价格  
清算价格的单位为交易产品的计价币，如 `BTC-USDT`中的`USDT`。  
仅当质押物和借币都只有一种时，该字段有效。其他情况返回""。  
curLTV | String | 当前质押率，如 `0.1`代表`10%`  
注：LTV(Loan-to-Value，贷款价值比)  
marginCallLTV | String | 预警质押率，如 `0.1`代表`10%`  
您的质押率达到预警质押率时，系统将会提示您当前质押率过高，即将触发强平。  
liqLTV | String | 强平质押率，如 `0.1`代表`10%`  
若您的借贷达到强平质押率并被强平，您将损失质押物及已完成的还款。