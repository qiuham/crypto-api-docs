---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/options-trading/error-code
api_type: REST
updated_at: 2026-01-15T23:40:56.784567
---

# Error Codes

> Here is the error JSON payload:
    
    
    {  
      "code":-1121,  
      "msg":"Invalid symbol."  
    }  
    

Errors consist of two parts: an error code and a message.  
Codes are universal,but messages can vary.

## 10xx - General Server or Network issues[​](/docs/derivatives/options-trading/error-code#10xx---general-server-or-network-issues "Direct link to 10xx - General Server or Network issues")

### -1000 UNKNOWN[​](/docs/derivatives/options-trading/error-code#-1000-unknown "Direct link to -1000 UNKNOWN")

  * An unknown error occurred while processing the request.



### -1001 DISCONNECTED[​](/docs/derivatives/options-trading/error-code#-1001-disconnected "Direct link to -1001 DISCONNECTED")

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED[​](/docs/derivatives/options-trading/error-code#-1002-unauthorized "Direct link to -1002 UNAUTHORIZED")

  * You are not authorized to execute this request.



### -1008 TOO_MANY_REQUESTS[​](/docs/derivatives/options-trading/error-code#-1008-too_many_requests "Direct link to -1008 TOO_MANY_REQUESTS")

  * Too many requests queued.
  * Too much request weight used; please use the websocket for live updates to avoid polling the API.
  * Too much request weight used; current limit is %s request weight per %s %s. Please use the websocket for live updates to avoid polling the API.
  * Way too much request weight used; IP banned until %s. Please use the websocket for live updates to avoid bans.



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/derivatives/options-trading/error-code#-1014-unknown_order_composition "Direct link to -1014 UNKNOWN_ORDER_COMPOSITION")

  * Unsupported order combination.



### -1015 TOO_MANY_ORDERS[​](/docs/derivatives/options-trading/error-code#-1015-too_many_orders "Direct link to -1015 TOO_MANY_ORDERS")

  * Too many new orders.
  * Too many new orders; current limit is %s orders per %s.



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/derivatives/options-trading/error-code#-1016-service_shutting_down "Direct link to -1016 SERVICE_SHUTTING_DOWN")

  * This service is no longer available.



### -1020 UNSUPPORTED_OPERATION[​](/docs/derivatives/options-trading/error-code#-1020-unsupported_operation "Direct link to -1020 UNSUPPORTED_OPERATION")

  * This operation is not supported.



### -1021 INVALID_TIMESTAMP[​](/docs/derivatives/options-trading/error-code#-1021-invalid_timestamp "Direct link to -1021 INVALID_TIMESTAMP")

  * Timestamp for this request is outside of the recvWindow.
  * Timestamp for this request was 1000ms ahead of the server's time.



### -1022 INVALID_SIGNATURE[​](/docs/derivatives/options-trading/error-code#-1022-invalid_signature "Direct link to -1022 INVALID_SIGNATURE")

  * Signature for this request is not valid.



## 11xx - 2xxx Request issues[​](/docs/derivatives/options-trading/error-code#11xx---2xxx-request-issues "Direct link to 11xx - 2xxx Request issues")

### -1100 ILLEGAL_CHARS[​](/docs/derivatives/options-trading/error-code#-1100-illegal_chars "Direct link to -1100 ILLEGAL_CHARS")

  * Illegal characters found in a parameter.
  * Illegal characters found in a parameter. %s
  * Illegal characters found in parameter `%s`; legal range is `%s`.



### -1101 TOO_MANY_PARAMETERS[​](/docs/derivatives/options-trading/error-code#-1101-too_many_parameters "Direct link to -1101 TOO_MANY_PARAMETERS")

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected `%s` and received `%s`.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/derivatives/options-trading/error-code#-1102-mandatory_param_empty_or_malformed "Direct link to -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter `%s` was not sent, was empty/null, or malformed.
  * Param `%s` or `%s` must be sent, but both were empty/null!



### -1103 UNKNOWN_PARAM[​](/docs/derivatives/options-trading/error-code#-1103-unknown_param "Direct link to -1103 UNKNOWN_PARAM")

  * An unknown parameter was sent.



### -1104 UNREAD_PARAMETERS[​](/docs/derivatives/options-trading/error-code#-1104-unread_parameters "Direct link to -1104 UNREAD_PARAMETERS")

  * Not all sent parameters were read.
  * Not all sent parameters were read; read `%s` parameter(s) but was sent `%s`.



### -1105 PARAM_EMPTY[​](/docs/derivatives/options-trading/error-code#-1105-param_empty "Direct link to -1105 PARAM_EMPTY")

  * A parameter was empty.
  * Parameter `%s` was empty.



### -1106 PARAM_NOT_REQUIRED[​](/docs/derivatives/options-trading/error-code#-1106-param_not_required "Direct link to -1106 PARAM_NOT_REQUIRED")

  * A parameter was sent when not required.
  * Parameter `%s` sent when not required.



### -1111 BAD_PRECISION[​](/docs/derivatives/options-trading/error-code#-1111-bad_precision "Direct link to -1111 BAD_PRECISION")

  * Precision is over the maximum defined for this asset.



### -1115 INVALID_TIF[​](/docs/derivatives/options-trading/error-code#-1115-invalid_tif "Direct link to -1115 INVALID_TIF")

  * Invalid timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/derivatives/options-trading/error-code#-1116-invalid_order_type "Direct link to -1116 INVALID_ORDER_TYPE")

  * Invalid orderType.



### -1117 INVALID_SIDE[​](/docs/derivatives/options-trading/error-code#-1117-invalid_side "Direct link to -1117 INVALID_SIDE")

  * Invalid side.



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/derivatives/options-trading/error-code#-1118-empty_new_cl_ord_id "Direct link to -1118 EMPTY_NEW_CL_ORD_ID")

  * New client order ID was empty.



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/derivatives/options-trading/error-code#-1119-empty_org_cl_ord_id "Direct link to -1119 EMPTY_ORG_CL_ORD_ID")

  * Original client order ID was empty.



### -1120 BAD_INTERVAL[​](/docs/derivatives/options-trading/error-code#-1120-bad_interval "Direct link to -1120 BAD_INTERVAL")

  * Invalid interval.



### -1121 BAD_SYMBOL[​](/docs/derivatives/options-trading/error-code#-1121-bad_symbol "Direct link to -1121 BAD_SYMBOL")

  * Invalid symbol.



### -1125 INVALID_LISTEN_KEY[​](/docs/derivatives/options-trading/error-code#-1125-invalid_listen_key "Direct link to -1125 INVALID_LISTEN_KEY")

  * This listenKey does not exist.



### -1127 MORE_THAN_XX_HOURS[​](/docs/derivatives/options-trading/error-code#-1127-more_than_xx_hours "Direct link to -1127 MORE_THAN_XX_HOURS")

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 BAD_CONTRACT[​](/docs/derivatives/options-trading/error-code#-1128-bad_contract "Direct link to -1128 BAD_CONTRACT")

  * Invalid underlying



### -1129 BAD_CURRENCY[​](/docs/derivatives/options-trading/error-code#-1129-bad_currency "Direct link to -1129 BAD_CURRENCY")

  * Invalid asset。



### -1130 INVALID_PARAMETER[​](/docs/derivatives/options-trading/error-code#-1130-invalid_parameter "Direct link to -1130 INVALID_PARAMETER")

  * Invalid data sent for a parameter.
  * Data sent for paramter `%s` is not valid.



### -1131 BAD_RECV_WINDOW[​](/docs/derivatives/options-trading/error-code#-1131-bad_recv_window "Direct link to -1131 BAD_RECV_WINDOW")

  * recvWindow must be less than 60000



### -2010 NEW_ORDER_REJECTED[​](/docs/derivatives/options-trading/error-code#-2010-new_order_rejected "Direct link to -2010 NEW_ORDER_REJECTED")

  * NEW_ORDER_REJECTED



### -2013 NO_SUCH_ORDER[​](/docs/derivatives/options-trading/error-code#-2013-no_such_order "Direct link to -2013 NO_SUCH_ORDER")

  * Order does not exist.



### -2014 BAD_API_KEY_FMT[​](/docs/derivatives/options-trading/error-code#-2014-bad_api_key_fmt "Direct link to -2014 BAD_API_KEY_FMT")

  * API-key format invalid.



### -2015 INVALID_API_KEY[​](/docs/derivatives/options-trading/error-code#-2015-invalid_api_key "Direct link to -2015 INVALID_API_KEY")

  * Invalid API-key, IP, or permissions for action.



### -2018 BALANCE_NOT_SUFFICIENT[​](/docs/derivatives/options-trading/error-code#-2018-balance_not_sufficient "Direct link to -2018 BALANCE_NOT_SUFFICIENT")

  * Balance is insufficient.



### -2027 OPTION_MARGIN_NOT_SUFFICIENT[​](/docs/derivatives/options-trading/error-code#-2027-option_margin_not_sufficient "Direct link to -2027 OPTION_MARGIN_NOT_SUFFICIENT")

  * Option margin is insufficient.



## 3xxx-5xxx Filters and other issues[​](/docs/derivatives/options-trading/error-code#3xxx-5xxx-filters-and-other-issues "Direct link to 3xxx-5xxx Filters and other issues")

### -3029 TRANSFER_FAILED[​](/docs/derivatives/options-trading/error-code#-3029-transfer_failed "Direct link to -3029 TRANSFER_FAILED")

  * Asset transfer fail.



### -4001 PRICE_LESS_THAN_ZERO[​](/docs/derivatives/options-trading/error-code#-4001-price_less_than_zero "Direct link to -4001 PRICE_LESS_THAN_ZERO")

  * Price less than 0.



### -4002 PRICE_GREATER_THAN_MAX_PRICE[​](/docs/derivatives/options-trading/error-code#-4002-price_greater_than_max_price "Direct link to -4002 PRICE_GREATER_THAN_MAX_PRICE")

  * Price greater than max price.



### -4003 QTY_LESS_THAN_ZERO[​](/docs/derivatives/options-trading/error-code#-4003-qty_less_than_zero "Direct link to -4003 QTY_LESS_THAN_ZERO")

  * Quantity less than zero.



### -4004 QTY_LESS_THAN_MIN_QTY[​](/docs/derivatives/options-trading/error-code#-4004-qty_less_than_min_qty "Direct link to -4004 QTY_LESS_THAN_MIN_QTY")

  * Quantity less than min quantity.



### -4005 QTY_GREATER_THAN_MAX_QTY[​](/docs/derivatives/options-trading/error-code#-4005-qty_greater_than_max_qty "Direct link to -4005 QTY_GREATER_THAN_MAX_QTY")

  * Quantity greater than max quantity.



### -4013 PRICE_LESS_THAN_MIN_PRICE[​](/docs/derivatives/options-trading/error-code#-4013-price_less_than_min_price "Direct link to -4013 PRICE_LESS_THAN_MIN_PRICE")

  * Price less than min price.



### -4029 INVALID_TICK_SIZE_PRECISION[​](/docs/derivatives/options-trading/error-code#-4029-invalid_tick_size_precision "Direct link to -4029 INVALID_TICK_SIZE_PRECISION")

  * Tick size precision is invalid.



### -4030 INVALID_QTY_PRECISION[​](/docs/derivatives/options-trading/error-code#-4030-invalid_qty_precision "Direct link to -4030 INVALID_QTY_PRECISION")

  * Step size precision is invalid.



### -4055 AMOUNT_MUST_BE_POSITIVE[​](/docs/derivatives/options-trading/error-code#-4055-amount_must_be_positive "Direct link to -4055 AMOUNT_MUST_BE_POSITIVE")

  * Amount must be positive.



### -4056 INVALID_AMOUNT[​](/docs/derivatives/options-trading/error-code#-4056-invalid_amount "Direct link to -4056 INVALID_AMOUNT")

  * Amount is invalid.



### -4078 OPTIONS_COMMON_ERROR[​](/docs/derivatives/options-trading/error-code#-4078-options_common_error "Direct link to -4078 OPTIONS_COMMON_ERROR")

  * options internal error



### -5001 USER_EXIST[​](/docs/derivatives/options-trading/error-code#-5001-user_exist "Direct link to -5001 USER_EXIST")

  * Option user already exist



### -5002 USER_NOT_ACCESS[​](/docs/derivatives/options-trading/error-code#-5002-user_not_access "Direct link to -5002 USER_NOT_ACCESS")

  * Option user not access



### -5003 BAD_INVITE_CODE[​](/docs/derivatives/options-trading/error-code#-5003-bad_invite_code "Direct link to -5003 BAD_INVITE_CODE")

  * Invalid invite code



### -5004 USED_INVITE_CODE[​](/docs/derivatives/options-trading/error-code#-5004-used_invite_code "Direct link to -5004 USED_INVITE_CODE")

  * Invite code has bean used



### -5005 BLACK_COUNTRY[​](/docs/derivatives/options-trading/error-code#-5005-black_country "Direct link to -5005 BLACK_COUNTRY")

  * Black country



### -5006 ITEMS_EXIST[​](/docs/derivatives/options-trading/error-code#-5006-items_exist "Direct link to -5006 ITEMS_EXIST")

  * Items '%s' already exist



### -5007 USER_API_EXIST[​](/docs/derivatives/options-trading/error-code#-5007-user_api_exist "Direct link to -5007 USER_API_EXIST")

  * User api already exist



### -5008 KYC_NOT_PASS[​](/docs/derivatives/options-trading/error-code#-5008-kyc_not_pass "Direct link to -5008 KYC_NOT_PASS")

  * User kyc not pass



### -5009 IP_COUNTRY_BLACK[​](/docs/derivatives/options-trading/error-code#-5009-ip_country_black "Direct link to -5009 IP_COUNTRY_BLACK")

  * Restricted jurisdiction ip address



### -5010 NOT_ENOUGH_POSITION[​](/docs/derivatives/options-trading/error-code#-5010-not_enough_position "Direct link to -5010 NOT_ENOUGH_POSITION")

  * User doesn't have enough position to sell



### -6001 INVALID_MMP_WINDOW_TIME_LIMIT[​](/docs/derivatives/options-trading/error-code#-6001-invalid_mmp_window_time_limit "Direct link to -6001 INVALID_MMP_WINDOW_TIME_LIMIT")

  * Invalid mmp window time limit



### -6002 INVALID_MMP_FROZEN_TIME_LIMIT[​](/docs/derivatives/options-trading/error-code#-6002-invalid_mmp_frozen_time_limit "Direct link to -6002 INVALID_MMP_FROZEN_TIME_LIMIT")

  * Invalid mmp frozen time limit



### -6003 INVALID_UNDERLYING[​](/docs/derivatives/options-trading/error-code#-6003-invalid_underlying "Direct link to -6003 INVALID_UNDERLYING")

  * Invalid underlying



### -6004 MMP_UNDERLYING_NOT_FOUND[​](/docs/derivatives/options-trading/error-code#-6004-mmp_underlying_not_found "Direct link to -6004 MMP_UNDERLYING_NOT_FOUND")

  * Underlying not found



### -6005 IS_NOT_MARKET_MAKER[​](/docs/derivatives/options-trading/error-code#-6005-is_not_market_maker "Direct link to -6005 IS_NOT_MARKET_MAKER")

  * It is not market maker



### -6006 MMP_RULES_NOT_EXISTING[​](/docs/derivatives/options-trading/error-code#-6006-mmp_rules_not_existing "Direct link to -6006 MMP_RULES_NOT_EXISTING")

  * Mmp rules are not existing



### -6007 MMP_ERROR_UNKNOWN[​](/docs/derivatives/options-trading/error-code#-6007-mmp_error_unknown "Direct link to -6007 MMP_ERROR_UNKNOWN")

  * Mmp unknown error



### -6008 INVALID_LIMIT[​](/docs/derivatives/options-trading/error-code#-6008-invalid_limit "Direct link to -6008 INVALID_LIMIT")

  * parameter 'limit' is invalid.



### -6009 INVALID_COUNTDOWN_TIME[​](/docs/derivatives/options-trading/error-code#-6009-invalid_countdown_time "Direct link to -6009 INVALID_COUNTDOWN_TIME")

  * countdownTime must be no less than 5000 or equal to 0



### -6010 OPEN_INTEREST_ERR_DATA[​](/docs/derivatives/options-trading/error-code#-6010-open_interest_err_data "Direct link to -6010 OPEN_INTEREST_ERR_DATA")

  * open interest error data.



### -6011 EXCEED_MAXIMUM_BATCH_ORDERS[​](/docs/derivatives/options-trading/error-code#-6011-exceed_maximum_batch_orders "Direct link to -6011 EXCEED_MAXIMUM_BATCH_ORDERS")

  * Maximum 10 orders in one batchOrder request.



### -6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS[​](/docs/derivatives/options-trading/error-code#-6012-exceed_maximum_block_order_legs "Direct link to -6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS")

  * Exceed maximum number of legs in one block order request.



### -6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL[​](/docs/derivatives/options-trading/error-code#-6013-block_order_legs_with_duplicate_symbol "Direct link to -6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL")

  * Duplicate symbol in one block order request.



### -6014 GRFQ_INVALID_LEGS[​](/docs/derivatives/options-trading/error-code#-6014-grfq_invalid_legs "Direct link to -6014 GRFQ_INVALID_LEGS")

  * Invalid legs



### -6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY[​](/docs/derivatives/options-trading/error-code#-6015-grfq_qty_is_not_multiple_of_minimum_qty "Direct link to -6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY")

  * Quantity is not multiple of minimum quantity



### -6016 GRFQ_QUOTE_NOT_FOUND[​](/docs/derivatives/options-trading/error-code#-6016-grfq_quote_not_found "Direct link to -6016 GRFQ_QUOTE_NOT_FOUND")

  * Quote is not found



### -6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT[​](/docs/derivatives/options-trading/error-code#-6017-grfq_quote_not_enough_qty_left "Direct link to -6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT")

  * Not enough quantity left



### -6018 GRFQ_QUOTE_REQUEST_NOT_FOUND[​](/docs/derivatives/options-trading/error-code#-6018-grfq_quote_request_not_found "Direct link to -6018 GRFQ_QUOTE_REQUEST_NOT_FOUND")

  * Quote request is not found



### -6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME[​](/docs/derivatives/options-trading/error-code#-6019-grfq_quote_invalid_expire_time "Direct link to -6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME")

  * Invalid quote expire time



### -6020 GRFQ_QUOTE_EXPIRED[​](/docs/derivatives/options-trading/error-code#-6020-grfq_quote_expired "Direct link to -6020 GRFQ_QUOTE_EXPIRED")

  * Quote expired



### -6021 GRFQ_INVALID_SIDE[​](/docs/derivatives/options-trading/error-code#-6021-grfq_invalid_side "Direct link to -6021 GRFQ_INVALID_SIDE")

  * Invalid side



### -6022 GRFQ_INVALID_USER[​](/docs/derivatives/options-trading/error-code#-6022-grfq_invalid_user "Direct link to -6022 GRFQ_INVALID_USER")

  * Not Global RFQ user



### -6023 SELF_TRADE_PREVENTION[​](/docs/derivatives/options-trading/error-code#-6023-self_trade_prevention "Direct link to -6023 SELF_TRADE_PREVENTION")

  * Self trade prevention



### -6024 CHANGE_USER_FLAG_FAILED[​](/docs/derivatives/options-trading/error-code#-6024-change_user_flag_failed "Direct link to -6024 CHANGE_USER_FLAG_FAILED")

  * Change user flag failed



### -6025 GRFQ_INVALID_QUOTE_PRICE[​](/docs/derivatives/options-trading/error-code#-6025-grfq_invalid_quote_price "Direct link to -6025 GRFQ_INVALID_QUOTE_PRICE")

  * Invalid quote price



### -6026 INVALID_QTY[​](/docs/derivatives/options-trading/error-code#-6026-invalid_qty "Direct link to -6026 INVALID_QTY")

  * Invalid qty



### -6027 INVALID_PRICE[​](/docs/derivatives/options-trading/error-code#-6027-invalid_price "Direct link to -6027 INVALID_PRICE")

  * Invalid price



### -6028 ORDER_IS_FINAL[​](/docs/derivatives/options-trading/error-code#-6028-order_is_final "Direct link to -6028 ORDER_IS_FINAL")

  * Order is in final state



### -6029 PARAMETER_IS_REQUIRED[​](/docs/derivatives/options-trading/error-code#-6029-parameter_is_required "Direct link to -6029 PARAMETER_IS_REQUIRED")

  * %s is required



### -6030 INVALID_TIME_INTERVAL[​](/docs/derivatives/options-trading/error-code#-6030-invalid_time_interval "Direct link to -6030 INVALID_TIME_INTERVAL")

  * Invalid time interval.



### -6031 START_TIME_GREATER_THAN_END_TIME[​](/docs/derivatives/options-trading/error-code#-6031-start_time_greater_than_end_time "Direct link to -6031 START_TIME_GREATER_THAN_END_TIME")

  * Start time is greater than end time.



### -6032 HAS_OPEN_ORDER[​](/docs/derivatives/options-trading/error-code#-6032-has_open_order "Direct link to -6032 HAS_OPEN_ORDER")

  * Has open order.



### -6033 HAS_NEGATIVE_BALANCE[​](/docs/derivatives/options-trading/error-code#-6033-has_negative_balance "Direct link to -6033 HAS_NEGATIVE_BALANCE")

  * Has negative balance.



### -6034 HAS_POSITION[​](/docs/derivatives/options-trading/error-code#-6034-has_position "Direct link to -6034 HAS_POSITION")

  * Has position.



### -6035 NO_NEED_TO_CHANGE[​](/docs/derivatives/options-trading/error-code#-6035-no_need_to_change "Direct link to -6035 NO_NEED_TO_CHANGE")

  * No need to change.



### -6036 NO_PERMISSION_TO_CHANGE[​](/docs/derivatives/options-trading/error-code#-6036-no_permission_to_change "Direct link to -6036 NO_PERMISSION_TO_CHANGE")

  * no permission to change.



### -6037 NO_RECORDS_FOUND[​](/docs/derivatives/options-trading/error-code#-6037-no_records_found "Direct link to -6037 NO_RECORDS_FOUND")

  * No records found.



### -6038 SCALE_NOT_MATCH[​](/docs/derivatives/options-trading/error-code#-6038-scale_not_match "Direct link to -6038 SCALE_NOT_MATCH")

  * scale not match.



### -6039 INVALID_STEP_SIZE_PRECISION[​](/docs/derivatives/options-trading/error-code#-6039-invalid_step_size_precision "Direct link to -6039 INVALID_STEP_SIZE_PRECISION")

  * Step size precision is invalid.



### -6040 INVALID_QTYLIMIT_DELTALIMIT[​](/docs/derivatives/options-trading/error-code#-6040-invalid_qtylimit_deltalimit "Direct link to -6040 INVALID_QTYLIMIT_DELTALIMIT")

  * Invalid qtyLimit or deltaLimit.



### -6041 START_TRADING_MUST_SLOWLY[​](/docs/derivatives/options-trading/error-code#-6041-start_trading_must_slowly "Direct link to -6041 START_TRADING_MUST_SLOWLY")

  * Start Trading Must Slowly..



### -6042 INDEX_COMMISSION_NOT_MATCH[​](/docs/derivatives/options-trading/error-code#-6042-index_commission_not_match "Direct link to -6042 INDEX_COMMISSION_NOT_MATCH")

  * Index Commission Not Match..



### -6043 INDEX_RISKPARAMETER_NOT_MATCH[​](/docs/derivatives/options-trading/error-code#-6043-index_riskparameter_not_match "Direct link to -6043 INDEX_RISKPARAMETER_NOT_MATCH")

  * Index RiskParameter Not Match..



### -6044 CLI_ORD_ID_ERROR[​](/docs/derivatives/options-trading/error-code#-6044-cli_ord_id_error "Direct link to -6044 CLI_ORD_ID_ERROR")

  * clientOrderId is duplicated



### -6045 REDUCE_ONLY_REJECT[​](/docs/derivatives/options-trading/error-code#-6045-reduce_only_reject "Direct link to -6045 REDUCE_ONLY_REJECT")

  * Reduce-only order rejected. The new reduce-only order conflicts with existing open orders. Please cancel the conflicting orders and resubmit.



### -6046 FOK_ORDER_REJECT[​](/docs/derivatives/options-trading/error-code#-6046-fok_order_reject "Direct link to -6046 FOK_ORDER_REJECT")

  * Due to the order could not be filled immediately, the FOK order has been rejected.



### -6047 GTX_ORDER_REJECT[​](/docs/derivatives/options-trading/error-code#-6047-gtx_order_reject "Direct link to -6047 GTX_ORDER_REJECT")

  * Due to the order could not be executed as maker, the Post Only order will be rejected.



### -6048 INVALID_BLOCK_ORDER[​](/docs/derivatives/options-trading/error-code#-6048-invalid_block_order "Direct link to -6048 INVALID_BLOCK_ORDER")

  * Block order parameter is invalid



### -6049 SYMBOL_NOT_TRADING[​](/docs/derivatives/options-trading/error-code#-6049-symbol_not_trading "Direct link to -6049 SYMBOL_NOT_TRADING")

  * this symbol is not in trading status



### -6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6050-max_open_orders_on_symbol_exceeded "Direct link to -6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED")

  * Maximum open orders reached for this symbol. Please cancel existing orders and try again.



### -6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6051-max_open_orders_on_index_exceeded "Direct link to -6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED")

  * Maximum open orders reached for this underlying. Please cancel existing orders and try again.



### -6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6052-max_short_position_on_symbol_exceeded "Direct link to -6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED")

  * Maximum short position size reached for this symbol



### -6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6053-max_short_position_on_index_exceeded "Direct link to -6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED")

  * Maximum short position size reached for this underlying



### -6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED[​](/docs/derivatives/options-trading/error-code#-6054-max_quantity_on_single_order_exceeded "Direct link to -6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED")

  * Quantity greater than max quantity



### -6055 USER_LIQUIDATING[​](/docs/derivatives/options-trading/error-code#-6055-user_liquidating "Direct link to -6055 USER_LIQUIDATING")

  * User is in liquidation process



### -6056 REDUCE_ONLY_MARGIN_CHECK_FAILED[​](/docs/derivatives/options-trading/error-code#-6056-reduce_only_margin_check_failed "Direct link to -6056 REDUCE_ONLY_MARGIN_CHECK_FAILED")

  * Reduce-only order failed. Your new reduce-only order, when combined with existing same-side open orders, would flip your position and cause insufficient margin. Please cancel those open orders and try again.



### -6057 WRITER_CANT_NAKED_SELL[​](/docs/derivatives/options-trading/error-code#-6057-writer_cant_naked_sell "Direct link to -6057 WRITER_CANT_NAKED_SELL")

  * The current symbol is not eligible for option writing.



### -6058 MMP_TRIGGERED[​](/docs/derivatives/options-trading/error-code#-6058-mmp_triggered "Direct link to -6058 MMP_TRIGGERED")

  * MMP triggered. Please reset MMP config



### -6059 USER_IN_LIQUIDATION[​](/docs/derivatives/options-trading/error-code#-6059-user_in_liquidation "Direct link to -6059 USER_IN_LIQUIDATION")

  * User is in liquidation process



### -6060 LOCKED_BALANCE_NOT_FOUND[​](/docs/derivatives/options-trading/error-code#-6060-locked_balance_not_found "Direct link to -6060 LOCKED_BALANCE_NOT_FOUND")

  * OTC order fail due to unable to lock balance



### -6061 LOCKED_OTC_ORDER_NOT_FOUNT[​](/docs/derivatives/options-trading/error-code#-6061-locked_otc_order_not_fount "Direct link to -6061 LOCKED_OTC_ORDER_NOT_FOUNT")

  * OTC order fail due to unable to lock order



### -6062 INVALID_USER_STATUS[​](/docs/derivatives/options-trading/error-code#-6062-invalid_user_status "Direct link to -6062 INVALID_USER_STATUS")

  * Operation is not supported for current user status



### -6063 CANCEL_REJECTED[​](/docs/derivatives/options-trading/error-code#-6063-cancel_rejected "Direct link to -6063 CANCEL_REJECTED")

  * Cancel rejected by system

---

# 错误代码

> error JSON payload:
    
    
    {  
      "code":-1121,  
      "msg":"Invalid symbol."  
    }  
    

错误由两部分组成：错误代码和消息。 代码是通用的，但是消息可能会有所不同。

## 10xx -常规服务器或网络问题[​](/docs/zh-CN/derivatives/options-trading/error-code#10xx--常规服务器或网络问题 "10xx -常规服务器或网络问题的直接链接")

### -1000 UNKNOWN[​](/docs/zh-CN/derivatives/options-trading/error-code#-1000-unknown "-1000 UNKNOWN的直接链接")

  * 处理请求时发生未知错误。



### -1001 DISCONNECTED[​](/docs/zh-CN/derivatives/options-trading/error-code#-1001-disconnected "-1001 DISCONNECTED的直接链接")

  * 内部错误; 无法处理您的请求。 请再试一次.



### -1002 UNAUTHORIZED[​](/docs/zh-CN/derivatives/options-trading/error-code#-1002-unauthorized "-1002 UNAUTHORIZED的直接链接")

  * 您无权执行此请求。



### -1008 TOO_MANY_REQUESTS[​](/docs/zh-CN/derivatives/options-trading/error-code#-1008-too_many_requests "-1008 TOO_MANY_REQUESTS的直接链接")

  * 排队的请求过多。
  * 请求权重过多； 请使用websocket获取实时更新。
  * 请求权重过多； 当前限制为每分钟％s请求权重。 请使用websocket进行实时更新，以避免轮询API。
  * 请求权重过多； IP被禁止，直到％s。 请使用websocket进行实时更新，以免被禁。



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/zh-CN/derivatives/options-trading/error-code#-1014-unknown_order_composition "-1014 UNKNOWN_ORDER_COMPOSITION的直接链接")

  * 不支持的订单组合。



### -1015 TOO_MANY_ORDERS[​](/docs/zh-CN/derivatives/options-trading/error-code#-1015-too_many_orders "-1015 TOO_MANY_ORDERS的直接链接")

  * 新订单太多。
  * 新订单太多； 当前限制为每％s ％s个订单。



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/zh-CN/derivatives/options-trading/error-code#-1016-service_shutting_down "-1016 SERVICE_SHUTTING_DOWN的直接链接")

  * 该服务不可用。



### -1020 UNSUPPORTED_OPERATION[​](/docs/zh-CN/derivatives/options-trading/error-code#-1020-unsupported_operation "-1020 UNSUPPORTED_OPERATION的直接链接")

  * 不支持此操作。



### -1021 INVALID_TIMESTAMP[​](/docs/zh-CN/derivatives/options-trading/error-code#-1021-invalid_timestamp "-1021 INVALID_TIMESTAMP的直接链接")

  * 此请求的时间戳在recvWindow之外。
  * 此请求的时间戳比服务器时间提前1000毫秒。



### -1022 INVALID_SIGNATURE[​](/docs/zh-CN/derivatives/options-trading/error-code#-1022-invalid_signature "-1022 INVALID_SIGNATURE的直接链接")

  * 此请求的签名无效。



## 11xx - 2xxx Request issues[​](/docs/zh-CN/derivatives/options-trading/error-code#11xx---2xxx-request-issues "11xx - 2xxx Request issues的直接链接")

### -1100 ILLEGAL_CHARS[​](/docs/zh-CN/derivatives/options-trading/error-code#-1100-illegal_chars "-1100 ILLEGAL_CHARS的直接链接")

  * 在参数中发现非法字符。
  * 在参数中发现非法字符。`％s`
  * 在参数`％s`中发现非法字符； 合法范围是`％s`。



### -1101 TOO_MANY_PARAMETERS[​](/docs/zh-CN/derivatives/options-trading/error-code#-1101-too_many_parameters "-1101 TOO_MANY_PARAMETERS的直接链接")

  * 为此端点发送的参数太多。
  * 参数太多； 预期为`％s`并收到了`％s`。
  * 检测到的参数值重复。



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/zh-CN/derivatives/options-trading/error-code#-1102-mandatory_param_empty_or_malformed "-1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED的直接链接")

  * 未发送强制性参数，该参数为空/空或格式错误。
  * 强制参数`％s`未发送，为空/空或格式错误。
  * 必须发送参数`％s`或`％s`，但两者均为空！



### -1103 UNKNOWN_PARAM[​](/docs/zh-CN/derivatives/options-trading/error-code#-1103-unknown_param "-1103 UNKNOWN_PARAM的直接链接")

  * 发送了未知参数。



### -1104 UNREAD_PARAMETERS[​](/docs/zh-CN/derivatives/options-trading/error-code#-1104-unread_parameters "-1104 UNREAD_PARAMETERS的直接链接")

  * 并非所有发送的参数都被读取。
  * 并非所有发送的参数都被读取； 读取了`％s`参数，但被发送了`％s`。



### -1105 PARAM_EMPTY[​](/docs/zh-CN/derivatives/options-trading/error-code#-1105-param_empty "-1105 PARAM_EMPTY的直接链接")

  * 参数为空。
  * 参数`％s`为空。



### -1106 PARAM_NOT_REQUIRED[​](/docs/zh-CN/derivatives/options-trading/error-code#-1106-param_not_required "-1106 PARAM_NOT_REQUIRED的直接链接")

  * 不需要时已发送参数。
  * 不需要时发送参数`％s`。



### -1111 BAD_PRECISION[​](/docs/zh-CN/derivatives/options-trading/error-code#-1111-bad_precision "-1111 BAD_PRECISION的直接链接")

  * 精度超过为此资产定义的最大值。



### -1115 INVALID_TIF[​](/docs/zh-CN/derivatives/options-trading/error-code#-1115-invalid_tif "-1115 INVALID_TIF的直接链接")

  * 无效 timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/zh-CN/derivatives/options-trading/error-code#-1116-invalid_order_type "-1116 INVALID_ORDER_TYPE的直接链接")

  * 无效订单类型。



### -1117 INVALID_SIDE[​](/docs/zh-CN/derivatives/options-trading/error-code#-1117-invalid_side "-1117 INVALID_SIDE的直接链接")

  * 无效买卖方向。



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/zh-CN/derivatives/options-trading/error-code#-1118-empty_new_cl_ord_id "-1118 EMPTY_NEW_CL_ORD_ID的直接链接")

  * 新的客户订单ID为空。



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/zh-CN/derivatives/options-trading/error-code#-1119-empty_org_cl_ord_id "-1119 EMPTY_ORG_CL_ORD_ID的直接链接")

  * 客户自定义的订单ID为空。



### -1120 BAD_INTERVAL[​](/docs/zh-CN/derivatives/options-trading/error-code#-1120-bad_interval "-1120 BAD_INTERVAL的直接链接")

  * 无效时间间隔。



### -1121 BAD_SYMBOL[​](/docs/zh-CN/derivatives/options-trading/error-code#-1121-bad_symbol "-1121 BAD_SYMBOL的直接链接")

  * 无效的交易对。



### -1125 INVALID_LISTEN_KEY[​](/docs/zh-CN/derivatives/options-trading/error-code#-1125-invalid_listen_key "-1125 INVALID_LISTEN_KEY的直接链接")

  * 该listenKey不存在。



### -1127 MORE_THAN_XX_HOURS[​](/docs/zh-CN/derivatives/options-trading/error-code#-1127-more_than_xx_hours "-1127 MORE_THAN_XX_HOURS的直接链接")

  * 查询间隔太大。
  * 从开始时间到结束时间之间超过％s小时。



### -1128 BAD_CONTRACT[​](/docs/zh-CN/derivatives/options-trading/error-code#-1128-bad_contract "-1128 BAD_CONTRACT的直接链接")

  * 无效的期权合约标的。



### -1129 BAD_CURRENCY[​](/docs/zh-CN/derivatives/options-trading/error-code#-1129-bad_currency "-1129 BAD_CURRENCY的直接链接")

  * 无效的资产类型。



### -1130 INVALID_PARAMETER[​](/docs/zh-CN/derivatives/options-trading/error-code#-1130-invalid_parameter "-1130 INVALID_PARAMETER的直接链接")

  * 发送的参数为无效数据。
  * 发送参数`％s`的数据无效。



### -1131 BAD_RECV_WINDOW[​](/docs/zh-CN/derivatives/options-trading/error-code#-1131-bad_recv_window "-1131 BAD_RECV_WINDOW的直接链接")

  * `recvWindow` 必须小于 60000



### -2010 NEW_ORDER_REJECTED[​](/docs/zh-CN/derivatives/options-trading/error-code#-2010-new_order_rejected "-2010 NEW_ORDER_REJECTED的直接链接")

  * 新订单被拒绝



### -2013 NO_SUCH_ORDER[​](/docs/zh-CN/derivatives/options-trading/error-code#-2013-no_such_order "-2013 NO_SUCH_ORDER的直接链接")

  * 订单不存在。



### -2014 BAD_API_KEY_FMT[​](/docs/zh-CN/derivatives/options-trading/error-code#-2014-bad_api_key_fmt "-2014 BAD_API_KEY_FMT的直接链接")

  * API-key 格式无效。



### -2015 INVALID_API_KEY[​](/docs/zh-CN/derivatives/options-trading/error-code#-2015-invalid_api_key "-2015 INVALID_API_KEY的直接链接")

  * 无效的API密钥，IP或操作权限。



### -2018 BALANCE_NOT_SUFFICIENT[​](/docs/zh-CN/derivatives/options-trading/error-code#-2018-balance_not_sufficient "-2018 BALANCE_NOT_SUFFICIENT的直接链接")

  * 余额不足。



### -2027 OPTION_MARGIN_NOT_SUFFICIENT[​](/docs/zh-CN/derivatives/options-trading/error-code#-2027-option_margin_not_sufficient "-2027 OPTION_MARGIN_NOT_SUFFICIENT的直接链接")

  * 期权可用余额不足。



## 3xxx-5xxx Filters and other issues[​](/docs/zh-CN/derivatives/options-trading/error-code#3xxx-5xxx-filters-and-other-issues "3xxx-5xxx Filters and other issues的直接链接")

### -3029 TRANSFER_FAILED[​](/docs/zh-CN/derivatives/options-trading/error-code#-3029-transfer_failed "-3029 TRANSFER_FAILED的直接链接")

  * 资金划转失败。



### -4001 PRICE_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/options-trading/error-code#-4001-price_less_than_zero "-4001 PRICE_LESS_THAN_ZERO的直接链接")

  * 价格小于0。



### -4002 PRICE_GREATER_THAN_MAX_PRICE[​](/docs/zh-CN/derivatives/options-trading/error-code#-4002-price_greater_than_max_price "-4002 PRICE_GREATER_THAN_MAX_PRICE的直接链接")

  * 价格超过最大值。



### -4003 QTY_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/options-trading/error-code#-4003-qty_less_than_zero "-4003 QTY_LESS_THAN_ZERO的直接链接")

  * 数量小于0。



### -4004 QTY_LESS_THAN_MIN_QTY[​](/docs/zh-CN/derivatives/options-trading/error-code#-4004-qty_less_than_min_qty "-4004 QTY_LESS_THAN_MIN_QTY的直接链接")

  * 数量小于最小值。



### -4005 QTY_GREATER_THAN_MAX_QTY[​](/docs/zh-CN/derivatives/options-trading/error-code#-4005-qty_greater_than_max_qty "-4005 QTY_GREATER_THAN_MAX_QTY的直接链接")

  * 数量大于最大值。



### -4013 PRICE_LESS_THAN_MIN_PRICE[​](/docs/zh-CN/derivatives/options-trading/error-code#-4013-price_less_than_min_price "-4013 PRICE_LESS_THAN_MIN_PRICE的直接链接")

  * 价格小于最小价格。



### -4029 INVALID_TICK_SIZE_PRECISION[​](/docs/zh-CN/derivatives/options-trading/error-code#-4029-invalid_tick_size_precision "-4029 INVALID_TICK_SIZE_PRECISION的直接链接")

  * 价格精度小数点位数不正确。



### -4030 INVALID_QTY_PRECISION[​](/docs/zh-CN/derivatives/options-trading/error-code#-4030-invalid_qty_precision "-4030 INVALID_QTY_PRECISION的直接链接")

  * 数量精度小数点位数不正确。



### -4055 AMOUNT_MUST_BE_POSITIVE[​](/docs/zh-CN/derivatives/options-trading/error-code#-4055-amount_must_be_positive "-4055 AMOUNT_MUST_BE_POSITIVE的直接链接")

  * 金额必须大于零。



### -4056 INVALID_AMOUNT[​](/docs/zh-CN/derivatives/options-trading/error-code#-4056-invalid_amount "-4056 INVALID_AMOUNT的直接链接")

  * 金额无效。



### -4078 OPTIONS_COMMON_ERROR[​](/docs/zh-CN/derivatives/options-trading/error-code#-4078-options_common_error "-4078 OPTIONS_COMMON_ERROR的直接链接")

  * 期权内部错误。



### -5001 USER_EXIST[​](/docs/zh-CN/derivatives/options-trading/error-code#-5001-user_exist "-5001 USER_EXIST的直接链接")

  * Option 用户已存在。



### -5002 USER_NOT_ACCESS[​](/docs/zh-CN/derivatives/options-trading/error-code#-5002-user_not_access "-5002 USER_NOT_ACCESS的直接链接")

  * Option 用户无权限访问。



### -5003 BAD_INVITE_CODE[​](/docs/zh-CN/derivatives/options-trading/error-code#-5003-bad_invite_code "-5003 BAD_INVITE_CODE的直接链接")

  * 邀请码无效。



### -5004 USED_INVITE_CODE[​](/docs/zh-CN/derivatives/options-trading/error-code#-5004-used_invite_code "-5004 USED_INVITE_CODE的直接链接")

  * 邀请码已被使用。



### -5005 BLACK_COUNTRY[​](/docs/zh-CN/derivatives/options-trading/error-code#-5005-black_country "-5005 BLACK_COUNTRY的直接链接")

  * 黑名单国家/地区限制。



### -5006 ITEMS_EXIST[​](/docs/zh-CN/derivatives/options-trading/error-code#-5006-items_exist "-5006 ITEMS_EXIST的直接链接")

  * 项目 '%s' 已存在。



### -5007 USER_API_EXIST[​](/docs/zh-CN/derivatives/options-trading/error-code#-5007-user_api_exist "-5007 USER_API_EXIST的直接链接")

  * 用户 API 已存在。



### -5008 KYC_NOT_PASS[​](/docs/zh-CN/derivatives/options-trading/error-code#-5008-kyc_not_pass "-5008 KYC_NOT_PASS的直接链接")

  * 用户 KYC 未通过。



### -5009 IP_COUNTRY_BLACK[​](/docs/zh-CN/derivatives/options-trading/error-code#-5009-ip_country_black "-5009 IP_COUNTRY_BLACK的直接链接")

  * 所在 IP 属于受限司法辖区。



### -5010 NOT_ENOUGH_POSITION[​](/docs/zh-CN/derivatives/options-trading/error-code#-5010-not_enough_position "-5010 NOT_ENOUGH_POSITION的直接链接")

  * 用户没有足够的仓位卖出。



### -6001 INVALID_MMP_WINDOW_TIME_LIMIT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6001-invalid_mmp_window_time_limit "-6001 INVALID_MMP_WINDOW_TIME_LIMIT的直接链接")

  * MMP 窗口时间限制无效。



### -6002 INVALID_MMP_FROZEN_TIME_LIMIT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6002-invalid_mmp_frozen_time_limit "-6002 INVALID_MMP_FROZEN_TIME_LIMIT的直接链接")

  * MMP 冻结时间限制无效。



### -6003 INVALID_UNDERLYING[​](/docs/zh-CN/derivatives/options-trading/error-code#-6003-invalid_underlying "-6003 INVALID_UNDERLYING的直接链接")

  * 标的物无效。



### -6004 MMP_UNDERLYING_NOT_FOUND[​](/docs/zh-CN/derivatives/options-trading/error-code#-6004-mmp_underlying_not_found "-6004 MMP_UNDERLYING_NOT_FOUND的直接链接")

  * 未找到标的物。



### -6005 IS_NOT_MARKET_MAKER[​](/docs/zh-CN/derivatives/options-trading/error-code#-6005-is_not_market_maker "-6005 IS_NOT_MARKET_MAKER的直接链接")

  * 该用户不是做市商。



### -6006 MMP_RULES_NOT_EXISTING[​](/docs/zh-CN/derivatives/options-trading/error-code#-6006-mmp_rules_not_existing "-6006 MMP_RULES_NOT_EXISTING的直接链接")

  * MMP 规则不存在。



### -6007 MMP_ERROR_UNKNOWN[​](/docs/zh-CN/derivatives/options-trading/error-code#-6007-mmp_error_unknown "-6007 MMP_ERROR_UNKNOWN的直接链接")

  * MMP 未知错误。



### -6008 INVALID_LIMIT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6008-invalid_limit "-6008 INVALID_LIMIT的直接链接")

  * 参数 'limit' 无效。



### -6009 INVALID_COUNTDOWN_TIME[​](/docs/zh-CN/derivatives/options-trading/error-code#-6009-invalid_countdown_time "-6009 INVALID_COUNTDOWN_TIME的直接链接")

  * countdownTime 必须大于等于 5000 或等于 0。



### -6010 OPEN_INTEREST_ERR_DATA[​](/docs/zh-CN/derivatives/options-trading/error-code#-6010-open_interest_err_data "-6010 OPEN_INTEREST_ERR_DATA的直接链接")

  * 持仓量数据异常。



### -6011 EXCEED_MAXIMUM_BATCH_ORDERS[​](/docs/zh-CN/derivatives/options-trading/error-code#-6011-exceed_maximum_batch_orders "-6011 EXCEED_MAXIMUM_BATCH_ORDERS的直接链接")

  * 每次 batchOrder 最多允许下 10 单。



### -6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS[​](/docs/zh-CN/derivatives/options-trading/error-code#-6012-exceed_maximum_block_order_legs "-6012 EXCEED_MAXIMUM_BLOCK_ORDER_LEGS的直接链接")

  * Block order 的腿数超过最大限制。



### -6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL[​](/docs/zh-CN/derivatives/options-trading/error-code#-6013-block_order_legs_with_duplicate_symbol "-6013 BLOCK_ORDER_LEGS_WITH_DUPLICATE_SYMBOL的直接链接")

  * Block order 中包含重复的 symbol。



### -6014 GRFQ_INVALID_LEGS[​](/docs/zh-CN/derivatives/options-trading/error-code#-6014-grfq_invalid_legs "-6014 GRFQ_INVALID_LEGS的直接链接")

  * Legs 参数无效。



### -6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY[​](/docs/zh-CN/derivatives/options-trading/error-code#-6015-grfq_qty_is_not_multiple_of_minimum_qty "-6015 GRFQ_QTY_IS_NOT_MULTIPLE_OF_MINIMUM_QTY的直接链接")

  * 数量不是最小数量的整数倍。



### -6016 GRFQ_QUOTE_NOT_FOUND[​](/docs/zh-CN/derivatives/options-trading/error-code#-6016-grfq_quote_not_found "-6016 GRFQ_QUOTE_NOT_FOUND的直接链接")

  * 报价未找到。



### -6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6017-grfq_quote_not_enough_qty_left "-6017 GRFQ_QUOTE_NOT_ENOUGH_QTY_LEFT的直接链接")

  * 剩余数量不足。



### -6018 GRFQ_QUOTE_REQUEST_NOT_FOUND[​](/docs/zh-CN/derivatives/options-trading/error-code#-6018-grfq_quote_request_not_found "-6018 GRFQ_QUOTE_REQUEST_NOT_FOUND的直接链接")

  * 报价请求未找到。



### -6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME[​](/docs/zh-CN/derivatives/options-trading/error-code#-6019-grfq_quote_invalid_expire_time "-6019 GRFQ_QUOTE_INVALID_EXPIRE_TIME的直接链接")

  * 报价过期时间无效。



### -6020 GRFQ_QUOTE_EXPIRED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6020-grfq_quote_expired "-6020 GRFQ_QUOTE_EXPIRED的直接链接")

  * 报价已过期。



### -6021 GRFQ_INVALID_SIDE[​](/docs/zh-CN/derivatives/options-trading/error-code#-6021-grfq_invalid_side "-6021 GRFQ_INVALID_SIDE的直接链接")

  * Side 参数无效。



### -6022 GRFQ_INVALID_USER[​](/docs/zh-CN/derivatives/options-trading/error-code#-6022-grfq_invalid_user "-6022 GRFQ_INVALID_USER的直接链接")

  * 非 Global RFQ 用户。



### -6023 SELF_TRADE_PREVENTION[​](/docs/zh-CN/derivatives/options-trading/error-code#-6023-self_trade_prevention "-6023 SELF_TRADE_PREVENTION的直接链接")

  * 触发自成交保护。



### -6024 CHANGE_USER_FLAG_FAILED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6024-change_user_flag_failed "-6024 CHANGE_USER_FLAG_FAILED的直接链接")

  * 修改用户标志失败。



### -6025 GRFQ_INVALID_QUOTE_PRICE[​](/docs/zh-CN/derivatives/options-trading/error-code#-6025-grfq_invalid_quote_price "-6025 GRFQ_INVALID_QUOTE_PRICE的直接链接")

  * 报价价格无效。



### -6026 INVALID_QTY[​](/docs/zh-CN/derivatives/options-trading/error-code#-6026-invalid_qty "-6026 INVALID_QTY的直接链接")

  * 数量无效。



### -6027 INVALID_PRICE[​](/docs/zh-CN/derivatives/options-trading/error-code#-6027-invalid_price "-6027 INVALID_PRICE的直接链接")

  * 价格无效。



### -6028 ORDER_IS_FINAL[​](/docs/zh-CN/derivatives/options-trading/error-code#-6028-order_is_final "-6028 ORDER_IS_FINAL的直接链接")

  * 订单已经处于最终状态。



### -6029 PARAMETER_IS_REQUIRED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6029-parameter_is_required "-6029 PARAMETER_IS_REQUIRED的直接链接")

  * %s 为必填参数。



### -6030 INVALID_TIME_INTERVAL[​](/docs/zh-CN/derivatives/options-trading/error-code#-6030-invalid_time_interval "-6030 INVALID_TIME_INTERVAL的直接链接")

  * 时间区间无效。



### -6031 START_TIME_GREATER_THAN_END_TIME[​](/docs/zh-CN/derivatives/options-trading/error-code#-6031-start_time_greater_than_end_time "-6031 START_TIME_GREATER_THAN_END_TIME的直接链接")

  * 开始时间大于结束时间。



### -6032 HAS_OPEN_ORDER[​](/docs/zh-CN/derivatives/options-trading/error-code#-6032-has_open_order "-6032 HAS_OPEN_ORDER的直接链接")

  * 存在未完成订单。



### -6033 HAS_NEGATIVE_BALANCE[​](/docs/zh-CN/derivatives/options-trading/error-code#-6033-has_negative_balance "-6033 HAS_NEGATIVE_BALANCE的直接链接")

  * 存在负余额。



### -6034 HAS_POSITION[​](/docs/zh-CN/derivatives/options-trading/error-code#-6034-has_position "-6034 HAS_POSITION的直接链接")

  * 用户存在持仓。



### -6035 NO_NEED_TO_CHANGE[​](/docs/zh-CN/derivatives/options-trading/error-code#-6035-no_need_to_change "-6035 NO_NEED_TO_CHANGE的直接链接")

  * 无需变更。



### -6036 NO_PERMISSION_TO_CHANGE[​](/docs/zh-CN/derivatives/options-trading/error-code#-6036-no_permission_to_change "-6036 NO_PERMISSION_TO_CHANGE的直接链接")

  * 无权限变更。



### -6037 NO_RECORDS_FOUND[​](/docs/zh-CN/derivatives/options-trading/error-code#-6037-no_records_found "-6037 NO_RECORDS_FOUND的直接链接")

  * 未找到记录。



### -6038 SCALE_NOT_MATCH[​](/docs/zh-CN/derivatives/options-trading/error-code#-6038-scale_not_match "-6038 SCALE_NOT_MATCH的直接链接")

  * 精度不匹配。



### -6039 INVALID_STEP_SIZE_PRECISION[​](/docs/zh-CN/derivatives/options-trading/error-code#-6039-invalid_step_size_precision "-6039 INVALID_STEP_SIZE_PRECISION的直接链接")

  * 步长精度无效。



### -6040 INVALID_QTYLIMIT_DELTALIMIT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6040-invalid_qtylimit_deltalimit "-6040 INVALID_QTYLIMIT_DELTALIMIT的直接链接")

  * qtyLimit 或 deltaLimit 无效。



### -6041 START_TRADING_MUST_SLOWLY[​](/docs/zh-CN/derivatives/options-trading/error-code#-6041-start_trading_must_slowly "-6041 START_TRADING_MUST_SLOWLY的直接链接")

  * 开始交易需逐步进行。



### -6042 INDEX_COMMISSION_NOT_MATCH[​](/docs/zh-CN/derivatives/options-trading/error-code#-6042-index_commission_not_match "-6042 INDEX_COMMISSION_NOT_MATCH的直接链接")

  * 指数手续费不匹配。



### -6043 INDEX_RISKPARAMETER_NOT_MATCH[​](/docs/zh-CN/derivatives/options-trading/error-code#-6043-index_riskparameter_not_match "-6043 INDEX_RISKPARAMETER_NOT_MATCH的直接链接")

  * 指数风险参数不匹配。



### -6044 CLI_ORD_ID_ERROR[​](/docs/zh-CN/derivatives/options-trading/error-code#-6044-cli_ord_id_error "-6044 CLI_ORD_ID_ERROR的直接链接")

  * clientOrderId 已被使用。



### -6045 REDUCE_ONLY_REJECT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6045-reduce_only_reject "-6045 REDUCE_ONLY_REJECT的直接链接")

  * Reduce-Only 订单被拒绝。新的 Reduce-Only 订单与现有同向挂单冲突。请取消冲突订单后重试。



### -6046 FOK_ORDER_REJECT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6046-fok_order_reject "-6046 FOK_ORDER_REJECT的直接链接")

  * 因无法立即完全成交，FOK 订单被拒绝。



### -6047 GTX_ORDER_REJECT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6047-gtx_order_reject "-6047 GTX_ORDER_REJECT的直接链接")

  * 因无法作为 maker 执行，Post Only（GTX）订单被拒绝。



### -6048 INVALID_BLOCK_ORDER[​](/docs/zh-CN/derivatives/options-trading/error-code#-6048-invalid_block_order "-6048 INVALID_BLOCK_ORDER的直接链接")

  * Block order 参数无效。



### -6049 SYMBOL_NOT_TRADING[​](/docs/zh-CN/derivatives/options-trading/error-code#-6049-symbol_not_trading "-6049 SYMBOL_NOT_TRADING的直接链接")

  * 当前交易对不在交易状态。



### -6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6050-max_open_orders_on_symbol_exceeded "-6050 MAX_OPEN_ORDERS_ON_SYMBOL_EXCEEDED的直接链接")

  * 当前交易对已达最大挂单数量，请取消部分订单后重试。



### -6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6051-max_open_orders_on_index_exceeded "-6051 MAX_OPEN_ORDERS_ON_INDEX_EXCEEDED的直接链接")

  * 当前标的已达最大挂单数量，请取消部分订单后重试。



### -6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6052-max_short_position_on_symbol_exceeded "-6052 MAX_SHORT_POSITION_ON_SYMBOL_EXCEEDED的直接链接")

  * 当前交易对的最大可开空头仓位已达到上限。



### -6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6053-max_short_position_on_index_exceeded "-6053 MAX_SHORT_POSITION_ON_INDEX_EXCEEDED的直接链接")

  * 当前标的的最大可开空头仓位已达到上限。



### -6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6054-max_quantity_on_single_order_exceeded "-6054 MAX_QUANTITY_ON_SINGLE_ORDER_EXCEEDED的直接链接")

  * 下单数量超过最大限制。



### -6055 USER_LIQUIDATING[​](/docs/zh-CN/derivatives/options-trading/error-code#-6055-user_liquidating "-6055 USER_LIQUIDATING的直接链接")

  * 用户正在爆仓处理中。



### -6056 REDUCE_ONLY_MARGIN_CHECK_FAILED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6056-reduce_only_margin_check_failed "-6056 REDUCE_ONLY_MARGIN_CHECK_FAILED的直接链接")

  * Reduce-Only 下单失败。新下单与现有同方向挂单叠加会导致反向持仓并造成保证金不足，请取消相关挂单后重试。



### -6057 WRITER_CANT_NAKED_SELL[​](/docs/zh-CN/derivatives/options-trading/error-code#-6057-writer_cant_naked_sell "-6057 WRITER_CANT_NAKED_SELL的直接链接")

  * 当前交易对不支持裸卖（Option Writing）。



### -6058 MMP_TRIGGERED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6058-mmp_triggered "-6058 MMP_TRIGGERED的直接链接")

  * MMP 已触发，请重置 MMP 配置。



### -6059 USER_IN_LIQUIDATION[​](/docs/zh-CN/derivatives/options-trading/error-code#-6059-user_in_liquidation "-6059 USER_IN_LIQUIDATION的直接链接")

  * 用户正在爆仓处理中。



### -6060 LOCKED_BALANCE_NOT_FOUND[​](/docs/zh-CN/derivatives/options-trading/error-code#-6060-locked_balance_not_found "-6060 LOCKED_BALANCE_NOT_FOUND的直接链接")

  * OTC 下单失败：无法锁定余额。



### -6061 LOCKED_OTC_ORDER_NOT_FOUNT[​](/docs/zh-CN/derivatives/options-trading/error-code#-6061-locked_otc_order_not_fount "-6061 LOCKED_OTC_ORDER_NOT_FOUNT的直接链接")

  * OTC 下单失败：无法锁定订单。



### -6062 INVALID_USER_STATUS[​](/docs/zh-CN/derivatives/options-trading/error-code#-6062-invalid_user_status "-6062 INVALID_USER_STATUS的直接链接")

  * 当前用户状态不支持此操作。



### -6063 CANCEL_REJECTED[​](/docs/zh-CN/derivatives/options-trading/error-code#-6063-cancel_rejected "-6063 CANCEL_REJECTED的直接链接")

  * 系统拒绝取消订单。