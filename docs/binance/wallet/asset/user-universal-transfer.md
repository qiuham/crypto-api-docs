---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/user-universal-transfer
api_type: REST
updated_at: 2026-01-15T23:49:36.380530
---

# User Universal Transfer (USER_DATA)

## API Description[​](/docs/wallet/asset/user-universal-transfer#api-description "Direct link to API Description")

user universal transfer

## HTTP Request[​](/docs/wallet/asset/user-universal-transfer#http-request "Direct link to HTTP Request")

POST `/sapi/v1/asset/transfer`

You need to enable `Permits Universal Transfer` option for the API Key which requests this endpoint.

## Request Weight(UID)[​](/docs/wallet/asset/user-universal-transfer#request-weightuid "Direct link to Request Weight\(UID\)")

**900**

## Request Parameters[​](/docs/wallet/asset/user-universal-transfer#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
type| ENUM| YES|   
asset| STRING| YES|   
amount| DECIMAL| YES|   
fromSymbol| STRING| NO|   
toSymbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * `fromSymbol` must be sent when type are ISOLATEDMARGIN_MARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

  * `toSymbol` must be sent when type are MARGIN_ISOLATEDMARGIN and ISOLATEDMARGIN_ISOLATEDMARGIN

  * ENUM of transfer types:

    * MAIN_UMFUTURE Spot account transfer to USDⓈ-M Futures account
    * MAIN_CMFUTURE Spot account transfer to COIN-M Futures account
    * MAIN_MARGIN Spot account transfer to Margin（cross）account
    * UMFUTURE_MAIN USDⓈ-M Futures account transfer to Spot account
    * UMFUTURE_MARGIN USDⓈ-M Futures account transfer to Margin（cross）account
    * CMFUTURE_MAIN COIN-M Futures account transfer to Spot account
    * CMFUTURE_MARGIN COIN-M Futures account transfer to Margin(cross) account
    * MARGIN_MAIN Margin（cross）account transfer to Spot account
    * MARGIN_UMFUTURE Margin（cross）account transfer to USDⓈ-M Futures
    * MARGIN_CMFUTURE Margin（cross）account transfer to COIN-M Futures
    * ISOLATEDMARGIN_MARGIN Isolated margin account transfer to Margin(cross) account
    * MARGIN_ISOLATEDMARGIN Margin(cross) account transfer to Isolated margin account
    * ISOLATEDMARGIN_ISOLATEDMARGIN Isolated margin account transfer to Isolated margin account
    * MAIN_FUNDING Spot account transfer to Funding account
    * FUNDING_MAIN Funding account transfer to Spot account
    * FUNDING_UMFUTURE Funding account transfer to UMFUTURE account
    * UMFUTURE_FUNDING UMFUTURE account transfer to Funding account
    * MARGIN_FUNDING MARGIN account transfer to Funding account
    * FUNDING_MARGIN Funding account transfer to Margin account
    * FUNDING_CMFUTURE Funding account transfer to CMFUTURE account
    * CMFUTURE_FUNDING CMFUTURE account transfer to Funding account
    * MAIN_OPTION Spot account transfer to Options account
    * OPTION_MAIN Options account transfer to Spot account
    * UMFUTURE_OPTION USDⓈ-M Futures account transfer to Options account
    * OPTION_UMFUTURE Options account transfer to USDⓈ-M Futures account
    * MARGIN_OPTION Margin（cross）account transfer to Options account
    * OPTION_MARGIN Options account transfer to Margin（cross）account
    * FUNDING_OPTION Funding account transfer to Options account
    * OPTION_FUNDING Options account transfer to Funding account
    * MAIN_PORTFOLIO_MARGIN Spot account transfer to Portfolio Margin account
    * PORTFOLIO_MARGIN_MAIN Portfolio Margin account transfer to Spot account



## Response Example[​](/docs/wallet/asset/user-universal-transfer#response-example "Direct link to Response Example")
    
    
    {  
        "tranId":13526853623  
    }

---

# 用户万向划转(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/user-universal-transfer#接口描述 "接口描述的直接链接")

用户万向划转

## HTTP请求[​](/docs/zh-CN/wallet/asset/user-universal-transfer#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/asset/transfer`

您需要开通api key `允许万向划转`权限来调用此接口。

## 请求权重(UID)[​](/docs/zh-CN/wallet/asset/user-universal-transfer#请求权重uid "请求权重\(UID\)的直接链接")

**900**

## 请求参数[​](/docs/zh-CN/wallet/asset/user-universal-transfer#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
type| ENUM| YES|   
asset| STRING| YES|   
amount| DECIMAL| YES|   
fromSymbol| STRING| NO|   
toSymbol| STRING| NO|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
  * `fromSymbol` 必须要发送，当类型为 ISOLATEDMARGIN_MARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN

  * `toSymbol` 必须要发送，当类型为 MARGIN_ISOLATEDMARGIN 和 ISOLATEDMARGIN_ISOLATEDMARGIN

  * 目前支持的type划转类型:

    * MAIN_UMFUTURE 现货钱包转向U本位合约钱包
    * MAIN_CMFUTURE 现货钱包转向币本位合约钱包
    * MAIN_MARGIN 现货钱包转向杠杆全仓钱包
    * UMFUTURE_MAIN U本位合约钱包转向现货钱包
    * UMFUTURE_MARGIN U本位合约钱包转向杠杆全仓钱包
    * CMFUTURE_MAIN 币本位合约钱包转向现货钱包
    * MARGIN_MAIN 杠杆全仓钱包转向现货钱包
    * MARGIN_UMFUTURE 杠杆全仓钱包转向U本位合约钱包
    * MARGIN_CMFUTURE 杠杆全仓钱包转向币本位合约钱包
    * CMFUTURE_MARGIN 币本位合约钱包转向杠杆全仓钱包
    * ISOLATEDMARGIN_MARGIN 杠杆逐仓钱包转向杠杆全仓钱包
    * MARGIN_ISOLATEDMARGIN 杠杆全仓钱包转向杠杆逐仓钱包
    * ISOLATEDMARGIN_ISOLATEDMARGIN 杠杆逐仓钱包转向杠杆逐仓钱包
    * MAIN_FUNDING 现货钱包转向资金钱包
    * FUNDING_MAIN 资金钱包转向现货钱包
    * FUNDING_UMFUTURE 资金钱包转向U本位合约钱包
    * UMFUTURE_FUNDING U本位合约钱包转向资金钱包
    * MARGIN_FUNDING 杠杆全仓钱包转向资金钱包
    * FUNDING_MARGIN 资金钱包转向杠杆全仓钱包
    * FUNDING_CMFUTURE 资金钱包转向币本位合约钱包
    * CMFUTURE_FUNDING 币本位合约钱包转向资金钱包
    * MAIN_OPTION 现货钱包转向期权钱包
    * OPTION_MAIN 期权钱包转向现货钱包
    * UMFUTURE_OPTION U本位合约钱包转向期权钱包
    * OPTION_UMFUTURE 期权钱包转向U本位合约钱包
    * MARGIN_OPTION 杠杆全仓钱包转向期权钱包
    * OPTION_MARGIN 期权全仓钱包转向杠杆钱包
    * FUNDING_OPTION 资金钱包转向期权钱包
    * OPTION_FUNDING 期权钱包转向资金钱包
    * MAIN_PORTFOLIO_MARGIN 现货钱包转向统一账户钱包
    * PORTFOLIO_MARGIN_MAIN 统一账户钱包转向现货钱包
    * MAIN_ISOLATED_MARGIN 现货钱包转向逐仓账户钱包
    * ISOLATED_MARGIN_MAIN 逐仓钱包转向现货账户钱包



## 响应示例[​](/docs/zh-CN/wallet/asset/user-universal-transfer#响应示例 "响应示例的直接链接")
    
    
    {  
        "tranId":13526853623  
    }