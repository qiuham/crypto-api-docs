---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-sol-staking-get-balance
anchor_id: financial-product-sol-staking-get-balance
api_type: API
updated_at: 2026-01-15T23:28:05.149253
---

# GET / Balance

The balance is summarized all OKSOL assets (including assets in redeeming) in account.

#### Rate Limit: 6 requests per second

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/staking-defi/sol/balance`

> Request Example
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### Request Parameters

None

> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
ccy | String | Currency, e.g. `OKSOL`  
amt | String | Currency amount  
latestInterestAccrual | String | Latest interest accrual  
totalInterestAccrual | String | Total interest accrual

---

# GET / 获取余额

该余额是一个汇总账户OKSOL资产（含赎回中）的实时数据。

#### 限速：6 次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP 请求

`GET /api/v5/finance/staking-defi/sol/balance`

> 请求示例
    
    
    GET /api/v5/finance/staking-defi/sol/balance
    
    
    
    
    import okx.Finance.SolStaking as SolStaking
    
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    StackingAPI = SolStaking.SolStakingAPI(apikey, secretkey, passphrase, False, flag)
    
    result = StackingAPI.sol_balance()
    print(result)
    

#### 请求参数

None

> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "amt": "0.01100012",
                "ccy": "OKSOL",
                "latestInterestAccrual": "0.00000012",
                "totalInterestAccrual": "0.00000012"
            }
        ],
        "msg": ""
    }
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
ccy | String | 币种名称，如 `OKSOL`  
amt | String | 币种数量  
latestInterestAccrual | String | 最近收益  
totalInterestAccrual | String | 历史总收益