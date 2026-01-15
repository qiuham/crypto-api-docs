---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address
api_type: Account
updated_at: 2026-01-15T23:51:25.597322
---

# Get Managed Sub-account Deposit Address (For Investor Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#api-description "Direct link to API Description")

Get investor's managed sub-account deposit address.

## HTTP Request[​](/docs/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#http-request "Direct link to HTTP Request")

`GET /sapi/v1/managed-subaccount/deposit/address`

## Request Weight(UID)[​](/docs/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#request-weightuid "Direct link to Request Weight\(UID\)")

**1**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Sub user email  
coin| STRING| YES|   
network| STRING| NO| networks can be found in `GET /sapi/v1/capital/deposit/address`  
amount| DECIMAL| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `network` is not send, return with default `network` of the `coin`.
>   *     * `amount` needs to be sent if using LIGHTNING network
> 


## Response Example[​](/docs/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#response-example "Direct link to Response Example")
    
    
    {  
        "coin": "USDT",  
        "address": "0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d",  
        "tag": "",  
        "url": "https://etherscan.io/address/0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d"  
    }

---

# 获取托管子账户充值地址 (适用投资人母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#接口描述 "接口描述的直接链接")

获取投资人之托管子账户充值地址

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/deposit/address`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#请求权重uid "请求权重\(UID\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 托管子账户邮箱  
coin| STRING| YES|   
network| STRING| NO| 网络可以在`GET /sapi/v1/capital/deposit/address`获取  
amount| DECIMAL| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `network`不传时，返回该`coin`默认的`network`.
>   * 使用LIGHTNING网络时，`amount`必须传
> 


## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Get-Managed-Sub-account-Deposit-Address#响应示例 "响应示例的直接链接")
    
    
    {  
        "coin": "USDT",  
        "address": "0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d",  
        "tag": "",  
        "url": "https://etherscan.io/address/0x206c22d833bb0bb2102da6b7c7d4c3eb14bcf73d"  
    }