---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/account/Query-Cross-Margin-Account-Details
api_type: Account
updated_at: 2026-01-15T23:48:17.862582
---

# Query Cross Margin Account Details (USER_DATA)

## API Description[​](/docs/margin_trading/account/Query-Cross-Margin-Account-Details#api-description "Direct link to API Description")

Query Cross Margin Account Details

## HTTP Request[​](/docs/margin_trading/account/Query-Cross-Margin-Account-Details#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/account`

## Request Weight[​](/docs/margin_trading/account/Query-Cross-Margin-Account-Details#request-weight "Direct link to Request Weight")

**10(IP)**

## Request Parameters[​](/docs/margin_trading/account/Query-Cross-Margin-Account-Details#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/account/Query-Cross-Margin-Account-Details#response-example "Direct link to Response Example")
    
    
    {  
          "created" : true, // True means margin account created , false means margin account not created.  
          "borrowEnabled": true,  
          "marginLevel": "11.64405625",  
          "collateralMarginLevel" : "3.2",  
          "totalAssetOfBtc": "6.82728457",  
          "totalLiabilityOfBtc": "0.58633215",  
          "totalNetAssetOfBtc": "6.24095242",  
          "TotalCollateralValueInUSDT": "5.82728457",  
          "totalOpenOrderLossInUSDT": "582.728457",  
          "tradeEnabled": true,  
          "transferInEnabled": true,  
          "transferOutEnabled": true,  
          "accountType": "MARGIN_1",  // // MARGIN_1 for Cross Margin Classic, MARGIN_2 for Cross Margin Pro  
          "userAssets": [  
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

# 查询全仓杠杆账户详情 (USER_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Account-Details#接口描述 "接口描述的直接链接")

查询全仓杠杆账户详情

## HTTP请求[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Account-Details#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/account`

## 请求权重[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Account-Details#请求权重 "请求权重的直接链接")

**10(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Account-Details#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
recvWindow| LONG| NO| 赋值不能大于 `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/account/Query-Cross-Margin-Account-Details#响应示例 "响应示例的直接链接")
    
    
    {  
          "created" : true, // true 表示已开户, false 表示未开户  
          "borrowEnabled": true,  
          "marginLevel": "11.64405625",  
          "collateralMarginLevel" : "3.2",  
          "totalAssetOfBtc": "6.82728457",  
          "totalLiabilityOfBtc": "0.58633215",  
          "totalNetAssetOfBtc": "6.24095242",  
          "TotalCollateralValueInUSDT": "5.82728457",  
          "totalOpenOrderLossInUSDT": "582.728457",  
          "tradeEnabled": true,  
          "transferInEnabled": true,  
          "transferOutEnabled": true,  
          "accountType": "MARGIN_1", // MARGIN_1 全仓Classic模式账户, MARGIN_2 全仓Pro模式账户  
          "userAssets": [  
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