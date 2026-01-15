---
exchange: binance
source_url: https://developers.binance.com/docs/algo/spot-algo/Query-Historical-Algo-Orders
api_type: REST
updated_at: 2026-01-15T23:49:14.371456
---

# Query Historical Algo Orders(USER_DATA)

## API Description[​](/docs/algo/spot-algo/Query-Historical-Algo-Orders#api-description "Direct link to API Description")

Get all historical SPOT TWAP orders

## HTTP Request[​](/docs/algo/spot-algo/Query-Historical-Algo-Orders#http-request "Direct link to HTTP Request")

GET `/sapi/v1/algo/spot/historicalOrders`

## Request Weight(IP)[​](/docs/algo/spot-algo/Query-Historical-Algo-Orders#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/algo/spot-algo/Query-Historical-Algo-Orders#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| NO| Trading symbol eg. BTCUSDT  
side| ENUM| NO| BUY or SELL  
startTime| LONG| NO| in milliseconds eg.1641522717552  
endTime| LONG| NO| in milliseconds eg.1641522526562  
page| INT| NO| Default is 1  
pageSize| INT| NO| MIN 1, MAX 100; Default 100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/algo/spot-algo/Query-Historical-Algo-Orders#response-example "Direct link to Response Example")
    
    
    {  
        "total": 1,  
        "orders": [  
            {  
                "algoId": 14518,  
                "symbol": "BNBUSDT",  
                "side": "BUY",  
                "totalQty": "100.00",  
                "executedQty": "0.00",  
                "executedAmt": "0.00000000",  
                "avgPrice": "0.000",  
                "clientAlgoId": "acacab56b3c44bef9f6a8f8ebd2a8408",  
                "bookTime": 1649757019503,  
                "endTime": 1649757088101,  
                "algoStatus": "CANCELLED",  
                "algoType": "VP",  
                "urgency": "LOW"  
            }  
        ]  
    }

---

# 查询历史策略订单(USER_DATA)

## 接口描述[​](/docs/zh-CN/algo/spot-algo/Query-Historical-Algo-Orders#接口描述 "接口描述的直接链接")

查询现货TWAP历史订单

## HTTP请求[​](/docs/zh-CN/algo/spot-algo/Query-Historical-Algo-Orders#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/algo/spot/historicalOrders`

## 请求权重(IP)[​](/docs/zh-CN/algo/spot-algo/Query-Historical-Algo-Orders#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/algo/spot-algo/Query-Historical-Algo-Orders#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| NO| 交易对 eg. BTCUSDT  
side| ENUM| NO| BUY 或者 SELL  
startTime| LONG| NO| 毫秒级时间戳 eg.1641522717552  
endTime| LONG| NO| 毫秒级时间戳 eg.1641522526562  
page| INT| NO| 默认 1  
pageSize| INT| NO| 最小 1, 最大 100; 默认 100  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/algo/spot-algo/Query-Historical-Algo-Orders#响应示例 "响应示例的直接链接")
    
    
    {  
        "total": 1,  
        "orders": [  
            {  
                "algoId": 14518,      //策略订单ID  
                "symbol": "BNBUSDT",  //交易对  
                "side": "BUY",        //买卖方向  
                "totalQty": "100.00",    //总共下单数量  
                "executedQty": "0.00",   //执行数量  
                "executedAmt": "0.00000000",  //执行价值  
                "avgPrice": "0.000",          //平均价格  
                "clientAlgoId": "acacab56b3c44bef9f6a8f8ebd2a8408",  //用户自定义策略订单ID  
                "bookTime": 1649757019503,    //用户下单时间  
                "endTime": 1649757088101,     //结束时间  
                "algoStatus": "CANCELLED",    //策略订单状态  
                "algoType": "VP",             //策略订单类型  
                "urgency": "LOW"              //执行速率  
            }  
        ]  
    }