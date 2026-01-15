---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/query-user-wallet-balance
api_type: REST
updated_at: 2026-01-15T23:49:33.533754
---

# Query User Wallet Balance (USER_DATA)

## API Description[​](/docs/wallet/asset/query-user-wallet-balance#api-description "Direct link to API Description")

Query User Wallet Balance

## HTTP Request[​](/docs/wallet/asset/query-user-wallet-balance#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/wallet/balance`

## Request Weight(IP)[​](/docs/wallet/asset/query-user-wallet-balance#request-weightip "Direct link to Request Weight\(IP\)")

**60**

## Request Parameters[​](/docs/wallet/asset/query-user-wallet-balance#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
quoteAsset| STRING| NO| `USDT`, `ETH`, `USDC`, `BNB`, etc. default `BTC`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/asset/query-user-wallet-balance#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Spot"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Funding"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Cross Margin"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Isolated Margin"  
      },   
      {  
        "activate": true,  
        "balance": "0.71842752",  
        "walletName": "USDⓈ-M Futures"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "COIN-M Futures"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Earn"  
      },   
      {  
        "activate": false,  
        "balance": "0",  
        "walletName": "Options"  
      },  
      {  
          "activate": true,  
          "balance": "0",  
          "walletName": "Trading Bots"  
      },  
      {  
          "activate": true,  
          "balance": "0",  
          "walletName": "Copy Trading"  
      }  
    ]

---

# 查询用户钱包余额(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/query-user-wallet-balance#接口描述 "接口描述的直接链接")

查询用户钱包余额

## HTTP请求[​](/docs/zh-CN/wallet/asset/query-user-wallet-balance#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/wallet/balance`

## 请求权重(IP)[​](/docs/zh-CN/wallet/asset/query-user-wallet-balance#请求权重ip "请求权重\(IP\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/wallet/asset/query-user-wallet-balance#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
quoteAsset| LONG| NO| `USDT`, `ETH`, `USDC`, `BNB`, 等。 默认 `BTC`  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/asset/query-user-wallet-balance#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Spot"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Funding"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Cross Margin"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Isolated Margin"  
      },   
      {  
        "activate": true,  
        "balance": "0.71842752",  
        "walletName": "USDⓈ-M Futures"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "COIN-M Futures"  
      },   
      {  
        "activate": true,  
        "balance": "0",  
        "walletName": "Earn"  
      },   
      {  
        "activate": false,  
        "balance": "0",  
        "walletName": "Options"  
      },  
      {  
          "activate": true,  
          "balance": "0",  
          "walletName": "Trading Bots"  
      },  
      {  
          "activate": true,  
          "balance": "0",  
          "walletName": "Copy Trading"  
      }  
    ]