---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Get-Sub-account-Deposit-History
api_type: Account
updated_at: 2026-01-15T23:51:05.491531
---

# Get Sub-account Deposit History (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-History#api-description "Direct link to API Description")

Fetch sub-account deposit history

## HTTP Request[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-History#http-request "Direct link to HTTP Request")

GET `/sapi/v1/capital/deposit/subHisrec`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-History#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-History#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
email| STRING| YES| Sub account email  
coin| STRING| NO|   
status| INT| NO| 0(0:pending,6: credited but cannot withdraw,7:Wrong Deposit,8:Waiting User confirm,1:success)  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO|   
offset| INT| NO| default:0  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
txId| STRING| NO|   
  
## Response Example[​](/docs/sub_account/asset-management/Get-Sub-account-Deposit-History#response-example "Direct link to Response Example")
    
    
    [  
        {  
            "id": "769800519366885376",  
            "amount": "0.001",  
            "coin": "BNB",  
            "network": "BNB",  
            "status": 0,  
            "address": "bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23",  
            "addressTag": "101764890",  
            "txId": "98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC",  
            "insertTime": 1661493146000,  
            "transferType": 0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0  
        },  
        {  
            "id": "769754833590042625",  
            "amount":"0.50000000",  
            "coin":"IOTA",  
            "network":"IOTA",  
            "status":1,  
            "address":"SIZ9VLMHWATXKV99LH99CIGFJFUMLEHGWVZVNNZXRJJVWBPHYWPPBOSDORZ9EQSHCZAMPVAPGFYQAUUV9DROOXJLNW",  
            "addressTag":"",  
            "txId":"ESBFVQUTPIWQNJSPXFNHNYHSQNTGKRVKPRABQWTAXCDWOAKDKYWPTVG9BGXNVNKTLEJGESAVXIKIZ9999",  
            "insertTime":1599620082000,  
            "transferType":0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0  
        }  
    ]

---

# 获取子账户充值记录 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-History#接口描述 "接口描述的直接链接")

获取子账户充值记录

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/capital/deposit/subHisrec `

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-History#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-History#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
email| STRING| YES| 子账户邮箱 [备注](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-History#request-email-address)  
coin| STRING| NO|   
status| INT| NO| 0(0:pending,6: credited but cannot withdraw,7:Wrong Deposit,8:Waiting User confirm,1:success)  
startTime| LONG| NO|   
endTime| LONG| NO|   
limit| INT| NO|   
offset| INT| NO| default:0  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
txId| STRING| NO|   
  
## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Sub-account-Deposit-History#响应示例 "响应示例的直接链接")
    
    
    [  
        {  
            "id": "769800519366885376",  
            "amount": "0.001",  
            "coin": "BNB",  
            "network": "BNB",  
            "status": 0,  
            "address": "bnb136ns6lfw4zs5hg4n85vdthaad7hq5m4gtkgf23",  
            "addressTag": "101764890",  
            "txId": "98A3EA560C6B3336D348B6C83F0F95ECE4F1F5919E94BD006E5BF3BF264FACFC",  
            "insertTime": 1661493146000,  
            "transferType": 0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0  
        },  
        {  
            "id": "769754833590042625",  
            "amount":"0.50000000",  
            "coin":"IOTA",  
            "network":"IOTA",  
            "status":1,  
            "address":"SIZ9VLMHWATXKV99LH99CIGFJFUMLEHGWVZVNNZXRJJVWBPHYWPPBOSDORZ9EQSHCZAMPVAPGFYQAUUV9DROOXJLNW",  
            "addressTag":"",  
            "txId":"ESBFVQUTPIWQNJSPXFNHNYHSQNTGKRVKPRABQWTAXCDWOAKDKYWPTVG9BGXNVNKTLEJGESAVXIKIZ9999",  
            "insertTime":1599620082000,  
            "transferType":0,  
            "confirmTimes": "1/1",  
            "unlockConfirm": 0,  
            "walletType": 0  
        }  
    ]