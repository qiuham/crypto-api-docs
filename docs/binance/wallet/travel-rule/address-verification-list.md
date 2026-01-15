---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/address-verification-list
api_type: REST
updated_at: 2026-01-15T23:49:46.643295
---

# Fetch address verification list (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/address-verification-list#api-description "Direct link to API Description")

Fetch address verification list for user to check on status and other details for the addresses stored in Address Book.

## HTTP Request[​](/docs/wallet/travel-rule/address-verification-list#http-request "Direct link to HTTP Request")

GET `/sapi/v1/addressVerify/list`

## Request Weight(IP)[​](/docs/wallet/travel-rule/address-verification-list#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/travel-rule/address-verification-list#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/wallet/travel-rule/address-verification-list#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "status": "PENDING",  
        "token": "AVAX",  
        "network": "AVAXC",  
        "walletAddress": "0xc03a6aa728a8dde7464c33828424ede7553a0021",  
        "addressQuestionnaire": {   
          "sendTo": 1,  
          "satoshiToken": "AVAX",  
          "isAddressOwner": 1,  
          "verifyMethod": 1  
        }  
      }  
    ]  
    

  1. `status`: Refers to the status of the address verification. Response would return either of the following - Verified, Unverified, Pending.
  2. `token` & `network`: Address is verified for this particular token/network withdrawals.
  3. `walletAddress`: Wallet address that was added into the address book.
  4. `addressQuestionaire`: Details of what you answered for the verification questionnaire.

---

# Fetch address verification list (USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/address-verification-list#接口描述 "接口描述的直接链接")

获取地址验证列表，以便用户检查地址簿中存储的地址的状态和其他详细信息。

## HTTP 请求[​](/docs/zh-CN/wallet/travel-rule/address-verification-list#http-请求 "HTTP 请求的直接链接")

GET `/sapi/v1/addressVerify/list`

## 请求权重(IP)[​](/docs/zh-CN/wallet/travel-rule/address-verification-list#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/address-verification-list#请求参数 "请求参数的直接链接")

名称| 类型| 是否必须| 描述  
---|---|---|---  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/wallet/travel-rule/address-verification-list#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "status": "PENDING",  
        "token": "AVAX",  
        "network": "AVAXC",  
        "walletAddress": "0xc03a6aa728a8dde7464c33828424ede7553a0021",  
        "addressQuestionnaire": {   
          "sendTo": 1,  
          "satoshiToken": "AVAX",  
          "isAddressOwner": 1,  
          "verifyMethod": 1  
        }  
      }  
    ]  
    

  1. `status`：指地址验证的状态。响应将返回以下状态之一 - 已验证、未验证、待验证。
  2. `token` 和 `network`：已验证此特定代币/网络提现的地址。
  3. `walletAddress`：已添加到地址簿的钱包地址。
  4. `addressQuestionaire`：您在验证问卷中回答的详细信息。