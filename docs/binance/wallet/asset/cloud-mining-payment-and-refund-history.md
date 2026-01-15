---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/asset/cloud-mining-payment-and-refund-history
api_type: REST
updated_at: 2026-01-15T23:49:27.194017
---

# Get Cloud-Mining payment and refund history (USER_DATA)

## API Description[​](/docs/wallet/asset/cloud-mining-payment-and-refund-history#api-description "Direct link to API Description")

The query of Cloud-Mining payment and refund history

## HTTP Request[​](/docs/wallet/asset/cloud-mining-payment-and-refund-history#http-request "Direct link to HTTP Request")

GET `/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`

## Request Weight(UID)[​](/docs/wallet/asset/cloud-mining-payment-and-refund-history#request-weightuid "Direct link to Request Weight\(UID\)")

**600**

## Request Parameters[​](/docs/wallet/asset/cloud-mining-payment-and-refund-history#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
tranId| LONG| NO| The transaction id  
clientTranId| STRING| NO| The unique flag  
asset| STRING| NO| If it is blank, we will query all assets  
startTime| LONG| YES| inclusive, unit: ms  
endTime| LONG| YES| exclusive, unit: ms  
current| INTEGER| NO| current page, default 1, the min value is 1  
size| INTEGER| NO| page size, default 10, the max value is 100  
  
>   * Just return the SUCCESS records of payment and refund.
>   * For response, type = 248 means payment, type = 249 means refund, status =S means SUCCESS.
> 


## Response Example[​](/docs/wallet/asset/cloud-mining-payment-and-refund-history#response-example "Direct link to Response Example")
    
    
    {  
      "total":5,  
      "rows":[  
        {"createTime":1667880112000,"tranId":121230610120,"type":248,"asset":"USDT","amount":"25.0068","status":"S"},  
        {"createTime":1666776366000,"tranId":119991507468,"type":249,"asset":"USDT","amount":"0.027","status":"S"},  
        {"createTime":1666764505000,"tranId":119977966327,"type":248,"asset":"USDT","amount":"0.027","status":"S"},  
        {"createTime":1666758189000,"tranId":119973601721,"type":248,"asset":"USDT","amount":"0.018","status":"S"},  
        {"createTime":1666757278000,"tranId":119973028551,"type":248,"asset":"USDT","amount":"0.018","status":"S"}  
      ]  
    }

---

# 云算力历史记录分页查询(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/asset/cloud-mining-payment-and-refund-history#接口描述 "接口描述的直接链接")

云算力支付和退款历史分页查询

## HTTP请求[​](/docs/zh-CN/wallet/asset/cloud-mining-payment-and-refund-history#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/asset/ledger-transfer/cloud-mining/queryByPage`

## 请求权重(UID)[​](/docs/zh-CN/wallet/asset/cloud-mining-payment-and-refund-history#请求权重uid "请求权重\(UID\)的直接链接")

**600**

## 请求参数[​](/docs/zh-CN/wallet/asset/cloud-mining-payment-and-refund-history#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
tranId| LONG| NO| 流水号  
clientTranId| STRING| NO| 外部唯一流水号  
asset| STRING| NO| 不传或者空字符串查全部  
startTime| LONG| YES| 开始时间（包含），单位：毫秒  
endTime| LONG| YES| 结束时间（不包含），单位：毫秒  
current| INTEGER| NO| 当前页面，默认1，最小值为1  
size| INTEGER| NO| 页面大小，默认10，最大值为100  
  
## 响应示例[​](/docs/zh-CN/wallet/asset/cloud-mining-payment-and-refund-history#响应示例 "响应示例的直接链接")
    
    
    {  
      "total":5,  
      "rows":[  
        {"createTime":1667880112000,"tranId":121230610120,"type":248,"asset":"USDT","amount":"25.0068","status":"S"},  
        {"createTime":1666776366000,"tranId":119991507468,"type":249,"asset":"USDT","amount":"0.027","status":"S"},  
        {"createTime":1666764505000,"tranId":119977966327,"type":248,"asset":"USDT","amount":"0.027","status":"S"},  
        {"createTime":1666758189000,"tranId":119973601721,"type":248,"asset":"USDT","amount":"0.018","status":"S"},  
        {"createTime":1666757278000,"tranId":119973028551,"type":248,"asset":"USDT","amount":"0.018","status":"S"}  
      ]  
    }