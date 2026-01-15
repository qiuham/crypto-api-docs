---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow
api_type: Account
updated_at: 2026-01-15T23:48:17.800597
---

# Query Cross Isolated Margin Capital Flow (USER_DATA)

## API Description[​](/docs/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#api-description "Direct link to API Description")

Query Cross Isolated Margin Capital Flow

## HTTP Request[​](/docs/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/capital-flow`

## Request Weight[​](/docs/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#request-weight "Direct link to Request Weight")

**100(IP)**

## Request Parameters[​](/docs/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
asset| STRING| NO|   
symbol| STRING| NO| 查询逐仓数据时必填  
type| STRING| NO|   
startTime| LONG| NO| 只支持查询最近90天的数据  
endTime| LONG| NO|   
fromId| LONG| NO| 如设置fromId, 将返回id > fromId的数据。否则将返回最新数据  
limit| LONG| NO| 每次返回的数据条数限制。默认 500; 最大 1000.  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * Only supports querying the data of the last 90 days
  * The time between startTime and endTime cannot be longer than 7 days.
  * If fromId is set, the data with id > fromId will be returned. Otherwise the latest data will be returned
  * To query isolated data, Symbol needs to be entered.
  * Supported types: 
    * TRANSFER("Transfer")
    * BORROW("Borrow")
    * REPAY("Repay")
    * BUY_INCOME("Buy-Trading Income")
    * BUY_EXPENSE("Buy-Trading Expense")
    * SELL_INCOME("Sell-Trading Income")
    * SELL_EXPENSE("Sell-Trading Expense")
    * TRADING_COMMISSION("Trading Commission")
    * BUY_LIQUIDATION("Buy by Liquidation")
    * SELL_LIQUIDATION("Sell by Liquidation")
    * REPAY_LIQUIDATION("Repay by Liquidation")
    * OTHER_LIQUIDATION("Other Liquidation")
    * LIQUIDATION_FEE("Liquidation Fee")
    * SMALL_BALANCE_CONVERT("Small Balance Convert")
    * COMMISSION_RETURN("Commission Return")
    * SMALL_CONVERT("Small Convert")



## Response Example[​](/docs/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#response-example "Direct link to Response Example")
    
    
    [  
      {   
        "id": 123456,  
        "tranId": 123123,  
        "timestamp": 1691116657000,  
        "asset": "USDT",  
        "symbol": "BTCUSDT",  
        "type": "BORROW",  
        "amount": "101"  
      },  
      {  
        "id": 123457,  
        "tranId": 123124,  
        "timestamp": 1691116658000,  
        "asset": "BTC",  
        "symbol": "BTCUSDT",  
        "type": "REPAY",  
        "amount": "10"  
      }  
    ]

---

# 查询全仓/逐仓资金流水 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#接口描述 "接口描述的直接链接")

查询全仓/逐仓资金流水

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/capital-flow`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#请求权重 "请求权重的直接链接")

**100(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
asset| STRING| NO|   
symbol| STRING| NO| 查询逐仓数据时必填  
type| STRING| NO|   
startTime| LONG| NO| 只支持查询最近90天的数据  
endTime| LONG| NO|   
fromId| LONG| NO| 如设置fromId, 将返回id > fromId的数据。否则将返回最新数据  
limit| LONG| NO| 每次返回的数据条数限制。默认 500; 最大 1000.  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
  * 只支持查询最近90天的数据
  * startTime 和 endTime 的最大间隔为7天
  * 如设置`fromId`, 将返回`id` > `fromId`的数据。否则将返回最新订单。
  * 查询逐仓数据，需要输入`symbol`
  * 支持的type: 
    * TRANSFER("Transfer", "转账")
    * BORROW("Borrow", "借款")
    * REPAY("Repay", "还款")
    * BUY_INCOME("Buy-Trading Income", "买单-交易收入")
    * BUY_EXPENSE("Buy-Trading Expense", "买单-交易支出")
    * SELL_INCOME("Sell-Trading Income", "卖单-交易收入")
    * SELL_EXPENSE("Sell-Trading Expense", "卖单-交易支出")
    * TRADING_COMMISSION("Trading Commission", "交易手续费")
    * BUY_LIQUIDATION("Buy by Liquidation", "强平买入")
    * SELL_LIQUIDATION("Sell by Liquidation", "强平卖出")
    * REPAY_LIQUIDATION("Repay by Liquidation", "强平还款")
    * OTHER_LIQUIDATION("Other Liquidation", "其他强平")
    * LIQUIDATION_FEE("Liquidation Fee", "强平清算费用")
    * SMALL_BALANCE_CONVERT("Small Balance Convert", "小额兑换")
    * COMMISSION_RETURN("Commission Return", "手续费返还")
    * SMALL_CONVERT("Small Convert", "强平小额转换")



## 响应示例[​](/docs/zh-CN/margin_trading/account/Query-Cross-Isolated-Margin-Capital-Flow#响应示例 "响应示例的直接链接")
    
    
    [  
      {   
        "id": 123456,  
        "tranId": 123123,  
        "timestamp": 1691116657000,  
        "asset": "USDT",  
        "symbol": "BTCUSDT",  
        "type": "BORROW",  
        "amount": "101"  
      },  
      {  
        "id": 123457,  
        "tranId": 123124,  
        "timestamp": 1691116658000,  
        "asset": "BTC",  
        "symbol": "BTCUSDT",  
        "type": "REPAY",  
        "amount": "10"  
      }  
    ]