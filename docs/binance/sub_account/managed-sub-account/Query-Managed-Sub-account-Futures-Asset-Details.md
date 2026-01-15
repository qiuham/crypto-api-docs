---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details
api_type: Account
updated_at: 2026-01-15T23:51:32.049718
---

# Query Managed Sub-account Futures Asset Details (For Investor Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#api-description "Direct link to API Description")

Investor can use this api to query managed sub account futures asset details

## HTTP Request[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#http-request "Direct link to HTTP Request")

GET `/sapi/v1/managed-subaccount/fetch-future-asset`

## Request Weight(UID)[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#request-weightuid "Direct link to Request Weight\(UID\)")

**60**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Managed Sub Account Email  
accountType| STRING| NO| No input or input "USDT_FUTURE" to get UM Futures account details. Input "COIN_FUTURE" to get CM Futures account details.  
  
## Response Example[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#response-example "Direct link to Response Example")
    
    
    {  
      "code": "200",  
      "message": "OK",  
      "snapshotVos": [  
        {  
          "type": "FUTURES",  
          "updateTime": 1672893855394,  
          "data": {  
            "assets": [  
              {  
                "asset": "USDT",  
                "marginBalance": 100,  
                "walletBalance": 120  
              }  
            ],  
            "position": [  
              {  
                "symbol": "BTCUSDT",  
                "entryPrice": 17000,  
                "markPrice": 17000,  
                "positionAmt": 0.0001  
              }  
            ]  
          }  
        }  
      ]  
    }

---

# 投资人账户查询托管子账户期货资产 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#接口描述 "接口描述的直接链接")

投资人可以根据此接口查询其托管子账户期货资产

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/fetch-future-asset`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 托管子账户邮箱  
accountType| STRING| NO| 不输入或输入USDT_FUTURE，取得UM期货帐户资产。 输入COIN_FUTURE"，取得CM期货帐户资产。  
  
## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-account-Futures-Asset-Details#响应示例 "响应示例的直接链接")
    
    
    {  
      "code": "200",  
      "message": "OK",  
      "snapshotVos": [  
        {  
          "type": "FUTURES",  
          "updateTime": 1672893855394,  
          "data": {  
            "assets": [  
              {  
                "asset": "USDT",  
                "marginBalance": 100,  
                "walletBalance": 120  
              }  
            ],  
            "position": [  
              {  
                "symbol": "BTCUSDT",  
                "entryPrice": 17000,  
                "markPrice": 17000,  
                "positionAmt": 0.0001  
              }  
            ]  
          }  
        }  
      ]  
    }