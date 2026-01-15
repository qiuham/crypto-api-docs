---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading
api_type: Trading
updated_at: 2026-01-15T23:48:43.563656
---

# Create Special Key(Low-Latency Trading)(TRADE)

## API Description[​](/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#api-description "Direct link to API Description")

  * Binance Margin offers low-latency trading through a [special key](https://www.binance.com/en/support/faq/frequently-asked-questions-on-margin-special-api-key-3208663e900d4d2e9fec4140e1832f4e), available exclusively to users with VIP level 4 or higher.
  * If you are VIP level 3 or below, please contact your VIP manager for eligibility criterias.**



**Supported Products:**

  * Cross Margin
  * Isolated Margin
  * Portfolio Margin Pro
  * Cross Margin Pro (Additional agreement required and subject to meeting eligibility criteria)



**Unsupported Products:**

  * Portfolio Margin



We support several types of API keys:

  * Ed25519 (recommended)
  * HMAC
  * RSA



We recommend to **use Ed25519 API keys** as it should provide the best performance and security out of all supported key types. We accept PKCS#8 (BEGIN PUBLIC KEY). For how to generate an RSA key pair to send API requests on Binance. Please refer to the document below [FAQ](https://www.binance.com/en/support/faq/how-to-generate-an-rsa-key-pair-to-send-api-requests-on-binance-2b79728f331e43079b27440d9d15c5db) .

## How to use the Margin Special Key[​](/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#how-to-use-the-margin-special-key "Direct link to How to use the Margin Special Key")

  * Use the below `sapi` endpoint to create your margin special API Key.
  * For accessing the Cross Margin account, do not send the `symbol` parameter.
  * For accessing the Isolated Margin account(s), pass the relevant `symbol` parameter in the API Key creation request.
  * Use the generated API Key (and Secret key, if applicable) to perform margin trading and listenKey generation via **Spot** REST API (`https://api.binance.com/api/v3/*`) endpoints.



Read [REST API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#signed-trade-and-user_data-endpoint-security) or [WebSocket API](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md#request-security) documentation to learn how to use different API keys

You need to enable Permits “Enable Spot & Margin Trading” option for the API Key which requests this endpoint.

## HTTP Request[​](/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#http-request "Direct link to HTTP Request")

POST `/sapi/v1/margin/apiKey`

## Request Weight[​](/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#request-weight "Direct link to Request Weight")

**1(UID)**

## Request Parameters[​](/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
apiName| STRING| YES|   
symbol| STRING| NO| isolated margin pair  
ip| STRING| NO| Can be added in batches, separated by commas. Max 30 for an API key  
publicKey| STRING| NO| 1\. If publicKey is inputted it will create an RSA or Ed25519 key.   
2\. Need to be encoded to URL-encoded format  
permissionMode| enum| NO| This parameter is only for the Ed25519 API key, and does not effact for other encryption methods. The value can be TRADE (TRADE for all permissions) or READ (READ for USER_DATA, FIX_API_READ_ONLY). The default value is TRADE.  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## Response Example[​](/docs/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#response-example "Direct link to Response Example")
    
    
    {  
      "apiKey":"npOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoGx",  
      "secretKey":"87ssWB7azoy6ACRfyp6OVOL5U3rtZptX31QWw2kWjl1jHEYRbyM1pd6qykRBQw8p" //secretKey will be null when creating an RSA key  
      "type": "HMAC_SHA256"   //HMAC_SHA256 or RSA  
    }  
    

Error Code Description

  * **UNSUPPORTED_OPERATION** : Portfolio Margin is an unsupported product, please change the account type to a supported margin product.
  * **Forbidden** : Cross Margin Pro accounts require additional agreements, please contact your relationship manager.

---

# 新建低延迟交易SpecialKey(TRADE)

## 接口描述[​](/docs/zh-CN/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#接口描述 "接口描述的直接链接")

  * 杠杆交易为VIP4及以上的用户提供了低延迟交易接口，这类接口通过特定的[SpecialKey](https://www.binance.com/zh-CN/support/faq/%E5%B8%81%E5%AE%89%E6%9D%A0%E6%9D%86-margin-special-key-%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98-3208663e900d4d2e9fec4140e1832f4e)实现杠杆交易。
  * 若您的VIP级别为3及以下，请联系您的VIP经理获取相关SpecialKey的使用许可标准。



**该接口支持以下产品：**

  * 全仓杠杆
  * 逐仓杠杆
  * 统一账户Pro模式
  * 全仓杠杆Pro模式（需要签订额外的协议并符合资格标准）



**该接口不支持以下产品：**

  * 统一账户普通模式



我们提供以下3类接口：

  * Ed25519 (recommended)
  * HMAC
  * RSA



这3类接口中，我们推荐用户使用**use Ed25519 API keys** ，它具有最高的性能和安全系数。

我们接受PKCS#8 (BEGIN PUBLIC KEY). 关于如何生成RSA密钥对发送API请求，请参考 [FAQ](https://www.binance.com/zh-TC/support/faq/%E5%A6%82%E4%BD%95%E5%9C%A8%E5%B9%A3%E5%AE%89%E4%B8%8A%E7%94%9F%E6%88%90-rsa-%E9%87%91%E9%91%B0%E5%B0%8D%E4%B8%A6%E7%99%BC%E9%80%81-api-%E8%AB%8B%E6%B1%82-2b79728f331e43079b27440d9d15c5db) 。

## 如何使用杠杆专用密钥[​](/docs/zh-CN/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#如何使用杠杆专用密钥 "如何使用杠杆专用密钥的直接链接")

  * 使用以下 `sapi` 接口创建您的杠杆专用 SpecialKey。
  * 关于访问全仓杠杆账户，请勿发送 `symbol` 参数。
  * 关于访问逐仓杠杆账户，请在创建 SpecialKey 的请求中传入相关的 `symbol` 参数。
  * 使用生成的 SpecialKey（以及对应的 Secret key，如适用）通过 **现货** REST API (`https://api.binance.com/api/v3/*`) 端点执行杠杆交易和 listenKey 生成操作。



关于如何使用其他API，请参考[REST API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#signed-trade-and-user_data-endpoint-security) 或 [WebSocket API](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md#request-security) 。

您需要为special key开通"允许现货及杠杆交易"权限才能调用此接口。

## HTTP请求[​](/docs/zh-CN/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/margin/apiKey`

## 请求权重[​](/docs/zh-CN/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#请求权重 "请求权重的直接链接")

**1(UID)**

## 请求参数[​](/docs/zh-CN/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#请求参数 "请求参数的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
apiName| STRING| YES|   
symbol| STRING| NO| isolated margin pair  
ip| STRING| NO| Can be added in batches, separated by commas. Max 30 for an API key  
publicKey| STRING| NO| 1\. If publicKey is inputted it will create an RSA or Ed25519 key.   
2\. Need to be encoded to URL-encoded format  
permissionMode| ENUM| NO| 该参数只对Ed25519 API密钥有效，若为其他加密方式不需要传递该参数。取值为 TRADE （TRADE表示所有权限） 或 READ（READ表示 USER_DATA, FIX_API_READ_ONLY）。 默认取值为TRADE。  
recvWindow| LONG| NO| The value cannot be greater than `60000`  
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/margin_trading/trade/Create-Special-Key-of-Low-Latency-Trading#响应示例 "响应示例的直接链接")
    
    
    {  
      "apiKey":"npOzOAeLVgr2TuxWfNo43AaPWpBbJEoKezh1o8mSQb6ryE2odE11A4AoVlJbQoGx",  
      "secretKey":"87ssWB7azoy6ACRfyp6OVOL5U3rtZptX31QWw2kWjl1jHEYRbyM1pd6qykRBQw8p", //secretKey will be null when creating an RSA key  
      "type": "HMAC_SHA256"   //HMAC_SHA256 or RSA  
    }  
    

**常见错误代码：**

  * **UNSUPPORTED_OPERATION** : 该接口不支持统一账户普通模式，请转换账户类型到支持该接口的产品模式。

  * **Forbidden** : 全仓Pro模式需要签订额外的协议，请联系您的VIP经历获得相应支持。