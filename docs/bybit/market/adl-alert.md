---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/market/adl-alert
api_type: Market Data
updated_at: 2026-06-16 19:49:16.247600
---

# Get Fee Group Structure

Query for the [group fee structure](https://www.bybit.com/en/help-center/article/Group-Fee-Structure-Symbol-Grouping) and fee rates.

note

The new grouped fee structure only applies to Pro-level and Market Maker clients. It does not apply to retail traders.

For more details please refer to the [fee structure update announcement](https://announcements.bybit.com/article/bybit-fee-structure-update-for-pro-and-market-maker-clients-blt06875b6d623e7581/).

> **Covers: USDT Perpetual / USDT Delivery / USDC Perpetual / USDC Delivery / Inverse Contracts**

info

  * **Weighted maker volume** = Σ(Maker volume on pair × Group weighting factor (`weightingFactor`))
  * **Weighted maker share** = (Your total weighted maker volume ÷ Bybit's total weighted maker volume)
  * _Note: Bybit's total weighted maker volume is not provided by the API. Weighted maker share will be provided in the monthly MM report_.



### HTTP Request

GET`/v5/market/fee-group-info`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
productType| **true**|  string| Product type. `contract` only  
[groupId](/docs/v5/enum#groupid)| false| string| Group ID. `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| List of fee group objects  
> [groupName](/docs/v5/enum#groupname)| string| Fee group name  
> weightingFactor| integer| Group weighting factor  
> symbolsNumbers| integer| No. of symbols  
> symbols| array| Symbol name  
> feeRates| object| Fee rate details for different categories. `pro`, `marketMaker`  
>> pro| array| Pro-level fee structures  
>>> level| string| Pro level name. `Pro 1`, `Pro 2`, `Pro 3`, `Pro 4`, `Pro 5`, `Pro 6`  
>>> takerFeeRate| string| Taker fee rate  
>>> makerFeeRate| string| Maker fee rate  
>>> makerRebate| string| Maker rebate fee rate  
>> marketMaker| array| Market Maker-level fee structures  
>>> level| string| Market Maker level name. `MM 1`, `MM 2`, `MM 3`  
>>> takerFeeRate| string| Taker fee rate  
>>> makerFeeRate| string| Maker fee rate  
>>> makerRebate| string| Maker rebate fee rate  
> updateTime| string| Latest data update timestamp (ms)  
  
* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/fee-group-info?productType=contract&groupId=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_fee_group_info(  
        productType="contract",  
        groupId="1"  
    ))  
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "groupName": "G1(Major Coins)",  
                    "weightingFactor": 1,  
                    "symbolsNumbers": 4,  
                    "symbols": [  
                        "ETHUSDT",  
                        "XRPUSDT",  
                        "SOLUSDT",  
                        "BTCUSDT"  
                    ],  
                    "feeRates": {  
                        "pro": [  
                            {  
                                "level": "Pro 1",  
                                "takerFeeRate": "0.00028",  
                                "makerFeeRate": "0.0001",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 2",  
                                "takerFeeRate": "0.00025",  
                                "makerFeeRate": "0.00005",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 3",  
                                "takerFeeRate": "0.00022",  
                                "makerFeeRate": "0.000025",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 4",  
                                "takerFeeRate": "0.0002",  
                                "makerFeeRate": "0.00001",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 5",  
                                "takerFeeRate": "0.00018",  
                                "makerFeeRate": "0",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 6",  
                                "takerFeeRate": "0.00015",  
                                "makerFeeRate": "0",  
                                "makerRebate": ""  
                            }  
                        ],  
                        "marketMaker": [  
                            {  
                                "level": "MM 1",  
                                "takerFeeRate": "",  
                                "makerFeeRate": "",  
                                "makerRebate": "-0.0000075"  
                            },  
                            {  
                                "level": "MM 2",  
                                "takerFeeRate": "",  
                                "makerFeeRate": "",  
                                "makerRebate": "-0.000015"  
                            },  
                            {  
                                "level": "MM 3",  
                                "takerFeeRate": "",  
                                "makerFeeRate": "",  
                                "makerRebate": "-0.000025"  
                            }  
                        ]  
                    },  
                    "updateTime": "1753240500012"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1758627388542  
    }

---

# 查詢分組手續費结构

查詢[分組手續費結構](https://www.bybit.com/en/help-center/article/Group-Fee-Structure-Symbol-Grouping)相關信息及費率

備註

新的分組費率結構僅適用於專業級別和做市商客戶, 不適用於散戶交易者

更多詳情請參考[費率結構更新公告](https://announcements.bybit.com/article/bybit-fee-structure-update-for-pro-and-market-maker-clients-blt06875b6d623e7581/)

> **覆蓋範圍: USDT 永續 / USDT 交割 / USDC 永續 / USDC 交割 / 反向合約**

信息

  * **加權 Maker 交易量** = Σ(單個交易對的 Maker 交易量 × `weightingFactor`組別權重係數)
  * **加權 Maker 份額** = (您的加權 Maker 總交易量 ÷ Bybit 加權 Maker 總交易量)  
_注意: Bybit 加權 Maker 總交易量不會通過 API 提供，加權 Maker 份額將會在每月的做市商報告中提供_



### HTTP 請求

GET`/v5/market/fee-group-info`

### 請求參數

Parameter| Required| Type| Comments  
---|---|---|---  
productType| **true**|  string| 產品類型, 僅支援`contract`  
[groupId](/docs/zh-TW/v5/enum#groupid)| false| string| 分組ID, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`  
  
### 響應參數

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> [groupName](/docs/zh-TW/v5/enum#groupname)| string| 費率群組名稱  
> weightingFactor| integer| 分組權重  
> symbolsNumbers| integer| 分组交易对数量  
> symbols| array| 合約名稱  
> feeRates| object| 不同類別的費率詳細資訊, `pro`, `marketMaker`  
>> pro| array| Pro 等級費率結構  
>>> level| string| Pro 等級名稱, `Pro 1`, `Pro 2`, `Pro 3`, `Pro 4`, `Pro 5`, `Pro 6`  
>>> takerFeeRate| string| 吃單手續費率  
>>> makerFeeRate| string| 掛單手續費率  
>>> makerRebate| string| 掛單返佣率  
>> marketMaker| array| 做市商等級費率結構  
>>> level| string| 做市商等級名稱, `MM 1`, `MM 2`, `MM 3`  
>>> takerFeeRate| string| 吃單手續費率  
>>> makerFeeRate| string| 掛單手續費率  
>>> makerRebate| string| 掛單返佣率  
> updateTime| string| 數據最近更新的時間戳 (毫秒)  
  
* * *

### Request Example

  * HTTP
  * Python
  * Go
  * Java
  * Node.js


    
    
    GET /v5/market/fee-group-info?productType=contract&groupId=1 HTTP/1.1  
    Host: api-testnet.bybit.com  
    
    
    
      
    
    
    
      
    
    
    
      
    
    
    
      
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "OK",  
        "result": {  
            "list": [  
                {  
                    "groupName": "G1(Major Coins)",  
                    "weightingFactor": 1,  
                    "symbolsNumbers": 4,  
                    "symbols": [  
                        "ETHUSDT",  
                        "XRPUSDT",  
                        "SOLUSDT",  
                        "BTCUSDT"  
                    ],  
                    "feeRates": {  
                        "pro": [  
                            {  
                                "level": "Pro 1",  
                                "takerFeeRate": "0.00028",  
                                "makerFeeRate": "0.0001",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 2",  
                                "takerFeeRate": "0.00025",  
                                "makerFeeRate": "0.00005",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 3",  
                                "takerFeeRate": "0.00022",  
                                "makerFeeRate": "0.000025",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 4",  
                                "takerFeeRate": "0.0002",  
                                "makerFeeRate": "0.00001",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 5",  
                                "takerFeeRate": "0.00018",  
                                "makerFeeRate": "0",  
                                "makerRebate": ""  
                            },  
                            {  
                                "level": "Pro 6",  
                                "takerFeeRate": "0.00015",  
                                "makerFeeRate": "0",  
                                "makerRebate": ""  
                            }  
                        ],  
                        "marketMaker": [  
                            {  
                                "level": "MM 1",  
                                "takerFeeRate": "",  
                                "makerFeeRate": "",  
                                "makerRebate": "-0.0000075"  
                            },  
                            {  
                                "level": "MM 2",  
                                "takerFeeRate": "",  
                                "makerFeeRate": "",  
                                "makerRebate": "-0.000015"  
                            },  
                            {  
                                "level": "MM 3",  
                                "takerFeeRate": "",  
                                "makerFeeRate": "",  
                                "makerRebate": "-0.000025"  
                            }  
                        ]  
                    },  
                    "updateTime": "1753240500012"  
                }  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1758627388542  
    }