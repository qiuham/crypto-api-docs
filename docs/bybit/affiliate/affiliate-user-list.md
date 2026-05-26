---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/affiliate/affiliate-user-list
api_type: REST
updated_at: 2026-01-16T09:38:15.205397
---

# Get Affiliate User List

To use this endpoint, you should have an affiliate account and only tick "affiliate" permission while creating the API key.  
Affiliate site: <https://affiliates.bybit.com>

tip

  * Use master UID only
  * The api key can only have "Affiliate" permission



### HTTP Request

GET `/v5/affiliate/aff-user-list`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
size| false| integer| Limit for data size per page. [`0`, `1000`]. Default: `0`  
cursor| false| string| Cursor. Use the `nextPageCursor` token from the response to retrieve the next page of the result set  
needDeposit| false| boolean| `true`: return deposit info; `false`(default): does not return deposit info  
need30| false| boolean| `true`: return 30 days trading info; `false`(default): does not return 30 days trading info  
need365| false| boolean| `true`: return 365 days trading info; `false`(default): does not return 365 days trading info  
startDate| false| string| Start date of the query period, format `YYYY-MM-DD`  
endDate| false| string| End date of the query period, format `YYYY-MM-DD`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
list| array| Object  
> userId| string| user Id  
> registerTime| string| user register time  
> source| string| user registration source, from which referrer code  
> remarks| string| The remark  
> isKyc| boolean| Whether KYC is completed  
> takerVol30Day| string| Taker volume in last 30 days (USDT), update at T + 1. All volume related attributes below includes Derivatives, Option, Spot volume  
> makerVol30Day| string| Maker volume in last 30 days (USDT), update at T + 1  
> tradeVol30Day| string| Total trading volume in last 30 days (USDT), update at T + 1  
> depositAmount30Day| string| Deposit amount in last 30 days (USDT)  
> takerVol365Day| string| Taker volume in the past year (USDT), update at T + 1  
> makerVol365Day| string| Maker volume in the past year (USDT), update at T + 1  
> tradeVol365Day| string| Total trading volume in the past year (USDT), update at T + 1  
> depositAmount365Day| string| Total deposit amount in the past year (USDT)  
> takerVol| string| Taker volume in [`startDate`, `endDate`] (USDT), update at T + 1, includes Derivatives, Option, Spot volume  
> makerVol| string| Maker volume in [`startDate`, `endDate`] (USDT), update at T + 1, includes Derivatives, Option, Spot volume  
> tradeVol| string| Total trading volume in [`startDate`, `endDate`] (USDT), update at T + 1, includes Derivatives, Option, Spot volume  
> startDate| string| Start date of the query period  
> endDate| string| End date of the query period  
nextPageCursor| string| Refer to the `cursor` request parameter  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/affiliate/aff-user-list?cursor=0&size=2&need365=true&need30=true&needDeposit=true&startDate=2025-10-21&endDate=2025-10-22 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1685596324209  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_affiliate_user_list(  
        cursor="0",  
        size="2",  
        need365=True,  
        need30=True,  
        needDeposit=True,  
        startDate="2025-10-21",  
        endDate="2025-10-22",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAffiliateUserInfo({ size: 2 })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "userId": "1001699821",  
                    "registerTime": "0001-01-01",  
                    "source": "aff_14650_10087",  
                    "remarks": "front_hub_robot",  
                    "isKyc": false,  
                    "takerVol30Day": "",  
                    "makerVol30Day": "",  
                    "tradeVol30Day": "",  
                    "depositAmount30Day": "",  
                    "takerVol365Day": "",  
                    "makerVol365Day": "",  
                    "tradeVol365Day": "",  
                    "depositAmount365Day": "",  
                    "takerVol": "",  
                    "makerVol": "",  
                    "tradeVol": "",  
                    "startDate": "2025-09-21",  
                    "endDate": "2025-10-21"  
                },  
                {  
                    "userId": "1001625535",  
                    "registerTime": "0001-01-01",  
                    "source": "aff_14650_10087",  
                    "remarks": "front_hub_robot",  
                    "isKyc": false,  
                    "takerVol30Day": "",  
                    "makerVol30Day": "",  
                    "tradeVol30Day": "",  
                    "depositAmount30Day": "",  
                    "takerVol365Day": "",  
                    "makerVol365Day": "",  
                    "tradeVol365Day": "",  
                    "depositAmount365Day": "",  
                    "takerVol": "",  
                    "makerVol": "",  
                    "tradeVol": "",  
                    "startDate": "2025-09-21",  
                    "endDate": "2025-10-21"  
                }  
            ],  
            "nextPageCursor": "16197"  
        },  
        "retExtInfo": {},  
        "time": 1733205472513  
    }

---

# 查詢代理用戶列表

要使用此接口，您应该有一个代理商账户，并且在创建 API 密钥时仅勾选“代理商”权限。  
代理商网站: <https://affiliates.bybit.com>

提示

  * 僅支持使用母帳戶uid
  * 若要查詢該接口, api key僅能擁有代理商權限, 若擁有任何其他權限想, 請移除



### HTTP 請求

GET `/v5/affiliate/aff-user-list`

### 請求參數

參數| 是否必需| 類型| 說明  
---|---|---|---  
size| false| integer| 每頁數量限制. [`0`, `1000`]. 默認: `0`  
cursor| false| string| 游標，用於翻頁  
needDeposit| false| boolean| `true`: 返回入金信息; `false`(默認): 不返回入金信息  
need30| false| boolean| `true`: 返回最近30天交易信息; `false`(default): 不返回最近30天交易信息  
need365| false| boolean| `true`: 返回最近365天交易信息; `false`(default): 不返回最近365天交易信息  
startDate| false| string| 查詢時段開始日期，格式為 `YYYY-MM-DD`  
endDate| false| string| 查詢時段結束日期，格式為 `YYYY-MM-DD`  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
list| array| Object  
> userId| string| 帳戶uid  
> registerTime| string| 用戶註冊時間  
> source| string| 用戶註冊來源，來自哪个Referrer Code  
> remarks| string| 備註  
> isKyc| boolean| KYC是否完成  
> takerVol30Day| string| 過去30天的吃單交易量, T+1更新. 單位: USDT. 所有下方交易量相關的字段, 包含了期貨、期權和現貨的交易量  
> makerVol30Day| string| 過去30天的掛單交易量, T+1更新. 單位: USDT  
> tradeVol30Day| string| 過去30天的總交易量, T+1更新. 單位: USDT  
> depositAmount30Day| string| 過去30天的入金金額. 單位: USDT  
> takerVol365Day| string| 過去一年的吃單交易量, T+1更新. 單位: USDT  
> makerVol365Day| string| 過去一年的掛單交易量, T+1更新. 單位: USDT  
> tradeVol365Day| string| 過去一年的總交易量, T+1更新. 單位: USDT  
> depositAmount365Day| string| 過去一年的總入金金額. 單位: USDT  
> takerVol| string| 在 [`startDate`, `endDate`] 區間內的吃單成交量 (USDT)，於 T + 1 更新，包含衍生品、期權與現貨成交量  
> makerVol| string| 在 [`startDate`, `endDate`] 區間內的掛單成交量 (USDT)，於 T + 1 更新，包含衍生品、期權與現貨成交量  
> tradeVol| string| 在 [`startDate`, `endDate`] 區間內的總成交量 (USDT)，於 T + 1 更新，包含衍生品、期權與現貨成交量  
> startDate| string| 查詢時段開始日期  
> endDate| string| 查詢時段結束日期  
nextPageCursor| string| 游標，用於翻頁  
  
* * *

### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    GET /v5/affiliate/aff-user-list?cursor=0&size=2&need365=true&need30=true&needDeposit=true&startDate=2025-10-21&endDate=2025-10-22 HTTP/1.1  
    Host: api-testnet.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1685596324209  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: xxxxxx  
    Content-Type: application/json  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.get_affiliate_user_list(  
        cursor="0",  
        size="2",  
        need365=True,  
        need30=True,  
        needDeposit=True,  
        startDate="2025-10-21",  
        endDate="2025-10-22",  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .getAffiliateUserInfo({ size: 2 })  
      .then((response) => {  
        console.log(response);  
      })  
      .catch((error) => {  
        console.error(error);  
      });  
    

### Response Example
    
    
    {  
        "retCode": 0,  
        "retMsg": "",  
        "result": {  
            "list": [  
                {  
                    "userId": "1001699821",  
                    "registerTime": "0001-01-01",  
                    "source": "aff_14650_10087",  
                    "remarks": "front_hub_robot",  
                    "isKyc": false,  
                    "takerVol30Day": "",  
                    "makerVol30Day": "",  
                    "tradeVol30Day": "",  
                    "depositAmount30Day": "",  
                    "takerVol365Day": "",  
                    "makerVol365Day": "",  
                    "tradeVol365Day": "",  
                    "depositAmount365Day": "",  
                    "takerVol": "",  
                    "makerVol": "",  
                    "tradeVol": "",  
                    "startDate": "2025-09-21",  
                    "endDate": "2025-10-21"  
                },  
                {  
                    "userId": "1001625535",  
                    "registerTime": "0001-01-01",  
                    "source": "aff_14650_10087",  
                    "remarks": "front_hub_robot",  
                    "isKyc": false,  
                    "takerVol30Day": "",  
                    "makerVol30Day": "",  
                    "tradeVol30Day": "",  
                    "depositAmount30Day": "",  
                    "takerVol365Day": "",  
                    "makerVol365Day": "",  
                    "tradeVol365Day": "",  
                    "depositAmount365Day": "",  
                    "takerVol": "",  
                    "makerVol": "",  
                    "tradeVol": "",  
                    "startDate": "2025-09-21",  
                    "endDate": "2025-10-21"  
                }  
            ],  
            "nextPageCursor": "16197"  
        },  
        "retExtInfo": {},  
        "time": 1733205472513  
    }