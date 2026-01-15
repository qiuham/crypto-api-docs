---
exchange: okx
source_url: https://www.okx.com/docs-v5/en/#order-book-trading-trade-get-account-rate-limit
anchor_id: order-book-trading-trade-get-account-rate-limit
api_type: API
updated_at: 2026-01-15T23:27:52.968706
---

# GET / Account rate limit

Get account rate limit related information.   

Only new order requests and amendment order requests will be counted towards this limit. For batch order requests consisting of multiple orders, each order will be counted individually.   

For details, please refer to [Fill ratio based sub-account rate limit](/docs-v5/en/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit)

#### Rate Limit: 1 request per second

#### Rate limit rule: User ID

#### HTTP Request

`GET /api/v5/trade/account-rate-limit`

> Request Example
    
    
    # Get the account rate limit
    GET /api/v5/trade/account-rate-limit
    
    

#### Request Parameters

None

> Response Example
    
    
    {
       "code":"0",
       "data":[
          {
             "accRateLimit":"2000",
             "fillRatio":"0.1234",
             "mainFillRatio":"0.1234",
             "nextAccRateLimit":"2000",
             "ts":"123456789000"
          }
       ],
       "msg":""
    }
    
    

#### Response Parameters

Parameter | Type | Description  
---|---|---  
fillRatio | String | Sub account fill ratio during the monitoring period   
Applicable for users with trading fee level >= VIP 5 and return "" for others   
For accounts with no trading volume during the monitoring period, return "0". For accounts with trading volume but no order count due to our counting logic, return "9999".  
mainFillRatio | String | Master account aggregated fill ratio during the monitoring period   
Applicable for users with trading fee level >= VIP 5 and return "" for others   
For accounts with no trading volume during the monitoring period, return "0"  
accRateLimit | String | Current sub-account rate limit per two seconds  
nextAccRateLimit | String | Expected sub-account rate limit (per two seconds) in the next period   
Applicable for users with trading fee level >= VIP 5 and return "" for others  
ts | String | Data update time   
For users with trading fee level >= VIP 5, the data will be generated at 08:00 am (UTC)   
For users with trading fee level < VIP 5, return the current timestamp

---

# GET / 获取账户限速

获取账户限速相关信息  

仅有新订单及修改订单请求会被计入此限制。对于包含多个订单的批量请求，每个订单将被单独计数。  

更多细节，请见 [基于成交比率的子账户限速](/docs-v5/zh/#overview-rate-limits-fill-ratio-based-sub-account-rate-limit)

#### 限速：1次/s

#### 限速规则：User ID

#### 权限：读取

#### HTTP请求

`GET /api/v5/trade/account-rate-limit`

> 请求示例
    
    
    # 获取账户限速相关信息
    GET /api/v5/trade/account-rate-limit
    
    

#### 请求参数

None

> 返回结果
    
    
    {
       "code":"0",
       "data":[
          {
             "accRateLimit":"2000",
             "fillRatio":"0.1234",
             "mainFillRatio":"0.1234",
             "nextAccRateLimit":"2000",
             "ts":"123456789000"
          }
       ],
       "msg":""
    }
    
    

#### 返回参数

参数名 | 类型 | 描述  
---|---|---  
fillRatio | String | 监测期内子账户的成交比率   
适用于交易费等级 >= VIP 5的用户，其余用户返回""   
对于监测期内没有交易量的账户，返回"0"。对于监测期内有交易量，但没有订单操作数的用户，返回"9999"。  
mainFillRatio | String | 监测期内母账户合计成交比率   
适用于交易费等级 >= VIP 5的用户，其余用户返回""   
对于监测期内没有交易量的账户，返回"0"  
accRateLimit | String | 当前子账户交易限速（每两秒）  
nextAccRateLimit | String | 预计下一周期子账户交易限速（每两秒）  
适用于交易费等级 >= VIP 5的用户，其余用户返回""  
ts | String | 数据更新时间   
对于交易费等级>= VIP 5的用户，数据将于每日16:00（UTC+8）生成   
对于交易费等级 < VIP 5的用户，返回当前时间戳