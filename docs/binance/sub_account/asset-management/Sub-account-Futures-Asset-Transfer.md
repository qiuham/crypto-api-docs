---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer
api_type: Account
updated_at: 2026-01-15T23:51:17.455867
---

# Sub-account Futures Asset Transfer (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#api-description "Direct link to API Description")

Sub-account Futures Asset Transfer

## HTTP Request[​](/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#http-request "Direct link to HTTP Request")

POST `/sapi/v1/sub-account/futures/internalTransfer`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
fromEmail| STRING| YES| Sender email  
toEmail| STRING| YES| Recipient email  
futuresType| LONG| YES| 1:USDT-margined Futures，2: Coin-margined Futures  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * Master account can transfer max 2000 times a minute
>   * There must be sufficient margin balance in futures wallet to execute transferring.
> 


## Response Example[​](/docs/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#response-example "Direct link to Response Example")
    
    
    {  
        "success":true,  
        "txnId":"2934662589"  
    }

---

# 执行子账户合约资金划转 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#接口描述 "接口描述的直接链接")

执行子账户合约资金划转

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/sub-account/futures/internalTransfer`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
fromEmail| STRING| YES| 发送者邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#request-email-address)  
toEmail| STRING| YES| 接收者邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#request-email-address)  
futuresType| LONG| YES| 1:USDT合约， 2: 币本位合约  
asset| STRING| YES|   
amount| DECIMAL| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 每个母账户每分钟上限2000次
>   * 您期货钱包中须有足够保证金余额才能执行转账
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Sub-account-Futures-Asset-Transfer#响应示例 "响应示例的直接链接")
    
    
    {  
        "success":true,  
        "txnId":"2934662589"  
    }