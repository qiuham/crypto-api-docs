---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-post-adjust-collateral
anchor_id: financial-product-flexible-loan-post-adjust-collateral
api_type: API
updated_at: 2026-01-15T23:28:05.628885
---

# POST / Adjust collateral

#### Rate Limit: 5 requests per 2 seconds  
  
#### Rate limit rule: User ID

#### Permission: Trade

#### HTTP Request

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> Request Example
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
type | String | Yes | Operation type  
`add`: Add collateral  
`reduce`: Reduce collateral  
collateralCcy | String | Yes | Collateral currency, e.g. `BTC`  
collateralAmt | String | Yes | Collateral amount  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### Response Parameters

code = `0` means your request has been accepted (It doesn't mean the request has been successfully handled.)

---

# POST / 调整抵押物

#### 限速：5次/2s  
  
#### 限速规则：User ID

#### 权限：交易

#### HTTP请求

`POST /api/v5/finance/flexible-loan/adjust-collateral`

> 请求示例
    
    
    POST /api/v5/finance/flexible-loan/adjust-collateral
    body
    {
        "type":"add",
        "collateralCcy": "BTC",
        "collateralAmt": "0.1"
    }
    
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.adjust_collateral(type="add", collateralCcy="USDT", collateralAmt="1")
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
type | String | 是 | 操作类型  
`add`：补充抵押物  
`reduce`：减少抵押物  
collateralCcy | String | 是 | 抵押物币种，如 `BTC`  
collateralAmt | String | 是 | 抵押物数量  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
        ],
        "msg": ""
    }
    

#### 返回参数

code = `0` 代表请求已被接受(不代表处理成功)