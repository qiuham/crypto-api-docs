---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-requests
api_type: WebSocket
updated_at: 2026-01-15T23:37:13.667911
---

# General requests

### Test connectivity[​](/docs/binance-spot-api-docs/websocket-api/general-requests#test-connectivity "Direct link to Test connectivity")
    
    
    {  
        "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",  
        "method": "ping"  
    }  
    

Test connectivity to the WebSocket API.

**Note:** You can use regular WebSocket ping frames to test connectivity as well, WebSocket API will respond with pong frames as soon as possible. `ping` request along with `time` is a safe way to test request-response handling in your application.

**Weight:** 1

**Parameters:** NONE

**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",  
        "status": 200,  
        "result": {},  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

### Check server time[​](/docs/binance-spot-api-docs/websocket-api/general-requests#check-server-time "Direct link to Check server time")
    
    
    {  
        "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",  
        "method": "time"  
    }  
    

Test connectivity to the WebSocket API and get the current server time.

**Weight:** 1

**Parameters:** NONE

**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",  
        "status": 200,  
        "result": {  
            "serverTime": 1656400526260  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

### Exchange information[​](/docs/binance-spot-api-docs/websocket-api/general-requests#exchange-information "Direct link to Exchange information")
    
    
    {  
        "id": "5494febb-d167-46a2-996d-70533eb4d976",  
        "method": "exchangeInfo",  
        "params": {  
            "symbols": ["BNBBTC"]  
        }  
    }  
    

Query current exchange trading rules, rate limits, and symbol information.

**Weight:** 20

**Parameters:**

Name | Type | Mandatory | Description  
---|---|---|---  
`symbol` | STRING | NO | Describe a single symbol  
`symbols` | ARRAY of STRING | Describe multiple symbols  
`permissions` | ARRAY of STRING | Filter symbols by permissions  
`showPermissionSets` | BOOLEAN | Controls whether the content of the `permissionSets` field is populated or not. Defaults to `true`.  
`symbolStatus` | ENUM | Filters for symbols that have this `tradingStatus`.  
  
Valid values: `TRADING`, `HALT`, `BREAK`   
Cannot be used in combination with `symbol` or `symbols`  
  
Notes:

  * Only one of `symbol`, `symbols`, `permissions` parameters can be specified.

  * Without parameters, `exchangeInfo` displays all symbols with `["SPOT, "MARGIN", "LEVERAGED"]` permissions.

    * In order to list _all_ active symbols on the exchange, you need to explicitly request all permissions.
  * `permissions` accepts either a list of permissions, or a single permission name. E.g. `"SPOT"`.

  * [Available Permissions](/docs/binance-spot-api-docs/enums#account-and-symbol-permissions)




**Examples of Symbol Permissions Interpretation from the Response:**

  * `[["A","B"]]` means you may place an order if your account has either permission "A" **or** permission "B".
  * `[["A"],["B"]]` means you can place an order if your account has permission "A" **and** permission "B".
  * `[["A"],["B","C"]]` means you can place an order if your account has permission "A" **and** permission "B" or permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission "B" and permission "C".)



**Data Source:** Memory

**Response:**
    
    
    {  
        "id": "5494febb-d167-46a2-996d-70533eb4d976",  
        "status": 200,  
        "result": {  
            "timezone": "UTC",  
            "serverTime": 1655969291181,  
            // Global rate limits. See "Rate limits" section.  
            "rateLimits": [  
                {  
                    "rateLimitType": "REQUEST_WEIGHT",     // Rate limit type: REQUEST_WEIGHT, ORDERS, CONNECTIONS  
                    "interval": "MINUTE",                  // Rate limit interval: SECOND, MINUTE, DAY  
                    "intervalNum": 1,                      // Rate limit interval multiplier (i.e., "1 minute")  
                    "limit": 6000                          // Rate limit per interval  
                },  
                {  
                    "rateLimitType": "ORDERS",  
                    "interval": "SECOND",  
                    "intervalNum": 10,  
                    "limit": 50  
                },  
                {  
                    "rateLimitType": "ORDERS",  
                    "interval": "DAY",  
                    "intervalNum": 1,  
                    "limit": 160000  
                },  
                {  
                    "rateLimitType": "CONNECTIONS",  
                    "interval": "MINUTE",  
                    "intervalNum": 5,  
                    "limit": 300  
                }  
            ],  
            // Exchange filters are explained on the "Filters" page:  
            // https://github.com/binance/binance-spot-api-docs/blob/master/filters.md  
            // All exchange filters are optional.  
            "exchangeFilters": [],  
            "symbols": [  
                {  
                    "symbol": "BNBBTC",  
                    "status": "TRADING",  
                    "baseAsset": "BNB",  
                    "baseAssetPrecision": 8,  
                    "quoteAsset": "BTC",  
                    "quotePrecision": 8,  
                    "quoteAssetPrecision": 8,  
                    "baseCommissionPrecision": 8,  
                    "quoteCommissionPrecision": 8,  
                    "orderTypes": [  
                        "LIMIT",  
                        "LIMIT_MAKER",  
                        "MARKET",  
                        "STOP_LOSS_LIMIT",  
                        "TAKE_PROFIT_LIMIT"  
                    ],  
                    "icebergAllowed": true,  
                    "ocoAllowed": true,  
                    "otoAllowed": true,  
                    "opoAllowed": true,  
                    "quoteOrderQtyMarketAllowed": true,  
                    "allowTrailingStop": true,  
                    "cancelReplaceAllowed": true,  
                    "amendAllowed": false,  
                    "pegInstructionsAllowed": true,  
                    "isSpotTradingAllowed": true,  
                    "isMarginTradingAllowed": true,  
                    // Symbol filters are explained on the "Filters" page:  
                    // https://github.com/binance/binance-spot-api-docs/blob/master/filters.md  
                    // All symbol filters are optional.  
                    "filters": [  
                        {  
                            "filterType": "PRICE_FILTER",  
                            "minPrice": "0.00000100",  
                            "maxPrice": "100000.00000000",  
                            "tickSize": "0.00000100"  
                        },  
                        {  
                            "filterType": "LOT_SIZE",  
                            "minQty": "0.00100000",  
                            "maxQty": "100000.00000000",  
                            "stepSize": "0.00100000"  
                        }  
                    ],  
                    "permissions": [],  
                    "permissionSets": [["SPOT", "MARGIN", "TRD_GRP_004"]],  
                    "defaultSelfTradePreventionMode": "NONE",  
                    "allowedSelfTradePreventionModes": ["NONE"]  
                }  
            ],  
            // Optional field. Present only when SOR is available.  
            // https://github.com/binance/binance-spot-api-docs/blob/master/faqs/sor_faq.md  
            "sors": [  
                {  
                    "baseAsset": "BTC",  
                    "symbols": ["BTCUSDT", "BTCUSDC"]  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 20  
            }  
        ]  
    }

---

# 常用请求信息

### 测试连通性[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/general-requests#测试连通性 "测试连通性的直接链接")
    
    
    {  
        "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",  
        "method": "ping"  
    }  
    

测试能否联通 WebSocket API。

**注意:**

您也可以使用常规 WebSocket ping 帧来测试连通性， WebSocket API 将尽快以 pong 帧响应。 `ping` 请求和 `time` 是在应用程序中测试请求-响应处理的安全方法。

**权重:** 1

**参数:** NONE

**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",  
        "status": 200,  
        "result": {},  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

### 检查服务器时间[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/general-requests#检查服务器时间 "检查服务器时间的直接链接")
    
    
    {  
        "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",  
        "method": "time"  
    }  
    

测试与 WebSocket API 的连通性并获取当前服务器时间。

**权重:** 1

**参数:** NONE

**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",  
        "status": 200,  
        "result": {  
            "serverTime": 1656400526260  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 1  
            }  
        ]  
    }  
    

### 交易规范信息[​](/docs/zh-CN/binance-spot-api-docs/websocket-api/general-requests#交易规范信息 "交易规范信息的直接链接")
    
    
    {  
        "id": "5494febb-d167-46a2-996d-70533eb4d976",  
        "method": "exchangeInfo",  
        "params": {  
            "symbols": ["BNBBTC"]  
        }  
    }  
    

获取交易规则，速率限制，和交易对信息。

**权重:** 20

**参数:**

名称 | 类型 | 是否必需 | 描述  
---|---|---|---  
`symbol` | STRING | NO | 代表单个交易对  
`symbols` | ARRAY of STRING | 代表多个交易对  
`permissions` | ARRAY of STRING | 按权限过滤交易对  
`showPermissionSets` | BOOLEAN | 控制是否返回 `permissionSets` 字段的内容，默认为 `true`  
`symbolStatus` | ENUM | 过滤具有此 `tradingStatus` 的交易对  
有效值： `TRADING`， `HALT`， `BREAK`   
不能与 `symbol` 或 `symbols` 组合使用  
  
备注：

  * 参数 `symbol`、`symbols` 和 `permissions` 不能相互组合使用。

  * 如果没有参数，`exchangeInfo` 将显示具有 `SPOT`、`MARGIN` 或 `LEVERAGED` 权限的所有交易对。

    * 要显示具有任何权限的交易对，您需要在 `permissions` 中明确指定它们：（例如 `["SPOT","MARGIN",...]`)。有关完整列表，请参阅 [可用权限](/docs/zh-CN/binance-spot-api-docs/enums#account-and-symbol-permissions)。



**解释响应中的`permissionSets`：**

  * `[["A","B"]]` \- 有权限"A"**或** 权限"B"的账户可以下订单。
  * `[["A"],["B"]]` \- 有权限"A"**和** 权限"B"的账户可以下订单。
  * `[["A"],["B","C"]]` \- 有权限"A"**和** 权限"B"或权限"C"的账户可以下订单。（此处应用的是包含或，而不是排除或，因此账户可以同时拥有权限"B"和权限"C"。）



**数据源:** 缓存

**响应:**
    
    
    {  
        "id": "5494febb-d167-46a2-996d-70533eb4d976",  
        "status": 200,  
        "result": {  
            "timezone": "UTC",  
            "serverTime": 1655969291181,  
            // 全局速率限制。请参阅 "速率限制" 部分。  
            "rateLimits": [  
                {  
                    "rateLimitType": "REQUEST_WEIGHT",     // 速率限制类型: REQUEST_WEIGHT，ORDERS，CONNECTIONS  
                    "interval": "MINUTE",                  // 速率限制间隔: SECOND，MINUTE，DAY  
                    "intervalNum": 1,                      // 速率限制间隔乘数 (i.e.，"1 minute")  
                    "limit": 6000                          // 每个间隔的速率限制  
                },  
                {  
                    "rateLimitType": "ORDERS",  
                    "interval": "SECOND",  
                    "intervalNum": 10,  
                    "limit": 50  
                },  
                {  
                    "rateLimitType": "ORDERS",  
                    "interval": "DAY",  
                    "intervalNum": 1,  
                    "limit": 160000  
                },  
                {  
                    "rateLimitType": "CONNECTIONS",  
                    "interval": "MINUTE",  
                    "intervalNum": 5,  
                    "limit": 300  
                }  
            ],  
            // 交易所级别过滤器在 "过滤器" 页面上进行了说明：  
            // https://github.com/binance/binance-spot-api-docs/blob/master/filters_CN.md  
            // 全部交易过滤器是可选的。  
            "exchangeFilters": [],  
            "symbols": [  
                {  
                    "symbol": "BNBBTC",  
                    "status": "TRADING",  
                    "baseAsset": "BNB",  
                    "baseAssetPrecision": 8,  
                    "quoteAsset": "BTC",  
                    "quotePrecision": 8,  
                    "quoteAssetPrecision": 8,  
                    "baseCommissionPrecision": 8,  
                    "quoteCommissionPrecision": 8,  
                    "orderTypes": [  
                        "LIMIT",  
                        "LIMIT_MAKER",  
                        "MARKET",  
                        "STOP_LOSS_LIMIT",  
                        "TAKE_PROFIT_LIMIT"  
                    ],  
                    "icebergAllowed": true,  
                    "ocoAllowed": true,  
                    "otoAllowed": true,  
                    "opoAllowed": true,  
                    "quoteOrderQtyMarketAllowed": true,  
                    "allowTrailingStop": true,  
                    "cancelReplaceAllowed": true,  
                    "amendAllowed": false,  
                    "pegInstructionsAllowed": true,  
                    "isSpotTradingAllowed": true,  
                    "isMarginTradingAllowed": true,  
                    // 交易对过滤器在"过滤器"页面上进行了说明：  
                    // https://github.com/binance/binance-spot-api-docs/blob/master/filters_CN.md  
                    // 全部交易对过滤器是可选的。  
                    "filters": [  
                        {  
                            "filterType": "PRICE_FILTER",  
                            "minPrice": "0.00000100",  
                            "maxPrice": "100000.00000000",  
                            "tickSize": "0.00000100"  
                        },  
                        {  
                            "filterType": "LOT_SIZE",  
                            "minQty": "0.00100000",  
                            "maxQty": "100000.00000000",  
                            "stepSize": "0.00100000"  
                        }  
                    ],  
                    "permissions": [],  
                    "permissionSets": [["SPOT", "MARGIN", "TRD_GRP_004"]],  
                    "defaultSelfTradePreventionMode": "NONE",  
                    "allowedSelfTradePreventionModes": ["NONE"]  
                }  
            ],  
            // 可选字段，仅当 SOR 可用时才会被显示出来。  
            // https://github.com/binance/binance-spot-api-docs/blob/master/faqs/sor_faq_CN.md  
            "sors": [  
                {  
                    "baseAsset": "BTC",  
                    "symbols": ["BTCUSDT", "BTCUSDC"]  
                }  
            ]  
        },  
        "rateLimits": [  
            {  
                "rateLimitType": "REQUEST_WEIGHT",  
                "interval": "MINUTE",  
                "intervalNum": 1,  
                "limit": 6000,  
                "count": 20  
            }  
        ]  
    }