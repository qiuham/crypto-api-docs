---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#financial-product-flexible-loan-get-collateral-assets
anchor_id: financial-product-flexible-loan-get-collateral-assets
api_type: API
updated_at: 2026-01-15T23:28:05.539043
---

# GET / Collateral assets

Get collateral assets in funding account.  
  
#### Rate Limit: 5 requests per 2 seconds

#### Rate limit rule: User ID

#### Permission: Read

#### HTTP Request

`GET /api/v5/finance/flexible-loan/collateral-assets`

> Request Example
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API initialization
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # Production trading:0 , demo trading:1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets()
    print(result)
    

#### Request Parameters

**Parameters** | **Types** | **Required** | **Description**  
---|---|---|---  
ccy | String | No | Collateral currency, e.g. `BTC`  
  
> Response Example
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### Response Parameters

**Parameter** | **Type** | **Description**  
---|---|---  
assets | Array of objects | Collateral assets data  
> ccy | String | Currency, e.g. `BTC`  
> amt | String | Available amount  
> notionalUsd | String | Notional value in `USD`

---

# GET / 可抵押资产

获取可抵押资产信息（仅支持资金账户中的资产）  
  
#### 限速：5次/2s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/finance/flexible-loan/collateral-assets`

> 请求示例
    
    
    GET /api/v5/finance/flexible-loan/collateral-assets
    
    
    
    from okx.Finance import FlexibleLoan
    
    # API 初始化
    apikey = "YOUR_API_KEY"
    secretkey = "YOUR_SECRET_KEY"
    passphrase = "YOUR_PASSPHRASE"
    
    flag = "0"  # 实盘: 0, 模拟盘: 1
    
    flexibleLoanAPI = FlexibleLoan.FlexibleLoanAPI(apikey, secretkey, passphrase, False, flag)
    result = flexibleLoanAPI.collateral_assets()
    print(result)
    

#### 请求参数

参数 | 类型 | 是否必须 | 描述  
---|---|---|---  
ccy | String | 否 | 币种，如 `BTC`  
  
> 返回结果
    
    
    {
        "code": "0",
        "data": [
            {
                "assets": [
                    {
                        "amt": "1.7921483143067599",
                        "ccy": "BTC",
                        "notionalUsd": "158292.621793314105231"
                    },
                    {
                        "amt": "1.9400755578876945",
                        "ccy": "ETH",
                        "notionalUsd": "6325.6652712507628946"
                    },
                    {
                        "amt": "63.9795959720319628",
                        "ccy": "USDT",
                        "notionalUsd": "64.3650372635940345"
                    }
                ]
            }
        ],
        "msg": ""
    }
    

#### 返回参数

**参数名** | **类型** | **描述**  
---|---|---  
assets | Array of objects | 可抵押资产信息  
> ccy | String | 币种，如 `BTC`  
> amt | String | 可用数量  
> notionalUsd | String | 可抵押资产的美金价值