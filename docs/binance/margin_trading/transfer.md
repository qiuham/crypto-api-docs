---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/transfer
api_type: REST
updated_at: 2026-01-15T23:49:00.041766
---

# Get Cross Margin Transfer History (USER_DATA)

## API Description[​](/docs/margin_trading/transfer#api-description "Direct link to API Description")

Get Cross Margin Transfer History

## HTTP Request[​](/docs/margin_trading/transfer#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/transfer`

## Request Weight[​](/docs/margin_trading/transfer#request-weight "Direct link to Request Weight")

**1(IP)**

## Request Parameters[​](/docs/margin_trading/transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
type| STRING| NO| Transfer Type: ROLL_IN, ROLL_OUT  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| Currently querying page. Start from 1. Default:1  
size| LONG| NO| Default:10 Max:100  
isolatedSymbol| STRING| NO| Symbol in Isolated Margin  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * Response in descending order
  * The max interval between `startTime` and `endTime` is 30 days.
  * Returns data for last 7 days by default



## Response Example[​](/docs/margin_trading/transfer#response-example "Direct link to Response Example")
    
    
    {  
      "rows": [  
        {  
          "amount": "0.10000000",  
          "asset": "BNB",  
          "status": "CONFIRMED",  
          "timestamp": 1566898617,  
          "txId": 5240372201,  
          "type": "ROLL_IN",  
          "transFrom": "SPOT", //SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
          "transTo": "ISOLATED_MARGIN",//SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
        },  
        {  
          "amount": "5.00000000",  
          "asset": "USDT",  
          "status": "CONFIRMED",  
          "timestamp": 1566888436,  
          "txId": 5239810406,  
          "type": "ROLL_OUT",  
          "transFrom": "ISOLATED_MARGIN",//SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
          "transTo": "ISOLATED_MARGIN", //SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
          "fromSymbol": "BNBUSDT",  
          "toSymbol": "BTCUSDT"  
        },  
        {  
          "amount": "1.00000000",  
          "asset": "EOS",  
          "status": "CONFIRMED",  
          "timestamp": 1566888403,  
          "txId": 5239808703,  
          "type": "ROLL_IN"  
        }  
      ],  
      "total": 3  
    }  
    

**Error Code Description:**

  * **EXCEED_MAX_ROLLOUT**

Sometimes, your collateral margin level may be too low to allow a transfer out of your account. You will get an error response {"code":-3020,"msg":"Transfer out amount exceeds max amount."}. To resolve it, you can reduce your outstanding debt or add more assets to meet the required margin level for the transfer.

  * **PREPAREDELIST_CANT_TRANSFER_IN**

This error {“code”: -3065, “msg”: “%s has been scheduled for delisting. You may only transfer up to %s %s, which is the amount of liabilities less any collateral already available.”} indicates that a specific asset is planned to be delisted. As a result, there are restrictions on how much of this asset you can transfer out of your account. When transferring the asset out of Binance, you will not be able to exceed the allowed amount

  * **NET_ASSET_MUST_LTE_RATIO**

This error {“code”:-21003, “msg”: ”Fail to retrieve margin assets.”} typically occurs when users send requests at a very high frequency. Because asset information updates need processing time, sending requests too frequently can cause failures or delayed responses.

We recommend that users maintain at least a 500 milliseconds (0.5 seconds) interval between each request. This interval allows the system enough time to process and update asset information, reducing errors or delays caused by high-frequency requests.

---

# 获取全仓杠杆划转历史 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/transfer#接口描述 "接口描述的直接链接")

获取全仓杠杆划转历史

## HTTP请求[​](/docs/zh-CN/margin_trading/transfer#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/transfer`

## 请求权重[​](/docs/zh-CN/margin_trading/transfer#请求权重 "请求权重的直接链接")

**1(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
type| STRING| NO| 划转类型: ROLL_IN, ROLL_OUT  
startTime| LONG| NO|   
endTime| LONG| NO|   
current| LONG| NO| 当前查询页。 从 1开始。 默认:1  
size| LONG| NO| 默认:10 最大:100  
isolatedSymbol| STRING| NO| 逐仓交易对，适用于逐仓查询  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 响应返回为降序排列。
  * 查询时间范围最大不得超过30天。
  * 若`startTime`和`endTime`没传，则默认返回最近7天数据



## 响应示例[​](/docs/zh-CN/margin_trading/transfer#响应示例 "响应示例的直接链接")
    
    
    {  
      "rows": [  
        {  
          "amount": "0.10000000",  
          "asset": "BNB",  
          "status": "CONFIRMED",  
          "timestamp": 1566898617,  
          "txId": 5240372201,  
          "type": "ROLL_IN",  
          "transFrom": "SPOT",//SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
          "transTo": "ISOLATED_MARGIN",//SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
        },  
        {  
          "amount": "5.00000000",  
          "asset": "USDT",  
          "status": "CONFIRMED",  
          "timestamp": 1566888436,  
          "txId": 5239810406,  
          "type": "ROLL_OUT",  
          "transFrom": "ISOLATED_MARGIN",//SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
          "transTo": "ISOLATED_MARGIN",//SPOT,FUTURES,FIAT,DELIVERY,MINING,ISOLATED_MARGIN,FUNDING,MOTHER_SPOT,OPTION,SUB_SPOT,SUB_MARGIN,CROSS_MARGIN  
          "fromSymbol": "BNBUSDT",  
          "toSymbol": "BTCUSDT"  
        },  
        {  
          "amount": "1.00000000",  
          "asset": "EOS",  
          "status": "CONFIRMED",  
          "timestamp": 1566888403,  
          "txId": 5239808703,  
          "type": "ROLL_IN"  
        }  
      ],  
      "total": 3  
    }  
    

**常见错误代码： **

  * **EXCEED_MAX_ROLLOUT** 由于您的质押风险率过低，系统会拒绝您从账户转出资金，并返回错误提示 {"code":-3020,"msg":"Transfer out amount exceeds max amount."}。此时，您可以通过降低未偿还的借款额度或增加更多资产来提升质押风险率，从而满足转账要求。
  * **PREPAREDELIST_CANT_TRANSFER_IN** 错误提示 {“code”: -3065, “msg”: “%s has been scheduled for delisting. You may only transfer up to %s %s, which is the amount of liabilities less any collateral already available.”} 出现在某个资产即将被下架，因此对该资产的转出额度有限制。您在将该资产从币安转出时，不能超过平台规定的最大转出数量。
  * **NET_ASSET_MUST_LTE_RATIO** 错误提示 {“code”:-21003, “msg”: ”Fail to retrieve margin assets.”} 通常出现在用户请求频率过快的情况。因为资产信息的更新需要一定时间，频繁发起请求可能会导致请求失败或响应延迟。 建议用户在每次请求之间保持至少 500 毫秒（0.5秒）的间隔，这样系统才能有充足时间处理和更新资产数据，降低因高频请求导致的错误和延迟。