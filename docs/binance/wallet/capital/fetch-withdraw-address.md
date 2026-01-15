---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/fetch-withdraw-address
api_type: REST
updated_at: 2026-01-15T23:49:39.650049
---

# Fetch withdraw address list (USER_DATA)

## API Description[​](/docs/wallet/capital/fetch-withdraw-address#api-description "Direct link to API Description")

Fetch withdraw address list

## HTTP Request[​](/docs/wallet/capital/fetch-withdraw-address#http-request "Direct link to HTTP Request")

GET `/sapi/v1/capital/withdraw/address/list`

## Request Weight(IP)[​](/docs/wallet/capital/fetch-withdraw-address#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/wallet/capital/fetch-withdraw-address#request-parameters "Direct link to Request Parameters")

NONE

## Response Example[​](/docs/wallet/capital/fetch-withdraw-address#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",  
        "addressTag": "",  
        "coin": "BTC",  
        "name": "Satoshi",        //is a user-defined name  
        "network": "BTC",  
        "origin": "bla",      //if originType != 'others', this value is blank, otherwise the origin is manually filled in by the user  
        "originType": "others",  //Address source type, including but not limited to: type Exchange Address: Binance, CoinBase, HTX, Bitfinex, OKX, Bithumb, Kraken, Kucoin, Gemini, Bitget, Bybit, Upbit, Gate.io;  type Wallet Address: Binance Web3 Wallet, Trust Wallet, MetaMask, Rabby Wallet, Phantom, OKX Web 3 Wallet, Coinbase Wallet, Bitget Wallet; type Others: others(multilanguage support)  
        "whiteStatus": true      //Is it whitelisted  
      }  
    ]

---

# 查询提现地址簿

## 接口描述[​](/docs/zh-CN/wallet/capital/fetch-withdraw-address#接口描述 "接口描述的直接链接")

查询提现地址簿

## HTTP请求[​](/docs/zh-CN/wallet/capital/fetch-withdraw-address#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/capital/withdraw/address/list`

## 请求权重(IP)[​](/docs/zh-CN/wallet/capital/fetch-withdraw-address#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/wallet/capital/fetch-withdraw-address#请求参数 "请求参数的直接链接")

NONE

## 响应示例[​](/docs/zh-CN/wallet/capital/fetch-withdraw-address#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",  
            "addressTag": "",  
            "coin": "BTC",  
            "name": "Satoshi",        //用户自定义  
            "network": "BTC",  
            "origin": "bla",      //如果 originType != 'others'，则该值为空，否则 origin 由用户手动填写  
            "originType": "others",  //地址来源类型，包括但不限于: 交易所地址类型: Binance, CoinBase, HTX, Bitfinex, OKX, Bithumb, Kraken, Kucoin, Gemini, Bitget, Bybit, Upbit, Gate.io; 个人钱包类型: Binance Web3 Wallet, Trust Wallet, MetaMask, Rabby Wallet, Phantom, OKX Web 3 Wallet, Coinbase Wallet, Bitget Wallet; 其他 Others 类型: others(支持多语言)  
            "whiteStatus": true      //是否是白名单  
        }  
    ]