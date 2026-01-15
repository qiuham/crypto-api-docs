---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-get-maximum-collateral-redeem-amount
anchor_id: financial-product-flexible-loan-get-maximum-collateral-redeem-amount
api_type: API
updated_at: 2026-01-15T23:28:05.598754
---

# GET / Maximum collateral redeem amount

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount("USDT")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | Yes | Collateral currency, e.g. `USDT`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
ccy | String | Collateral currency, e.g. `USDT`  
maxRedeemAmt | String | Maximum collateral redeem amount

---

# GET / 抵押物最大可赎回数量

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/max-collateral-redeem-amount?ccy=USDT
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.max_collateral_redeem_amount("USDT")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 是 | 抵押物币种，如 `USDT`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "ccy": "USDT",
                "maxRedeemAmt": "1"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
ccy | String | 抵押物币种，如 `USDT`  
maxRedeemAmt | String | 抵押物最大可赎回数量