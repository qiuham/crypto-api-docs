---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/deposite-address
api_type: REST
updated_at: 2026-01-15T23:49:36.513511
---

# Deposit Address(supporting network) (USER_DATA)

## API Description[​](/docs/wallet/capital/deposite-address#api-description "Direct link to API Description")

Fetch deposit address with network.

## HTTP Request[​](/docs/wallet/capital/deposite-address#http-request "Direct link to HTTP Request")

GET `/sapi/v1/capital/deposit/address`

## Request Weight(IP)[​](/docs/wallet/capital/deposite-address#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/wallet/capital/deposite-address#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
coin| STRING| YES|   
network| STRING| NO|   
amount| DECIMAL| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `network` is not send, return with default network of the coin.
>   * You can get `network` and `isDefault` in `networkList` in the response of `Get /sapi/v1/capital/config/getall (HMAC SHA256)`.
>   * `amount` needs to be sent if using LIGHTNING network
> 


## Response Example[​](/docs/wallet/capital/deposite-address#response-example "Direct link to Response Example")
    
    
    {  
    	"address": "1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv",  
     	"coin": "BTC",  
     	"tag": "",  
     	"url": "https://btc.com/1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv"  
    }

---

# 获取充值地址(支持多网络)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/capital/deposite-address#接口描述 "接口描述的直接链接")

获取充值地址

## HTTP请求[​](/docs/zh-CN/wallet/capital/deposite-address#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/capital/deposit/address`

## 请求权重(IP)[​](/docs/zh-CN/wallet/capital/deposite-address#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/wallet/capital/deposite-address#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
coin| STRING| YES|   
network| STRING| NO|   
amount| DECIMAL| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/capital/deposite-address#响应示例 "响应示例的直接链接")
    
    
    {  
    	"address": "1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv",  
     	"coin": "BTC",  
     	"tag": "",  
     	"url": "https://btc.com/1HPn8Rx2y6nNSfagQBKy27GB99Vbzg89wv"  
    }