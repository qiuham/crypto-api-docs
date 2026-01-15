---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/deposit-history
api_type: REST
updated_at: 2026-01-15T23:49:50.426303
---

# Deposit History (for local entities that required travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/deposit-history#api-description "Direct link to API Description")

Fetch deposit history for local entities that required travel rule.

## HTTP Request[​](/docs/wallet/travel-rule/deposit-history#http-request "Direct link to HTTP Request")

GET `/sapi/v1/localentity/deposit/history`

## Request Weight(IP)[​](/docs/wallet/travel-rule/deposit-history#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/wallet/travel-rule/deposit-history#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
trId| STRING| NO| Comma(,) separated list of travel rule record Ids.  
txId| STRING| NO| Comma(,) separated list of transaction Ids.  
tranId| STRING| NO| Comma(,) separated list of wallet tran Ids.  
network| STRING| NO|   
coin| STRING| NO|   
travelRuleStatus| INTEGER| NO| 0:Completed,1:Pending,2:Failed  
pendingQuestionnaire| BOOLEAN| NO| true: Only return records that pending deposit questionnaire. false/not provided: return all records.  
startTime| LONG| NO| Default: 90 days from current timestamp  
endTime| LONG| NO| Default: present timestamp  
offset| INT| NO| Default:0  
limit| INT| NO| Default:1000, Max:1000  
timestamp| LONG| YES|   
  
>   * Please notice the default `startTime` and `endTime` to make sure that time interval is within 0-90 days.
>   * If both `startTime` and `endTime` are sent, time between `startTime` and `endTime` must be less than 90 days.
> 


## Response Example[​](/docs/wallet/travel-rule/deposit-history#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "trId": 123451123,  
            "tranId": 17644346245865,  
            "amount": "0.001",  
            "coin": "BNB",  
            "network": "BNB",  
            "depositStatus": 0,  
            "travelRuleStatus": 1,  
            "address": "bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23",  
            "addressTag": "101764890",  
            "txId": "98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC",  
            "insertTime": 1661493146000,  
            "transferType": 0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0,  
            "requireQuestionnaire": false, // true: This deposit require user to answer questionnaire to get it credited  
                                           // false: This deposit doesn't require user to answer questionnaire as it's already completed or information has been verified  
            "questionnaire": null  
        },  
        {  
            "trId": 2451123,  
            "tranId": 4544346245865,  
            "amount":"0.50000000",  
            "coin":"IOTA",  
            "network":"IOTA",  
            "depositStatus": 0,  
            "travelRuleStatus": 0,  
            "address":"SIZ9VLMHWATXKV99LH99CIGFJFUMLEHGWVZVNNZXRJJVWBPHYWPPBOSDORZ9EQSHCZAMPVAPGFYQAUUV9DROOXJLNW",  
            "addressTag":"",  
            "txId":"ESBFVQUTPIWQNJSPXFNHNYHSQNTGKRVKPRABQWTAXCDWOAKDKYWPTVG9BGXNVNKTLEJGESAVXIKIZ9999",  
            "insertTime":1599620082000,  
            "transferType":0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0,  
            "requireQuestionnaire": false,  
            "questionnaire": "{\'question1\':\'answer1\',\'question2\':\'answer2\'}"  
        }  
    ]

---

# 获取充值历史(针对需要旅行规则的本地站)(支持多网络)

## 接口描述[​](/docs/zh-CN/wallet/travel-rule/deposit-history#接口描述 "接口描述的直接链接")

获取充值历史(针对需要旅行规则的本地站)(支持多网络)

## HTTP请求[​](/docs/zh-CN/wallet/travel-rule/deposit-history#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/localentity/deposit/history`

## 请求权重(IP)[​](/docs/zh-CN/wallet/travel-rule/deposit-history#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/wallet/travel-rule/deposit-history#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
trId| STRING| NO| 旅行规则记录ID，支持多条查询，以半角逗号(,) 分隔  
txId| STRING| NO| 链上TxId，支持多条查询，以半角逗号(,) 分隔  
tranId| STRING| NO| 充值记录ID，支持多条查询，以半角逗号(,) 分隔  
network| STRING| NO|   
coin| STRING| NO|   
travelRuleStatus| INTEGER| NO| 0:处理完成，1:等待处理，2:请求被拒绝  
pendingQuestionnaire| BOOLEAN| NO| true: 只返回需要回答充值问卷的记录，false/缺省:返回所有记录  
startTime| LONG| NO| 默认当前时间90天前的时间戳  
endTime| LONG| NO| 默认当前时间戳  
offset| INTEGER| NO| 默认:0  
limit| INTEGER| NO| 默认:1000，最大1000  
timestamp| LONG| YES|   
  
>   * 请注意`startTime` 与 `endTime` 的默认时间戳，保证请求时间间隔不超过90天。
>   * 同时提交`startTime` 与 `endTime`间隔不得超过90天。
>   * 请注意，由于网络特定的特性，返回的源地址可能不准确。 如果找到多个源地址，则仅返回第一个地址。
> 


## 响应示例[​](/docs/zh-CN/wallet/travel-rule/deposit-history#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "trId": 123451123,  
            "tranId": 17644346245865,  
            "amount": "0.001",  
            "coin": "BNB",  
            "network": "BNB",  
            "depositStatus": 0,  
            "travelRuleStatus": 1,  
            "address": "bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23",  
            "addressTag": "101764890",  
            "txId": "98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC",  
            "insertTime": 1661493146000,  
            "transferType": 0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0,  
            "requireQuestionnaire": false, // true: This deposit require user to answer questionnaire to get it credited  
                                           // false: This deposit doesn't require user to answer questionnaire as it's already completed or information has been verified  
            "questionnaire": null  
        },  
        {  
            "trId": 2451123,  
            "tranId": 4544346245865,  
            "amount":"0.50000000",  
            "coin":"IOTA",  
            "network":"IOTA",  
            "depositStatus": 0,  
            "travelRuleStatus": 0,  
            "address":"SIZ9VLMHWATXKV99LH99CIGFJFUMLEHGWVZVNNZXRJJVWBPHYWPPBOSDORZ9EQSHCZAMPVAPGFYQAUUV9DROOXJLNW",  
            "addressTag":"",  
            "txId":"ESBFVQUTPIWQNJSPXFNHNYHSQNTGKRVKPRABQWTAXCDWOAKDKYWPTVG9BGXNVNKTLEJGESAVXIKIZ9999",  
            "insertTime":1599620082000,  
            "transferType":0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0,  
            "requireQuestionnaire": false,  
            "questionnaire": "{\'question1\':\'answer1\',\'question2\':\'answer2\'}"  
        }  
    ]