---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/user/modify-master-apikey
api_type: REST
updated_at: 2026-01-16T09:41:34.356162
---

# Modify Master API Key

Modify the settings of master api key. Use the api key pending to be modified to call the endpoint. Use **master user's api key** **only**.

tip

The API key must have one of the below permissions in order to call this endpoint..

  * master API key: "Account Transfer", "Subaccount Transfer", "Withdrawal"



info

Only the api key that calls this interface can be modified

### HTTP Request

POST `/v5/user/update-api`

### Request Parameters

Parameter| Required| Type| Comments  
---|---|---|---  
readOnly| false| integer| `0` (default): Read and Write. `1`: Read only  
ips| false| string| Set the IP bind. example: `"192.168.0.1,192.168.0.2"`**note:**

  * don't pass ips or pass with `"*"` means no bind
  * No ip bound api key will be **invalid after 90 days**
  * api key will be invalid after **7 days** once the account password is changed

  
permissions| false| Object| Tick the types of permission. Don't send this param if you don't want to change the permission  
> ContractTrade| false| array| Contract Trade. `["Order","Position"]`  
> Spot| false| array| Spot Trade. `["SpotTrade"]`  
> Wallet| false| array| Wallet. `["AccountTransfer","SubMemberTransfer"]`  
> Options| false| array| USDC Contract. `["OptionsTrade"]`  
> Exchange| false| array| Convert. `["ExchangeHistory"]`  
> Earn| false| array| Earn product. `["Earn"]`  
> FiatP2P| false| array| P2P `FiatP2POrder`, `Advertising`  
> FiatBybitPay| false| array| Bybit Pay `FaitPayOrder`  
> FiatConvertBroker| false| array| Fiat convert `FiatConvertBrokerOrder`  
> Affiliate| false| array| Affiliate. `["Affiliate"]`

  * This permission is only useful for affiliate
  * If you need this permission, make sure you remove all other permissions

  
> Derivatives| false| array| `["DerivativesTrade"]`  
> BlockTrade| false| array| Blocktrade. `["BlockTrade"]`  
  
### Response Parameters

Parameter| Type| Comments  
---|---|---  
id| string| Unique id. Internal used  
note| string| The remark  
apiKey| string| Api key  
readOnly| integer| `0`: Read and Write. `1`: Read only  
secret| string| Always `""`  
permissions| Object| The types of permission  
> ContractTrade| array| Permisson of contract trade  
> Spot| array| Permisson of spot  
> Wallet| array| Permisson of wallet  
> Options| array| Permission of USDC Contract. It supports trade option and usdc perpetual.  
> Derivatives| array| Permission of Unified account  
> BlockTrade| array| Permission of blocktrade  
> Exchange| array| Permission of convert  
> Earn| array| Permission of earn  
> Affiliate| array| Affiliate permission  
> FiatP2P| array| Permission of P2P  
> FiatBybitPay| array| Permission of Bybit pay  
> FiatConvertBroker| array| Permission of fiat convert  
> NFT| array| **Deprecated** , always `[]`  
> CopyTrading| array| **Deprecated** , always `[]`  
ips| array| IP bound  
  
### Request Example

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/update-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676431264739  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
      
    {  
        "readOnly": null,  
        "ips": "*",  
        "permissions": {  
                "ContractTrade": [  
                    "Order",  
                    "Position"  
                ],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer",  
                    "SubMemberTransfer"  
                ],  
                "Options": [  
                    "OptionsTrade"  
                ],  
                "CopyTrading": [  
                    "CopyTrading"  
                ],  
                "BlockTrade": [],  
                "Exchange": [  
                    "ExchangeHistory"  
                ],  
                "NFT": [  
                    "NFTQueryProductList"  
                ]  
            }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.modify_master_api_key(  
        ips="*",  
        permissions={  
                "ContractTrade": [  
                    "Order",  
                    "Position"  
                ],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer",  
                    "SubMemberTransfer"  
                ],  
                "Options": [  
                    "OptionsTrade"  
                ],  
                "Derivatives": [  
                    "DerivativesTrade"  
                ],  
                "CopyTrading": [  
                    "CopyTrading"  
                ],  
                "BlockTrade": [],  
                "Exchange": [  
                    "ExchangeHistory"  
                ],  
                "NFT": [  
                    "NFTQueryProductList"  
                ]  
            }  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .updateMasterApiKey({  
        ips: ['*'],  
        permissions: {  
          ContractTrade: ['Order', 'Position'],  
          Spot: ['SpotTrade'],  
          Wallet: ['AccountTransfer', 'SubMemberTransfer'],  
          Options: ['OptionsTrade'],  
          Derivatives: ['DerivativesTrade'],  
          CopyTrading: ['CopyTrading'],  
          BlockTrade: [],  
          Exchange: ['ExchangeHistory'],  
          NFT: ['NFTQueryProductList'],  
        },  
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
        "retMsg": "",  
        "result": {  
            "id": "13770661",  
            "note": "xxxxx",  
            "apiKey": "xxxxx",  
            "readOnly": 0,  
            "secret": "",  
            "permissions": {  
                "ContractTrade": [  
                    "Order",  
                    "Position"  
                ],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer",  
                    "SubMemberTransfer"  
                ],  
                "Options": [  
                    "OptionsTrade"  
                ],  
                "Derivatives": [  
                    "DerivativesTrade"  
                ],  
                "CopyTrading": [  
                    "CopyTrading"  
                ],  
                "BlockTrade": [],  
                "Exchange": [  
                    "ExchangeHistory"  
                ],  
                "Earn": [],  
                "NFT": [  
                    "NFTQueryProductList"  
                ]  
            },  
            "ips": [  
                "*"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1676431265427  
    }

---

# 修改母帳戶的API Key設置

修改母帳戶API key的設置。使用待修改的api key調用接口。需使用**母** 帳戶的API key。

提示

在調用接口時，使用的API key至少需要擁有以下其中一種權限

  * 母API key: "Account Transfer（資產帳戶劃轉）", "Subaccount Transfer（母子帳戶劃轉）", "Withdrawal（提幣）"



信息

只能修改調用該接口的api key

### HTTP 請求

POST `/v5/user/update-api`

### 請求參數

參數| 是否必須| 類型| 說明  
---|---|---|---  
readOnly| false| integer| `0` (默認)：可讀可寫. `1`：只讀  
ips| false| string| 綁定IP. 比如: "192.168.0.1,192.168.0.2"**注意:**

  * 不傳參數ips 或者入参值為`"*"`意味著不綁定
  * 不綁定IP的api key將有**90天的有效期限**
  * 一旦帳戶密碼做了修改，帳戶下的非永久api key將在**7天後失效**

  
permissions| false| Object| 勾選api key權限. 如果不修改權限, 則不要傳入該參數  
> ContractTrade| false| array| 合約. ["Order","Position"]  
> Spot| false| array| 現貨. ["SpotTrade"]  
> Wallet| false| array| 錢包. ["AccountTransfer","SubMemberTransfer"]  
> Options| false| array| USDC合約和期權. ["OptionsTrade"]  
> Derivatives| false| array| 統一帳戶權限. ["DerivativesTrade"]  
> BlockTrade| false| array| 大宗商品交易. ["BlockTrade"]  
> Exchange| false| array| 兌換. ["ExchangeHistory"]  
> Earn| false| array| 理財產品的權限 ["Earn"]  
> FiatP2P| false| array| P2P `FiatP2POrder`, `Advertising`  
> FiatBybitPay| false| array| Bybit Pay `FaitPayOrder`  
> FiatConvertBroker| false| array| 數法兌換權限 `FiatConvertBrokerOrder`  
> Affiliate| false| array| 代理商查詢權限. ["Affiliate"]

  * 該權限僅作用於代理商
  * 如果您需要該權限, 請確保移除所有其他權限項

  
  
### 返回參數

參數| 類型| 說明  
---|---|---  
id| string| 唯一id. 內部使用  
note| string| 備註  
apiKey| string| Api key  
readOnly| integer| `0`：可讀可寫. `1`：只讀  
secret| string| 總是 `""`  
permissions| Object| 權限類型  
> ContractTrade| array| 合約交易的權限  
> Spot| array| 現貨交易的權限  
> Wallet| array| 錢包的權限  
> Options| array| USDC合約和期權  
> Derivatives| array| 統一帳戶權限  
> Earn| array| 理財的權限  
> Exchange| array| 兌換的權限  
> FiatP2P| array| P2P `FiatP2POrder`, `Advertising`  
> FiatBybitPay| array| Bybit Pay `FaitPayOrder`  
> FiatConvertBroker| array| 數法兌換權限 `FiatConvertBrokerOrder`  
> Affiliate| array| 代理商查詢權限  
> BlockTrade| array| 大宗交易的權限  
> NFT| array| **廢棄** , 總是[]  
> CopyTrading| array| **廢棄** , 總是[]  
ips| array| 綁定的IP  
  
### 請求示例

  * HTTP
  * Python
  * Node.js


    
    
    POST /v5/user/update-api HTTP/1.1  
    Host: api.bybit.com  
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx  
    X-BAPI-TIMESTAMP: 1676431264739  
    X-BAPI-RECV-WINDOW: 5000  
    X-BAPI-SIGN: XXXXXX  
    Content-Type: application/json  
      
    {  
        "readOnly": null,  
        "ips": "*",  
        "permissions": {  
                "ContractTrade": [  
                    "Order",  
                    "Position"  
                ],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer",  
                    "SubMemberTransfer"  
                ],  
                "Options": [  
                    "OptionsTrade"  
                ],  
                "CopyTrading": [  
                    "CopyTrading"  
                ],  
                "BlockTrade": [],  
                "Exchange": [  
                    "ExchangeHistory"  
                ],  
                "NFT": [  
                    "NFTQueryProductList"  
                ]  
            }  
    }  
    
    
    
    from pybit.unified_trading import HTTP  
    session = HTTP(  
        testnet=True,  
        api_key="xxxxxxxxxxxxxxxxxx",  
        api_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  
    )  
    print(session.modify_master_api_key(  
        ips=["*"],  
        permissions={  
                "ContractTrade": [  
                    "Order",  
                    "Position"  
                ],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer",  
                    "SubMemberTransfer"  
                ],  
                "Options": [  
                    "OptionsTrade"  
                ],  
                "CopyTrading": [  
                    "CopyTrading"  
                ],  
                "BlockTrade": [],  
                "Exchange": [  
                    "ExchangeHistory"  
                ],  
                "NFT": [  
                    "NFTQueryProductList"  
                ]  
            }  
    ))  
    
    
    
    const { RestClientV5 } = require('bybit-api');  
      
    const client = new RestClientV5({  
      testnet: true,  
      key: 'xxxxxxxxxxxxxxxxxx',  
      secret: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',  
    });  
      
    client  
      .updateMasterApiKey({  
        ips: ['*'],  
        permissions: {  
          ContractTrade: ['Order', 'Position'],  
          Spot: ['SpotTrade'],  
          Wallet: ['AccountTransfer', 'SubMemberTransfer'],  
          Options: ['OptionsTrade'],  
          Derivatives: ['DerivativesTrade'],  
          CopyTrading: ['CopyTrading'],  
          BlockTrade: [],  
          Exchange: ['ExchangeHistory'],  
          NFT: ['NFTQueryProductList'],  
        },  
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
        "retMsg": "",  
        "result": {  
            "id": "13770661",  
            "note": "xxxxx",  
            "apiKey": "xxxxx",  
            "readOnly": 0,  
            "secret": "",  
            "permissions": {  
                "ContractTrade": [  
                    "Order",  
                    "Position"  
                ],  
                "Spot": [  
                    "SpotTrade"  
                ],  
                "Wallet": [  
                    "AccountTransfer",  
                    "SubMemberTransfer"  
                ],  
                "Options": [  
                    "OptionsTrade"  
                ],  
                "Derivatives": [  
                    "DerivativesTrade"  
                ],  
                "CopyTrading": [  
                    "CopyTrading"  
                ],  
                "BlockTrade": [],  
                "Exchange": [  
                    "ExchangeHistory"  
                ],  
                "NFT": [  
                    "NFTQueryProductList"  
                ]  
            },  
            "ips": [  
                "*"  
            ]  
        },  
        "retExtInfo": {},  
        "time": 1676431265427  
    }