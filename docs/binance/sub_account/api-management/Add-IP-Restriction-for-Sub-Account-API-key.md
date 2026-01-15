---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key
api_type: Account
updated_at: 2026-01-15T23:50:57.845689
---

# Add IP Restriction for Sub-Account API key (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#api-description "Direct link to API Description")

Add IP Restriction for Sub-Account API key

## HTTP Request[​](/docs/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#http-request "Direct link to HTTP Request")

POST `/sapi/v2/sub-account/subAccountApi/ipRestriction`

## Request Weight(UID)[​](/docs/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#request-weightuid "Direct link to Request Weight\(UID\)")

**3000**

## Request Parameters[​](/docs/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Sub-account email  
subAccountApiKey| STRING| YES|   
status| STRING| YES| IP Restriction status. 1 = IP Unrestricted. 2 = Restrict access to trusted IPs only.  
ipAddress| STRING| NO| Insert static IP in batch, separated by commas.  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * You need to enable Enable Spot & Margin Trading option for the api key which requests this endpoint
> 


## Response Example[​](/docs/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#response-example "Direct link to Response Example")
    
    
    {  
      "status": "2",   
      "ipList": [  
        "69.210.67.14",  
        "8.34.21.10",  //only return if you open IP restriction and input IP address.  
      ],  
      "updateTime": 1636371437000,  
      "apiKey": "k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf"  
    }

---

# 为子账户API Key增加IP白名单 (适用母账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#接口描述 "接口描述的直接链接")

为子账户API Key增加IP白名单

## HTTP请求[​](/docs/zh-CN/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#http请求 "HTTP请求的直接链接")

POST `/sapi/v2/sub-account/subAccountApi/ipRestriction`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#请求权重uid "请求权重\(UID\)的直接链接")

**3000**

## 请求参数[​](/docs/zh-CN/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| Sub-account email  
subAccountApiKey| STRING| YES|   
status| STRING| YES| IP限制状态。1或不填入(null) = IP未受限。2 = 仅限受信任IP访问。  
ipAddress| STRING| NO| 可批量填入IP，以逗号区隔  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 调用此端口前需要在api管理页开启允许现货及杠杆交易选项
> 


## 响应示例[​](/docs/zh-CN/sub_account/api-management/Add-IP-Restriction-for-Sub-Account-API-key#响应示例 "响应示例的直接链接")
    
    
    {  
      "status": "2",   
      "ipList": [  
        "69.210.67.14",  
        "8.34.21.10",  //只当您有开启IP白名单且添加了IP白名单地址时才返回  
      ],  
      "updateTime": 1636371437000,  
      "apiKey": "k5V49ldtn4tszj6W3hystegdfvmGbqDzjmkCtpTvC0G74WhK7yd4rfCTo4lShf"  
    }