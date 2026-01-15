---
exchange: binance
source_url: https://developers.binance.com/docs/wallet/travel-rule/broker-deposit-provide-info
api_type: REST
updated_at: 2026-01-15T23:49:46.780220
---

# Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/wallet/travel-rule/broker-deposit-provide-info#api-description "Direct link to API Description")

Submit questionnaire for brokers of local entities that require travel rule. The questionnaire is only applies to transactions from un-hosted wallets or VASPs that are not yet onboarded with GTR.

## HTTP Request[​](/docs/wallet/travel-rule/broker-deposit-provide-info#http-request "Direct link to HTTP Request")

PUT `/sapi/v1/localentity/broker/deposit/provide-info`

## Request Weight(UID)[​](/docs/wallet/travel-rule/broker-deposit-provide-info#request-weightuid "Direct link to Request Weight\(UID\)")

**600**

## Request Parameters[​](/docs/wallet/travel-rule/broker-deposit-provide-info#request-parameters "Direct link to Request Parameters")

Name| Type| Mandatory| Description  
---|---|---|---  
subAccountId| STRING| YES| External user ID.  
depositId| STRING| YES| Wallet deposit ID.  
questionnaire| STRING| YES| JSON format questionnaire answers.  
beneficiaryPii| STRING| YES| JSON format beneficiary Pii.  
network| STRING| NO|   
coin| STRING| NO|   
amount| BigDecimal| NO|   
address| STRING| NO|   
addressTag| STRING| NO|   
timestamp| LONG| YES| Epoch Sec  
signature| STRING| YES| Must be the last parameter  
  
>   * Questionnaire is different for each local entity, please refer to `Deposit Questionnaire Content` page.
>   * If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to verify the format of the questionnaire and use URL-encoded format.
> 


## StandardPii[​](/docs/wallet/travel-rule/broker-deposit-provide-info#standardpii "Direct link to StandardPii")

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
  
## Response Example[​](/docs/wallet/travel-rule/broker-deposit-provide-info#response-example "Direct link to Response Example")
    
    
    {  
    	"trId": 765127651,  
     	"accepted": true,  
     	"info": "Deposit questionnaire accepted."  
    }

---

# Submit Deposit Questionnaire (For local entities that require travel rule) (supporting network) (USER_DATA)

## API Description[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#api-description "API Description的直接链接")

Submit questionnaire for brokers of local entities that require travel rule. The questionnaire is only applies to transactions from un-hosted wallets or VASPs that are not yet onboarded with GTR.

## HTTP Request[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#http-request "HTTP Request的直接链接")

PUT `/sapi/v1/localentity/broker/deposit/provide-info`

## Request Weight(UID)[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#request-weightuid "Request Weight\(UID\)的直接链接")

**600**

## Request Parameters[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#request-parameters "Request Parameters的直接链接")

Name| Type| Mandatory| Description  
---|---|---|---  
subAccountId| STRING| YES| External user ID.  
depositId| STRING| YES| Wallet deposit ID.  
questionnaire| STRING| YES| JSON format questionnaire answers.  
beneficiaryPii| STRING| YES| JSON format beneficiary Pii.  
network| STRING| NO|   
coin| STRING| NO|   
amount| BigDecimal| NO|   
address| STRING| NO|   
addressTag| STRING| NO|   
timestamp| LONG| YES| Epoch Sec  
signature| STRING| YES| Must be the last parameter  
  
>   * Questionnaire is different for each local entity, please refer to `Deposit Questionnaire Content` page.
>   * If getting error like `Questionnaire format not valid.` or `Questionnaire must not be blank`, please try to verify the format of the questionnaire and use URL-encoded format.
> 


## StandardPii[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#standardpii "StandardPii的直接链接")

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
  
## Response Example[​](/docs/zh-CN/wallet/travel-rule/broker-deposit-provide-info#response-example "Response Example的直接链接")
    
    
    {  
    	"trId": 765127651,  
     	"accepted": true,  
     	"info": "Deposit questionnaire accepted."  
    }