---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Trade-List
api_type: Trading
updated_at: 2026-01-15T23:48:59.739618
---

# Query Margin Account's Trade List (USER_DATA)

## API Description[​](/docs/margin_trading/trade/Query-Margin-Account-Trade-List#api-description "Direct link to API Description")

Query Margin Account's Trade List

## HTTP Request[​](/docs/margin_trading/trade/Query-Margin-Account-Trade-List#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/myTrades`

## Request Weight[​](/docs/margin_trading/trade/Query-Margin-Account-Trade-List#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/trade/Query-Margin-Account-Trade-List#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| TradeId to fetch from. Default gets most recent trades.  
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * If fromId is set, it will get trades >= that fromId. Otherwise the trades within 24 hours are returned.
  * Less than 24 hours between startTime and endTime.



## Response Example[​](/docs/margin_trading/trade/Query-Margin-Account-Trade-List#response-example "Direct link to Response Example")
    
    
    [  
    	{  
    		"commission": "0.00006000",  
    		"commissionAsset": "BTC",  
    		"id": 34,  
    		"isBestMatch": true,  
    		"isBuyer": false,  
    		"isMaker": false,  
    		"orderId": 39324,  
    		"price": "0.02000000",  
    		"qty": "3.00000000",  
    		"symbol": "BNBBTC",  
    		"isIsolated": false,  
    		"time": 1561973357171  
    	}  
    ]

---

# Query Margin Account's Trade List (USER_DATA)

## API Description[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Trade-List#api-description "API Description的直接链接")

Query Margin Account's Trade List

## HTTP Request[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Trade-List#http-request "HTTP Request的直接链接")

GET `/sapi/v1/margin/myTrades`

## Request Weight[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Trade-List#request-weight "Request Weight的直接链接")

**10(IP)**

## Request Parameters[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Trade-List#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
isIsolated| STRING| NO| for isolated margin or not, "TRUE", "FALSE"，default "FALSE"  
orderId| LONG| NO|   
startTime| LONG| NO|   
endTime| LONG| NO|   
fromId| LONG| NO| TradeId to fetch from. Default gets most recent trades.  
limit| INT| NO| Default 500; max 1000.  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
  * If fromId is set, it will get trades >= that fromId. Otherwise the trades within 24 hours are returned.
  * Less than 24 hours between startTime and endTime.



## Response Example[​](/docs/zh-CN/margin_trading/trade/Query-Margin-Account-Trade-List#response-example "Response Example的直接链接")
    
    
    [  
    	{  
    		"commission": "0.00006000",  
    		"commissionAsset": "BTC",  
    		"id": 34,  
    		"isBestMatch": true,  
    		"isBuyer": false,  
    		"isMaker": false,  
    		"orderId": 39324,  
    		"price": "0.02000000",  
    		"qty": "3.00000000",  
    		"symbol": "BNBBTC",  
    		"isIsolated": false,  
    		"time": 1561973357171  
    	}  
    ]