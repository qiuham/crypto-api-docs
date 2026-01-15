---
exchange: binance
source_url: https://developers.binance.com/docs/sub_account/asset-management/Get-Move-Position-History-for-Sub-account
api_type: Account
updated_at: 2026-01-15T23:51:05.368133
---

# Get Move Position History for Sub-account (For Master Account) (USER_DATA)

## API Description[​](/docs/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#api-description "Direct link to API Description")

Query move position history

## HTTP Request[​](/docs/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#http-request "Direct link to HTTP Request")

GET `/sapi/v1/sub-account/futures/move-position`

## Request Weight(IP)[​](/docs/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#request-weightip "Direct link to Request Weight\(IP\)")

**1**

## Request Parameters[​](/docs/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
symbol| STRING| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| YES|   
row| INT| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * If `startTime` and `endTime` not sent, return records of the last 90 days by default with 1000 maximum limits
>   * If `startTime` is sent and `endTime` is not sent, return records of [max(startTime, now-90d), now].
>   * If `startTime` is not sent and `endTime` is sent, return records of [max(now,endTime-90d), endTime].
> 


## Response Example[​](/docs/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#response-example "Direct link to Response Example")
    
    
    {  
    	"total": 3,  
    	"futureMovePositionOrderVoList": [{  
    		"fromUserEmail": "testFrom@google.com",  
    		"toUserEmail": "testTo@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"price": "105025.50981609",  
    		"quantity": "0.00100000",  
    		"positionSide": "BOTH",  
    		"side": "SELL",  
    		"timeStamp": 1737544712000  
    	}, {  
    		"fromUserEmail": "testFrom1@google.com",  
    		"toUserEmail": "testTo1@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"price": "97100.00000000",  
    		"quantity": "0.00100000",  
    		"positionSide": "BOTH",  
    		"side": "SELL",  
    		"timeStamp": 1740041627000  
    	}, {  
    		"fromUserEmail": "testFrom2@google.com",  
    		"toUserEmail": "testTo2@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"price": "97108.62068889",  
    		"quantity": "0.00100000",  
    		"positionSide": "BOTH",  
    		"side": "SELL",  
    		"timeStamp": 1740041959000  
    	}]  
    }

---

# 查询账户移仓历史 (适用主账户) (USER_DATA)

## 接口描述[​](/docs/zh-CN/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#接口描述 "接口描述的直接链接")

查询账户移仓历史

## HTTP请求[​](/docs/zh-CN/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/sub-account/futures/move-position`

## 请求权重(IP)[​](/docs/zh-CN/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#请求权重ip "请求权重\(IP\)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#请求参数 "请求参数的直接链接")

名称| 类型| 是否必需| 描述  
---|---|---|---  
symbol| STRING| YES|   
startTime| LONG| NO|   
endTime| LONG| NO|   
page| INT| YES|   
row| INT| YES|   
recvWindow| LONG| NO|   
timestamp| LONG| YES|   
  
>   * 如果 `startTime` 和 `endTime`都没有传，返回最近90天内最大1000条记录。
>   * 如果传了 `startTime` 但没有传`endTime`，返回记录时间范围为[max(startTime, now-90d), now].
>   * 如果传了`startTime` 但没有传 `endTime`， 返回记录时间范围为 [max(now,endTime-90d), endTime].
> 


## 响应示例[​](/docs/zh-CN/sub_account/asset-management/Get-Move-Position-History-for-Sub-account#响应示例 "响应示例的直接链接")
    
    
    {  
    	"total": 3,  
    	"futureMovePositionOrderVoList": [{  
    		"fromUserEmail": "testFrom@google.com",  
    		"toUserEmail": "testTo@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"price": "105025.50981609",  
    		"quantity": "0.00100000",  
    		"positionSide": "BOTH",  
    		"side": "SELL",  
    		"timeStamp": 1737544712000  
    	}, {  
    		"fromUserEmail": "testFrom1@google.com",  
    		"toUserEmail": "testTo1@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"price": "97100.00000000",  
    		"quantity": "0.00100000",  
    		"positionSide": "BOTH",  
    		"side": "SELL",  
    		"timeStamp": 1740041627000  
    	}, {  
    		"fromUserEmail": "testFrom2@google.com",  
    		"toUserEmail": "testTo2@google.com",  
    		"productType": "UM",  
    		"symbol": "BTCUSDT",  
    		"price": "97108.62068889",  
    		"quantity": "0.00100000",  
    		"positionSide": "BOTH",  
    		"side": "SELL",  
    		"timeStamp": 1740041959000  
    	}]  
    }