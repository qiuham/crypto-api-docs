---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/broker-withdraw
api_type: REST
updated_at: 2026-01-15T23:49:50.360140
---

# Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/broker-withdraw#api-description "Direct link to API Description")

Submit a withdrawal request for brokers of local entities that required travel rule.

## HTTP Request[​](/docs/wallet/travel-rule/broker-withdraw#http-request "Direct link to HTTP Request")

POST `/sapi/v1/localentity/broker/withdraw/apply`

## Request Weight(UID)[​](/docs/wallet/travel-rule/broker-withdraw#request-weightuid "Direct link to Request Weight\(UID\)")

**600**

## Request Parameters[​](/docs/wallet/travel-rule/broker-withdraw#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
address| STRING| YES|   
addressTag| STRING| NO| Secondary address identifier for coins like XRP,XMR etc.  
network| STRING| NO|   
coin| STRING| YES|   
addressName| STRING| NO| Description of the address. Address book cap is 200, space in name should be encoded into `%20`  
amount| BigDECIMAL| YES|   
withdrawOrderId| STRING| YES| withdrawID defined by the client (i.e. client's internal withdrawID)  
transactionFeeFlag| BOOLEAN| NO| When making internal transfer, `true` for returning the fee to the destination account; `false` for returning the fee back to the departure account. Default `false`.  
walletType| INTEGER| NO| The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current "selected wallet" under wallet->Fiat and Spot/Funding->Deposit  
questionnaire| STRING| YES| JSON format questionnaire answers.  
originatorPii| STRING| YES| JSON format originator Pii, see StandardPii section below  
timestamp| LONG| YES|   
signature| STRING| YES| Must be the last parameter.  
  
>   * If `network` not send, return with default network of the coin, but if the address could not match default network, the withdraw will be rejected.
>   * You can get `network` in `networkList` of a coin in the response of `Get /sapi/v1/capital/config/getall (HMAC SHA256)`.
>   * Questionnaire is different for each local entity, please refer to the `Withdraw Questionnaire Contents` page.
>   * If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to verify the format of the questionnaire and use URL-encoded format.
> 


## StandardPii[​](/docs/wallet/travel-rule/broker-withdraw#standardpii "Direct link to StandardPii")

**For Natural Person**

Name| Type| Mandatory| Description  
---|---|---|---  
piiType| INTEGER| YES| Fix to 0: Natural Person  
latinNames| List| YES| In case a person have complicated names or multiple names, this parameter is a list  
localNames| List| NO| In case a person have complicated names or multiple names, this parameter is a list  
nationality| STRING| NO|   
residenceCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
dateOfBirth| STRING| NO| yyyy-mm-dd. Not required but strongly recommended. Providing DOB could greatly reduce false positive rate during risk checking process.  
placeOfBirth| STRING| NO|   
address| STRING| NO|   
  
**For Legal Person**

Name| Type| Mandatory| Description  
---|---|---|---  
piiType| INTEGER| YES| Fix to 1: Legal Person  
latinName| STRING| YES| It's company name for Legal Person  
localName| STRING| NO|   
registrationCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
registrationDate| STRING| NO| yyyy-mm-dd. Not required but strongly recommended.  
address| STRING| NO|   
walletAddress| STRING| NO|   
walletTag| STRING| NO|   
  
**PiiName**

Name| Type| Mandatory| Description  
---|---|---|---  
firstName| STRING| YES| Mandatory for Natural person  
middleName| STRING| NO|   
lastName| STRING| NO|   
  
## Response Example[​](/docs/wallet/travel-rule/broker-withdraw#response-example "Direct link to Response Example")
    
    
    {  
        "trId": 123456, # The travel rule record Id  
        "accpted": true, # Whether the withdraw request is accepted  
        "info": "Withdraw request accepted" # The detailed infomation of the withdrawal result.  
    }

---

# Broker Withdraw (for brokers of local entities that require travel rule) (USER_DATA)

## API Description[​](/docs/zh-CN/wallet/travel-rule/broker-withdraw#api-description "API Description的直接链接")

Submit a withdrawal request for brokers of local entities that required travel rule.

## HTTP Request[​](/docs/zh-CN/wallet/travel-rule/broker-withdraw#http-request "HTTP Request的直接链接")

POST `/sapi/v1/localentity/broker/withdraw/apply`

## Request Weight(UID)[​](/docs/zh-CN/wallet/travel-rule/broker-withdraw#request-weightuid "Request Weight\(UID\)的直接链接")

**600**

## Request Parameters[​](/docs/zh-CN/wallet/travel-rule/broker-withdraw#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
address| STRING| YES|   
addressTag| STRING| NO| Secondary address identifier for coins like XRP,XMR etc.  
network| STRING| NO|   
coin| STRING| YES|   
addressName| STRING| NO| Description of the address. Address book cap is 200, space in name should be encoded into `%20`  
amount| BigDECIMAL| YES|   
withdrawOrderId| STRING| YES| withdrawID defined by the client (i.e. client's internal withdrawID)  
transactionFeeFlag| BOOLEAN| NO| When making internal transfer, `true` for returning the fee to the destination account; `false` for returning the fee back to the departure account. Default `false`.  
walletType| INTEGER| NO| The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current "selected wallet" under wallet->Fiat and Spot/Funding->Deposit  
questionnaire| STRING| YES| JSON format questionnaire answers.  
originatorPii| STRING| YES| JSON format originator Pii, see StandardPii section below  
timestamp| LONG| YES|   
signature| STRING| YES| Must be the last parameter.  
  
>   * If `network` not send, return with default network of the coin, but if the address could not match default network, the withdraw will be rejected.
>   * You can get `network` in `networkList` of a coin in the response of `Get /sapi/v1/capital/config/getall (HMAC SHA256)`.
>   * Questionnaire is different for each local entity, please refer to the `Withdraw Questionnaire Contents` page.
>   * If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to verify the format of the questionnaire and use URL-encoded format.
> 


## StandardPii[​](/docs/zh-CN/wallet/travel-rule/broker-withdraw#standardpii "StandardPii的直接链接")

**For Natural Person**

Name| Type| Mandatory| Description  
---|---|---|---  
piiType| INTEGER| YES| Fix to 0: Natural Person  
latinNames| List| YES| In case a person have complicated names or multiple names, this parameter is a list  
localNames| List| NO| In case a person have complicated names or multiple names, this parameter is a list  
nationality| STRING| NO|   
residenceCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
dateOfBirth| STRING| NO| yyyy-mm-dd. Not required but strongly recommended. Providing DOB could greatly reduce false positive rate during risk checking process.  
placeOfBirth| STRING| NO|   
address| STRING| NO|   
  
**For Legal Person**

Name| Type| Mandatory| Description  
---|---|---|---  
piiType| INTEGER| YES| Fix to 1: Legal Person  
latinName| STRING| YES| It's company name for Legal Person  
localName| STRING| NO|   
registrationCountry| STRING| YES|   
nationalIdentifier| STRING| NO|   
nationalIdentifierType| STRING| NO|   
nationalIdentifierIssueCountry| STRING| NO|   
registrationDate| STRING| NO| yyyy-mm-dd. Not required but strongly recommended.  
address| STRING| NO|   
walletAddress| STRING| NO|   
walletTag| STRING| NO|   
  
**PiiName**

Name| Type| Mandatory| Description  
---|---|---|---  
firstName| STRING| YES| Mandatory for Natural person  
middleName| STRING| NO|   
lastName| STRING| NO|   
  
## Response Example[​](/docs/zh-CN/wallet/travel-rule/broker-withdraw#response-example "Response Example的直接链接")
    
    
    {  
        "trId": 123456, # The travel rule record Id  
        "accpted": true, # Whether the withdraw request is accepted  
        "info": "Withdraw request accepted" # The detailed infomation of the withdrawal result.  
    }