---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/trade-data-stream
api_type: Trading
updated_at: 2026-01-15T23:48:39.691126
---

# listenToken Subscription Methods

## Create Margin Account listenToken (USER_STREAM)[​](/docs/margin_trading/trade-data-stream#create-margin-account-listentoken-user_stream "Direct link to Create Margin Account listenToken \(USER_STREAM\)")

### Description[​](/docs/margin_trading/trade-data-stream#description "Direct link to Description")

Create a listenToken that authorizes the user to access the User Data Stream of the current account for a limited amout of time. The stream's validity is specified by the validity parameter (milliseconds), default 24 hours, maximum 24 hours. The response includes the listenToken and the corresponding expirationTime (in milliseconds).

### HTTP Request[​](/docs/margin_trading/trade-data-stream#http-request "Direct link to HTTP Request")

**POST** `/sapi/v1/userListenToken`

**Request weight (UID)** : 1

### Request Parameters[​](/docs/margin_trading/trade-data-stream#request-parameters "Direct link to Request Parameters")

Name| Type| Required| Description  
---|---|---|---  
symbol| STRING| CONDITIONAL| Trading pair symbol; required when isIsolated is true, e.g., BNBUSDT  
isIsolated| BOOLEAN| NO| Whether it is isolated margin; true means isolated; default is cross margin  
validity| LONG| NO| Validity in milliseconds; default 24 hours, maximum 24 hours  
  
### Notes[​](/docs/margin_trading/trade-data-stream#notes "Direct link to Notes")

  * The token validity is determined by the validity parameter; default is 24 hours, maximum 24 hours. expirationTime = current time + validity.
  * The response returns the token and expirationTime.



### Response Example[​](/docs/margin_trading/trade-data-stream#response-example "Direct link to Response Example")
    
    
    {  
      "token": "6xXxePXwZRjVSHKhzUCCGnmN3fkvMTXru+pYJS8RwijXk9Vcyr3rkwfVOTcP2OkONqciYA",  
      "expirationTime": 1758792204196  
    }  
    

## Subscribe to User Data Stream using listenToken (USER_STREAM)[​](/docs/margin_trading/trade-data-stream#subscribe-to-user-data-stream-using-listentoken-user_stream "Direct link to Subscribe to User Data Stream using listenToken \(USER_STREAM\)")

### Description[​](/docs/margin_trading/trade-data-stream#description-1 "Direct link to Description")

Subscribe to the user data stream using listenToken.

This method must be called on the WebSocket API. For more information about how to use the WebSocket API, see : [WebSocket API documentation](https://developers.binance.com/docs/binance-spot-api-docs/websocket-api/general-api-information)

### method[​](/docs/margin_trading/trade-data-stream#method "Direct link to method")

`userDataStream.subscribe.listenToken`

### Request Example[​](/docs/margin_trading/trade-data-stream#request-example "Direct link to Request Example")
    
    
    {  
      "id": "f3a8f7a29f2e54df796db582f3d",  
      "method": "userDataStream.subscribe.listenToken",  
      "params": {  
        "listenToken": "5DbylArkmImhyHkpG6s9tbiFy5uAMTFwzx9vwsFjDv9dC3GkKxSuoTCj0HvcJC0WYi8fA"  
      }  
    }  
    

### **Request weight** : 2[​](/docs/margin_trading/trade-data-stream#request-weight-2 "Direct link to request-weight-2")

### Request Parameters[​](/docs/margin_trading/trade-data-stream#request-parameters-1 "Direct link to Request Parameters")

Name| Type| Required| Description  
---|---|---|---  
listenToken| STRING| YES| The listen token  
  
### Notes[​](/docs/margin_trading/trade-data-stream#notes-1 "Direct link to Notes")

  * Non-authenticated sessions are allowed to use this feature.
  * If the listenToken is invalid, an error **-1209** will be returned.
  * The subscription is not automatically renewed by the WebSocket API. To extend the validity of your subscription, you must call `/sapi/v1/userListenToken` before the expiration of your current subscription, obtain a new listenToken with an updated expirationTime, and call `userDataStream.subscribe.listenToken` again passing the new listenToken. This will seamlessly extend your subscription to the new expirationDate.
  * If the subscription is not extended, it will expire and you will receive a `eventStreamTerminated` event (see example below).
  * You can receive the events in SBE instead of JSON if you require better performance. See the [Simple Binary Encoding (SBE) FAQ](https://developers.binance.com/docs/binance-spot-api-docs/faqs/sbe_faq) for more details.



### Response Example[​](/docs/margin_trading/trade-data-stream#response-example-1 "Direct link to Response Example")
    
    
    {  
      "subscriptionId": 1,  
      "expirationTime": 1749094553955907  
    }  
    

### Subscription Expiration Example[​](/docs/margin_trading/trade-data-stream#subscription-expiration-example "Direct link to Subscription Expiration Example")
    
    
    {  
      "subscriptionId": 0,  
      "event": {  
        "e": "eventStreamTerminated",  
        "E": 1759089357377  
      }  
    }

---

# listenToken订阅用户数据流

## 生成杠杆账户listenToken(USER_STREAM)[​](/docs/zh-CN/margin_trading/trade-data-stream#生成杠杆账户listentokenuser_stream "生成杠杆账户listenToken\(USER_STREAM\)的直接链接")

### 接口描述[​](/docs/zh-CN/margin_trading/trade-data-stream#接口描述 "接口描述的直接链接")

创建一个新的listenToken，授权用户在限定时间内访问当前账户的用户数据流。数据流的有效期由validity参数指定（毫秒） ，数据流的有效期由 validity 参数（毫秒）指定，默认为 24 小时，最长为 24 小时。响应中包含 listenToken 和相应的 expirationTime（以毫秒为单位）。

### HTTP请求[​](/docs/zh-CN/margin_trading/trade-data-stream#http请求 "HTTP请求的直接链接")

**POST** `/sapi/v1/userListenToken`

**请求权重(UID)** : 1

### 请求参数[​](/docs/zh-CN/margin_trading/trade-data-stream#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| CONDITIONAL| 交易对名称，当isIsolated为true时必填，例如：BNBUSDT  
isIsolated| BOOLEAN| NO| 是否为逐仓杠杆，true表示逐仓，默认为全仓  
validity| LONG| NO| 有效期（毫秒） ，默认24小时，最大24小时  
  
### 说明[​](/docs/zh-CN/margin_trading/trade-data-stream#说明 "说明的直接链接")

  * 数据流的有效期由validity参数指定，默认24小时，最大24小时。过期时间 = 当前时间 + 有效期。
  * 返回token和过期时间expirationTime。



### 响应示例[​](/docs/zh-CN/margin_trading/trade-data-stream#响应示例 "响应示例的直接链接")
    
    
    {  
      "token": "6xXxePXwZRjVSHKhzUCCGnmN3fkvMTXru+pYJS8RwijXk9Vcyr3rkwfVOTcP2OkONqciYA",  
      "expirationTime": 1758792204196  
    }  
    

## 订阅用户数据流使用listenToken (USER_STREAM)[​](/docs/zh-CN/margin_trading/trade-data-stream#订阅用户数据流使用listentoken-user_stream "订阅用户数据流使用listenToken \(USER_STREAM\)的直接链接")

### 接口描述[​](/docs/zh-CN/margin_trading/trade-data-stream#接口描述-1 "接口描述的直接链接")

使用 listenToken 订阅用户数据流。

该方法必需由WebSocket API调用。关于WebSocket API的更多信息请参考:[WebSocket API](https://developers.binance.com/docs/zh-CN/binance-spot-api-docs/websocket-api/general-api-information) 。

### 请求示例[​](/docs/zh-CN/margin_trading/trade-data-stream#请求示例 "请求示例的直接链接")
    
    
    {  
      "id": "f3a8f7a29f2e54df796db582f3d",  
      "method": "userDataStream.subscribe.listenToken",  
       "params": {  
          "listenToken": "5DbylArkmImhyHkpG6s9tbiFy5uAMTFwzx9vwsFjDv9dC3GkKxSuoTCj0HvcJC0WYi8  
      }  
    }  
    

### 请求权重(UID)：2[​](/docs/zh-CN/margin_trading/trade-data-stream#请求权重uid2 "请求权重\(UID\)：2的直接链接")

### 请求参数[​](/docs/zh-CN/margin_trading/trade-data-stream#请求参数-1 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
listenToken| STRING| YES| 监听token  
  
### 说明[​](/docs/zh-CN/margin_trading/trade-data-stream#说明-1 "说明的直接链接")

  * 允许非登录会话使用此功能。
  * 如果 listenToken 无效，将返回错误代码 **-1209** 。
  * WebSocket API 不会自动续订订阅。要延长订阅的有效期，您必须在当前订阅到期前调用 `/sapi/v1/userListenToken`，获取一个包含更新后的 expirationTime 的新 listenToken，然后再次调用 `userDataStream.subscribe.listenToken` 并传入新的 listenToken。这样可以无缝地将您的订阅续订至新的 expirationDate。
  * 如果订阅未延长，它将过期，您将收到“eventStreamTerminated”事件（见下面的示例）。
  * 如果您需要更佳性能，可以使用 SBE 格式而非 JSON 格式接收事件。更多详情，请参阅[简单二进制编码 (SBE) 常见问题解答](https://developers.binance.com/docs/zh-CN/binance-spot-api-docs/faqs/sbe_faq)



### 响应示例[​](/docs/zh-CN/margin_trading/trade-data-stream#响应示例-1 "响应示例的直接链接")
    
    
    {  
      "subscriptionId": 0,  
      "expirationTime": 1749094553955907  
    }  
    

### 订阅过期示例[​](/docs/zh-CN/margin_trading/trade-data-stream#订阅过期示例 "订阅过期示例的直接链接")
    
    
    {  
      "subscriptionId": 0,  
      "event": {  
        "e": "eventStreamTerminated",  
        "E": 1759089357377  
      }  
    }