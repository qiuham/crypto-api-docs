---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/capital/withdraw
api_type: REST
updated_at: 2026-01-15T23:49:39.857982
---

# Withdraw(USER_DATA)

## API Description[​](/docs/wallet/capital/withdraw#api-description "Direct link to API Description")

Submit a withdraw request.

## HTTP Request[​](/docs/wallet/capital/withdraw#http-request "Direct link to HTTP Request")

POST `/sapi/v1/capital/withdraw/apply`

## Request Weight(UID)[​](/docs/wallet/capital/withdraw#request-weightuid "Direct link to Request Weight\(UID\)")

**900**

## Request Parameters[​](/docs/wallet/capital/withdraw#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
coin| STRING| YES|   
withdrawOrderId| STRING| NO| client side id for withdrawal, if provide here, can be used in GET `/sapi/v1/capital/withdraw/history` for query.  
network| STRING| NO|   
address| STRING| YES|   
addressTag| STRING| NO| Secondary address identifier for coins like XRP,XMR etc.  
amount| DECIMAL| YES|   
transactionFeeFlag| BOOLEAN| NO| When making internal transfer, `true` for returning the fee to the destination account; `false` for returning the fee back to the departure account. Default `false`.  
name| STRING| NO| Description of the address. Address book cap is 200, space in name should be encoded into `%20`  
walletType| INTEGER| NO| The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current "selected wallet" under wallet->Fiat and Spot/Funding->Deposit  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `network` not send, return with default network of the coin.
>   * You can get `network` and `isDefault` in `networkList` of a coin in the response of `Get /sapi/v1/capital/config/getall (HMAC SHA256)`.
>   * To check if travel rule is required, by using `GET /sapi/v1/localentity/questionnaire-requirements` and if it returns anything other than `NIL` you will need update SAPI to `POST /sapi/v1/localentity/withdraw/apply` else you can continue `POST /sapi/v1/capital/withdraw/apply`. Please note that if you are required to comply to travel rule please refer to the Travel Rule SAPI.
> 


## Response Example[​](/docs/wallet/capital/withdraw#response-example "Direct link to Response Example")
    
    
    {  
        "id":"7213fea8e94b4a5593d507237e5a555b"  
    }

---

# 提币(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/capital/withdraw#接口描述 "接口描述的直接链接")

提币

## HTTP请求[​](/docs/zh-CN/wallet/capital/withdraw#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/capital/withdraw/apply`

## 请求权重(UID)[​](/docs/zh-CN/wallet/capital/withdraw#请求权重uid "请求权重\(UID\)的直接链接")

**900**

## 请求参数[​](/docs/zh-CN/wallet/capital/withdraw#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
coin| STRING| YES|   
withdrawOrderId| STRING| NO| 用户自定义提币ID, 后续可以在GET `/sapi/v1/capital/withdraw/history` 中使用这个字段进行查询  
network| STRING| NO| 提币网络  
address| STRING| YES| 提币地址  
addressTag| STRING| NO| 某些币种例如 XRP,XMR 允许填写次级地址标签  
amount| DECIMAL| YES| 数量  
transactionFeeFlag| BOOLEAN| NO| 当站内转账时免手续费, `true`: 手续费归资金转入方; `false`: 手续费归资金转出方; . 默认 `false`.  
name| STRING| NO| 地址的备注，填写该参数后会加入该币种的提现地址簿。地址簿上限为200，超出后会造成提现失败。地址中的空格需要encode成`%20`  
walletType| INTEGER| NO| 表示出金使用的钱包，0为现货钱包，1为资金钱包。默认walletType为"充币账户"是您设置在钱包->现货账户或资金账户->充值。  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果`network`未发送，则返回该币种的默认网络。
>   * 您可以在`Get /sapi/v1/capital/config/getall (HMAC SHA256)`的响应中，获取某个币种的`networkList`中的`network`和`isDefault`。
>   * 要检查是否需要遵守旅行规则，可以使用接口 `GET /sapi/v1/localentity/questionnaire-requirements`，如果返回结果不是 NIL，则需要使用更新后的 SAPI 接口 `POST /sapi/v1/localentity/withdraw/apply`；否则，可以继续使用 `POST /sapi/v1/capital/withdraw/apply`。请注意，如果需要遵守旅行规则，请参考旅行规则相关的 SAPI 文档。
> 


## 响应示例[​](/docs/zh-CN/wallet/capital/withdraw#响应示例 "响应示例的直接链接")
    
    
    {  
        "id":"7213fea8e94b4a5593d507237e5a555b"  
    }