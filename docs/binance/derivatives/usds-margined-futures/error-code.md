---
exchange: binance
source_url: https://developers.binance.com/docs/derivatives/usds-margined-futures/error-code
api_type: REST
updated_at: 2026-01-15T23:46:40.130606
---

# Error Codes

> Here is the error JSON payload:
    
    
    {  
      "code":-1121,  
      "msg":"Invalid symbol."  
    }  
    

Errors consist of two parts: an error code and a message.  
Codes are universal,but messages can vary.

## 10xx - General Server or Network issues[​](/docs/derivatives/usds-margined-futures/error-code#10xx---general-server-or-network-issues "Direct link to 10xx - General Server or Network issues")

### -1000 UNKNOWN[​](/docs/derivatives/usds-margined-futures/error-code#-1000-unknown "Direct link to -1000 UNKNOWN")

  * An unknown error occured while processing the request.



### -1001 DISCONNECTED[​](/docs/derivatives/usds-margined-futures/error-code#-1001-disconnected "Direct link to -1001 DISCONNECTED")

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED[​](/docs/derivatives/usds-margined-futures/error-code#-1002-unauthorized "Direct link to -1002 UNAUTHORIZED")

  * You are not authorized to execute this request.



### -1003 TOO_MANY_REQUESTS[​](/docs/derivatives/usds-margined-futures/error-code#-1003-too_many_requests "Direct link to -1003 TOO_MANY_REQUESTS")

  * Too many requests; current limit is %s requests per minute. Please use the websocket for live updates to avoid polling the API.
  * Way too many requests; IP banned until %s. Please use the websocket for live updates to avoid bans.



### -1004 DUPLICATE_IP[​](/docs/derivatives/usds-margined-futures/error-code#-1004-duplicate_ip "Direct link to -1004 DUPLICATE_IP")

  * This IP is already on the white list



### -1005 NO_SUCH_IP[​](/docs/derivatives/usds-margined-futures/error-code#-1005-no_such_ip "Direct link to -1005 NO_SUCH_IP")

  * No such IP has been white listed



### -1006 UNEXPECTED_RESP[​](/docs/derivatives/usds-margined-futures/error-code#-1006-unexpected_resp "Direct link to -1006 UNEXPECTED_RESP")

  * An unexpected response was received from the message bus. Execution status unknown.



### -1007 TIMEOUT[​](/docs/derivatives/usds-margined-futures/error-code#-1007-timeout "Direct link to -1007 TIMEOUT")

  * Timeout waiting for response from backend server. Send status unknown; execution status unknown.



### -1008 Request Throttled[​](/docs/derivatives/usds-margined-futures/error-code#-1008-request-throttled "Direct link to -1008 Request Throttled")

  * Server is currently overloaded with other requests. Please try again in a few minutes.
  * Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again.



### -1010 ERROR_MSG_RECEIVED[​](/docs/derivatives/usds-margined-futures/error-code#-1010-error_msg_received "Direct link to -1010 ERROR_MSG_RECEIVED")

  * ERROR_MSG_RECEIVED.



### -1011 NON_WHITE_LIST[​](/docs/derivatives/usds-margined-futures/error-code#-1011-non_white_list "Direct link to -1011 NON_WHITE_LIST")

  * This IP cannot access this route.



### -1013 INVALID_MESSAGE[​](/docs/derivatives/usds-margined-futures/error-code#-1013-invalid_message "Direct link to -1013 INVALID_MESSAGE")

  * INVALID_MESSAGE.



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/derivatives/usds-margined-futures/error-code#-1014-unknown_order_composition "Direct link to -1014 UNKNOWN_ORDER_COMPOSITION")

  * Unsupported order combination.



### -1015 TOO_MANY_ORDERS[​](/docs/derivatives/usds-margined-futures/error-code#-1015-too_many_orders "Direct link to -1015 TOO_MANY_ORDERS")

  * Too many new orders.
  * Too many new orders; current limit is %s orders per %s.



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/derivatives/usds-margined-futures/error-code#-1016-service_shutting_down "Direct link to -1016 SERVICE_SHUTTING_DOWN")

  * This service is no longer available.



### -1020 UNSUPPORTED_OPERATION[​](/docs/derivatives/usds-margined-futures/error-code#-1020-unsupported_operation "Direct link to -1020 UNSUPPORTED_OPERATION")

  * This operation is not supported.



### -1021 INVALID_TIMESTAMP[​](/docs/derivatives/usds-margined-futures/error-code#-1021-invalid_timestamp "Direct link to -1021 INVALID_TIMESTAMP")

  * Timestamp for this request is outside of the recvWindow.
  * Timestamp for this request was 1000ms ahead of the server's time.



### -1022 INVALID_SIGNATURE[​](/docs/derivatives/usds-margined-futures/error-code#-1022-invalid_signature "Direct link to -1022 INVALID_SIGNATURE")

  * Signature for this request is not valid.



### -1023 START_TIME_GREATER_THAN_END_TIME[​](/docs/derivatives/usds-margined-futures/error-code#-1023-start_time_greater_than_end_time "Direct link to -1023 START_TIME_GREATER_THAN_END_TIME")

  * Start time is greater than end time.



### -1099 NOT_FOUND[​](/docs/derivatives/usds-margined-futures/error-code#-1099-not_found "Direct link to -1099 NOT_FOUND")

  * Not found, unauthenticated, or unauthorized.



## 11xx - Request issues[​](/docs/derivatives/usds-margined-futures/error-code#11xx---request-issues "Direct link to 11xx - Request issues")

### -1100 ILLEGAL_CHARS[​](/docs/derivatives/usds-margined-futures/error-code#-1100-illegal_chars "Direct link to -1100 ILLEGAL_CHARS")

  * Illegal characters found in a parameter.
  * Illegal characters found in parameter '%s'; legal range is '%s'.



### -1101 TOO_MANY_PARAMETERS[​](/docs/derivatives/usds-margined-futures/error-code#-1101-too_many_parameters "Direct link to -1101 TOO_MANY_PARAMETERS")

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected '%s' and received '%s'.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/derivatives/usds-margined-futures/error-code#-1102-mandatory_param_empty_or_malformed "Direct link to -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
  * Param '%s' or '%s' must be sent, but both were empty/null!



### -1103 UNKNOWN_PARAM[​](/docs/derivatives/usds-margined-futures/error-code#-1103-unknown_param "Direct link to -1103 UNKNOWN_PARAM")

  * An unknown parameter was sent.



### -1104 UNREAD_PARAMETERS[​](/docs/derivatives/usds-margined-futures/error-code#-1104-unread_parameters "Direct link to -1104 UNREAD_PARAMETERS")

  * Not all sent parameters were read.
  * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.



### -1105 PARAM_EMPTY[​](/docs/derivatives/usds-margined-futures/error-code#-1105-param_empty "Direct link to -1105 PARAM_EMPTY")

  * A parameter was empty.
  * Parameter '%s' was empty.



### -1106 PARAM_NOT_REQUIRED[​](/docs/derivatives/usds-margined-futures/error-code#-1106-param_not_required "Direct link to -1106 PARAM_NOT_REQUIRED")

  * A parameter was sent when not required.
  * Parameter '%s' sent when not required.



### -1108 BAD_ASSET[​](/docs/derivatives/usds-margined-futures/error-code#-1108-bad_asset "Direct link to -1108 BAD_ASSET")

  * Invalid asset.



### -1109 BAD_ACCOUNT[​](/docs/derivatives/usds-margined-futures/error-code#-1109-bad_account "Direct link to -1109 BAD_ACCOUNT")

  * Invalid account.



### -1110 BAD_INSTRUMENT_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-1110-bad_instrument_type "Direct link to -1110 BAD_INSTRUMENT_TYPE")

  * Invalid symbolType.



### -1111 BAD_PRECISION[​](/docs/derivatives/usds-margined-futures/error-code#-1111-bad_precision "Direct link to -1111 BAD_PRECISION")

  * Precision is over the maximum defined for this asset.



### -1112 NO_DEPTH[​](/docs/derivatives/usds-margined-futures/error-code#-1112-no_depth "Direct link to -1112 NO_DEPTH")

  * No orders on book for symbol.



### -1113 WITHDRAW_NOT_NEGATIVE[​](/docs/derivatives/usds-margined-futures/error-code#-1113-withdraw_not_negative "Direct link to -1113 WITHDRAW_NOT_NEGATIVE")

  * Withdrawal amount must be negative.



### -1114 TIF_NOT_REQUIRED[​](/docs/derivatives/usds-margined-futures/error-code#-1114-tif_not_required "Direct link to -1114 TIF_NOT_REQUIRED")

  * TimeInForce parameter sent when not required.



### -1115 INVALID_TIF[​](/docs/derivatives/usds-margined-futures/error-code#-1115-invalid_tif "Direct link to -1115 INVALID_TIF")

  * Invalid timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-1116-invalid_order_type "Direct link to -1116 INVALID_ORDER_TYPE")

  * Invalid orderType.



### -1117 INVALID_SIDE[​](/docs/derivatives/usds-margined-futures/error-code#-1117-invalid_side "Direct link to -1117 INVALID_SIDE")

  * Invalid side.



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/derivatives/usds-margined-futures/error-code#-1118-empty_new_cl_ord_id "Direct link to -1118 EMPTY_NEW_CL_ORD_ID")

  * New client order ID was empty.



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/derivatives/usds-margined-futures/error-code#-1119-empty_org_cl_ord_id "Direct link to -1119 EMPTY_ORG_CL_ORD_ID")

  * Original client order ID was empty.



### -1120 BAD_INTERVAL[​](/docs/derivatives/usds-margined-futures/error-code#-1120-bad_interval "Direct link to -1120 BAD_INTERVAL")

  * Invalid interval.



### -1121 BAD_SYMBOL[​](/docs/derivatives/usds-margined-futures/error-code#-1121-bad_symbol "Direct link to -1121 BAD_SYMBOL")

  * Invalid symbol.



### -1122 INVALID_SYMBOL_STATUS[​](/docs/derivatives/usds-margined-futures/error-code#-1122-invalid_symbol_status "Direct link to -1122 INVALID_SYMBOL_STATUS")

  * Invalid symbol status.



### -1125 INVALID_LISTEN_KEY[​](/docs/derivatives/usds-margined-futures/error-code#-1125-invalid_listen_key "Direct link to -1125 INVALID_LISTEN_KEY")

  * This listenKey does not exist. Please use `POST /fapi/v1/listenKey` to recreate `listenKey`



### -1126 ASSET_NOT_SUPPORTED[​](/docs/derivatives/usds-margined-futures/error-code#-1126-asset_not_supported "Direct link to -1126 ASSET_NOT_SUPPORTED")

  * This asset is not supported.



### -1127 MORE_THAN_XX_HOURS[​](/docs/derivatives/usds-margined-futures/error-code#-1127-more_than_xx_hours "Direct link to -1127 MORE_THAN_XX_HOURS")

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 OPTIONAL_PARAMS_BAD_COMBO[​](/docs/derivatives/usds-margined-futures/error-code#-1128-optional_params_bad_combo "Direct link to -1128 OPTIONAL_PARAMS_BAD_COMBO")

  * Combination of optional parameters invalid.



### -1130 INVALID_PARAMETER[​](/docs/derivatives/usds-margined-futures/error-code#-1130-invalid_parameter "Direct link to -1130 INVALID_PARAMETER")

  * Invalid data sent for a parameter.
  * Data sent for parameter '%s' is not valid.



### -1136 INVALID_NEW_ORDER_RESP_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-1136-invalid_new_order_resp_type "Direct link to -1136 INVALID_NEW_ORDER_RESP_TYPE")

  * Invalid newOrderRespType.



## 20xx - Processing Issues[​](/docs/derivatives/usds-margined-futures/error-code#20xx---processing-issues "Direct link to 20xx - Processing Issues")

### -2010 NEW_ORDER_REJECTED[​](/docs/derivatives/usds-margined-futures/error-code#-2010-new_order_rejected "Direct link to -2010 NEW_ORDER_REJECTED")

  * NEW_ORDER_REJECTED



### -2011 CANCEL_REJECTED[​](/docs/derivatives/usds-margined-futures/error-code#-2011-cancel_rejected "Direct link to -2011 CANCEL_REJECTED")

  * CANCEL_REJECTED
  * Cancel request failure as open order not found in the orderbook: "Unknown order sent".



### -2012 CANCEL_ALL_FAIL[​](/docs/derivatives/usds-margined-futures/error-code#-2012-cancel_all_fail "Direct link to -2012 CANCEL_ALL_FAIL")

  * Batch cancel failure.



### -2013 NO_SUCH_ORDER[​](/docs/derivatives/usds-margined-futures/error-code#-2013-no_such_order "Direct link to -2013 NO_SUCH_ORDER")

  * Order does not exist.



### -2014 BAD_API_KEY_FMT[​](/docs/derivatives/usds-margined-futures/error-code#-2014-bad_api_key_fmt "Direct link to -2014 BAD_API_KEY_FMT")

  * API-key format invalid.



### -2015 REJECTED_MBX_KEY[​](/docs/derivatives/usds-margined-futures/error-code#-2015-rejected_mbx_key "Direct link to -2015 REJECTED_MBX_KEY")

  * Invalid API-key, IP, or permissions for action.



### -2016 NO_TRADING_WINDOW[​](/docs/derivatives/usds-margined-futures/error-code#-2016-no_trading_window "Direct link to -2016 NO_TRADING_WINDOW")

  * No trading window could be found for the symbol. Try ticker/24hrs instead.



### -2017 API_KEYS_LOCKED[​](/docs/derivatives/usds-margined-futures/error-code#-2017-api_keys_locked "Direct link to -2017 API_KEYS_LOCKED")

  * API Keys are locked on this account.



### -2018 BALANCE_NOT_SUFFICIENT[​](/docs/derivatives/usds-margined-futures/error-code#-2018-balance_not_sufficient "Direct link to -2018 BALANCE_NOT_SUFFICIENT")

  * Balance is insufficient.



### -2019 MARGIN_NOT_SUFFICIEN[​](/docs/derivatives/usds-margined-futures/error-code#-2019-margin_not_sufficien "Direct link to -2019 MARGIN_NOT_SUFFICIEN")

  * Margin is insufficient.



### -2020 UNABLE_TO_FILL[​](/docs/derivatives/usds-margined-futures/error-code#-2020-unable_to_fill "Direct link to -2020 UNABLE_TO_FILL")

  * Unable to fill.



### -2021 ORDER_WOULD_IMMEDIATELY_TRIGGER[​](/docs/derivatives/usds-margined-futures/error-code#-2021-order_would_immediately_trigger "Direct link to -2021 ORDER_WOULD_IMMEDIATELY_TRIGGER")

  * Order would immediately trigger.



### -2022 REDUCE_ONLY_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-2022-reduce_only_reject "Direct link to -2022 REDUCE_ONLY_REJECT")

  * ReduceOnly Order is rejected.
  * This indicates the new reduce-only order conflicts with existing open orders; cancel the existing order and resubmit the reduce-only order.



### -2023 USER_IN_LIQUIDATION[​](/docs/derivatives/usds-margined-futures/error-code#-2023-user_in_liquidation "Direct link to -2023 USER_IN_LIQUIDATION")

  * User in liquidation mode now.



### -2024 POSITION_NOT_SUFFICIENT[​](/docs/derivatives/usds-margined-futures/error-code#-2024-position_not_sufficient "Direct link to -2024 POSITION_NOT_SUFFICIENT")

  * Position is not sufficient.



### -2025 MAX_OPEN_ORDER_EXCEEDED[​](/docs/derivatives/usds-margined-futures/error-code#-2025-max_open_order_exceeded "Direct link to -2025 MAX_OPEN_ORDER_EXCEEDED")

  * Reach max open order limit.



### -2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED[​](/docs/derivatives/usds-margined-futures/error-code#-2026-reduce_only_order_type_not_supported "Direct link to -2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED")

  * This OrderType is not supported when reduceOnly.



### -2027 MAX_LEVERAGE_RATIO[​](/docs/derivatives/usds-margined-futures/error-code#-2027-max_leverage_ratio "Direct link to -2027 MAX_LEVERAGE_RATIO")

  * Exceeded the maximum allowable position at current leverage.



### -2028 MIN_LEVERAGE_RATIO[​](/docs/derivatives/usds-margined-futures/error-code#-2028-min_leverage_ratio "Direct link to -2028 MIN_LEVERAGE_RATIO")

  * Leverage is smaller than permitted: insufficient margin balance.



## 40xx - Filters and other Issues[​](/docs/derivatives/usds-margined-futures/error-code#40xx---filters-and-other-issues "Direct link to 40xx - Filters and other Issues")

### -4000 INVALID_ORDER_STATUS[​](/docs/derivatives/usds-margined-futures/error-code#-4000-invalid_order_status "Direct link to -4000 INVALID_ORDER_STATUS")

  * Invalid order status.



### -4001 PRICE_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4001-price_less_than_zero "Direct link to -4001 PRICE_LESS_THAN_ZERO")

  * Price less than 0.



### -4002 PRICE_GREATER_THAN_MAX_PRICE[​](/docs/derivatives/usds-margined-futures/error-code#-4002-price_greater_than_max_price "Direct link to -4002 PRICE_GREATER_THAN_MAX_PRICE")

  * Price greater than max price.



### -4003 QTY_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4003-qty_less_than_zero "Direct link to -4003 QTY_LESS_THAN_ZERO")

  * Quantity less than zero.



### -4004 QTY_LESS_THAN_MIN_QTY[​](/docs/derivatives/usds-margined-futures/error-code#-4004-qty_less_than_min_qty "Direct link to -4004 QTY_LESS_THAN_MIN_QTY")

  * Quantity less than min quantity.



### -4005 QTY_GREATER_THAN_MAX_QTY[​](/docs/derivatives/usds-margined-futures/error-code#-4005-qty_greater_than_max_qty "Direct link to -4005 QTY_GREATER_THAN_MAX_QTY")

  * Quantity greater than max quantity.



### -4006 STOP_PRICE_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4006-stop_price_less_than_zero "Direct link to -4006 STOP_PRICE_LESS_THAN_ZERO")

  * Stop price less than zero.



### -4007 STOP_PRICE_GREATER_THAN_MAX_PRICE[​](/docs/derivatives/usds-margined-futures/error-code#-4007-stop_price_greater_than_max_price "Direct link to -4007 STOP_PRICE_GREATER_THAN_MAX_PRICE")

  * Stop price greater than max price.



### -4008 TICK_SIZE_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4008-tick_size_less_than_zero "Direct link to -4008 TICK_SIZE_LESS_THAN_ZERO")

  * Tick size less than zero.



### -4009 MAX_PRICE_LESS_THAN_MIN_PRICE[​](/docs/derivatives/usds-margined-futures/error-code#-4009-max_price_less_than_min_price "Direct link to -4009 MAX_PRICE_LESS_THAN_MIN_PRICE")

  * Max price less than min price.



### -4010 MAX_QTY_LESS_THAN_MIN_QTY[​](/docs/derivatives/usds-margined-futures/error-code#-4010-max_qty_less_than_min_qty "Direct link to -4010 MAX_QTY_LESS_THAN_MIN_QTY")

  * Max qty less than min qty.



### -4011 STEP_SIZE_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4011-step_size_less_than_zero "Direct link to -4011 STEP_SIZE_LESS_THAN_ZERO")

  * Step size less than zero.



### -4012 MAX_NUM_ORDERS_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4012-max_num_orders_less_than_zero "Direct link to -4012 MAX_NUM_ORDERS_LESS_THAN_ZERO")

  * Max mum orders less than zero.



### -4013 PRICE_LESS_THAN_MIN_PRICE[​](/docs/derivatives/usds-margined-futures/error-code#-4013-price_less_than_min_price "Direct link to -4013 PRICE_LESS_THAN_MIN_PRICE")

  * Price less than min price.



### -4014 PRICE_NOT_INCREASED_BY_TICK_SIZE[​](/docs/derivatives/usds-margined-futures/error-code#-4014-price_not_increased_by_tick_size "Direct link to -4014 PRICE_NOT_INCREASED_BY_TICK_SIZE")

  * Price not increased by tick size.



### -4015 INVALID_CL_ORD_ID_LEN[​](/docs/derivatives/usds-margined-futures/error-code#-4015-invalid_cl_ord_id_len "Direct link to -4015 INVALID_CL_ORD_ID_LEN")

  * Client order id is not valid.
  * Client order id length should not be more than 36 chars



### -4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP[​](/docs/derivatives/usds-margined-futures/error-code#-4016-price_highter_than_multiplier_up "Direct link to -4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP")

  * Price is higher than mark price multiplier cap.



### -4017 MULTIPLIER_UP_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4017-multiplier_up_less_than_zero "Direct link to -4017 MULTIPLIER_UP_LESS_THAN_ZERO")

  * Multiplier up less than zero.



### -4018 MULTIPLIER_DOWN_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4018-multiplier_down_less_than_zero "Direct link to -4018 MULTIPLIER_DOWN_LESS_THAN_ZERO")

  * Multiplier down less than zero.



### -4019 COMPOSITE_SCALE_OVERFLOW[​](/docs/derivatives/usds-margined-futures/error-code#-4019-composite_scale_overflow "Direct link to -4019 COMPOSITE_SCALE_OVERFLOW")

  * Composite scale too large.



### -4020 TARGET_STRATEGY_INVALID[​](/docs/derivatives/usds-margined-futures/error-code#-4020-target_strategy_invalid "Direct link to -4020 TARGET_STRATEGY_INVALID")

  * Target strategy invalid for orderType '%s',reduceOnly '%b'.



### -4021 INVALID_DEPTH_LIMIT[​](/docs/derivatives/usds-margined-futures/error-code#-4021-invalid_depth_limit "Direct link to -4021 INVALID_DEPTH_LIMIT")

  * Invalid depth limit.
  * '%s' is not valid depth limit.



### -4022 WRONG_MARKET_STATUS[​](/docs/derivatives/usds-margined-futures/error-code#-4022-wrong_market_status "Direct link to -4022 WRONG_MARKET_STATUS")

  * market status sent is not valid.



### -4023 QTY_NOT_INCREASED_BY_STEP_SIZE[​](/docs/derivatives/usds-margined-futures/error-code#-4023-qty_not_increased_by_step_size "Direct link to -4023 QTY_NOT_INCREASED_BY_STEP_SIZE")

  * Qty not increased by step size.



### -4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN[​](/docs/derivatives/usds-margined-futures/error-code#-4024-price_lower_than_multiplier_down "Direct link to -4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN")

  * Price is lower than mark price multiplier floor.



### -4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4025-multiplier_decimal_less_than_zero "Direct link to -4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO")

  * Multiplier decimal less than zero.



### -4026 COMMISSION_INVALID[​](/docs/derivatives/usds-margined-futures/error-code#-4026-commission_invalid "Direct link to -4026 COMMISSION_INVALID")

  * Commission invalid.
  * `%s` less than zero.
  * `%s` absolute value greater than `%s`



### -4027 INVALID_ACCOUNT_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4027-invalid_account_type "Direct link to -4027 INVALID_ACCOUNT_TYPE")

  * Invalid account type.



### -4028 INVALID_LEVERAGE[​](/docs/derivatives/usds-margined-futures/error-code#-4028-invalid_leverage "Direct link to -4028 INVALID_LEVERAGE")

  * Invalid leverage
  * Leverage `%s` is not valid
  * Leverage `%s` already exist with `%s`



### -4029 INVALID_TICK_SIZE_PRECISION[​](/docs/derivatives/usds-margined-futures/error-code#-4029-invalid_tick_size_precision "Direct link to -4029 INVALID_TICK_SIZE_PRECISION")

  * Tick size precision is invalid.



### -4030 INVALID_STEP_SIZE_PRECISION[​](/docs/derivatives/usds-margined-futures/error-code#-4030-invalid_step_size_precision "Direct link to -4030 INVALID_STEP_SIZE_PRECISION")

  * Step size precision is invalid.



### -4031 INVALID_WORKING_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4031-invalid_working_type "Direct link to -4031 INVALID_WORKING_TYPE")

  * Invalid parameter working type
  * Invalid parameter working type: `%s`



### -4032 EXCEED_MAX_CANCEL_ORDER_SIZE[​](/docs/derivatives/usds-margined-futures/error-code#-4032-exceed_max_cancel_order_size "Direct link to -4032 EXCEED_MAX_CANCEL_ORDER_SIZE")

  * Exceed maximum cancel order size.
  * Invalid parameter working type: `%s`



### -4033 INSURANCE_ACCOUNT_NOT_FOUND[​](/docs/derivatives/usds-margined-futures/error-code#-4033-insurance_account_not_found "Direct link to -4033 INSURANCE_ACCOUNT_NOT_FOUND")

  * Insurance account not found.



### -4044 INVALID_BALANCE_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4044-invalid_balance_type "Direct link to -4044 INVALID_BALANCE_TYPE")

  * Balance Type is invalid.



### -4045 MAX_STOP_ORDER_EXCEEDED[​](/docs/derivatives/usds-margined-futures/error-code#-4045-max_stop_order_exceeded "Direct link to -4045 MAX_STOP_ORDER_EXCEEDED")

  * Reach max stop order limit.



### -4046 NO_NEED_TO_CHANGE_MARGIN_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4046-no_need_to_change_margin_type "Direct link to -4046 NO_NEED_TO_CHANGE_MARGIN_TYPE")

  * No need to change margin type.



### -4047 THERE_EXISTS_OPEN_ORDERS[​](/docs/derivatives/usds-margined-futures/error-code#-4047-there_exists_open_orders "Direct link to -4047 THERE_EXISTS_OPEN_ORDERS")

  * Margin type cannot be changed if there exists open orders.



### -4048 THERE_EXISTS_QUANTITY[​](/docs/derivatives/usds-margined-futures/error-code#-4048-there_exists_quantity "Direct link to -4048 THERE_EXISTS_QUANTITY")

  * Margin type cannot be changed if there exists position.



### -4049 ADD_ISOLATED_MARGIN_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-4049-add_isolated_margin_reject "Direct link to -4049 ADD_ISOLATED_MARGIN_REJECT")

  * Add margin only support for isolated position.



### -4050 CROSS_BALANCE_INSUFFICIENT[​](/docs/derivatives/usds-margined-futures/error-code#-4050-cross_balance_insufficient "Direct link to -4050 CROSS_BALANCE_INSUFFICIENT")

  * Cross balance insufficient.



### -4051 ISOLATED_BALANCE_INSUFFICIENT[​](/docs/derivatives/usds-margined-futures/error-code#-4051-isolated_balance_insufficient "Direct link to -4051 ISOLATED_BALANCE_INSUFFICIENT")

  * Isolated balance insufficient.



### -4052 NO_NEED_TO_CHANGE_AUTO_ADD_MARGIN[​](/docs/derivatives/usds-margined-futures/error-code#-4052-no_need_to_change_auto_add_margin "Direct link to -4052 NO_NEED_TO_CHANGE_AUTO_ADD_MARGIN")

  * No need to change auto add margin.



### -4053 AUTO_ADD_CROSSED_MARGIN_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-4053-auto_add_crossed_margin_reject "Direct link to -4053 AUTO_ADD_CROSSED_MARGIN_REJECT")

  * Auto add margin only support for isolated position.



### -4054 ADD_ISOLATED_MARGIN_NO_POSITION_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-4054-add_isolated_margin_no_position_reject "Direct link to -4054 ADD_ISOLATED_MARGIN_NO_POSITION_REJECT")

  * Cannot add position margin: position is 0.



### -4055 AMOUNT_MUST_BE_POSITIVE[​](/docs/derivatives/usds-margined-futures/error-code#-4055-amount_must_be_positive "Direct link to -4055 AMOUNT_MUST_BE_POSITIVE")

  * Amount must be positive.



### -4056 INVALID_API_KEY_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4056-invalid_api_key_type "Direct link to -4056 INVALID_API_KEY_TYPE")

  * Invalid api key type.



### -4057 INVALID_RSA_PUBLIC_KEY[​](/docs/derivatives/usds-margined-futures/error-code#-4057-invalid_rsa_public_key "Direct link to -4057 INVALID_RSA_PUBLIC_KEY")

  * Invalid api public key



### -4058 MAX_PRICE_TOO_LARGE[​](/docs/derivatives/usds-margined-futures/error-code#-4058-max_price_too_large "Direct link to -4058 MAX_PRICE_TOO_LARGE")

  * maxPrice and priceDecimal too large,please check.



### -4059 NO_NEED_TO_CHANGE_POSITION_SIDE[​](/docs/derivatives/usds-margined-futures/error-code#-4059-no_need_to_change_position_side "Direct link to -4059 NO_NEED_TO_CHANGE_POSITION_SIDE")

  * No need to change position side.



### -4060 INVALID_POSITION_SIDE[​](/docs/derivatives/usds-margined-futures/error-code#-4060-invalid_position_side "Direct link to -4060 INVALID_POSITION_SIDE")

  * Invalid position side.



### -4061 POSITION_SIDE_NOT_MATCH[​](/docs/derivatives/usds-margined-futures/error-code#-4061-position_side_not_match "Direct link to -4061 POSITION_SIDE_NOT_MATCH")

  * Order's position side does not match user's setting.



### -4062 REDUCE_ONLY_CONFLICT[​](/docs/derivatives/usds-margined-futures/error-code#-4062-reduce_only_conflict "Direct link to -4062 REDUCE_ONLY_CONFLICT")

  * Invalid or improper reduceOnly value.



### -4063 INVALID_OPTIONS_REQUEST_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4063-invalid_options_request_type "Direct link to -4063 INVALID_OPTIONS_REQUEST_TYPE")

  * Invalid options request type



### -4064 INVALID_OPTIONS_TIME_FRAME[​](/docs/derivatives/usds-margined-futures/error-code#-4064-invalid_options_time_frame "Direct link to -4064 INVALID_OPTIONS_TIME_FRAME")

  * Invalid options time frame



### -4065 INVALID_OPTIONS_AMOUNT[​](/docs/derivatives/usds-margined-futures/error-code#-4065-invalid_options_amount "Direct link to -4065 INVALID_OPTIONS_AMOUNT")

  * Invalid options amount



### -4066 INVALID_OPTIONS_EVENT_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4066-invalid_options_event_type "Direct link to -4066 INVALID_OPTIONS_EVENT_TYPE")

  * Invalid options event type



### -4067 POSITION_SIDE_CHANGE_EXISTS_OPEN_ORDERS[​](/docs/derivatives/usds-margined-futures/error-code#-4067-position_side_change_exists_open_orders "Direct link to -4067 POSITION_SIDE_CHANGE_EXISTS_OPEN_ORDERS")

  * Position side cannot be changed if there exists open orders.



### -4068 POSITION_SIDE_CHANGE_EXISTS_QUANTITY[​](/docs/derivatives/usds-margined-futures/error-code#-4068-position_side_change_exists_quantity "Direct link to -4068 POSITION_SIDE_CHANGE_EXISTS_QUANTITY")

  * Position side cannot be changed if there exists position.



### -4069 INVALID_OPTIONS_PREMIUM_FEE[​](/docs/derivatives/usds-margined-futures/error-code#-4069-invalid_options_premium_fee "Direct link to -4069 INVALID_OPTIONS_PREMIUM_FEE")

  * Invalid options premium fee



### -4070 INVALID_CL_OPTIONS_ID_LEN[​](/docs/derivatives/usds-margined-futures/error-code#-4070-invalid_cl_options_id_len "Direct link to -4070 INVALID_CL_OPTIONS_ID_LEN")

  * Client options id is not valid.
  * Client options id length should be less than 32 chars



### -4071 INVALID_OPTIONS_DIRECTION[​](/docs/derivatives/usds-margined-futures/error-code#-4071-invalid_options_direction "Direct link to -4071 INVALID_OPTIONS_DIRECTION")

  * Invalid options direction



### -4072 OPTIONS_PREMIUM_NOT_UPDATE[​](/docs/derivatives/usds-margined-futures/error-code#-4072-options_premium_not_update "Direct link to -4072 OPTIONS_PREMIUM_NOT_UPDATE")

  * premium fee is not updated, reject order



### -4073 OPTIONS_PREMIUM_INPUT_LESS_THAN_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4073-options_premium_input_less_than_zero "Direct link to -4073 OPTIONS_PREMIUM_INPUT_LESS_THAN_ZERO")

  * input premium fee is less than 0, reject order



### -4074 OPTIONS_AMOUNT_BIGGER_THAN_UPPER[​](/docs/derivatives/usds-margined-futures/error-code#-4074-options_amount_bigger_than_upper "Direct link to -4074 OPTIONS_AMOUNT_BIGGER_THAN_UPPER")

  * Order amount is bigger than upper boundary or less than 0, reject order



### -4075 OPTIONS_PREMIUM_OUTPUT_ZERO[​](/docs/derivatives/usds-margined-futures/error-code#-4075-options_premium_output_zero "Direct link to -4075 OPTIONS_PREMIUM_OUTPUT_ZERO")

  * output premium fee is less than 0, reject order



### -4076 OPTIONS_PREMIUM_TOO_DIFF[​](/docs/derivatives/usds-margined-futures/error-code#-4076-options_premium_too_diff "Direct link to -4076 OPTIONS_PREMIUM_TOO_DIFF")

  * original fee is too much higher than last fee



### -4077 OPTIONS_PREMIUM_REACH_LIMIT[​](/docs/derivatives/usds-margined-futures/error-code#-4077-options_premium_reach_limit "Direct link to -4077 OPTIONS_PREMIUM_REACH_LIMIT")

  * place order amount has reached to limit, reject order



### -4078 OPTIONS_COMMON_ERROR[​](/docs/derivatives/usds-margined-futures/error-code#-4078-options_common_error "Direct link to -4078 OPTIONS_COMMON_ERROR")

  * options internal error



### -4079 INVALID_OPTIONS_ID[​](/docs/derivatives/usds-margined-futures/error-code#-4079-invalid_options_id "Direct link to -4079 INVALID_OPTIONS_ID")

  * invalid options id
  * invalid options id: %s
  * duplicate options id %d for user %d



### -4080 OPTIONS_USER_NOT_FOUND[​](/docs/derivatives/usds-margined-futures/error-code#-4080-options_user_not_found "Direct link to -4080 OPTIONS_USER_NOT_FOUND")

  * user not found
  * user not found with id: %s



### -4081 OPTIONS_NOT_FOUND[​](/docs/derivatives/usds-margined-futures/error-code#-4081-options_not_found "Direct link to -4081 OPTIONS_NOT_FOUND")

  * options not found
  * options not found with id: %s



### -4082 INVALID_BATCH_PLACE_ORDER_SIZE[​](/docs/derivatives/usds-margined-futures/error-code#-4082-invalid_batch_place_order_size "Direct link to -4082 INVALID_BATCH_PLACE_ORDER_SIZE")

  * Invalid number of batch place orders.
  * Invalid number of batch place orders: %s



### -4083 PLACE_BATCH_ORDERS_FAIL[​](/docs/derivatives/usds-margined-futures/error-code#-4083-place_batch_orders_fail "Direct link to -4083 PLACE_BATCH_ORDERS_FAIL")

  * Fail to place batch orders.



### -4084 UPCOMING_METHOD[​](/docs/derivatives/usds-margined-futures/error-code#-4084-upcoming_method "Direct link to -4084 UPCOMING_METHOD")

  * Method is not allowed currently. Upcoming soon.



### -4085 INVALID_NOTIONAL_LIMIT_COEF[​](/docs/derivatives/usds-margined-futures/error-code#-4085-invalid_notional_limit_coef "Direct link to -4085 INVALID_NOTIONAL_LIMIT_COEF")

  * Invalid notional limit coefficient



### -4086 INVALID_PRICE_SPREAD_THRESHOLD[​](/docs/derivatives/usds-margined-futures/error-code#-4086-invalid_price_spread_threshold "Direct link to -4086 INVALID_PRICE_SPREAD_THRESHOLD")

  * Invalid price spread threshold



### -4087 REDUCE_ONLY_ORDER_PERMISSION[​](/docs/derivatives/usds-margined-futures/error-code#-4087-reduce_only_order_permission "Direct link to -4087 REDUCE_ONLY_ORDER_PERMISSION")

  * User can only place reduce only order



### -4088 NO_PLACE_ORDER_PERMISSION[​](/docs/derivatives/usds-margined-futures/error-code#-4088-no_place_order_permission "Direct link to -4088 NO_PLACE_ORDER_PERMISSION")

  * User can not place order currently



### -4104 INVALID_CONTRACT_TYPE[​](/docs/derivatives/usds-margined-futures/error-code#-4104-invalid_contract_type "Direct link to -4104 INVALID_CONTRACT_TYPE")

  * Invalid contract type



### -4109 INACTIVE_ACCOUNT[​](/docs/derivatives/usds-margined-futures/error-code#-4109-inactive_account "Direct link to -4109 INACTIVE_ACCOUNT")

  * Inactive account
  * Transfer any amount of asset to future wallet to reactive



### -4114 INVALID_CLIENT_TRAN_ID_LEN[​](/docs/derivatives/usds-margined-futures/error-code#-4114-invalid_client_tran_id_len "Direct link to -4114 INVALID_CLIENT_TRAN_ID_LEN")

  * clientTranId is not valid
  * Client tran id length should be less than 64 chars



### -4115 DUPLICATED_CLIENT_TRAN_ID[​](/docs/derivatives/usds-margined-futures/error-code#-4115-duplicated_client_tran_id "Direct link to -4115 DUPLICATED_CLIENT_TRAN_ID")

  * clientTranId is duplicated
  * Client tran id should be unique within 7 days



### -4116 DUPLICATED_CLIENT_ORDER_ID[​](/docs/derivatives/usds-margined-futures/error-code#-4116-duplicated_client_order_id "Direct link to -4116 DUPLICATED_CLIENT_ORDER_ID")

  * clientOrderId is duplicated



### -4117 STOP_ORDER_TRIGGERING[​](/docs/derivatives/usds-margined-futures/error-code#-4117-stop_order_triggering "Direct link to -4117 STOP_ORDER_TRIGGERING")

  * stop order is triggering



### -4118 REDUCE_ONLY_MARGIN_CHECK_FAILED[​](/docs/derivatives/usds-margined-futures/error-code#-4118-reduce_only_margin_check_failed "Direct link to -4118 REDUCE_ONLY_MARGIN_CHECK_FAILED")

  * ReduceOnly Order Failed. Please check your existing position and open orders
  * This indicates that the new reduce-only order, combined with an existing same-side open order, would create an opposite-side position and lead to insufficient margin; please cancel the open order and try again.



### -4120 STOP_ORDER_SWITCH_ALGO[​](/docs/derivatives/usds-margined-futures/error-code#-4120-stop_order_switch_algo "Direct link to -4120 STOP_ORDER_SWITCH_ALGO")

  * Order type not supported for this endpoint. Please use the Algo Order API endpoints instead.



### -4131 MARKET_ORDER_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-4131-market_order_reject "Direct link to -4131 MARKET_ORDER_REJECT")

  * The counterparty's best price does not meet the PERCENT_PRICE filter limit



### -4135 INVALID_ACTIVATION_PRICE[​](/docs/derivatives/usds-margined-futures/error-code#-4135-invalid_activation_price "Direct link to -4135 INVALID_ACTIVATION_PRICE")

  * Invalid activation price



### -4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION[​](/docs/derivatives/usds-margined-futures/error-code#-4137-quantity_exists_with_close_position "Direct link to -4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION")

  * Quantity must be zero with closePosition equals true



### -4138 REDUCE_ONLY_MUST_BE_TRUE[​](/docs/derivatives/usds-margined-futures/error-code#-4138-reduce_only_must_be_true "Direct link to -4138 REDUCE_ONLY_MUST_BE_TRUE")

  * Reduce only must be true with closePosition equals true



### -4139 ORDER_TYPE_CANNOT_BE_MKT[​](/docs/derivatives/usds-margined-futures/error-code#-4139-order_type_cannot_be_mkt "Direct link to -4139 ORDER_TYPE_CANNOT_BE_MKT")

  * Order type can not be market if it's unable to cancel



### -4140 INVALID_OPENING_POSITION_STATUS[​](/docs/derivatives/usds-margined-futures/error-code#-4140-invalid_opening_position_status "Direct link to -4140 INVALID_OPENING_POSITION_STATUS")

  * Invalid symbol status for opening position



### -4141 SYMBOL_ALREADY_CLOSED[​](/docs/derivatives/usds-margined-futures/error-code#-4141-symbol_already_closed "Direct link to -4141 SYMBOL_ALREADY_CLOSED")

  * Symbol is closed



### -4142 STRATEGY_INVALID_TRIGGER_PRICE[​](/docs/derivatives/usds-margined-futures/error-code#-4142-strategy_invalid_trigger_price "Direct link to -4142 STRATEGY_INVALID_TRIGGER_PRICE")

  * REJECT: take profit or stop order will be triggered immediately



### -4144 INVALID_PAIR[​](/docs/derivatives/usds-margined-futures/error-code#-4144-invalid_pair "Direct link to -4144 INVALID_PAIR")

  * Invalid pair



### -4161 ISOLATED_LEVERAGE_REJECT_WITH_POSITION[​](/docs/derivatives/usds-margined-futures/error-code#-4161-isolated_leverage_reject_with_position "Direct link to -4161 ISOLATED_LEVERAGE_REJECT_WITH_POSITION")

  * Leverage reduction is not supported in Isolated Margin Mode with open positions



### -4164 MIN_NOTIONAL[​](/docs/derivatives/usds-margined-futures/error-code#-4164-min_notional "Direct link to -4164 MIN_NOTIONAL")

  * Order's notional must be no smaller than 5.0 (unless you choose reduce only)
  * Order's notional must be no smaller than %s (unless you choose reduce only)



### -4165 INVALID_TIME_INTERVAL[​](/docs/derivatives/usds-margined-futures/error-code#-4165-invalid_time_interval "Direct link to -4165 INVALID_TIME_INTERVAL")

  * Invalid time interval
  * Maximum time interval is %s days



### -4167 ISOLATED_REJECT_WITH_JOINT_MARGIN[​](/docs/derivatives/usds-margined-futures/error-code#-4167-isolated_reject_with_joint_margin "Direct link to -4167 ISOLATED_REJECT_WITH_JOINT_MARGIN")

  * Unable to adjust to Multi-Assets mode with symbols of USDⓈ-M Futures under isolated-margin mode.



### -4168 JOINT_MARGIN_REJECT_WITH_ISOLATED[​](/docs/derivatives/usds-margined-futures/error-code#-4168-joint_margin_reject_with_isolated "Direct link to -4168 JOINT_MARGIN_REJECT_WITH_ISOLATED")

  * Unable to adjust to isolated-margin mode under the Multi-Assets mode.



### -4169 JOINT_MARGIN_REJECT_WITH_MB[​](/docs/derivatives/usds-margined-futures/error-code#-4169-joint_margin_reject_with_mb "Direct link to -4169 JOINT_MARGIN_REJECT_WITH_MB")

  * Unable to adjust Multi-Assets Mode with insufficient margin balance in USDⓈ-M Futures.



### -4170 JOINT_MARGIN_REJECT_WITH_OPEN_ORDER[​](/docs/derivatives/usds-margined-futures/error-code#-4170-joint_margin_reject_with_open_order "Direct link to -4170 JOINT_MARGIN_REJECT_WITH_OPEN_ORDER")

  * Unable to adjust Multi-Assets Mode with open orders in USDⓈ-M Futures.



### -4171 NO_NEED_TO_CHANGE_JOINT_MARGIN[​](/docs/derivatives/usds-margined-futures/error-code#-4171-no_need_to_change_joint_margin "Direct link to -4171 NO_NEED_TO_CHANGE_JOINT_MARGIN")

  * Adjusted asset mode is currently set and does not need to be adjusted repeatedly.



### -4172 JOINT_MARGIN_REJECT_WITH_NEGATIVE_BALANCE[​](/docs/derivatives/usds-margined-futures/error-code#-4172-joint_margin_reject_with_negative_balance "Direct link to -4172 JOINT_MARGIN_REJECT_WITH_NEGATIVE_BALANCE")

  * Unable to adjust Multi-Assets Mode with a negative wallet balance of margin available asset in USDⓈ-M Futures account.



### -4183 ISOLATED_REJECT_WITH_JOINT_MARGIN[​](/docs/derivatives/usds-margined-futures/error-code#-4183-isolated_reject_with_joint_margin "Direct link to -4183 ISOLATED_REJECT_WITH_JOINT_MARGIN")

  * Price is higher than stop price multiplier cap.
  * Limit price can't be higher than %s.



### -4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN[​](/docs/derivatives/usds-margined-futures/error-code#-4184-price_lower_than_stop_multiplier_down "Direct link to -4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN")

  * Price is lower than stop price multiplier floor.
  * Limit price can't be lower than %s.



### -4192 COOLING_OFF_PERIOD[​](/docs/derivatives/usds-margined-futures/error-code#-4192-cooling_off_period "Direct link to -4192 COOLING_OFF_PERIOD")

  * Trade forbidden due to Cooling-off Period.



### -4202 ADJUST_LEVERAGE_KYC_FAILED[​](/docs/derivatives/usds-margined-futures/error-code#-4202-adjust_leverage_kyc_failed "Direct link to -4202 ADJUST_LEVERAGE_KYC_FAILED")

  * Intermediate Personal Verification is required for adjusting leverage over 20x



### -4203 ADJUST_LEVERAGE_ONE_MONTH_FAILED[​](/docs/derivatives/usds-margined-futures/error-code#-4203-adjust_leverage_one_month_failed "Direct link to -4203 ADJUST_LEVERAGE_ONE_MONTH_FAILED")

  * More than 20x leverage is available one month after account registration.



### -4205 ADJUST_LEVERAGE_X_DAYS_FAILED[​](/docs/derivatives/usds-margined-futures/error-code#-4205-adjust_leverage_x_days_failed "Direct link to -4205 ADJUST_LEVERAGE_X_DAYS_FAILED")

  * More than 20x leverage is available %s days after Futures account registration.



### -4206 ADJUST_LEVERAGE_KYC_LIMIT[​](/docs/derivatives/usds-margined-futures/error-code#-4206-adjust_leverage_kyc_limit "Direct link to -4206 ADJUST_LEVERAGE_KYC_LIMIT")

  * Users in this country has limited adjust leverage.
  * Users in your location/country can only access a maximum leverage of %s



### -4208 ADJUST_LEVERAGE_ACCOUNT_SYMBOL_FAILED[​](/docs/derivatives/usds-margined-futures/error-code#-4208-adjust_leverage_account_symbol_failed "Direct link to -4208 ADJUST_LEVERAGE_ACCOUNT_SYMBOL_FAILED")

  * Current symbol leverage cannot exceed 20 when using position limit adjustment service.



### -4209 ADJUST_LEVERAGE_SYMBOL_FAILED[​](/docs/derivatives/usds-margined-futures/error-code#-4209-adjust_leverage_symbol_failed "Direct link to -4209 ADJUST_LEVERAGE_SYMBOL_FAILED")

  * The max leverage of Symbol is 20x
  * Leverage adjustment failed. Current symbol max leverage limit is %sx



### -4210 STOP_PRICE_HIGHER_THAN_PRICE_MULTIPLIER_LIMIT[​](/docs/derivatives/usds-margined-futures/error-code#-4210-stop_price_higher_than_price_multiplier_limit "Direct link to -4210 STOP_PRICE_HIGHER_THAN_PRICE_MULTIPLIER_LIMIT")

  * Stop price is higher than price multiplier cap.
  * Stop price can't be higher than %s



### -4211 STOP_PRICE_LOWER_THAN_PRICE_MULTIPLIER_LIMIT[​](/docs/derivatives/usds-margined-futures/error-code#-4211-stop_price_lower_than_price_multiplier_limit "Direct link to -4211 STOP_PRICE_LOWER_THAN_PRICE_MULTIPLIER_LIMIT")

  * Stop price is lower than price multiplier floor.
  * Stop price can't be lower than %s



### -4400 TRADING_QUANTITATIVE_RULE[​](/docs/derivatives/usds-margined-futures/error-code#-4400-trading_quantitative_rule "Direct link to -4400 TRADING_QUANTITATIVE_RULE")

  * Futures Trading Quantitative Rules violated, only reduceOnly order is allowed, please try again later.



### -4401 LARGE_POSITION_SYM_RULE[​](/docs/derivatives/usds-margined-futures/error-code#-4401-large_position_sym_rule "Direct link to -4401 LARGE_POSITION_SYM_RULE")

  * Futures Trading Risk Control Rules of large position holding violated, only reduceOnly order is allowed, please reduce the position. .



### -4402 COMPLIANCE_BLACK_SYMBOL_RESTRICTION[​](/docs/derivatives/usds-margined-futures/error-code#-4402-compliance_black_symbol_restriction "Direct link to -4402 COMPLIANCE_BLACK_SYMBOL_RESTRICTION")

  * Dear user, as per our Terms of Use and compliance with local regulations, this feature is currently not available in your region.



### -4403 ADJUST_LEVERAGE_COMPLIANCE_FAILED[​](/docs/derivatives/usds-margined-futures/error-code#-4403-adjust_leverage_compliance_failed "Direct link to -4403 ADJUST_LEVERAGE_COMPLIANCE_FAILED")

  * Dear user, as per our Terms of Use and compliance with local regulations, the leverage can only up to 10x in your region
  * Dear user, as per our Terms of Use and compliance with local regulations, the leverage can only up to %sx in your region



## 50xx - Order Execution Issues[​](/docs/derivatives/usds-margined-futures/error-code#50xx---order-execution-issues "Direct link to 50xx - Order Execution Issues")

### -5021 FOK_ORDER_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-5021-fok_order_reject "Direct link to -5021 FOK_ORDER_REJECT")

  * Due to the order could not be filled immediately, the FOK order has been rejected.



### -5022 GTX_ORDER_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-5022-gtx_order_reject "Direct link to -5022 GTX_ORDER_REJECT")

  * Due to the order could not be executed as maker, the Post Only order will be rejected.



### -5024 MOVE_ORDER_NOT_ALLOWED_SYMBOL_REASON[​](/docs/derivatives/usds-margined-futures/error-code#-5024-move_order_not_allowed_symbol_reason "Direct link to -5024 MOVE_ORDER_NOT_ALLOWED_SYMBOL_REASON")

  * Symbol is not in trading status. Order amendment is not permitted.



### -5025 LIMIT_ORDER_ONLY[​](/docs/derivatives/usds-margined-futures/error-code#-5025-limit_order_only "Direct link to -5025 LIMIT_ORDER_ONLY")

  * Only limit order is supported.



### -5026 Exceed_Maximum_Modify_Order_Limit[​](/docs/derivatives/usds-margined-futures/error-code#-5026-exceed_maximum_modify_order_limit "Direct link to -5026 Exceed_Maximum_Modify_Order_Limit")

  * Exceed maximum modify order limit.



### -5027 SAME_ORDER[​](/docs/derivatives/usds-margined-futures/error-code#-5027-same_order "Direct link to -5027 SAME_ORDER")

  * No need to modify the order.



### -5028 ME_RECVWINDOW_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-5028-me_recvwindow_reject "Direct link to -5028 ME_RECVWINDOW_REJECT")

  * Timestamp for this request is outside of the ME recvWindow.



### -5029 MODIFICATION_MIN_NOTIONAL[​](/docs/derivatives/usds-margined-futures/error-code#-5029-modification_min_notional "Direct link to -5029 MODIFICATION_MIN_NOTIONAL")

  * Order's notional must be no smaller than %s



### -5037 INVALID_PRICE_MATCH[​](/docs/derivatives/usds-margined-futures/error-code#-5037-invalid_price_match "Direct link to -5037 INVALID_PRICE_MATCH")

  * Invalid price match



### -5038 UNSUPPORTED_ORDER_TYPE_PRICE_MATCH[​](/docs/derivatives/usds-margined-futures/error-code#-5038-unsupported_order_type_price_match "Direct link to -5038 UNSUPPORTED_ORDER_TYPE_PRICE_MATCH")

  * Price match only supports order type: LIMIT, STOP AND TAKE_PROFIT



### -5039 INVALID_SELF_TRADE_PREVENTION_MODE[​](/docs/derivatives/usds-margined-futures/error-code#-5039-invalid_self_trade_prevention_mode "Direct link to -5039 INVALID_SELF_TRADE_PREVENTION_MODE")

  * Invalid self trade prevention mode



### -5040 FUTURE_GOOD_TILL_DATE[​](/docs/derivatives/usds-margined-futures/error-code#-5040-future_good_till_date "Direct link to -5040 FUTURE_GOOD_TILL_DATE")

  * The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000 (UTC 9999-12-31 23:59:59)



### -5041 BBO_ORDER_REJECT[​](/docs/derivatives/usds-margined-futures/error-code#-5041-bbo_order_reject "Direct link to -5041 BBO_ORDER_REJECT")

  * No depth matches this BBO order



### -5043 Existing_Pending_Modification[​](/docs/derivatives/usds-margined-futures/error-code#-5043-existing_pending_modification "Direct link to -5043 Existing_Pending_Modification")

  * A pending modification already exists for this order.

---

# 错误代码

> error JSON payload:
    
    
    {  
      "code":-1121,  
      "msg":"Invalid symbol."  
    }  
    

错误由两部分组成：错误代码和消息。 代码是通用的，但是消息可能会有所不同。

## 10xx - 常规服务器或网络问题[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#10xx---常规服务器或网络问题 "10xx - 常规服务器或网络问题的直接链接")

### -1000 UNKNOWN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1000-unknown "-1000 UNKNOWN的直接链接")

  * An unknown error occured while processing the request.
  * 处理请求时发生未知错误。



### -1001 DISCONNECTED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1001-disconnected "-1001 DISCONNECTED的直接�链接")

  * Internal error; unable to process your request. Please try again.
  * 内部错误; 无法处理您的请求。 请再试一次.



### -1002 UNAUTHORIZED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1002-unauthorized "-1002 UNAUTHORIZED的直接链接")

  * You are not authorized to execute this request.
  * 您无权执行此请求。



### -1003 TOO_MANY_REQUESTS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1003-too_many_requests "-1003 TOO_MANY_REQUESTS的直接链接")

  * Too many requests; current limit is %s requests per minute. Please use the websocket for live updates to avoid polling the API.
  * 请求权重过多； 当前限制为每分钟％s请求权重。 请使用websocket进行实时更新，以避免轮询API。
  * Way too many requests; IP banned until %s. Please use the websocket for live updates to avoid bans.
  * 请求权重过多； IP被禁止，直到％s。 请使用websocket进行实时更新，以免被禁。



### -1004 DUPLICATE_IP[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1004-duplicate_ip "-1004 DUPLICATE_IP的直接链接")

  * This IP is already on the white list
  * IP地址已经在白名单



### -1005 NO_SUCH_IP[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1005-no_such_ip "-1005 NO_SUCH_IP�的直接链接")

  * No such IP has been white listed
  * 白名单上没有此IP地址



### -1006 UNEXPECTED_RESP[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1006-unexpected_resp "-1006 UNEXPECTED_RESP的直接链接")

  * An unexpected response was received from the message bus. Execution status unknown.
  * 从消息总线收到意外的响应。执行状态未知。



### -1007 TIMEOUT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1007-timeout "-1007 TIMEOUT的直接链接")

  * Timeout waiting for response from backend server. Send status unknown; execution status unknown.
  * 等待后端服务器响应超时。 发送状态未知； 执行状态未知。



### -1008 Request Throttled[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1008-request-throttled "-1008 Request Throttled的直接链接")

  * Server is currently overloaded with other requests. Please try again in a few minutes.
  * 服务器当前请求过多，请几分钟后再试。
  * Request throttled by system-level protection. Reduce-only/close-position orders are exempt. Please try again.



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1014-unknown_order_composition "-1014 UNKNOWN_ORDER_COMPOSITION的直接链接")

  * Unsupported order combination.
  * 不支持当前的下单参数组合



### -1015 TOO_MANY_ORDERS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1015-too_many_orders "-1015 TOO_MANY_ORDERS的直接链接")

  * Too many new orders.
  * 新订单太多。
  * Too many new orders; current limit is %s orders per %s.  * 新订单太多； 当前限制为每％s ％s个订单。



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1016-service_shutting_down "-1016 SERVICE_SHUTTING_DOWN的直接链接")

  * This service is no longer available.
  * 该服务不可用。



### -1020 UNSUPPORTED_OPERATION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1020-unsupported_operation "-1020 UNSUPPORTED_OPERATION的直接链接")

  * This operation is not supported.
  * 不支持此操作。



### -1021 INVALID_TIMESTAMP[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1021-invalid_timestamp "-1021 INVALID_TIMESTAMP的直接链接")

  * Timestamp for this request is outside of the recvWindow.
  * 此请求的时间戳在recvWindow之外。
  * Timestamp for this request was 1000ms ahead of the server's time.  * 此请求的时间戳比服务器时间提前1000毫秒。



### -1022 INVALID_SIGNATURE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1022-invalid_signature "-1022 INVALID_SIGNATURE的直接链接")

  * Signature for this request is not valid.
  * 此请求的签名无效。



### -1023 START_TIME_GREATER_THAN_END_TIME[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1023-start_time_greater_than_end_time "-1023 START_TIME_GREATER_THAN_END_TIME的直接链接")

  * Start time is greater than end time.
  * 参数里面的开始时间在结束时间之后



### -1099 NOT_FOUND[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1099-not_found "-1099 NOT_FOUND的直接链接")

  * Not found, unauthenticated, or unauthorized.



## 11xx - Request issues[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#11xx---request-issues "11xx - Request issues的直接链接")

### -1100 ILLEGAL_CHARS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1100-illegal_chars "-1100 ILLEGAL_CHARS的直接链接")

  * Illegal characters found in a parameter.
  * 在参数中发现非法字符。
  * Illegal characters found in parameter '%s'; legal range is '%s'.
  * 在参数`％s`中发现非法字符； 合法范围是`％s`。



### -1101 TOO_MANY_PARAMETERS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1101-too_many_parameters "-1101 TOO_MANY_PARAMETERS的直接链接")

  * Too many parameters sent for this endpoint.
  * 为此端点发送的参数太多。
  * Too many parameters; expected '%s' and received '%s'.
  * 参数太多；预期为`％s`并收到了`％s`。
  * Duplicate values for a parameter detected.  * 检测到的参数值重复。



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1102-mandatory_param_empty_or_malformed "-1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED的直接链接")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * 未发送强制性参数，该参数为空/空或格式错误。
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.  * 强制参数`％s`未发送，为空/空或格式错误。
  * Param '%s' or '%s' must be sent, but both were empty/null!  * 必须发送参数`％s`或`％s`，但两者均为空！



### -1103 UNKNOWN_PARAM[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1103-unknown_param "-1103 UNKNOWN_PARAM的直接链接")

  * An unknown parameter was sent.
  * 发送了未知参数。



### -1104 UNREAD_PARAMETERS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1104-unread_parameters "-1104 UNREAD_PARAMETERS的直接链接")

  * Not all sent parameters were read.
  * 并非所有发送的参数都被读取。
  * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.
  * 并非所有发送的参数都被读取； 读取了`％s`参数，但被发送了`％s`。



### -1105 PARAM_EMPTY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1105-param_empty "-1105 PARAM_EMPTY的直接链接")

  * A parameter was empty.
  * 参数为空。
  * Parameter '%s' was empty.
  * 参数`％s`为空。



### -1106 PARAM_NOT_REQUIRED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1106-param_not_required "-1106 PARAM_NOT_REQUIRED的直接链接")

  * A parameter was sent when not required.
  * 发送了不需要的参数。
  * Parameter '%s' sent when not required.
  * 发送了不需要参数`％s`。



### -1108 BAD_ASSET[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1108-bad_asset "-1108 BAD_ASSET的直接链接")

  * Invalid asset.
  * 资产不正确



### -1109 BAD_ACCOUNT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1109-bad_account "-1109 BAD_ACCOUNT的直接链接")

  * Invalid account.
  * 非有效账户



### -1110 BAD_INSTRUMENT_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1110-bad_instrument_type "-1110 BAD_INSTRUMENT_TYPE的直接链接")

  * Invalid symbolType.
  * 交易对不正确



### -1111 BAD_PRECISION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1111-bad_precision "-1111 BAD_PRECISION的直接链接")

  * Precision is over the maximum defined for this asset.
  * 精度超过为此资产定义的最大值。



### -1112 NO_DEPTH[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1112-no_depth "-1112 NO_DEPTH的直接链接")

  * No orders on book for symbol.
  * 交易对没有挂单。



### -1113 WITHDRAW_NOT_NEGATIVE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1113-withdraw_not_negative "-1113 WITHDRAW_NOT_NEGATIVE的直接链接")

  * Withdrawal amount must be negative.
  * 提现数量需要为负



### -1114 TIF_NOT_REQUIRED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1114-tif_not_required "-1114 TIF_NOT_REQUIRED的直接链接")

  * TimeInForce parameter sent when not required.
  * 发送的`TimeInForce`参数不需要。



### -1115 INVALID_TIF[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1115-invalid_tif "-1115 INVALID_TIF的直接链接")

  * Invalid timeInForce.
  * 无效的`timeInForce`



### -1116 INVALID_ORDER_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1116-invalid_order_type "-1116 INVALID_ORDER_TYPE的直接链接")

  * Invalid orderType.
  * 无效订单类型。



### -1117 INVALID_SIDE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1117-invalid_side "-1117 INVALID_SIDE的直接链接")

  * Invalid side.
  * 无效买卖方向。



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1118-empty_new_cl_ord_id "-1118 EMPTY_NEW_CL_ORD_ID的直接链接")

  * New client order ID was empty.
  * 新的客户订单ID为空。



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1119-empty_org_cl_ord_id "-1119 EMPTY_ORG_CL_ORD_ID的直接链接")

  * Original client order ID was empty.
  * 客户自定义的订单ID为空。



### -1120 BAD_INTERVAL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1120-bad_interval "-1120 BAD_INTERVAL的直接链接")

  * Invalid interval.
  * 无效时间间隔。



### -1121 BAD_SYMBOL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1121-bad_symbol "-1121 BAD_SYMBOL的直接链接")

  * Invalid symbol.
  * 无效的交易对。



### -1122 INVALID_SYMBOL_STATUS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1122-invalid_symbol_status "-1122 INVALID_SYMBOL_STATUS的直接链接")

  * Invalid symbol status.
  * 交易对状态不正确。



### -1125 INVALID_LISTEN_KEY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1125-invalid_listen_key "-1125 INVALID_LISTEN_KEY的直接链接")

  * This listenKey does not exist.
  * 此`listenKey`不存在。建议重新使用`POST /fapi/v1/listenKey`生成`listenKey`



### -1126 ASSET_NOT_SUPPORTED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1126-asset_not_supported "-1126 ASSET_NOT_SUPPORTED的直接链接")

  * This asset is not supported.
  * 不支持该资产



### -1127 MORE_THAN_XX_HOURS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1127-more_than_xx_hours "-1127 MORE_THAN_XX_HOURS的直接链接")

  * Lookup interval is too big.
  * 查询间隔太大。
  * More than %s hours between startTime and endTime.
  * 从开始时间到结束时间之间超过`％s`小时。



### -1128 OPTIONAL_PARAMS_BAD_COMBO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1128-optional_params_bad_combo "-1128 OPTIONAL_PARAMS_BAD_COMBO的直接链接")

  * Combination of optional parameters invalid.
  * 可选参数组合无效。



### -1130 INVALID_PARAMETER[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1130-invalid_parameter "-1130 INVALID_PARAMETER的直接链接")

  * Invalid data sent for a parameter.
  * 发送的参数为无效数据。
  * Data sent for parameter '%s' is not valid.
  * 发送参数`％s`的数据无效。



### -1136 INVALID_NEW_ORDER_RESP_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-1136-invalid_new_order_resp_type "-1136 INVALID_NEW_ORDER_RESP_TYPE的直接链接")

  * Invalid newOrderRespType.
  * 无效的 newOrderRespType。



## 20xx - Processing Issues[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#20xx---processing-issues "20xx - Processing Issues的直接链接")

### -2010 NEW_ORDER_REJECTED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2010-new_order_rejected "-2010 NEW_ORDER_REJECTED的直接链接")

  * NEW_ORDER_REJECTED
  * 新订单被拒绝



### -2011 CANCEL_REJECTED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2011-cancel_rejected "-2011 CANCEL_REJECTED的直接链接")

  * CANCEL_REJECTED
  * 取消订单被拒绝 "Unknown order sent"



### -2012 CANCEL_ALL_FAIL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2012-cancel_all_fail "-2012 CANCEL_ALL_FAIL的直接链接")

  * Batch cancel failure.
  * 批量取消失败



### -2013 NO_SUCH_ORDER[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2013-no_such_order "-2013 NO_SUCH_ORDER的直接链接")

  * Order does not exist.
  * 订单不存在。



### -2014 BAD_API_KEY_FMT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2014-bad_api_key_fmt "-2014 BAD_API_KEY_FMT的直接链接")

  * API-key format invalid.
  * API-key 格式无效。



### -2015 REJECTED_MBX_KEY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2015-rejected_mbx_key "-2015 REJECTED_MBX_KEY的直接链接")

  * Invalid API-key, IP, or permissions for action.
  * 无效的API密钥，IP或操作权限。



### -2016 NO_TRADING_WINDOW[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2016-no_trading_window "-2016 NO_TRADING_WINDOW的直接链接")

  * No trading window could be found for the symbol. Try ticker/24hrs instead.
  * 找不到该交易对的交易窗口。 尝试改为24小时自动报价。



### -2017 API_KEYS_LOCKED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2017-api_keys_locked "-2017 API_KEYS_LOCKED的直接链接")

  * API Keys are locked on this account.
  * API key被上锁



### -2018 BALANCE_NOT_SUFFICIENT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2018-balance_not_sufficient "-2018 BALANCE_NOT_SUFFICIENT的直接链接")

  * Balance is insufficient.
  * 余额不足



### -2019 MARGIN_NOT_SUFFICIEN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2019-margin_not_sufficien "-2019 MARGIN_NOT_SUFFICIEN的直接链接")

  * Margin is insufficient.
  * 杠杆账户余额不足



### -2020 UNABLE_TO_FILL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2020-unable_to_fill "-2020 UNABLE_TO_FILL的直接链接")

  * Unable to fill.
  * 无法成交



### -2021 ORDER_WOULD_IMMEDIATELY_TRIGGER[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2021-order_would_immediately_trigger "-2021 ORDER_WOULD_IMMEDIATELY_TRIGGER的直接链接")

  * Order would immediately trigger.
  * 订单可能被立刻触发



### -2022 REDUCE_ONLY_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2022-reduce_only_reject "-2022 REDUCE_ONLY_REJECT的直接链接")

  * ReduceOnly Order is rejected.
  * `ReduceOnly`订单被拒绝
  * 这表示新的「仅减仓（reduce-only）」订单与当前未成交同向订单存在冲突；请先取消现有订单，然后重新提交仅减仓订单。



### -2023 USER_IN_LIQUIDATION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2023-user_in_liquidation "-2023 USER_IN_LIQUIDATION的直接链接")

  * User in liquidation mode now.
  * 用户正处于被强平模式



### -2024 POSITION_NOT_SUFFICIENT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2024-position_not_sufficient "-2024 POSITION_NOT_SUFFICIENT的直接链接")

  * Position is not sufficient.
  * 持仓不足



### -2025 MAX_OPEN_ORDER_EXCEEDED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2025-max_open_order_exceeded "-2025 MAX_OPEN_ORDER_EXCEEDED的直接链接")

  * Reach max open order limit.
  * 挂单量达到上限



### -2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2026-reduce_only_order_type_not_supported "-2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED的直接链接")

  * This OrderType is not supported when reduceOnly.
  * 当前订单类型不支持`reduceOnly`



### -2027 MAX_LEVERAGE_RATIO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2027-max_leverage_ratio "-2027 MAX_LEVERAGE_RATIO的��直接链接")

  * Exceeded the maximum allowable position at current leverage.
  * 挂单或持仓超出当前初始杠杆下的最大值



### -2028 MIN_LEVERAGE_RATIO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-2028-min_leverage_ratio "-2028 MIN_LEVERAGE_RATIO的直接链接")

  * Leverage is smaller than permitted: insufficient margin balance.
  * 调整初始杠杆过低，导致可用余额不足



## 40xx - Filters and other Issues[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#40xx---filters-and-other-issues "40xx - Filters and other Issues的直接链接")

### -4000 INVALID_ORDER_STATUS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4000-invalid_order_status "-4000 INVALID_ORDER_STATUS的直接链接")

  * Invalid order status.
  * 订单状态不正确



### -4001 PRICE_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4001-price_less_than_zero "-4001 PRICE_LESS_THAN_ZERO的直接链接")

  * Price less than 0.
  * 价格小于0



### -4002 PRICE_GREATER_THAN_MAX_PRICE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4002-price_greater_than_max_price "-4002 PRICE_GREATER_THAN_MAX_PRICE的直接链接")

  * Price greater than max price.
  * 价格超过最大值



### -4003 QTY_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4003-qty_less_than_zero "-4003 QTY_LESS_THAN_ZERO的直接链接")

  * Quantity less than zero.
  * 数量小于0



### -4004 QTY_LESS_THAN_MIN_QTY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4004-qty_less_than_min_qty "-4004 QTY_LESS_THAN_MIN_QTY的直接链接")

  * Quantity less than min quantity.
  * 数量小于最小值



### -4005 QTY_GREATER_THAN_MAX_QTY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4005-qty_greater_than_max_qty "-4005 QTY_GREATER_THAN_MAX_QTY的直接链接")

  * Quantity greater than max quantity.
  * 数量大于最大值



### -4006 STOP_PRICE_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4006-stop_price_less_than_zero "-4006 STOP_PRICE_LESS_THAN_ZERO的直接链接")

  * Stop price less than zero.
  * 触发价小于最小值



### -4007 STOP_PRICE_GREATER_THAN_MAX_PRICE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4007-stop_price_greater_than_max_price "-4007 STOP_PRICE_GREATER_THAN_MAX_PRICE的直接链接")

  * Stop price greater than max price.
  * 触发价大于最大值



### -4008 TICK_SIZE_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4008-tick_size_less_than_zero "-4008 TICK_SIZE_LESS_THAN_ZERO的直接链接")

  * Tick size less than zero.
  * 价格精度小于0



### -4009 MAX_PRICE_LESS_THAN_MIN_PRICE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4009-max_price_less_than_min_price "-4009 MAX_PRICE_LESS_THAN_MIN_PRICE的直接链接")

  * Max price less than min price.
  * 最大价格小于最小价格



### -4010 MAX_QTY_LESS_THAN_MIN_QTY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4010-max_qty_less_than_min_qty "-4010 MAX_QTY_LESS_THAN_MIN_QTY的直接链接")

  * Max qty less than min qty.
  * 最大数量小于最小数量



### -4011 STEP_SIZE_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4011-step_size_less_than_zero "-4011 STEP_SIZE_LESS_THAN_ZERO的直接链接")

  * Step size less than zero.
  * 步进值小于0



### -4012 MAX_NUM_ORDERS_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4012-max_num_orders_less_than_zero "-4012 MAX_NUM_ORDERS_LESS_THAN_ZERO的直接链接")

  * Max num orders less than zero.
  * 最大订单量小于0



### -4013 PRICE_LESS_THAN_MIN_PRICE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4013-price_less_than_min_price "-4013 PRICE_LESS_THAN_MIN_PRICE的直接链接")

  * Price less than min price.
  * 价格小于最小价格



### -4014 PRICE_NOT_INCREASED_BY_TICK_SIZE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4014-price_not_increased_by_tick_size "-4014 PRICE_NOT_INCREASED_BY_TICK_SIZE的直接链接")

  * Price not increased by tick size.
  * 价格增量不是价格精度的倍数。



### -4015 INVALID_CL_ORD_ID_LEN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4015-invalid_cl_ord_id_len "-4015 INVALID_CL_ORD_ID_LEN的直接链接")

  * Client order id is not valid.
  * 客户订单ID有误。
  * Client order id length should not be more than 36 chars
  * 客户订单ID长度应该不多于36字符



### -4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4016-price_highter_than_multiplier_up "-4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP的直接链接")

  * Price is higher than mark price multiplier cap.



### -4017 MULTIPLIER_UP_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4017-multiplier_up_less_than_zero "-4017 MULTIPLIER_UP_LESS_THAN_ZERO的直接链接")

  * Multiplier up less than zero.
  * 价格上限小于0



### -4018 MULTIPLIER_DOWN_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4018-multiplier_down_less_than_zero "-4018 MULTIPLIER_DOWN_LESS_THAN_ZERO的直接链接")

  * Multiplier down less than zero.
  * 价格下限小于0



### -4019 COMPOSITE_SCALE_OVERFLOW[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4019-composite_scale_overflow "-4019 COMPOSITE_SCALE_OVERFLOW的直接链接")

  * Composite scale too large.



### -4020 TARGET_STRATEGY_INVALID[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4020-target_strategy_invalid "-4020 TARGET_STRATEGY_INVALID的直接链接")

  * Target strategy invalid for orderType '%s',reduceOnly '%b'.
  * 目标策略值不适合`%s`订单状态, 只减仓`%b`。



### -4021 INVALID_DEPTH_LIMIT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4021-invalid_depth_limit "-4021 INVALID_DEPTH_LIMIT的直接链接")

  * Invalid depth limit.
  * 深度信息的`limit`值不正确。
  * '%s' is not valid depth limit.
  * `%s`不是合理的深度信息的`limit`值。



### -4022 WRONG_MARKET_STATUS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4022-wrong_market_status "-4022 WRONG_MARKET_STATUS的直接链接")

  * market status sent is not valid.
  * 发送的市场状态不正确。



### -4023 QTY_NOT_INCREASED_BY_STEP_SIZE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4023-qty_not_increased_by_step_size "-4023 QTY_NOT_INCREASED_BY_STEP_SIZE的直接链接")

  * Qty not increased by step size.
  * 数量的递增值不是步进值的倍数。



### -4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4024-price_lower_than_multiplier_down "-4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN的直接链接")

  * Price is lower than mark price multiplier floor.



### -4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4025-multiplier_decimal_less_than_zero "-4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO的直接链接")

  * Multiplier decimal less than zero.



### -4026 COMMISSION_INVALID[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4026-commission_invalid "-4026 COMMISSION_INVALID的直接链接")

  * Commission invalid.
  * 收益值不正确
  * `%s` less than zero.
  * `%s`少于0
  * `%s` absolute value greater than `%s`
  * `%s`绝对值大于`%s`



### -4027 INVALID_ACCOUNT_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4027-invalid_account_type "-4027 INVALID_ACCOUNT_TYPE的直接链接")

  * Invalid account type.
  * 账户类型不正确。



### -4028 INVALID_LEVERAGE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4028-invalid_leverage "-4028 INVALID_LEVERAGE的直接链接")

  * Invalid leverage
  * 杠杆倍数不正确
  * Leverage `%s` is not valid
  * 杠杆`%s`不正确
  * Leverage `%s` already exist with `%s`
  * 杠杆`%s`已经存在于`%s`



### -4029 INVALID_TICK_SIZE_PRECISION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4029-invalid_tick_size_precision "-4029 INVALID_TICK_SIZE_PRECISION的直接链接")

  * Tick size precision is invalid.
  * 价格精度小数点位数不正确。



### -4030 INVALID_STEP_SIZE_PRECISION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4030-invalid_step_size_precision "-4030 INVALID_STEP_SIZE_PRECISION的直接链接")

  * Step size precision is invalid.
  * 步进值小数点位数不正确。



### -4031 INVALID_WORKING_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4031-invalid_working_type "-4031 INVALID_WORKING_TYPE的直接链接")

  * Invalid parameter working type
  * 不正确的参数类型
  * Invalid parameter working type: `%s`
  * 不正确的参数类型: `%s`



### -4032 EXCEED_MAX_CANCEL_ORDER_SIZE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4032-exceed_max_cancel_order_size "-4032 EXCEED_MAX_CANCEL_ORDER_SIZE的直接链接")

  * Exceed maximum cancel order size.
  * 超过可以取消的最大订单量。
  * Invalid parameter working type: `%s`
  * 不正确的参数类型: `%s`



### -4033 INSURANCE_ACCOUNT_NOT_FOUND[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4033-insurance_account_not_found "-4033 INSURANCE_ACCOUNT_NOT_FOUND的直接链接")

  * Insurance account not found.
  * 风险保障基金账号没找到。



### -4044 INVALID_BALANCE_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4044-invalid_balance_type "-4044 INVALID_BALANCE_TYPE的直接链接")

  * Balance Type is invalid.
  * 余额类型不正确。



### -4045 MAX_STOP_ORDER_EXCEEDED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4045-max_stop_order_exceeded "-4045 MAX_STOP_ORDER_EXCEEDED的直接链接")

  * Reach max stop order limit.
  * 达到止损单的上限。



### -4046 NO_NEED_TO_CHANGE_MARGIN_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4046-no_need_to_change_margin_type "-4046 NO_NEED_TO_CHANGE_MARGIN_TYPE的直接链接")

  * No need to change margin type.
  * 不需要切换仓位模式。



### -4047 THERE_EXISTS_OPEN_ORDERS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4047-there_exists_open_orders "-4047 THERE_EXISTS_OPEN_ORDERS的直接链接")

  * Margin type cannot be changed if there exists open orders.
  * 如果有挂单，仓位模式不能切换。



### -4048 THERE_EXISTS_QUANTITY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4048-there_exists_quantity "-4048 THERE_EXISTS_QUANTITY的直接链接")

  * Margin type cannot be changed if there exists position.
  * 如果有仓位，仓位模式不能切换。



### -4049 ADD_ISOLATED_MARGIN_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4049-add_isolated_margin_reject "-4049 ADD_ISOLATED_MARGIN_REJECT的直接链接")

  * Add margin only support for isolated position.



### -4050 CROSS_BALANCE_INSUFFICIENT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4050-cross_balance_insufficient "-4050 CROSS_BALANCE_INSUFFICIENT的直接链接")

  * Cross balance insufficient.
  * 全仓余额不足。



### -4051 ISOLATED_BALANCE_INSUFFICIENT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4051-isolated_balance_insufficient "-4051 ISOLATED_BALANCE_INSUFFICIENT的直接链接")

  * Isolated balance insufficient.
  * 逐仓余额不足。



### -4052 NO_NEED_TO_CHANGE_AUTO_ADD_MARGIN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4052-no_need_to_change_auto_add_margin "-4052 NO_NEED_TO_CHANGE_AUTO_ADD_MARGIN的直接链接")

  * No need to change auto add margin.



### -4053 AUTO_ADD_CROSSED_MARGIN_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4053-auto_add_crossed_margin_reject "-4053 AUTO_ADD_CROSSED_MARGIN_REJECT的直接链接")

  * Auto add margin only support for isolated position.
  * 自动增加保证金只适用于逐仓。



### -4054 ADD_ISOLATED_MARGIN_NO_POSITION_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4054-add_isolated_margin_no_position_reject "-4054 ADD_ISOLATED_MARGIN_NO_POSITION_REJECT的直接链接")

  * Cannot add position margin: position is 0.
  * 不能增加逐仓保证金: 持仓为0



### -4055 AMOUNT_MUST_BE_POSITIVE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4055-amount_must_be_positive "-4055 AMOUNT_MUST_BE_POSITIVE的直接链接")

  * Amount must be positive.
  * 数量必须是正整数



### -4056 INVALID_API_KEY_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4056-invalid_api_key_type "-4056 INVALID_API_KEY_TYPE的直接链接")

  * Invalid api key type.
  * API key的类型不正确



### -4057 INVALID_RSA_PUBLIC_KEY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4057-invalid_rsa_public_key "-4057 INVALID_RSA_PUBLIC_KEY的直接链接")

  * Invalid api public key
  * API key不正确



### -4058 MAX_PRICE_TOO_LARGE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4058-max_price_too_large "-4058 MAX_PRICE_TOO_LARGE的直接链接")

  * maxPrice and priceDecimal too large,please check.
  * maxPrice和priceDecimal太大，请检查。



### -4059 NO_NEED_TO_CHANGE_POSITION_SIDE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4059-no_need_to_change_position_side "-4059 NO_NEED_TO_CHANGE_POSITION_SIDE的直接链接")

  * No need to change position side.
  * 无需变更仓位方向



### -4060 INVALID_POSITION_SIDE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4060-invalid_position_side "-4060 INVALID_POSITION_SIDE的直接链接")

  * Invalid position side.
  * 仓位方向不正确。



### -4061 POSITION_SIDE_NOT_MATCH[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4061-position_side_not_match "-4061 POSITION_SIDE_NOT_MATCH的直接链接")

  * Order's position side does not match user's setting.
  * 订单的持仓方向和用户设置不一致。



### -4062 REDUCE_ONLY_CONFLICT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4062-reduce_only_conflict "-4062 REDUCE_ONLY_CONFLICT的直接链接")

  * Invalid or improper reduceOnly value.
  * 仅减仓的设置不正确。



### -4063 INVALID_OPTIONS_REQUEST_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4063-invalid_options_request_type "-4063 INVALID_OPTIONS_REQUEST_TYPE的直接链接")

  * Invalid options request type
  * 无效的期权请求类型



### -4064 INVALID_OPTIONS_TIME_FRAME[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4064-invalid_options_time_frame "-4064 INVALID_OPTIONS_TIME_FRAME的直接链接")

  * Invalid options time frame
  * 无效的期权时间窗口



### -4065 INVALID_OPTIONS_AMOUNT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4065-invalid_options_amount "-4065 INVALID_OPTIONS_AMOUNT的直接链接")

  * Invalid options amount
  * 无效的期权数量



### -4066 INVALID_OPTIONS_EVENT_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4066-invalid_options_event_type "-4066 INVALID_OPTIONS_EVENT_TYPE的直接链接")

  * Invalid options event type
  * 无效的期权事件类型



### -4067 POSITION_SIDE_CHANGE_EXISTS_OPEN_ORDERS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4067-position_side_change_exists_open_orders "-4067 POSITION_SIDE_CHANGE_EXISTS_OPEN_ORDERS的直接链接")

  * Position side cannot be changed if there exists open orders.
  * 如果有挂单，无法修改仓位方向。



### -4068 POSITION_SIDE_CHANGE_EXISTS_QUANTITY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4068-position_side_change_exists_quantity "-4068 POSITION_SIDE_CHANGE_EXISTS_QUANTITY的直接链接")

  * Position side cannot be changed if there exists position.
  * 如果有仓位, 无法修改仓位方向。



### -4069 INVALID_OPTIONS_PREMIUM_FEE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4069-invalid_options_premium_fee "-4069 INVALID_OPTIONS_PREMIUM_FEE的直接链接")

  * Invalid options premium fee
  * 无效的期权费



### -4070 INVALID_CL_OPTIONS_ID_LEN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4070-invalid_cl_options_id_len "-4070 INVALID_CL_OPTIONS_ID_LEN的直接链接")

  * Client options id is not valid.
  * 客户的期权ID不合法
  * Client options id length should be less than 32 chars
  * 客户的期权ID长度应该小于32个字符



### -4071 INVALID_OPTIONS_DIRECTION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4071-invalid_options_direction "-4071 INVALID_OPTIONS_DIRECTION的直接链接")

  * Invalid options direction
  * 期权的方向无效



### -4072 OPTIONS_PREMIUM_NOT_UPDATE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4072-options_premium_not_update "-4072 OPTIONS_PREMIUM_NOT_UPDATE的直接链接")

  * premium fee is not updated, reject order
  * 期权费没有更新



### -4073 OPTIONS_PREMIUM_INPUT_LESS_THAN_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4073-options_premium_input_less_than_zero "-4073 OPTIONS_PREMIUM_INPUT_LESS_THAN_ZERO的直接链接")

  * input premium fee is less than 0, reject order
  * 输入的期权费小于0



### -4074 OPTIONS_AMOUNT_BIGGER_THAN_UPPER[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4074-options_amount_bigger_than_upper "-4074 OPTIONS_AMOUNT_BIGGER_THAN_UPPER的直接链接")

  * Order amount is bigger than upper boundary or less than 0, reject order



### -4075 OPTIONS_PREMIUM_OUTPUT_ZERO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4075-options_premium_output_zero "-4075 OPTIONS_PREMIUM_OUTPUT_ZERO的直接链接")

  * output premium fee is less than 0, reject order



### -4076 OPTIONS_PREMIUM_TOO_DIFF[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4076-options_premium_too_diff "-4076 OPTIONS_PREMIUM_TOO_DIFF的直接链接")

  * original fee is too much higher than last fee
  * 期权的费用比之前的费用高



### -4077 OPTIONS_PREMIUM_REACH_LIMIT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4077-options_premium_reach_limit "-4077 OPTIONS_PREMIUM_REACH_LIMIT的直接链接")

  * place order amount has reached to limit, reject order
  * 下单的数量达到上限



### -4078 OPTIONS_COMMON_ERROR[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4078-options_common_error "-4078 OPTIONS_COMMON_ERROR的直接链接")

  * options internal error
  * 期权内部系统错误



### -4079 INVALID_OPTIONS_ID[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4079-invalid_options_id "-4079 INVALID_OPTIONS_ID的直接链接")

  * invalid options id
  * invalid options id: %s
  * duplicate options id %d for user %d
  * 期权ID无效



### -4080 OPTIONS_USER_NOT_FOUND[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4080-options_user_not_found "-4080 OPTIONS_USER_NOT_FOUND的直接链接")

  * user not found
  * user not found with id: %s
  * 用户找不到



### -4081 OPTIONS_NOT_FOUND[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4081-options_not_found "-4081 OPTIONS_NOT_FOUND的直接链接")

  * options not found
  * options not found with id: %s
  * 期权找不到



### -4082 INVALID_BATCH_PLACE_ORDER_SIZE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4082-invalid_batch_place_order_size "-4082 INVALID_BATCH_PLACE_ORDER_SIZE的直接链接")

  * Invalid number of batch place orders.
  * Invalid number of batch place orders: %s
  * 批量下单的数量不正确



### -4083 PLACE_BATCH_ORDERS_FAIL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4083-place_batch_orders_fail "-4083 PLACE_BATCH_ORDERS_FAIL的直接链接")

  * Fail to place batch orders.
  * 无法批量下单



### -4084 UPCOMING_METHOD[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4084-upcoming_method "-4084 UPCOMING_METHOD的直接链接")

  * Method is not allowed currently. Upcoming soon.
  * 方法不支持



### -4085 INVALID_NOTIONAL_LIMIT_COEF[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4085-invalid_notional_limit_coef "-4085 INVALID_NOTIONAL_LIMIT_COEF的直接链接")

  * Invalid notional limit coefficient
  * 期权的有限系数不正确



### -4086 INVALID_PRICE_SPREAD_THRESHOLD[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4086-invalid_price_spread_threshold "-4086 INVALID_PRICE_SPREAD_THRESHOLD的直接链接")

  * Invalid price spread threshold
  * 无效的价差阀值



### -4087 REDUCE_ONLY_ORDER_PERMISSION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4087-reduce_only_order_permission "-4087 REDUCE_ONLY_ORDER_PERMISSION的直接链接")

  * User can only place reduce only order
  * 用户只能下仅减仓订单



### -4088 NO_PLACE_ORDER_PERMISSION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4088-no_place_order_permission "-4088 NO_PLACE_ORDER_PERMISSION的直接链接")

  * User can not place order currently
  * 用户当前不能下单



### -4104 INVALID_CONTRACT_TYPE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4104-invalid_contract_type "-4104 INVALID_CONTRACT_TYPE的直接链接")

  * Invalid contract type
  * 无效的合约类型



### -4109 INACTIVE_ACCOUNT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4109-inactive_account "-4109 INACTIVE_ACCOUNT的直接链接")

  * Inactive account, transfer any amount of asset to future wallet to reactive
  * 账户被归档，请向合约账户转入任意资产重新激活



### -4114 INVALID_CLIENT_TRAN_ID_LEN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4114-invalid_client_tran_id_len "-4114 INVALID_CLIENT_TRAN_ID_LEN的直接链接")

  * clientTranId is not valid
  * clientTranId不正确
  * Client tran id length should be less than 64 chars
  * 客户的tranId长度应该小于64个字符



### -4115 DUPLICATED_CLIENT_TRAN_ID[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4115-duplicated_client_tran_id "-4115 DUPLICATED_CLIENT_TRAN_ID的直接链接")

  * clientTranId is duplicated
  * clientTranId重复
  * Client tran id should be unique within 7 days
  * 客户的tranId应在7天内唯一



### -4116 DUPLICATED_CLIENT_ORDER_ID[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4116-duplicated_client_order_id "-4116 DUPLICATED_CLIENT_ORDER_ID的直接链接")

  * clientOrderId is duplicated
  * clientOrderId 重复



### -4117 STOP_ORDER_TRIGGERING[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4117-stop_order_triggering "-4117 STOP_ORDER_TRIGGERING的直接链接")

  * stop order is triggering
  * stop订单在触发中



### -4118 REDUCE_ONLY_MARGIN_CHECK_FAILED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4118-reduce_only_margin_check_failed "-4118 REDUCE_ONLY_MARGIN_CHECK_FAILED的直接链接")

  * ReduceOnly Order Failed. Please check your existing position and open orders
  * 仅减仓订单失败。请检查现有的持仓和挂单
  * 这表示新的「仅减仓（reduce-only）」订单与同方向的未成交订单叠加后，会形成反向持仓并导致保证金不足；请先取消该未成交订单后再重试



### -4120 STOP_ORDER_SWITCH_ALGO[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4120-stop_order_switch_algo "-4120 STOP_ORDER_SWITCH_ALGO的直接链接")

  * Order type not supported for this endpoint. Please use the Algo Order API endpoints instead.
  * 该接口不支持此订单类型。请改用Algo Order API 接口。



### -4131 MARKET_ORDER_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4131-market_order_reject "-4131 MARKET_ORDER_REJECT的直接链接")

  * The counterparty's best price does not meet the PERCENT_PRICE filter limit
  * 交易对手的最高价格未达到PERCENT_PRICE过滤器限制



### -4135 INVALID_ACTIVATION_PRICE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4135-invalid_activation_price "-4135 INVALID_ACTIVATION_PRICE的直接链接")

  * Invalid activation price
  * 无效的激活价格



### -4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4137-quantity_exists_with_close_position "-4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION的直接链接")

  * Quantity must be zero with closePosition equals true
  * 数量必须为0，当closePosition为true时



### -4138 REDUCE_ONLY_MUST_BE_TRUE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4138-reduce_only_must_be_true "-4138 REDUCE_ONLY_MUST_BE_TRUE的直接链接")

  * Reduce only must be true with closePosition equals true
  * Reduce only 必须为true，当closePosition为true时



### -4139 ORDER_TYPE_CANNOT_BE_MKT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4139-order_type_cannot_be_mkt "-4139 ORDER_TYPE_CANNOT_BE_MKT的直接链接")

  * Order type can not be market if it's unable to cancel
  * 订单类型不能为市价单如果不能取消



### -4140 INVALID_OPENING_POSITION_STATUS[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4140-invalid_opening_position_status "-4140 INVALID_OPENING_POSITION_STATUS的直接链接")

  * Invalid symbol status for opening position
  * 无效的交易对状态



### -4141 SYMBOL_ALREADY_CLOSED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4141-symbol_already_closed "-4141 SYMBOL_ALREADY_CLOSED的直接链接")

  * Symbol is closed
  * 交易对已下架



### -4142 STRATEGY_INVALID_TRIGGER_PRICE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4142-strategy_invalid_trigger_price "-4142 STRATEGY_INVALID_TRIGGER_PRICE的直接链接")

  * REJECT: take profit or stop order will be triggered immediately
  * 拒绝：止盈止损单将立即被触发



### -4144 INVALID_PAIR[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4144-invalid_pair "-4144 INVALID_PAIR的直接链接")

  * Invalid pair
  * 无效的pair



### -4161 ISOLATED_LEVERAGE_REJECT_WITH_POSITION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4161-isolated_leverage_reject_with_position "-4161 ISOLATED_LEVERAGE_REJECT_WITH_POSITION的直接链接")

  * Leverage reduction is not supported in Isolated Margin Mode with open positions
  * 逐仓仓位模式下无法降低杠杆



### -4164 MIN_NOTIONAL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4164-min_notional "-4164 MIN_NOTIONAL的直接链接")

  * Order's notional must be no smaller than 5.0 (unless you choose reduce only)
  * 订单的名义价值不可以小于5，除了使用reduce only
  * Order's notional must be no smaller than %s (unless you choose reduce only)
  * 订单的名义价值不可以小于`%s`，除了使用reduce only



### -4165 INVALID_TIME_INTERVAL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4165-invalid_time_interval "-4165 INVALID_TIME_INTERVAL的直接链接")

  * Invalid time interval
  * 无效的间隔
  * Maximum time interval is %s days
  * 最大的时间间隔为 `%s` 天



### -4167 ISOLATED_REJECT_WITH_JOINT_MARGIN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4167-isolated_reject_with_joint_margin "-4167 ISOLATED_REJECT_WITH_JOINT_MARGIN的直接链接")

  * Unable to adjust to Multi-Assets mode with symbols of USDⓈ-M Futures under isolated-margin mode.
  * 因有交易对在逐仓模式，无法切换多资产模式



### -4168 JOINT_MARGIN_REJECT_WITH_ISOLATED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4168-joint_margin_reject_with_isolated "-4168 JOINT_MARGIN_REJECT_WITH_ISOLATED的直接链接")

  * Unable to adjust to isolated-margin mode under the Multi-Assets mode.
  * 多资产模式下无法使用逐仓



### -4169 JOINT_MARGIN_REJECT_WITH_MB[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4169-joint_margin_reject_with_mb "-4169 JOINT_MARGIN_REJECT_WITH_MB的直接链接")

  * Unable to adjust Multi-Assets Mode with insufficient margin balance in USDⓈ-M Futures.
  * 保证金不足无法切换多资产模式



### -4170 JOINT_MARGIN_REJECT_WITH_OPEN_ORDER[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4170-joint_margin_reject_with_open_order "-4170 JOINT_MARGIN_REJECT_WITH_OPEN_ORDER的直接链接")

  * Unable to adjust Multi-Assets Mode with open orders in USDⓈ-M Futures.
  * 账户有订单无法切换多资产模式



### -4171 NO_NEED_TO_CHANGE_JOINT_MARGIN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4171-no_need_to_change_joint_margin "-4171 NO_NEED_TO_CHANGE_JOINT_MARGIN的直接链接")

  * Adjusted asset mode is currently set and does not need to be adjusted repeatedly.
  * 多资产模式已经被设置



### -4172 JOINT_MARGIN_REJECT_WITH_NEGATIVE_BALANCE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4172-joint_margin_reject_with_negative_balance "-4172 JOINT_MARGIN_REJECT_WITH_NEGATIVE_BALANCE的直接链接")

  * Unable to adjust Multi-Assets Mode with a negative wallet balance of margin available asset in USDⓈ-M Futures account.



### -4183 PRICE_HIGHTER_THAN_STOP_MULTIPLIER_UP[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4183-price_highter_than_stop_multiplier_up "-4183 PRICE_HIGHTER_THAN_STOP_MULTIPLIER_UP的直接链接")

  * Price is higher than stop price multiplier cap.
  * 止盈止损订单价格不应高于触发价与报价乘数上限的乘积
  * Limit price can't be higher than %s.
  * 止盈止损订单价格不应高于 `%s`



### -4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4184-price_lower_than_stop_multiplier_down "-4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN的直接链接")

  * Price is lower than stop price multiplier floor.
  * 止盈止损订单价格不应低于触发价与报价乘数下限的乘积
  * Limit price can't be lower than %s.
  * 止盈止损订单价格不应低于 `%s`f



### -4192 COOLING_OFF_PERIOD[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4192-cooling_off_period "-4192 COOLING_OFF_PERIOD的直接链接")

  * Trade forbidden due to Cooling-off Period.
  * 合约冷静期禁止开仓



### -4202 ADJUST_LEVERAGE_KYC_FAILED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4202-adjust_leverage_kyc_failed "-4202 ADJUST_LEVERAGE_KYC_FAILED的直接链接")

  * Intermediate Personal Verification is required for adjusting leverage over 20x
  * 需要通过中级KYC才能使用20x以上杠杆



### -4203 ADJUST_LEVERAGE_ONE_MONTH_FAILED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4203-adjust_leverage_one_month_failed "-4203 ADJUST_LEVERAGE_ONE_MONTH_FAILED的直接链接")

  * More than 20x leverage is available one month after account registration.
  * 开户1个月后才可以使用20倍以上杠杆



### -4205 ADJUST_LEVERAGE_X_DAYS_FAILED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4205-adjust_leverage_x_days_failed "-4205 ADJUST_LEVERAGE_X_DAYS_FAILED的直接链接")

  * More than 20x leverage is available %s days after Futures account registration.
  * 开户%s天后才可以使用20倍以上杠杆



### -4206 ADJUST_LEVERAGE_KYC_LIMIT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4206-adjust_leverage_kyc_limit "-4206 ADJUST_LEVERAGE_KYC_LIMIT的直接链接")

  * Users in this country has limited adjust leverage.
  * Users in your location/country can only access a maximum leverage of %s
  * 该国家有杠杆限制
  * 该国家杠杆不能超过%s倍



### -4208 ADJUST_LEVERAGE_ACCOUNT_SYMBOL_FAILED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4208-adjust_leverage_account_symbol_failed "-4208 ADJUST_LEVERAGE_ACCOUNT_SYMBOL_FAILED的直接链接")

  * Current symbol leverage cannot exceed 20 when using position limit adjustment service.
  * 开启仓位放大功能的用户无法使用20x以上杠杆



### -4209 ADJUST_LEVERAGE_SYMBOL_FAILED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4209-adjust_leverage_symbol_failed "-4209 ADJUST_LEVERAGE_SYMBOL_FAILED的直接链接")

  * The max leverage of Symbol is 20x
  * Leverage adjustment failed. Current symbol max leverage limit is %sx
  * 交易对最大杠杆为20x
  * 杠杆调整失败。交易对最大杠杆为%sx



### -4210 STOP_PRICE_HIGHER_THAN_PRICE_MULTIPLIER_LIMIT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4210-stop_price_higher_than_price_multiplier_limit "-4210 STOP_PRICE_HIGHER_THAN_PRICE_MULTIPLIER_LIMIT的直接链接")

  * Stop price is higher than price multiplier cap.
  * Stop price can't be higher than %s
  * 触发价超过价格上限
  * 触发价不能超过%s



### -4211 STOP_PRICE_LOWER_THAN_PRICE_MULTIPLIER_LIMIT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4211-stop_price_lower_than_price_multiplier_limit "-4211 STOP_PRICE_LOWER_THAN_PRICE_MULTIPLIER_LIMIT的直接链接")

  * Stop price is lower than price multiplier floor.
  * Stop price can't be lower than %s
  * 触发价低于超过价格下限
  * 触发价不能低于%s



### -4400 TRADING_QUANTITATIVE_RULE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4400-trading_quantitative_rule "-4400 TRADING_QUANTITATIVE_RULE的直接链接")

  * Futures Trading Quantitative Rules violated, only reduceOnly order is allowed, please try again later.
  * 违反合约量化交易规则，账户设置为近减仓，请之后再试



### -4401 LARGE_POSITION_SYM_RULE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4401-large_position_sym_rule "-4401 LARGE_POSITION_SYM_RULE的直接链接")

  * Futures Trading Risk Control Rules of large position holding violated, only reduceOnly order is allowed, please reduce the position
  * 账户违反大持仓风控规则，仅能下减仓单，请减少仓位



### -4402 COMPLIANCE_BLACK_SYMBOL_RESTRICTION[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4402-compliance_black_symbol_restriction "-4402 COMPLIANCE_BLACK_SYMBOL_RESTRICTION的直接链接")

  * Dear user, as per our Terms of Use and compliance with local regulations, this feature is currently not available in your region.
  * 根据合规要求，所在地区不提供此服务



### -4403 ADJUST_LEVERAGE_COMPLIANCE_FAILED[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-4403-adjust_leverage_compliance_failed "-4403 ADJUST_LEVERAGE_COMPLIANCE_FAILED的直接链接")

  * Dear user, as per our Terms of Use and compliance with local regulations, the leverage can only up to 10x in your region
  * Dear user, as per our Terms of Use and compliance with local regulations, the leverage can only up to %sx in your region
  * 根据合规要求，所在地区杠杆不可超过10x
  * 根据合规要求，所在地区杠杆不可超过%sx



## 50xx - Order Execution Issues[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#50xx---order-execution-issues "50xx - Order Execution Issues的直接链接")

### -5021 FOK_ORDER_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5021-fok_order_reject "-5021 FOK_ORDER_REJECT的直接链接")

  * Due to the order could not be filled immediately, the FOK order has been rejected. The order will not be recorded in the order history
  * 订单无法完全成交，FOK订单被拒绝



### -5022 GTX_ORDER_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5022-gtx_order_reject "-5022 GTX_ORDER_REJECT的直接链接")

  * Due to the order could not be executed as maker, the Post Only order will be rejected. The order will not be recorded in the order history
  * 订单无法仅做maker单， Post Only订单被拒绝



### -5024 MOVE_ORDER_NOT_ALLOWED_SYMBOL_REASON[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5024-move_order_not_allowed_symbol_reason "-5024 MOVE_ORDER_NOT_ALLOWED_SYMBOL_REASON的直接链接")

  * Symbol is not in trading status. Order amendment is not permitted.
  * 交易对不在交易状态，无法改单



### -5025 LIMIT_ORDER_ONLY[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5025-limit_order_only "-5025 LIMIT_ORDER_ONLY的直接链接")

  * Only limit order is supported.
  * 仅支持限价单改单



### -5026 Exceed_Maximum_Modify_Order_Limit[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5026-exceed_maximum_modify_order_limit "-5026 Exceed_Maximum_Modify_Order_Limit的直接链接")

  * Exceed maximum modify order limit.
  * 超过单个订单改单次数上限



### -5027 SAME_ORDER[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5027-same_order "-5027 SAME_ORDER的直接链接")

  * No need to modify the order.
  * 与原订单相同，非必要改单



### -5028 ME_RECVWINDOW_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5028-me_recvwindow_reject "-5028 ME_RECVWINDOW_REJECT的直接链接")

  * Timestamp for this request is outside of the ME recvWindow.
  * 请求的时间戳在撮合的recvWindow之外



### -5029 MODIFICATION_MIN_NOTIONAL[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5029-modification_min_notional "-5029 MODIFICATION_MIN_NOTIONAL的直接链接")

  * Order's notional must be no smaller than %s
  * 请求的时间戳在撮合的recvWindow之外



### -5037 INVALID_PRICE_MATCH[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5037-invalid_price_match "-5037 INVALID_PRICE_MATCH的直接链接")

  * Invalid price match
  * 错误的价格匹配类型



### -5038 UNSUPPORTED_ORDER_TYPE_PRICE_MATCH[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5038-unsupported_order_type_price_match "-5038 UNSUPPORTED_ORDER_TYPE_PRICE_MATCH的直接链接")

  * Price match only supports order type: LIMIT, STOP AND TAKE_PROFIT
  * 价格匹配仅支持下列订单类型: LIMIT, STOP AND TAKE_PROFIT



### -5039 INVALID_SELF_TRADE_PREVENTION_MODE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5039-invalid_self_trade_prevention_mode "-5039 INVALID_SELF_TRADE_PREVENTION_MODE的直接链接")

  * Invalid self trade prevention mode
  * 错误的防治自成交类型



### -5040 FUTURE_GOOD_TILL_DATE[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5040-future_good_till_date "-5040 FUTURE_GOOD_TILL_DATE的直接链接")

  * The goodTillDate timestamp must be greater than the current time plus 600 seconds and smaller than 253402300799000 (UTC 9999-12-31 23:59:59)
  * GTD订单需要时间大于当前时间60s且小于253402300799000



### -5041 BBO_ORDER_REJECT[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5041-bbo_order_reject "-5041 BBO_ORDER_REJECT的直接链接")

  * No depth matches this BBO order
  * 盘口没有深度挂价格匹配订单



### -5043 Existing_Pending_Modification[​](/docs/zh-CN/derivatives/usds-margined-futures/error-code#-5043-existing_pending_modification "-5043 Existing_Pending_Modification的直接链接")

  * A pending modification already exists for this order.
  * 改订单已经有改单请求在处理