---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub
api_type: Account
updated_at: 2026-01-15T23:51:26.589749
---

# Query Managed Sub Account Transfer Log (For Trading Team Sub Account) (USER_DATA)

## API Description[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#api-description "Direct link to API Description")

Query Managed Sub Account Transfer Log (For Trading Team Sub Account)

## HTTP Request[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#http-request "Direct link to HTTP Request")

GET `/sapi/v1/managed-subaccount/query-trans-log`

## Request Weight(UID)[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#request-weightuid "Direct link to Request Weight\(UID\)")

**60**

## Request Parameters[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| YES| Start Time  
endTime| LONG| YES| End Time (The start time and end time interval cannot exceed half a year)  
page| INT| YES| Page  
limit| INT| YES| Limit (Max: 500)  
transfers| STRING| NO| Transfer Direction (FROM/TO)  
transferFunctionAccountType| STRING| NO| Transfer function account type (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## Response Example[​](/docs/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#response-example "Direct link to Response Example")
    
    
    {  
        "managerSubTransferHistoryVos": [  
            {  
                "fromEmail": "test_0_virtual@kq3kno9imanagedsub.com",  
                "fromAccountType": "SPOT",  
                "toEmail": "wdywl0lddakh@test.com",  
                "toAccountType": "SPOT",  
                "asset": "BNB",  
                "amount": "0.01",  
                "scheduledData": 1679416673000,  
                "createTime": 1679416673000,  
                "status": "SUCCESS",  
                "tranId": 91077779  
            },  
            {  
                "fromEmail": "wdywl0lddakh@test.com",  
                "fromAccountType": "SPOT",  
                "toEmail": "test_0_virtual@kq3kno9imanagedsub.com",  
                "toAccountType": "SPOT",  
                "asset": "BNB",  
                "amount": "1",  
                "scheduledData": 1679416616000,  
                "createTime": 1679416616000,  
                "status": "SUCCESS",  
                "tranId": 91077676  
            }  
        ],  
        "count": 2  
    }

---

# 查询托管子账户的划转记录 (适用交易团队子账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#接口描述 "接口描述的直接链接")

查询托管子账户的划转记录(适用交易团队子账户)

## HTTP请求[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/managed-subaccount/query-trans-log`

## 请求权重(UID)[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#请求权重uid "请求权重\(UID\)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#请求参数 "请求参数的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
startTime| LONG| YES| 开始时间  
endTime| LONG| YES| 结束时间(开始时间结束时间间隔不能超过半年)  
page| INT| YES| 页数  
limit| INT| YES| 每页数量 (最大值: 500)  
transfers| STRING| NO| 划转方向 (FROM/TO)  
transferFunctionAccountType| STRING| NO| 划转账户类型 (SPOT/MARGIN/ISOLATED_MARGIN/USDT_FUTURE/COIN_FUTURE)  
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
## 响应示例[​](/docs/zh-CN/sub_account/managed-sub-account/Query-Managed-Sub-Account-Transfer-Log-Trading-Team-Sub#响应示例 "响应示例的直接链接")
    
    
    {  
        "managerSubTransferHistoryVos": [  
            {  
                "fromEmail": "test_0_virtual@kq3kno9imanagedsub.com",  
                "fromAccountType": "SPOT",  
                "toEmail": "wdywl0lddakh@test.com",  
                "toAccountType": "SPOT",  
                "asset": "BNB",  
                "amount": "0.01",  
                "scheduledData": 1679416673000,  
                "createTime": 1679416673000,  
                "status": "SUCCESS",  
                "tranId": 91077779  
            },  
            {  
                "fromEmail": "wdywl0lddakh@test.com",  
                "fromAccountType": "SPOT",  
                "toEmail": "test_0_virtual@kq3kno9imanagedsub.com",  
                "toAccountType": "SPOT",  
                "asset": "BNB",  
                "amount": "1",  
                "scheduledData": 1679416616000,  
                "createTime": 1679416616000,  
                "status": "SUCCESS",  
                "tranId": 91077676  
            }  
        ],  
        "count": 2  
    }