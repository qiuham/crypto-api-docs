---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account
api_type: Account
updated_at: 2026-01-15T23:51:05.293303
---

# Get Detail on Sub-account's Margin Account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#api-description "Direct link to API Description")

Get Detail on Sub-account's Margin Account

## HTTP Request[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/margin/account`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#request-weightip "Direct link to Request Weight\(IP\)")

**10**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| [Sub-account email](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#email-address)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#response-example "Direct link to Response Example")
    
    
    {  
          "email":"123@test.com",  
          "marginLevel": "11.64405625",  
          "totalAssetOfBtc": "6.82728457",  
          "totalLiabilityOfBtc": "0.58633215",  
          "totalNetAssetOfBtc": "6.24095242",  
          "marginTradeCoeffVo":   
          		{  
    				"forceLiquidationBar": "1.10000000",  // Liquidation margin ratio  
    				"marginCallBar": "1.50000000",        // Margin call margin ratio  
    				"normalBar": "2.00000000"		      // Initial margin ratio  
    			},  
          "marginUserAssetVoList": [  
              {  
                  "asset": "BTC",  
                  "borrowed": "0.00000000",  
                  "free": "0.00499500",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "0.00499500"  
              },  
              {  
                  "asset": "BNB",  
                  "borrowed": "201.66666672",  
                  "free": "2346.50000000",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "2144.83333328"  
              },  
              {  
                  "asset": "ETH",  
                  "borrowed": "0.00000000",  
                  "free": "0.00000000",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "0.00000000"  
              },  
              {  
                  "asset": "USDT",  
                  "borrowed": "0.00000000",  
                  "free": "0.00000000",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "0.00000000"  
              }  
          ]  
    }

---

# 查询子账户Margin账户详情 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#接口描述 "接口描述的直接链接")

查询子账户Margin账户详情

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/margin/account`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#请求权重ip "请求权重\(IP\)的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#request-email-address)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Detail-on-Sub-accounts-Margin-Account#响应示例 "响应示例的直接链接")
    
    
    {  
          "email":"123@test.com",  
          "marginLevel": "11.64405625",  
          "totalAssetOfBtc": "6.82728457",  
          "totalLiabilityOfBtc": "0.58633215",  
          "totalNetAssetOfBtc": "6.24095242",  
          "marginTradeCoeffVo":   
          		{  
    				"forceLiquidationBar": "1.10000000",  // 强平风险率  
    				"marginCallBar": "1.50000000",        // 补仓风险率  
    				"normalBar": "2.00000000"	          // 初始风险率  
    			},  
          "marginUserAssetVoList": [  
              {  
                  "asset": "BTC",  
                  "borrowed": "0.00000000",  
                  "free": "0.00499500",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "0.00499500"  
              },  
              {  
                  "asset": "BNB",  
                  "borrowed": "201.66666672",  
                  "free": "2346.50000000",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "2144.83333328"  
              },  
              {  
                  "asset": "ETH",  
                  "borrowed": "0.00000000",  
                  "free": "0.00000000",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "0.00000000"  
              },  
              {  
                  "asset": "USDT",  
                  "borrowed": "0.00000000",  
                  "free": "0.00000000",  
                  "interest": "0.00000000",  
                  "locked": "0.00000000",  
                  "netAsset": "0.00000000"  
              }  
          ]  
    }