---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary
api_type: Account
updated_at: 2026-01-15T23:51:13.390579
---

# Query Sub-account Spot Assets Summary (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#api-description "Direct link to API Description")

Get BTC valued asset summary of subaccounts.

## HTTP Request[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/spotSummary`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| NO| Sub account email  
page| LONG| NO| default 1  
size| LONG| NO| default 10, max 20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#response-example "Direct link to Response Example")
    
    
    {  
    	"totalCount":2,  
    	"masterAccountTotalAsset": "0.23231201",  
    	"spotSubUserAssetBtcVoList":[  
    		{  
    			"email":"sub123@test.com",  
    			"totalAsset":"9999.00000000"  
    		},  
    		{  
    			"email":"test456@test.com",  
    			"totalAsset":"0.00000000"  
    		}  
    	]  
    }

---

# 查询子账户现货资产汇总 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#接口描述 "接口描述的直接链接")

获取BTC计价的子账户现货资产汇总。

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/spotSummary`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| NO| 子账户邮箱  
page| LONG| NO| 分页，默认 1  
size| LONG| NO| 单页条目数, 默认 10, 最大 20  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Query-Sub-account-Spot-Assets-Summary#响应示例 "响应示例的直接链接")
    
    
    {  
    	"totalCount":2,  
    	"masterAccountTotalAsset":"0.23231201",  
    	"spotSubUserAssetBtcVoList":[  
    		{  
    			"email":"sub123@test.com",  
    			"totalAsset":"9999.00000000"  
    		},  
    		{  
    			"email":"test456@test.com",  
    			"totalAsset":"0.00000000"  
    		}  
    	]  
    }