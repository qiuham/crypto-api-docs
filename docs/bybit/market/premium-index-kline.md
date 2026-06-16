---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/premium-index-kline
api_type: Market Data
updated_at: 2026-06-16 19:49:36.407156
---

# Get Recent Public Trades

Query recent public trading history in Bybit.

> **Covers: Spot / USDT contract / USDC contract / Inverse contract / Option**

You can download archived historical trades from the [website](https://www.bybit.com/en/derivative-activity/history-data)

### HTTP Request

GET`/v5/market/recent-trade`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
[category](/docs/v5/enum#category)| **true**|  string| Product type. `spot`,`linear`,`inverse`,`option`  
[symbol](/docs/v5/enum#symbol)| false| string| Symbol name, like `BTCUSDT`, uppercase only 

  * **required** for spot/linear/inverse
  * optional for option

  
baseCoin| false| string| Base coin, uppercase only 

  * Apply to `option` **only**
  * If the field is not passed, return **BTC** data by default

  
optionType| false| string| Option type. `Call` or `Put`. Apply to `option` **only**  
limit| false| integer| Limit for data size per page 

  * `spot`: [1,60], default: `60`
  * others: [1,1000], default: `500`

  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
category| string| Products category  
list| array| Object  
> execId| string| Execution ID  
> symbol| string| Symbol name  
> price| string| Trade price  
> size| string| Trade size  
> side| string| Side of taker `Buy`, `Sell`  
> time| string| Trade time (ms)  
> isBlockTrade| boolean| Whether the trade is block trade  
> isRPITrade| boolean| Whether the trade is RPI trade  
> mP| string| Mark price, unique field for `option`  
> iP| string| Index price, unique field for `option`  
> mIv| string| Mark iv, unique field for `option`  
> iv| string| iv, unique field for `option`  
> seq| string| cross sequence  
[](/docs/api-explorer/v5/market/recent-trade)

* * *

### Request Example

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/recent-trade?category=spot&symbol=BTCUSDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_public_trade_history(  
        category="spot",  
        symbol="BTCUSDT",  
        limit=1,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetPublicRecentTrades(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var recentTrade = MarketDataRequest.builder().category(CategoryType.OPTION).symbol("ETH-30JUN23-2050-C").build();  
    client.getRecentTradeData(recentTrade, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getPublicTradingHistory({  
            category: 'spot',  
            symbol: 'BTCUSDT',  
            limit: 1,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "spot",  
            "list": [  
                {  
                    "execId": "2100000000007764263",  
                    "symbol": "BTCUSDT",  
                    "price": "16618.49",  
                    "size": "0.00012",  
                    "side": "Buy",  
                    "time": "1672052955758",  
                    "isBlockTrade": false,  
                    "isRPITrade": true,  
                    "seq":"123456"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672053054358  
    }

---

# 查詢平台最近成交歷史

獲取平台最近成交數據

> **覆蓋範圍: 現貨 / USDT永續 / USDT交割 / USDC永續 / USDC交割 / 反向合約 / 期權**

您可以從這個[地址](https://www.bybit.com/en/derivative-activity/history-data) 下載到歸檔的更多的歷史成交數據:

### HTTP請求

GET`/v5/market/recent-trade`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
[category](/docs/zh-TW/v5/enum#category)| **true**|  string| 產品類型. `spot`,`linear`,`inverse`,`option`  
[symbol](/docs/zh-TW/v5/enum#symbol)| false| string| 合約名稱

  * 現貨/期貨**必傳**
  * 期權選傳

  
baseCoin| false| string| 交易幣種. 僅`option`, 若不傳, 則默認返回BTC數據  
optionType| false| string| 期權類型. `Call` 或 `Put`. 僅`option`  
limit| false| integer| 每頁數量限制.

  * `spot`: [1,60], 默认: `60`.
  * others: [1,1000], 默認: `500`

  
  
### 響應參數

參數| 類型| 說明  
---|---|---  
category| string| 產品類型  
list| array| Object  
> execId| string| 成交id  
> symbol| string| 合約名稱  
> price| string| 成交價格  
> size| string| 成交數量  
> side| string| 吃單方向. `Buy`, `Sell`  
> time| string| 成交時間戳 (毫秒)  
> isBlockTrade| boolean| 成交類型是否為大宗交易  
> isRPITrade| boolean| 成交類型是否為RPI交易  
> mP| string| 標記價格, 期權的特有字段  
> iP| string| 指數價格, 期權的特有字段  
> mIv| string| 標記iv, 期權的特有字段  
> iv| string| iv, 期權的特有字段  
> seq| string| 撮合版本號  
[](/docs/zh-TW/api-explorer/v5/market/recent-trade)

* * *

### 請求示例

  * HTTP
  * Python
  * GO
  * Java
  * Node.js


    
    
    GET /v5/market/recent-trade?category=spot&symbol=BTCUSDT&limit=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(testnet=True)  
    print(session.get_public_trade_history(  
        category="spot",  
        symbol="BTCUSDT",  
        limit=1,  
    ))  
    
    
    
    import (  
        "context"  
        "fmt"  
        bybit "github.com/bybit-exchange/bybit.go.api"  
    )  
    client := bybit.NewBybitHttpClient("", "", bybit.WithBaseURL(bybit.TESTNET))  
    params := map[string]interface{}{"category": "linear", "symbol": "BTCUSDT"}  
    client.NewUtaBybitServiceWithParams(params).GetPublicRecentTrades(context.Background())  
    
    
    
    import com.bybit.api.client.domain.CategoryType;  
    import com.bybit.api.client.domain.market.*;  
    import com.bybit.api.client.domain.market.request.MarketDataRequest;  
    import com.bybit.api.client.service.BybitApiClientFactory;  
    var client = BybitApiClientFactory.newInstance().newAsyncMarketDataRestClient();  
    var recentTrade = MarketDataRequest.builder().category(CategoryType.OPTION).symbol("ETH-30JUN23-2050-C").build();  
    client.getRecentTradeData(recentTrade, System.out::println);  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
        testnet: true,  
    });  
      
    client  
        .getPublicTradingHistory({  
            category: 'spot',  
            symbol: 'BTCUSDT',  
            limit: 1,  
        })  
        .then((response) => {  
            console.log(response);  
        })  
        .catch((error) => {  
            console.error(error);  
        });  
    

### 響應示例
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "category": "spot",  
            "list": [  
                {  
                    "execId": "2100000000007764263",  
                    "symbol": "BTCUSDT",  
                    "price": "16618.49",  
                    "size": "0.00012",  
                    "side": "Buy",  
                    "time": "1672052955758",  
                    "isBlockTrade": false,  
                    "isRPITrade": true  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1672053054358  
    }