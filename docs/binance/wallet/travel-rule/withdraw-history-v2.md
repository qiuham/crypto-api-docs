---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/withdraw-history-v2
api_type: REST
updated_at: 2026-01-15T23:49:56.074134
---

# Withdraw History V2 (for local entities that require travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/withdraw-history-v2#api-description "Direct link to API Description")

Fetch withdraw history for local entities that required travel rule.

## HTTP Request[​](/docs/wallet/travel-rule/withdraw-history-v2#http-request "Direct link to HTTP Request")

GET `/sapi/v2/localentity/withdraw/history`

## Request Weight(IP)[​](/docs/wallet/travel-rule/withdraw-history-v2#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/travel-rule/withdraw-history-v2#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
trId| STRING| NO| Comma(,) separated list of travel rule record Ids.  
txId| STRING| NO| Comma(,) separated list of transaction Ids.  
withdrawOrderId| STRING| NO| Withdraw ID defined by the client (i.e. client's internal withdrawID).  
network| STRING| NO|   
coin| STRING| NO|   
travelRuleStatus| INTEGER| NO| 0:Completed,1:Pending,2:Failed  
offset| INT| NO| Default: 0  
limit| INT| NO| Default: 1000, Max: 1000  
startTime| LONG| NO| Default: 90 days from current timestamp  
endTime| LONG| NO| Default: present timestamp  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * `network` may not be in the response for old withdraw.
>   * Withdrawal made through /sapi/v1/capital/withdraw/apply may not be in the response.
>   * Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
>   * If both `startTime` and `endTime`are sent, time between `startTime`and `endTime`must be less than 90 days.
>   * If withdrawOrderId is sent, time between startTime and endTime must be less than 7 days.
>   * If withdrawOrderId is sent, startTime and endTime are not sent, will return last 7 days records by default.
>   * Maximum support trId,txId number is 45.
>   * WithdrawOrderId only support 1.
>   * If responsible does not include withdrawalStatus, please input trId or txId retrieve the data.
> 


## Response Example[​](/docs/wallet/travel-rule/withdraw-history-v2#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "id": "b6ae22b3aa844210a7041aee7589627c",  // Withdrawal id in Binance  
        "trId": 1234456,  // Travel rule record id  
        "amount": "8.91000000",   // withdrawal amount  
        "transactionFee": "0.004", // only available for sAPI requests  
        "coin": "USDT",  
        "withdrawalStatus": 6, // Capital withdrawal status, only available for sAPI requests  
        "travelRuleStatus": 0, // Travel rule status.  
        "address": "0x94df8b352de7f46f64b01d3666bf6e936e44ce60",  
        "addressTag": "1231212",  
        "txId": "0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268"   // withdrawal transaction id  
        "applyTime": "2019-10-12 11:12:02",  // UTC time  
        "network": "ETH",  
        "transferType": 0 // 1 for internal transfer, 0 for external transfer, only available for sAPI requests    
        "withdrawOrderId": "WITHDRAWtest123", // will not be returned if there's no withdrawOrderId for this withdraw, only available for sAPI requests  
        "info": "The address is not valid. Please confirm with the recipient",  // reason for withdrawal failure, only available for sAPI requests  
        "confirmNo":3,  // confirm times for withdraw, only available for sAPI requests  
        "walletType": 1,  //1: Funding Wallet 0:Spot Wallet, only available for sAPI requests  
        "txKey": "", // only available for sAPI requests  
        "questionnaire": "{\'question1\':\'answer1\',\'question2\':\'answer2\'}", // The answers of the questionnaire  
        "completeTime": "2023-03-23 16:52:41" // complete UTC time when user's asset is deduct from withdrawing, only if status =  6(success)  
      },  
      {  
        "id": "156ec387f49b41df8724fa744fa82719",  
        "trId": 2231556234,  
        "amount": "0.00150000",  
        "transactionFee": "0.004",  
        "coin": "BTC",  
        "withdrawalStatus": 6,  
        "travelRuleStatus": 0,  
        "address": "1FZdVHtiBqMrWdjPyRPULCUceZPJ2WLCsB",  
        "txId": "60fd9007ebfddc753455f95fafa808c4302c836e4d1eebc5a132c36c1d8ac354"  
        "applyTime": "2019-09-24 12:43:45",  
        "network": "BTC",  
        "transferType": 0,  
        "info": "",  
        "confirmNo": 2,  
        "walletType": 1,  
        "txKey": "",  
        "questionnaire": "{\'question1\':\'answer1\',\'question2\':\'answer2\'}",  
        "completeTime": "2023-03-23 16:52:41"  
      }  
    ]

---

# 获取提币历史V2(针对需要旅行规则的本地站)(支持多网络)(USER_DATA)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/withdraw-history-v2#接口描述 "接口描述的直接链接")

获取需要旅行规则的本地站的提币历史记录

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/withdraw-history-v2#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/localentity/withdraw/history`

## 请求权重(IP)[​](/docs/zh-CN/wallet/travel-rule/withdraw-history-v2#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/withdraw-history-v2#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
trId| STRING| NO| 旅行规则记录ID, 支持多条查询，以半角逗号(,) 分隔.  
txId| STRING| NO| 链上TxId，支持多条查询，以半角逗号(,) 分隔.  
withdrawOrderId| STRING| NO| 客户端内部定义的提币ID.  
network| STRING| NO|   
coin| STRING| NO|   
travelRuleStatus| INTEGER| NO| 0:处理完成,1:处理中,2:请求被拒绝  
offset| INT| NO|   
limit| INT| NO| 默认：1000， 最大：1000  
startTime| LONG| NO| 默认当前时间90天前的时间戳  
endTime| LONG| NO| 默认当前时间戳  
timestamp| LONG| YES|   
  
>   * 支持多网络提币前的历史记录可能不会返回`network`字段。
>   * 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不得超过90天。
>   * 同时提交`startTime` 与 `endTime`间隔不得超过90天。
>   * 通过API：/sapi/v1/capital/withdraw/apply 提交的提币记录，可能通过该API无法获取内容。
>   * 如果通过`withdrawOrderId`查询`startTime`和`endTime`的默认时间间隔为7天.
>   * 如果通过`withdrawOrderId`查询`startTime`和`endTime`间隔不得超过7天.
>   * 如果通过`trId`,`txId`查询，最大支持的ID数量是45.
>   * 如果通过`WithdrawOrderId` 查询，ID最多只支持一个.
>   * 如果返回结果中不包含`withdrawalStatus`等信息, 请传入`trId`或者`txId`来查询数据.
> 


## 响应示例[​](/docs/zh-CN/wallet/travel-rule/withdraw-history-v2#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "id": "b6ae22b3aa844210a7041aee7589627c",  // 该笔提现在币安的id, 只在sAPI提现的记录中返回  
        "trId": 1234456,  // 旅行规则记录Id  
        "amount": "8.91000000",   // 提现转出金额  
        "transactionFee": "0.004", // 手续费, 只在sAPI提现的记录中返回  
        "coin": "USDT",  
        "withdrawalStatus": 6, // 提币状态, 只在sAPI提现的记录中返回  
        "travelRuleStatus": 0, // 旅行规则处理状态，处理完成(0)之后才会继续提币流程  
        "address": "0x94df8b352de7f46f64b01d3666bf6e936e44ce60",  
        "txId": "0xb5ef8c13b968a406cc62a93a8bd80f9e9a906ef1b3fcf20a2e48573c17659268",   // 提现交易id  
        "applyTime": "2019-10-12 11:12:02",  // UTC 时间  
        "network": "ETH",  
        "transferType": 0, // 1: 站内转账, 0: 站外转账, 只在sAPI提现的记录中返回  
        "withdrawOrderId": "WITHDRAWtest123", // 自定义ID, 如果没有则不返回该字段, 只在sAPI提现的记录中返回  
        "info": "The address is not valid. Please confirm with the recipient",  // 提币失败原因  
        "confirmNo":3,  // 提现确认数, 只在sAPI提现的记录中返回  
        "walletType": 1,  //1: 资金钱包 0:现货钱包, 只在sAPI提现的记录中返回  
        "txKey": "", //只在sAPI提现的记录中返回  
        "questionnaire": "{\'question1\':\'answer1\',\'question2\':\'answer2\'}", // 问卷回答  
        "completeTime": "2023-03-23 16:52:41"  // 提现完成，成功下账时间(UTC)  
      },  
      {  
        "id": "156ec387f49b41df8724fa744fa82719",  
        "trId": 22334411,  
        "amount": "0.00150000",  
        "transactionFee": "0.004",  
        "coin": "BTC",  
        "withdrawalStatus": 6,  
        "travelRuleStatus": 0,  
        "address": "1FZdVHtiBqMrWdjPyRPULCUceZPJ2WLCsB",  
        "txId": "60fd9007ebfddc753455f95fafa808c4302c836e4d1eebc5a132c36c1d8ac354",  
        "applyTime": "2019-09-24 12:43:45",  
        "network": "BTC",  
        "transferType": 0,   
        "info": "",  
        "confirmNo": 2,  
        "walletType": 1,  
        "txKey": "",  
        "questionnaire": "{\'question1\':\'answer1\',\'question2\':\'answer2\'}",  
        "completeTime": "2023-03-23 16:52:41"   
      }  
    ]