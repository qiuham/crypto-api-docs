---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/errors
api_type: REST
updated_at: 2026-01-15T23:35:52.532232
---

# Error codes for Binance

Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:
    
    
    {  
        "code": -1121,  
        "msg": "Invalid symbol."  
    }  
    

## 10xx - General Server or Network issues[​](/docs/binance-spot-api-docs/errors#10xx---general-server-or-network-issues "Direct link to 10xx - General Server or Network issues")

### -1000 UNKNOWN[​](/docs/binance-spot-api-docs/errors#-1000-unknown "Direct link to -1000 UNKNOWN")

  * An unknown error occurred while processing the request.



### -1001 DISCONNECTED[​](/docs/binance-spot-api-docs/errors#-1001-disconnected "Direct link to -1001 DISCONNECTED")

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED[​](/docs/binance-spot-api-docs/errors#-1002-unauthorized "Direct link to -1002 UNAUTHORIZED")

  * You are not authorized to execute this request.



### -1003 TOO_MANY_REQUESTS[​](/docs/binance-spot-api-docs/errors#-1003-too_many_requests "Direct link to -1003 TOO_MANY_REQUESTS")

  * Too many requests queued.
  * Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.
  * Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.



### -1006 UNEXPECTED_RESP[​](/docs/binance-spot-api-docs/errors#-1006-unexpected_resp "Direct link to -1006 UNEXPECTED_RESP")

  * An unexpected response was received from the message bus. Execution status unknown.



### -1007 TIMEOUT[​](/docs/binance-spot-api-docs/errors#-1007-timeout "Direct link to -1007 TIMEOUT")

  * Timeout waiting for response from backend server. Send status unknown; execution status unknown.



### -1008 SERVER_BUSY[​](/docs/binance-spot-api-docs/errors#-1008-server_busy "Direct link to -1008 SERVER_BUSY")

  * Server is currently overloaded with other requests. Please try again in a few minutes.



### -1013 INVALID_MESSAGE[​](/docs/binance-spot-api-docs/errors#-1013-invalid_message "Direct link to -1013 INVALID_MESSAGE")

  * The request is rejected by the API. (i.e. The request didn't reach the Matching Engine.)
  * Potential error messages can be found in [Filter Failures](/docs/binance-spot-api-docs/errors#filter-failures) or [Failures during order placement](/docs/binance-spot-api-docs/errors#other-errors).



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/binance-spot-api-docs/errors#-1014-unknown_order_composition "Direct link to -1014 UNKNOWN_ORDER_COMPOSITION")

  * Unsupported order combination.



### -1015 TOO_MANY_ORDERS[​](/docs/binance-spot-api-docs/errors#-1015-too_many_orders "Direct link to -1015 TOO_MANY_ORDERS")

  * Too many new orders.
  * Too many new orders; current limit is %s orders per %s.



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/binance-spot-api-docs/errors#-1016-service_shutting_down "Direct link to -1016 SERVICE_SHUTTING_DOWN")

  * This service is no longer available.



### -1020 UNSUPPORTED_OPERATION[​](/docs/binance-spot-api-docs/errors#-1020-unsupported_operation "Direct link to -1020 UNSUPPORTED_OPERATION")

  * This operation is not supported.



### -1021 INVALID_TIMESTAMP[​](/docs/binance-spot-api-docs/errors#-1021-invalid_timestamp "Direct link to -1021 INVALID_TIMESTAMP")

  * Timestamp for this request is outside of the recvWindow.
  * Timestamp for this request was 1000ms ahead of the server's time.



### -1022 INVALID_SIGNATURE[​](/docs/binance-spot-api-docs/errors#-1022-invalid_signature "Direct link to -1022 INVALID_SIGNATURE")

  * Signature for this request is not valid.



### -1033 COMP_ID_IN_USE[​](/docs/binance-spot-api-docs/errors#-1033-comp_id_in_use "Direct link to -1033 COMP_ID_IN_USE")

  * `SenderCompId(49)` is currently in use. Concurrent use of the same SenderCompId within one account is not allowed.



### -1034 TOO_MANY_CONNECTIONS[​](/docs/binance-spot-api-docs/errors#-1034-too_many_connections "Direct link to -1034 TOO_MANY_CONNECTIONS")

  * Too many concurrent connections; current limit is '%s'.
  * Too many connection attempts for account; current limit is %s per '%s'.
  * Too many connection attempts from IP; current limit is %s per '%s'.



### -1035 LOGGED_OUT[​](/docs/binance-spot-api-docs/errors#-1035-logged_out "Direct link to -1035 LOGGED_OUT")

  * Please send [Logout`<5>`](/docs/binance-spot-api-docs/fix-api#logout) message to close the session.



## 11xx - Request issues[​](/docs/binance-spot-api-docs/errors#11xx---request-issues "Direct link to 11xx - Request issues")

### -1100 ILLEGAL_CHARS[​](/docs/binance-spot-api-docs/errors#-1100-illegal_chars "Direct link to -1100 ILLEGAL_CHARS")

  * Illegal characters found in a parameter.
  * Illegal characters found in parameter '%s'; legal range is '%s'.



### -1101 TOO_MANY_PARAMETERS[​](/docs/binance-spot-api-docs/errors#-1101-too_many_parameters "Direct link to -1101 TOO_MANY_PARAMETERS")

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected '%s' and received '%s'.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/binance-spot-api-docs/errors#-1102-mandatory_param_empty_or_malformed "Direct link to -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
  * Param '%s' or '%s' must be sent, but both were empty/null!
  * Required tag '%s' missing.
  * Field value was empty or malformed.
  * '%s' contains unexpected value. Cannot be greater than %s.



### -1103 UNKNOWN_PARAM[​](/docs/binance-spot-api-docs/errors#-1103-unknown_param "Direct link to -1103 UNKNOWN_PARAM")

  * An unknown parameter was sent.
  * Undefined Tag.



### -1104 UNREAD_PARAMETERS[​](/docs/binance-spot-api-docs/errors#-1104-unread_parameters "Direct link to -1104 UNREAD_PARAMETERS")

  * Not all sent parameters were read.
  * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.



### -1105 PARAM_EMPTY[​](/docs/binance-spot-api-docs/errors#-1105-param_empty "Direct link to -1105 PARAM_EMPTY")

  * A parameter was empty.
  * Parameter '%s' was empty.



### -1106 PARAM_NOT_REQUIRED[​](/docs/binance-spot-api-docs/errors#-1106-param_not_required "Direct link to -1106 PARAM_NOT_REQUIRED")

  * A parameter was sent when not required.
  * Parameter '%s' sent when not required.
  * A tag '%s' was sent when not required.



### -1108 PARAM_OVERFLOW[​](/docs/binance-spot-api-docs/errors#-1108-param_overflow "Direct link to -1108 PARAM_OVERFLOW")

  * Parameter '%s' overflowed.



### -1111 BAD_PRECISION[​](/docs/binance-spot-api-docs/errors#-1111-bad_precision "Direct link to -1111 BAD_PRECISION")

  * Parameter '%s' has too much precision.



### -1112 NO_DEPTH[​](/docs/binance-spot-api-docs/errors#-1112-no_depth "Direct link to -1112 NO_DEPTH")

  * No orders on book for symbol.



### -1114 TIF_NOT_REQUIRED[​](/docs/binance-spot-api-docs/errors#-1114-tif_not_required "Direct link to -1114 TIF_NOT_REQUIRED")

  * TimeInForce parameter sent when not required.



### -1115 INVALID_TIF[​](/docs/binance-spot-api-docs/errors#-1115-invalid_tif "Direct link to -1115 INVALID_TIF")

  * Invalid timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/binance-spot-api-docs/errors#-1116-invalid_order_type "Direct link to -1116 INVALID_ORDER_TYPE")

  * Invalid orderType.



### -1117 INVALID_SIDE[​](/docs/binance-spot-api-docs/errors#-1117-invalid_side "Direct link to -1117 INVALID_SIDE")

  * Invalid side.



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/binance-spot-api-docs/errors#-1118-empty_new_cl_ord_id "Direct link to -1118 EMPTY_NEW_CL_ORD_ID")

  * New client order ID was empty.



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/binance-spot-api-docs/errors#-1119-empty_org_cl_ord_id "Direct link to -1119 EMPTY_ORG_CL_ORD_ID")

  * Original client order ID was empty.



### -1120 BAD_INTERVAL[​](/docs/binance-spot-api-docs/errors#-1120-bad_interval "Direct link to -1120 BAD_INTERVAL")

  * Invalid interval.



### -1121 BAD_SYMBOL[​](/docs/binance-spot-api-docs/errors#-1121-bad_symbol "Direct link to -1121 BAD_SYMBOL")

  * Invalid symbol.



### -1122 INVALID_SYMBOLSTATUS[​](/docs/binance-spot-api-docs/errors#-1122-invalid_symbolstatus "Direct link to -1122 INVALID_SYMBOLSTATUS")

  * Invalid symbolStatus.



### -1125 INVALID_LISTEN_KEY[​](/docs/binance-spot-api-docs/errors#-1125-invalid_listen_key "Direct link to -1125 INVALID_LISTEN_KEY")

  * This listenKey does not exist.



### -1127 MORE_THAN_XX_HOURS[​](/docs/binance-spot-api-docs/errors#-1127-more_than_xx_hours "Direct link to -1127 MORE_THAN_XX_HOURS")

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 OPTIONAL_PARAMS_BAD_COMBO[​](/docs/binance-spot-api-docs/errors#-1128-optional_params_bad_combo "Direct link to -1128 OPTIONAL_PARAMS_BAD_COMBO")

  * Combination of optional parameters invalid.
  * Combination of optional fields invalid. Recommendation: '%s' and '%s' must both be sent.
  * Fields [%s] must be sent together or omitted entirely.
  * Invalid `MDEntryType (269)` combination. BID and OFFER must be requested together.
  * Conflicting fields: ['%s'...]



### -1130 INVALID_PARAMETER[​](/docs/binance-spot-api-docs/errors#-1130-invalid_parameter "Direct link to -1130 INVALID_PARAMETER")

  * Invalid data sent for a parameter.
  * Data sent for parameter '%s' is not valid.



### -1134 BAD_STRATEGY_TYPE[​](/docs/binance-spot-api-docs/errors#-1134-bad_strategy_type "Direct link to -1134 BAD_STRATEGY_TYPE")

  * `strategyType` was less than 1000000.
  * `TargetStrategy (847)` was less than 1000000.



### -1135 INVALID_JSON[​](/docs/binance-spot-api-docs/errors#-1135-invalid_json "Direct link to -1135 INVALID_JSON")

  * Invalid JSON Request
  * JSON sent for parameter '%s' is not valid



### -1139 INVALID_TICKER_TYPE[​](/docs/binance-spot-api-docs/errors#-1139-invalid_ticker_type "Direct link to -1139 INVALID_TICKER_TYPE")

  * Invalid ticker type.



### -1145 INVALID_CANCEL_RESTRICTIONS[​](/docs/binance-spot-api-docs/errors#-1145-invalid_cancel_restrictions "Direct link to -1145 INVALID_CANCEL_RESTRICTIONS")

  * `cancelRestrictions` has to be either `ONLY_NEW` or `ONLY_PARTIALLY_FILLED`.



### -1151 DUPLICATE_SYMBOLS[​](/docs/binance-spot-api-docs/errors#-1151-duplicate_symbols "Direct link to -1151 DUPLICATE_SYMBOLS")

  * Symbol is present multiple times in the list.



### -1152 INVALID_SBE_HEADER[​](/docs/binance-spot-api-docs/errors#-1152-invalid_sbe_header "Direct link to -1152 INVALID_SBE_HEADER")

  * Invalid `X-MBX-SBE` header; expected `<SCHEMA_ID>:<VERSION>`.
  * Invalid SBE message header.



### -1153 UNSUPPORTED_SCHEMA_ID[​](/docs/binance-spot-api-docs/errors#-1153-unsupported_schema_id "Direct link to -1153 UNSUPPORTED_SCHEMA_ID")

  * Unsupported SBE schema ID or version specified in the `X-MBX-SBE` header.
  * Invalid SBE schema ID or version specified.



### -1155 SBE_DISABLED[​](/docs/binance-spot-api-docs/errors#-1155-sbe_disabled "Direct link to -1155 SBE_DISABLED")

  * SBE is not enabled.



### -1158 OCO_ORDER_TYPE_REJECTED[​](/docs/binance-spot-api-docs/errors#-1158-oco_order_type_rejected "Direct link to -1158 OCO_ORDER_TYPE_REJECTED")

  * Order type not supported in OCO.
  * If the order type provided in the `aboveType` and/or `belowType` is not supported.



### -1160 OCO_ICEBERGQTY_TIMEINFORCE[​](/docs/binance-spot-api-docs/errors#-1160-oco_icebergqty_timeinforce "Direct link to -1160 OCO_ICEBERGQTY_TIMEINFORCE")

  * Parameter '%s' is not supported if `aboveTimeInForce`/`belowTimeInForce` is not GTC.
  * If the order type for the above or below leg is `STOP_LOSS_LIMIT`, and `icebergQty` is provided for that leg, the `timeInForce` has to be `GTC` else it will throw an error.
  * `TimeInForce (59)` must be `GTC (1)` when `MaxFloor (111)` is used.



### -1161 DEPRECATED_SCHEMA[​](/docs/binance-spot-api-docs/errors#-1161-deprecated_schema "Direct link to -1161 DEPRECATED_SCHEMA")

  * Unable to encode the response in SBE schema 'x'. Please use schema 'y' or higher.



### -1165 BUY_OCO_LIMIT_MUST_BE_BELOW[​](/docs/binance-spot-api-docs/errors#-1165-buy_oco_limit_must_be_below "Direct link to -1165 BUY_OCO_LIMIT_MUST_BE_BELOW")

  * A limit order in a buy OCO must be below.



### -1166 SELL_OCO_LIMIT_MUST_BE_ABOVE[​](/docs/binance-spot-api-docs/errors#-1166-sell_oco_limit_must_be_above "Direct link to -1166 SELL_OCO_LIMIT_MUST_BE_ABOVE")

  * A limit order in a sell OCO must be above.



### -1168 BOTH_OCO_ORDERS_CANNOT_BE_LIMIT[​](/docs/binance-spot-api-docs/errors#-1168-both_oco_orders_cannot_be_limit "Direct link to -1168 BOTH_OCO_ORDERS_CANNOT_BE_LIMIT")

  * At least one OCO order must be contingent.



### -1169 INVALID_TAG_NUMBER[​](/docs/binance-spot-api-docs/errors#-1169-invalid_tag_number "Direct link to -1169 INVALID_TAG_NUMBER")

  * Invalid tag number.



### -1170 TAG_NOT_DEFINED_IN_MESSAGE[​](/docs/binance-spot-api-docs/errors#-1170-tag_not_defined_in_message "Direct link to -1170 TAG_NOT_DEFINED_IN_MESSAGE")

  * Tag '%s' not defined for this message type.



### -1171 TAG_APPEARS_MORE_THAN_ONCE[​](/docs/binance-spot-api-docs/errors#-1171-tag_appears_more_than_once "Direct link to -1171 TAG_APPEARS_MORE_THAN_ONCE")

  * Tag '%s' appears more than once.



### -1172 TAG_OUT_OF_ORDER[​](/docs/binance-spot-api-docs/errors#-1172-tag_out_of_order "Direct link to -1172 TAG_OUT_OF_ORDER")

  * Tag '%s' specified out of required order.



### -1173 GROUP_FIELDS_OUT_OF_ORDER[​](/docs/binance-spot-api-docs/errors#-1173-group_fields_out_of_order "Direct link to -1173 GROUP_FIELDS_OUT_OF_ORDER")

  * Repeating group '%s' fields out of order.



### -1174 INVALID_COMPONENT[​](/docs/binance-spot-api-docs/errors#-1174-invalid_component "Direct link to -1174 INVALID_COMPONENT")

  * Component '%s' is incorrectly populated on '%s' order. Recommendation: '%s'



### -1175 RESET_SEQ_NUM_SUPPORT[​](/docs/binance-spot-api-docs/errors#-1175-reset_seq_num_support "Direct link to -1175 RESET_SEQ_NUM_SUPPORT")

  * Continuation of sequence numbers to new session is currently unsupported. Sequence numbers must be reset for each new session.



### -1176 ALREADY_LOGGED_IN[​](/docs/binance-spot-api-docs/errors#-1176-already_logged_in "Direct link to -1176 ALREADY_LOGGED_IN")

  * [Logon`<A>`](/docs/binance-spot-api-docs/fix-api#logon-main) should only be sent once.



### -1177 GARBLED_MESSAGE[​](/docs/binance-spot-api-docs/errors#-1177-garbled_message "Direct link to -1177 GARBLED_MESSAGE")

  * `CheckSum(10)` contains an incorrect value.
  * `BeginString (8)` is not the first tag in a message.
  * `MsgType (35)` is not the third tag in a message.
  * `BodyLength (9)` does not contain the correct byte count.
  * Only printable ASCII characters and SOH (Start of Header) are allowed.
  * Tag specified without a value.
  * Invalid encodingType.



### -1178 BAD_SENDER_COMPID[​](/docs/binance-spot-api-docs/errors#-1178-bad_sender_compid "Direct link to -1178 BAD_SENDER_COMPID")

  * `SenderCompId(49)` contains an incorrect value. The SenderCompID value should not change throughout the lifetime of a session.



### -1179 BAD_SEQ_NUM[​](/docs/binance-spot-api-docs/errors#-1179-bad_seq_num "Direct link to -1179 BAD_SEQ_NUM")

  * `MsgSeqNum(34)` contains an unexpected value. Expected: '%d'.



### -1180 EXPECTED_LOGON[​](/docs/binance-spot-api-docs/errors#-1180-expected_logon "Direct link to -1180 EXPECTED_LOGON")

  * [Logon`<A>`](/docs/binance-spot-api-docs/fix-api#logon-main) must be the first message in the session.



### -1181 TOO_MANY_MESSAGES[​](/docs/binance-spot-api-docs/errors#-1181-too_many_messages "Direct link to -1181 TOO_MANY_MESSAGES")

  * Too many messages; current limit is '%d' messages per '%s'.



### -1182 PARAMS_BAD_COMBO[​](/docs/binance-spot-api-docs/errors#-1182-params_bad_combo "Direct link to -1182 PARAMS_BAD_COMBO")

  * Conflicting fields: [%s]



### -1183 NOT_ALLOWED_IN_DROP_COPY_SESSIONS[​](/docs/binance-spot-api-docs/errors#-1183-not_allowed_in_drop_copy_sessions "Direct link to -1183 NOT_ALLOWED_IN_DROP_COPY_SESSIONS")

  * Requested operation is not allowed in DropCopy sessions.



### -1184 DROP_COPY_SESSION_NOT_ALLOWED[​](/docs/binance-spot-api-docs/errors#-1184-drop_copy_session_not_allowed "Direct link to -1184 DROP_COPY_SESSION_NOT_ALLOWED")

  * DropCopy sessions are not supported on this server. Please reconnect to a drop copy server.



### -1185 DROP_COPY_SESSION_REQUIRED[​](/docs/binance-spot-api-docs/errors#-1185-drop_copy_session_required "Direct link to -1185 DROP_COPY_SESSION_REQUIRED")

  * Only DropCopy sessions are supported on this server. Either reconnect to order entry server or send `DropCopyFlag (9406)` field.



### -1186 NOT_ALLOWED_IN_ORDER_ENTRY_SESSIONS[​](/docs/binance-spot-api-docs/errors#-1186-not_allowed_in_order_entry_sessions "Direct link to -1186 NOT_ALLOWED_IN_ORDER_ENTRY_SESSIONS")

  * Requested operation is not allowed in order entry sessions.



### -1187 NOT_ALLOWED_IN_MARKET_DATA_SESSIONS[​](/docs/binance-spot-api-docs/errors#-1187-not_allowed_in_market_data_sessions "Direct link to -1187 NOT_ALLOWED_IN_MARKET_DATA_SESSIONS")

  * Requested operation is not allowed in market data sessions.



### -1188 INCORRECT_NUM_IN_GROUP_COUNT[​](/docs/binance-spot-api-docs/errors#-1188-incorrect_num_in_group_count "Direct link to -1188 INCORRECT_NUM_IN_GROUP_COUNT")

  * Incorrect NumInGroup count for repeating group '%s'.



### -1189 DUPLICATE_ENTRIES_IN_A_GROUP[​](/docs/binance-spot-api-docs/errors#-1189-duplicate_entries_in_a_group "Direct link to -1189 DUPLICATE_ENTRIES_IN_A_GROUP")

  * Group '%s' contains duplicate entries.



### -1190 INVALID_REQUEST_ID[​](/docs/binance-spot-api-docs/errors#-1190-invalid_request_id "Direct link to -1190 INVALID_REQUEST_ID")

  * `MDReqID (262)` contains a subscription request id that is already in use on this connection.
  * `MDReqID (262)` contains an unsubscription request id that does not match any active subscription.



### -1191 TOO_MANY_SUBSCRIPTIONS[​](/docs/binance-spot-api-docs/errors#-1191-too_many_subscriptions "Direct link to -1191 TOO_MANY_SUBSCRIPTIONS")

  * Too many subscriptions. Connection may create up to '%s' subscriptions at a time.
  * Similar subscription is already active on this connection. Symbol='%s', active subscription id: '%s'.



### -1194 INVALID_TIME_UNIT[​](/docs/binance-spot-api-docs/errors#-1194-invalid_time_unit "Direct link to -1194 INVALID_TIME_UNIT")

  * Invalid value for time unit; expected either MICROSECOND or MILLISECOND.



### -1196 BUY_OCO_STOP_LOSS_MUST_BE_ABOVE[​](/docs/binance-spot-api-docs/errors#-1196-buy_oco_stop_loss_must_be_above "Direct link to -1196 BUY_OCO_STOP_LOSS_MUST_BE_ABOVE")

  * A stop loss order in a buy OCO must be above.



### -1197 SELL_OCO_STOP_LOSS_MUST_BE_BELOW[​](/docs/binance-spot-api-docs/errors#-1197-sell_oco_stop_loss_must_be_below "Direct link to -1197 SELL_OCO_STOP_LOSS_MUST_BE_BELOW")

  * A stop loss order in a sell OCO must be below.



### -1198 BUY_OCO_TAKE_PROFIT_MUST_BE_BELOW[​](/docs/binance-spot-api-docs/errors#-1198-buy_oco_take_profit_must_be_below "Direct link to -1198 BUY_OCO_TAKE_PROFIT_MUST_BE_BELOW")

  * A take profit order in a buy OCO must be below.



### -1199 SELL_OCO_TAKE_PROFIT_MUST_BE_ABOVE[​](/docs/binance-spot-api-docs/errors#-1199-sell_oco_take_profit_must_be_above "Direct link to -1199 SELL_OCO_TAKE_PROFIT_MUST_BE_ABOVE")

  * A take profit order in a sell OCO must be above.



### -1210 INVALID_PEG_PRICE_TYPE[​](/docs/binance-spot-api-docs/errors#-1210-invalid_peg_price_type "Direct link to -1210 INVALID_PEG_PRICE_TYPE")

  * Invalid pegPriceType.



### -1211 INVALID_PEG_OFFSET_TYPE[​](/docs/binance-spot-api-docs/errors#-1211-invalid_peg_offset_type "Direct link to -1211 INVALID_PEG_OFFSET_TYPE")

  * Invalid pegOffsetType.



### -1220 SYMBOL_DOES_NOT_MATCH_STATUS[​](/docs/binance-spot-api-docs/errors#-1220-symbol_does_not_match_status "Direct link to -1220 SYMBOL_DOES_NOT_MATCH_STATUS")

  * The symbol's status does not match the requested symbolStatus.



### -1221 INVALID_SBE_MESSAGE_FIELD[​](/docs/binance-spot-api-docs/errors#-1221-invalid_sbe_message_field "Direct link to -1221 INVALID_SBE_MESSAGE_FIELD")

  * Invalid/missing field(s) in SBE message.



### -1222 OPO_WORKING_MUST_BE_BUY[​](/docs/binance-spot-api-docs/errors#-1222-opo_working_must_be_buy "Direct link to -1222 OPO_WORKING_MUST_BE_BUY")

  * Working order in an OPO list must be a bid.



### -1223 OPO_PENDING_MUST_BE_SELL[​](/docs/binance-spot-api-docs/errors#-1223-opo_pending_must_be_sell "Direct link to -1223 OPO_PENDING_MUST_BE_SELL")

  * Pending orders in an OPO list must be asks.



### -1224 WORKING_PARAM_REQUIRED[​](/docs/binance-spot-api-docs/errors#-1224-working_param_required "Direct link to -1224 WORKING_PARAM_REQUIRED")

  * Working order must include the '{param}' tag.



### -1225 PENDING_PARAM_NOT_REQUIRED[​](/docs/binance-spot-api-docs/errors#-1225-pending_param_not_required "Direct link to -1225 PENDING_PARAM_NOT_REQUIRED")

  * Pending orders should not include the '%s' tag.



### -2010 NEW_ORDER_REJECTED[​](/docs/binance-spot-api-docs/errors#-2010-new_order_rejected "Direct link to -2010 NEW_ORDER_REJECTED")

  * NEW_ORDER_REJECTED



### -2011 CANCEL_REJECTED[​](/docs/binance-spot-api-docs/errors#-2011-cancel_rejected "Direct link to -2011 CANCEL_REJECTED")

  * CANCEL_REJECTED



### -2013 NO_SUCH_ORDER[​](/docs/binance-spot-api-docs/errors#-2013-no_such_order "Direct link to -2013 NO_SUCH_ORDER")

  * Order does not exist.



### -2014 BAD_API_KEY_FMT[​](/docs/binance-spot-api-docs/errors#-2014-bad_api_key_fmt "Direct link to -2014 BAD_API_KEY_FMT")

  * API-key format invalid.



### -2015 REJECTED_MBX_KEY[​](/docs/binance-spot-api-docs/errors#-2015-rejected_mbx_key "Direct link to -2015 REJECTED_MBX_KEY")

  * Invalid API-key, IP, or permissions for action.



### -2016 NO_TRADING_WINDOW[​](/docs/binance-spot-api-docs/errors#-2016-no_trading_window "Direct link to -2016 NO_TRADING_WINDOW")

  * No trading window could be found for the symbol. Try ticker/24hrs instead.



### -2026 ORDER_ARCHIVED[​](/docs/binance-spot-api-docs/errors#-2026-order_archived "Direct link to -2026 ORDER_ARCHIVED")

  * Order was canceled or expired with no executed qty over 90 days ago and has been archived.



### -2035 SUBSCRIPTION_ACTIVE[​](/docs/binance-spot-api-docs/errors#-2035-subscription_active "Direct link to -2035 SUBSCRIPTION_ACTIVE")

  * User Data Stream subscription already active.



### -2036 SUBSCRIPTION_INACTIVE[​](/docs/binance-spot-api-docs/errors#-2036-subscription_inactive "Direct link to -2036 SUBSCRIPTION_INACTIVE")

  * User Data Stream subscription not active.



### -2039 CLIENT_ORDER_ID_INVALID[​](/docs/binance-spot-api-docs/errors#-2039-client_order_id_invalid "Direct link to -2039 CLIENT_ORDER_ID_INVALID")

  * Client order ID is not correct for this order ID.



### -2042 MAXIMUM_SUBSCRIPTION_IDS[​](/docs/binance-spot-api-docs/errors#-2042-maximum_subscription_ids "Direct link to -2042 MAXIMUM_SUBSCRIPTION_IDS")

  * Maximum subscription ID reached for this connection.



## Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, -2011 CANCEL_REJECTED, and -2038 ORDER_AMEND_REJECTED[​](/docs/binance-spot-api-docs/errors#messages-for--1010-error_msg_received--2010-new_order_rejected--2011-cancel_rejected-and--2038-order_amend_rejected "Direct link to Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, -2011 CANCEL_REJECTED, and -2038 ORDER_AMEND_REJECTED")

This code is sent when an error has been returned by the matching engine. The following messages which will indicate the specific error:

Error message| Description  
---|---  
"Unknown order sent."| The order (by either `orderId`, `clOrdId`, `origClOrdId`) could not be found.  
"Duplicate order sent."| The `clOrdId` is already in use.  
"Market is closed."| The symbol is not trading.  
"Account has insufficient balance for requested action."| Not enough funds to complete the action.  
"Market orders are not supported for this symbol."| `MARKET` is not enabled on the symbol.  
"Iceberg orders are not supported for this symbol."| `icebergQty` is not enabled on the symbol.  
"Stop loss orders are not supported for this symbol."| `STOP_LOSS` is not enabled on the symbol.  
"Stop loss limit orders are not supported for this symbol."| `STOP_LOSS_LIMIT` is not enabled on the symbol.  
"Take profit orders are not supported for this symbol."| `TAKE_PROFIT` is not enabled on the symbol.  
"Take profit limit orders are not supported for this symbol."| `TAKE_PROFIT_LIMIT` is not enabled on the symbol.  
"Order amend is not supported for this symbol."| Order amend keep priority is not enabled on the symbol.  
"Price * QTY is zero or less."| `price` * `quantity` is too low.  
"IcebergQty exceeds QTY."| `icebergQty` must be less than the order quantity.  
"This action is disabled on this account."| Contact customer support; some actions have been disabled on the account.  
"This account may not place or cancel orders."| Contact customer support; the account has trading ability disabled.  
"Unsupported order combination"| The `orderType`, `timeInForce`, `stopPrice`, and/or `icebergQty` combination isn't allowed.  
"Order would trigger immediately."| The order's stop price is not valid when compared to the last traded price.  
"Cancel order is invalid. Check origClOrdId and orderId."| No `origClOrdId` or `orderId` was sent in.  
"Order would immediately match and take."| `LIMIT_MAKER` order type would immediately match and trade, and not be a pure maker order.  
"The relationship of the prices for the orders is not correct."| The prices set in the `OCO` is breaking the Price restrictions.   
For reference:   
`BUY` : `LIMIT_MAKER` `price` < Last Traded Price < `stopPrice`   
`SELL` : `LIMIT_MAKER` `price` > Last Traded Price > `stopPrice`  
"OCO orders are not supported for this symbol"| `OCO` is not enabled on the symbol.  
"Quote order qty market orders are not support for this symbol."| `MARKET` orders using the parameter `quoteOrderQty` are not enabled on the symbol.  
"Trailing stop orders are not supported for this symbol."| Orders using `trailingDelta` are not enabled on the symbol.  
"Order cancel-replace is not supported for this symbol."| `POST /api/v3/order/cancelReplace` (REST API) or `order.cancelReplace` (WebSocket API) is not enabled on the symbol.  
"This symbol is not permitted for this account."| Account and symbol do not have the same permissions. (e.g. `SPOT`, `MARGIN`, etc)  
"This symbol is restricted for this account."| Account is unable to trade on that symbol. (e.g. An `ISOLATED_MARGIN` account cannot place `SPOT` orders.)  
"Order was not canceled due to cancel restrictions."| Either `cancelRestrictions` was set to `ONLY_NEW` but the order status was not `NEW`   
or   
`cancelRestrictions` was set to `ONLY_PARTIALLY_FILLED` but the order status was not `PARTIALLY_FILLED`.  
"Rest API trading is not enabled." / "WebSocket API trading is not enabled."| Order is being placed or a server that is not configured to allow access to `TRADE` endpoints.  
"FIX API trading is not enabled.| Order is placed on a FIX server that is not TRADE enabled.  
"Order book liquidity is less than `LOT_SIZE` filter minimum quantity."| Quote quantity market orders cannot be placed when the order book liquidity is less than minimum quantity configured for the `LOT_SIZE` filter.  
"Order book liquidity is less than `MARKET_LOT_SIZE` filter minimum quantity."| Quote quantity market orders cannot be placed when the order book liquidity is less than the minimum quantity for `MARKET_LOT_SIZE` filter.  
"Order book liquidity is less than symbol minimum quantity."| Quote quantity market orders cannot be placed when there are no orders on the book.  
"Order amend (quantity increase) is not supported."| `newQty` must be less than the order quantity.  
"The requested action would change no state; rejecting".| The request sent would not have changed the status quo.  
  
(e.g. `newQty` cannot equal the order quantity.)  
"Pegged orders are not supported for this symbol."| `pegInstructionsAllowed` has not been enabled.  
"This order type may not use pegged price."| You are using parameter `pegPriceType` with an unsupported order type. (e.g. `MARKET`)  
"This price peg cannot be used with this order type."| You are using `pegPriceType`=`MARKET_PEG` for a `LIMIT_MAKER` order.  
"Order book liquidity is too low for this pegged order."| The order book doesn’t have the best price level to peg the price to.  
OPO orders are not supported for this symbol.|   
Order amend (pending OPO order) is not supported.| You cannot amend the pending quantity of an OPO order  
  
## Errors regarding placing orders via cancelReplace[​](/docs/binance-spot-api-docs/errors#errors-regarding-placing-orders-via-cancelreplace "Direct link to Errors regarding placing orders via cancelReplace")

### -2021 Order cancel-replace partially failed[​](/docs/binance-spot-api-docs/errors#-2021-order-cancel-replace-partially-failed "Direct link to -2021 Order cancel-replace partially failed")

  * This code is sent when either the cancellation of the order failed or the new order placement failed but not both.



### -2022 Order cancel-replace failed.[​](/docs/binance-spot-api-docs/errors#-2022-order-cancel-replace-failed "Direct link to -2022 Order cancel-replace failed.")

  * This code is sent when both the cancellation of the order failed and the new order placement failed.



## Filter failures[​](/docs/binance-spot-api-docs/errors#filter-failures "Direct link to Filter failures")

Error message| Description  
---|---  
"Filter failure: PRICE_FILTER"| `price` is too high, too low, and/or not following the tick size rule for the symbol.  
"Filter failure: PERCENT_PRICE"| `price` is X% too high or X% too low from the average weighted price over the last Y minutes.  
"Filter failure: LOT_SIZE"| `quantity` is too high, too low, and/or not following the step size rule for the symbol.  
"Filter failure: MIN_NOTIONAL"| `price` * `quantity` is too low to be a valid order for the symbol.  
"Filter failure: NOTIONAL"| `price` * `quantity` is not within range of the `minNotional` and `maxNotional`  
"Filter failure: ICEBERG_PARTS"| `ICEBERG` order would break into too many parts; icebergQty is too small.  
"Filter failure: MARKET_LOT_SIZE"| `MARKET` order's `quantity` is too high, too low, and/or not following the step size rule for the symbol.  
"Filter failure: MAX_POSITION"| The account's position has reached the maximum defined limit.   
This is composed of the sum of the balance of the base asset, and the sum of the quantity of all open `BUY` orders.  
"Filter failure: MAX_NUM_ORDERS"| Account has too many open orders on the symbol.  
"Filter failure: MAX_NUM_ALGO_ORDERS"| Account has too many open stop loss and/or take profit orders on the symbol.  
"Filter failure: MAX_NUM_ICEBERG_ORDERS"| Account has too many open iceberg orders on the symbol.  
"Filter failure: MAX_NUM_ORDER_AMENDS"| Account has made too many amendments to a single order on the symbol.  
"Filter failure: MAX_NUM_ORDER_LISTS"| Account has too many open order lists on the symbol.  
"Filter failure: TRAILING_DELTA"| `trailingDelta` is not within the defined range of the filter for that order type.  
"Filter failure: EXCHANGE_MAX_NUM_ORDERS"| Account has too many open orders on the exchange.  
"Filter failure: EXCHANGE_MAX_NUM_ALGO_ORDERS"| Account has too many open stop loss and/or take profit orders on the exchange.  
"Filter failure: EXCHANGE_MAX_NUM_ICEBERG_ORDERS"| Account has too many open iceberg orders on the exchange.  
"Filter failure: EXCHANGE_MAX_NUM_ORDER_LISTS"| Account has too many open order lists on the exchange.

---

# 错误代码汇总

币安Rest接口(包括wapi)返回的错误包含两部分，错误码与错误信息. 错误码是大类，一个错误码可能对应多个不同的错误信息。 以下是一个完整错误码实例
    
    
    {  
        "code": -1121,  
        "msg": "Invalid symbol."  
    }  
    

## 10xx - 服务器或网络问题[​](/docs/zh-CN/binance-spot-api-docs/errors#10xx---服务器或网络问题 "10xx - 服务器或网络问题的直接链接")

### -1000 未知错误[​](/docs/zh-CN/binance-spot-api-docs/errors#-1000-未知错误 "-1000 未知错误的直接链接")

  * 未知错误



### -1001 连接断开[​](/docs/zh-CN/binance-spot-api-docs/errors#-1001-连接断开 "-1001 连接断开的直接链接")

  * 通常是一个内部错误，一般重试即可解决。



### -1002 未授权[​](/docs/zh-CN/binance-spot-api-docs/errors#-1002-未授权 "-1002 未授权的直接链接")

  * 请检查你的(API)权限



### -1003 请求过多[​](/docs/zh-CN/binance-spot-api-docs/errors#-1003-请求过多 "-1003 请求过多的直接链接")

  * 排队的请求过多。
  * 请求权重过多； 当前限制是 %s 每 %s 的请求权重。 请使用 Websocket Streams 进行实时更新，以避免轮询API。
  * 请求权重过多； IP被禁止，直到％s。 请使用 Websocket Streams 进行实时更新，以免被禁。



### -1006 非常规响应[​](/docs/zh-CN/binance-spot-api-docs/errors#-1006-非常规响应 "-1006 非常规响应的直接链接")

  * （从内部）接收到了不符合预设格式的消息，下单状态未知。



### -1007 超时[​](/docs/zh-CN/binance-spot-api-docs/errors#-1007-超时 "-1007 超时的直接链接")

  * 后端服务超时，下单状态未知。



### -1008 SERVER_BUSY[​](/docs/zh-CN/binance-spot-api-docs/errors#-1008-server_busy "-1008 SERVER_BUSY的直接链接")

  * 现货交易服务器当前因其他请求而过载。 请在几分钟后重试。



### -1013 消息无效[​](/docs/zh-CN/binance-spot-api-docs/errors#-1013-消息无效 "-1013 消息无效的直接链接")

  * 请求被 API 拒绝 （在这个情况中，此请求并没有到达撮合引擎）。
  * 潜在的错误信息可以在 [订单未能通过过滤器](/docs/zh-CN/binance-spot-api-docs/errors#filter-failures) 或 [下单失败](/docs/zh-CN/binance-spot-api-docs/errors#other-errors) 中找到。



### -1014 不支持的订单参数(组合)[​](/docs/zh-CN/binance-spot-api-docs/errors#-1014-不支持的订单参数组合 "-1014 不支持的订单参数\(组合\)的直接链接")

  * 不支持的订单参数组合.



### -1015 订单太多[​](/docs/zh-CN/binance-spot-api-docs/errors#-1015-订单太多 "-1015 订单太多的直接链接")

  * 下单(撤单)太多



### -1016 服务器下线[​](/docs/zh-CN/binance-spot-api-docs/errors#-1016-服务器下线 "-1016 服务器下线的直接链接")

  * 服务器下线



### -1020 不支持的操作[​](/docs/zh-CN/binance-spot-api-docs/errors#-1020-不支持的操作 "-1020 不支持的操作的直接链接")

  * 不支持的操作



### -1021 时间同步问题[​](/docs/zh-CN/binance-spot-api-docs/errors#-1021-时间同步问题 "-1021 时间同步问题的直接链接")

  * 时延过大，服务器根据接请求中的时间戳判定耗时已经超出了recevWindow。请改善网络条件或者增大recevWindow。
  * 时间偏移过大，服务器根据请求中的时间戳判定客户端时间比服务器时间提前了1秒钟以上。(该参数不可由客户端调节)



### -1022 签名不正确[​](/docs/zh-CN/binance-spot-api-docs/errors#-1022-签名不正确 "-1022 签名不正确的直接链接")

  * 请求中携带的signature与服务器根据规则计算得到的signature不一致。通常是因为客户端代码中使用的apisecret错误。



### -1033 正在使用的 Comp ID[​](/docs/zh-CN/binance-spot-api-docs/errors#-1033-正在使用的-comp-id "-1033 正在使用的 Comp ID的直接链接")

  * `SenderCompId(49)` is currently in use. Concurrent use of the same SenderCompId within one account is not allowed.



### -1034 连接太多[​](/docs/zh-CN/binance-spot-api-docs/errors#-1034-连接太多 "-1034 连接太多的直接链接")

  * Too many concurrent connections; current limit is '%s'.
  * Too many connection attempts for account; current limit is %s per '%s'.
  * Too many connection attempts from IP; current limit is %s



### -1035 会话注销[​](/docs/zh-CN/binance-spot-api-docs/errors#-1035-会话注销 "-1035 会话注销的直接链接")

  * Please send [Logout`<5>`](/docs/zh-CN/binance-spot-api-docs/fix-api#logout) message to close the session.



## 11xx - 请求内容中的问题[​](/docs/zh-CN/binance-spot-api-docs/errors#11xx---请求内容中的问题 "11xx - 请求内容中的问题的直接链接")

### -1100 非法字符[​](/docs/zh-CN/binance-spot-api-docs/errors#-1100-非法字符 "-1100 非法字符的直接链接")

  * Illegal characters found in a parameter.
  * Illegal characters found in parameter '%s'; legal range is '%s'.



### -1101 参数太多[​](/docs/zh-CN/binance-spot-api-docs/errors#-1101-参数太多 "-1101 参数太多的直接链接")

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected '%s' and received '%s'.
  * Duplicate values for a parameter detected.



### -1102 缺少必须参数[​](/docs/zh-CN/binance-spot-api-docs/errors#-1102-缺少必须参数 "-1102 缺少必须参数的直接链接")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
  * Param '%s' or '%s' must be sent, but both were empty/null!
  * Required tag '%s' missing.
  * Field value was empty or malformed.
  * '%s' contains unexpected value. Cannot be greater than %s.



### -1103 无法识别的参数[​](/docs/zh-CN/binance-spot-api-docs/errors#-1103-无法识别的参数 "-1103 无法识别的参数的直接链接")

  * An unknown parameter was sent.
  * Undefined Tag.



### -1104 冗余参数[​](/docs/zh-CN/binance-spot-api-docs/errors#-1104-冗余参数 "-1104 冗余参数的直接链接")

  * Not all sent parameters were read.
  * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.



### -1105 空参数(仅有参数名)[​](/docs/zh-CN/binance-spot-api-docs/errors#-1105-空参数仅有参数名 "-1105 空参数\(仅有参数名\)的直接链接")

  * A parameter was empty.
  * Parameter '%s' was empty.



### -1106 非必需参数[​](/docs/zh-CN/binance-spot-api-docs/errors#-1106-非必需参数 "-1106 非必需参数的直接链接")

  * A parameter was sent when not required.
  * Parameter '%s' sent when not required.
  * A tag '%s' was sent when not required.



### -1108 参数溢出[​](/docs/zh-CN/binance-spot-api-docs/errors#-1108-参数溢出 "-1108 参数溢出的直接链接")

  * Parameter '%s' overflowed.



### -1111 精度过高[​](/docs/zh-CN/binance-spot-api-docs/errors#-1111-精度过高 "-1111 精度过高的直接链接")

  * Parameter '%s' has too much precision.



### -1112 空白的orderbook[​](/docs/zh-CN/binance-spot-api-docs/errors#-1112-空白的orderbook "-1112 空白的orderbook的直接链接")

  * No orders on book for symbol.



### -1114 错误地发送了不需要的TIF参数[​](/docs/zh-CN/binance-spot-api-docs/errors#-1114-错误地发送了不需要的tif参数 "-1114 错误地发送了不需要的TIF参数的直接链接")

  * TimeInForce parameter sent when not required.



### -1115 无效的TIF参数[​](/docs/zh-CN/binance-spot-api-docs/errors#-1115-无效的tif参数 "-1115 无效的TIF参数的直接链接")

  * Invalid timeInForce.



### -1116 无效的订单类型[​](/docs/zh-CN/binance-spot-api-docs/errors#-1116-无效的订单类型 "-1116 无效的订单类型的直接链接")

  * Invalid orderType.



### -1117 无效的订单方向[​](/docs/zh-CN/binance-spot-api-docs/errors#-1117-无效的订单方向 "-1117 无效的订单方向的直接链接")

  * Invalid side.



### -1118 空白的newClientOrderId[​](/docs/zh-CN/binance-spot-api-docs/errors#-1118-空白的newclientorderid "-1118 空白的newClientOrderId的直接链接")

  * New client order ID was empty.



### -1119 空白的originalClientOrderId[​](/docs/zh-CN/binance-spot-api-docs/errors#-1119-空白的originalclientorderid "-1119 空白的originalClientOrderId的直接链接")

  * Original client order ID was empty.



### -1120 无效的间隔(interval)[​](/docs/zh-CN/binance-spot-api-docs/errors#-1120-无效的间隔interval "-1120 无效的间隔\(interval\)的直接链接")

  * Invalid interval.



### -1121 无效的交易对[​](/docs/zh-CN/binance-spot-api-docs/errors#-1121-无效的交易对 "-1121 无效的交易对的直接链接")

  * Invalid symbol.



### -1122 无效的交易对状态[​](/docs/zh-CN/binance-spot-api-docs/errors#-1122-无效的交易对状态 "-1122 无效的交易对状态的直接链接")

  * Invalid symbolStatus.



### -1125 无效的listenKey[​](/docs/zh-CN/binance-spot-api-docs/errors#-1125-无效的listenkey "-1125 无效的listenKey的直接链接")

  * This listenKey does not exist.



### -1127 查询间隔过长[​](/docs/zh-CN/binance-spot-api-docs/errors#-1127-查询间隔过长 "-1127 查询间隔过长的直接链接")

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 无效的可选参数组合[​](/docs/zh-CN/binance-spot-api-docs/errors#-1128-无效的可选参数组合 "-1128 无效的可选参数组合的直接链接")

  * Combination of optional parameters invalid.
  * Combination of optional fields invalid. Recommendation: '%s' and '%s' must both be sent.
  * Fields [%s] must be sent together or omitted entirely.
  * Invalid 'MDEntryType (269)' combination. BID and OFFER must be requested together.
  * Conflicting fields: ['%s'...]



### -1130 无效参数(值)[​](/docs/zh-CN/binance-spot-api-docs/errors#-1130-无效参数值 "-1130 无效参数\(值\)的直接链接")

  * Invalid data sent for a parameter.
  * Data sent for parameter '%s' is not valid.



### -1134 strategyType不符合需求[​](/docs/zh-CN/binance-spot-api-docs/errors#-1134-strategytype不符合需求 "-1134 strategyType不符合需求的直接链接")

  * `strategyType` was less than 1000000.
  * `TargetStrategy (847)` was less than 1000000.



### -1135 无效的JSON[​](/docs/zh-CN/binance-spot-api-docs/errors#-1135-无效的json "-1135 无效的JSON的直接链接")

  * Invalid JSON Request
  * JSON sent for parameter '%s' is not valid



### -1139 无效的Ticker类型[​](/docs/zh-CN/binance-spot-api-docs/errors#-1139-无效的ticker类型 "-1139 无效的Ticker类型的直接链接")

  * Invalid ticker type.



### -1145 无效的取消限制[​](/docs/zh-CN/binance-spot-api-docs/errors#-1145-无效的取消限制 "-1145 无效的取消限制的直接链接")

  * `cancelRestrictions` has to be either `ONLY_NEW` or `ONLY_PARTIALLY_FILLED`.



### -1151 重复的交易对[​](/docs/zh-CN/binance-spot-api-docs/errors#-1151-重复的交易对 "-1151 重复的交易对的直接链接")

  * Symbol is present multiple times in the list.



### -1152 无效的SBE报文头部[​](/docs/zh-CN/binance-spot-api-docs/errors#-1152-无效的sbe报文头部 "-1152 无效的SBE报文头部的直接链接")

  * Invalid `X-MBX-SBE` header; expected `<SCHEMA_ID>:<VERSION>`.
  * Invalid SBE message header.



### -1153 不支持的SCHEMA_ID[​](/docs/zh-CN/binance-spot-api-docs/errors#-1153-不支持的schema_id "-1153 不支持的SCHEMA_ID的直接链接")

  * Unsupported SBE schema ID or version specified in the `X-MBX-SBE` header.
  * Invalid SBE schema ID or version specified.



### -1155 SBE 没有开启[​](/docs/zh-CN/binance-spot-api-docs/errors#-1155-sbe-没有开启 "-1155 SBE 没有开启的直接链接")

  * SBE is not enabled.



### -1158 OCO 订单类型被拒绝[​](/docs/zh-CN/binance-spot-api-docs/errors#-1158-oco-订单类型被拒绝 "-1158 OCO 订单类型被拒绝的直接链接")

  * Order type not supported in OCO.
  * If the order type provided in the `aboveType` and/or `belowType` is not supported.



### -1160 OCO 订单类型的冰山数量参数与 time in force 参数的组合有问题[​](/docs/zh-CN/binance-spot-api-docs/errors#-1160-oco-订单类型的冰山数量参数与-time-in-force-参数的组合有问题 "-1160 OCO 订单类型的冰山数量参数与 time in force 参数的组合有问题的直接链接")

  * Parameter '%s' is not supported if `aboveTimeInForce`/`belowTimeInForce` is not GTC.
  * If the order type for the above or below leg is `STOP_LOSS_LIMIT`, and `icebergQty` is provided for that leg, the `timeInForce` has to be `GTC` else it will throw an error.
  * `TimeInForce (59)` must be `GTC (1)` when `MaxFloor (111)` is used.



### -1161 被弃用的模式[​](/docs/zh-CN/binance-spot-api-docs/errors#-1161-被弃用的模式 "-1161 被弃用的模式的直接链接")

  * Unable to encode the response in SBE schema 'x'. Please use schema 'y' or higher.



### -1165 买入 OCO 限价单必须较低[​](/docs/zh-CN/binance-spot-api-docs/errors#-1165-买入-oco-限价单必须较低 "-1165 买入 OCO 限价单必须较低的直接链接")

  * A limit order in a buy OCO must be below.



### -1166 卖出 OCO 限价单必须较高[​](/docs/zh-CN/binance-spot-api-docs/errors#-1166-卖出-oco-限价单必须较高 "-1166 卖出 OCO 限价单必须较高的直接链接")

  * A limit order in a sell OCO must be above.



### -1168 两个 OCO 订单不能都是是限价单[​](/docs/zh-CN/binance-spot-api-docs/errors#-1168-两个-oco-订单不能都是是限价单 "-1168 两个 OCO 订单不能都是是限价单的直接链接")

  * At least one OCO order must be contingent.



### -1169 Tag无效[​](/docs/zh-CN/binance-spot-api-docs/errors#-1169-tag无效 "-1169 Tag无效的直接链接")

  * Invalid tag number.



### -1170 Tag未被定义[​](/docs/zh-CN/binance-spot-api-docs/errors#-1170-tag未被定义 "-1170 Tag未被定义的直接链接")

  * Tag '%s' not defined for this message type.



### -1171 Tag重复出现[​](/docs/zh-CN/binance-spot-api-docs/errors#-1171-tag重复出现 "-1171 Tag重复出现的直接链接")

  * Tag '%s' appears more than once.



### -1172 Tag顺序错误[​](/docs/zh-CN/binance-spot-api-docs/errors#-1172-tag顺序错误 "-1172 Tag顺序错误的直接链接")

  * Tag '%s' specified out of required order.



### -1173 分组字段顺序错误[​](/docs/zh-CN/binance-spot-api-docs/errors#-1173-分组字段顺序错误 "-1173 分组字段顺序错误的直接链接")

  * Repeating group '%s' fields out of order.



### -1174 无效组件[​](/docs/zh-CN/binance-spot-api-docs/errors#-1174-无效组件 "-1174 无效组件的直接链接")

  * Component '%s' is incorrectly populated on '%s' order. Recommendation: '%s'



### -1175 序列号重置错误[​](/docs/zh-CN/binance-spot-api-docs/errors#-1175-序列号重置错误 "-1175 序列号重置错误的直接链接")

  * Continuation of sequence numbers to new session is currently unsupported. Sequence numbers must be reset for each new session.



### -1176 已登录[​](/docs/zh-CN/binance-spot-api-docs/errors#-1176-已登录 "-1176 已登录的直接链接")

  * [Logon`<A>`](/docs/zh-CN/binance-spot-api-docs/fix-api#logon-main) should only be sent once.



### -1177 错误消息[​](/docs/zh-CN/binance-spot-api-docs/errors#-1177-错误消息 "-1177 错误消息的直接链接")

  * `CheckSum(10)` contains an incorrect value.
  * `BeginString (8)` is not the first tag in a message.
  * `MsgType (35)` is not the third tag in a message.
  * `BodyLength (9)` does not contain the correct byte count.
  * Only printable ASCII characters and SOH (Start of Header) are allowed.
  * Tag specified without a value.
  * Invalid encodingType.



### -1178 Compid错误[​](/docs/zh-CN/binance-spot-api-docs/errors#-1178-compid错误 "-1178 Compid错误的直接链接")

  * `SenderCompId(49)` contains an incorrect value. The SenderCompID value should not change throughout the lifetime of a session.



### -1179 序列号错误[​](/docs/zh-CN/binance-spot-api-docs/errors#-1179-序列号错误 "-1179 序列号错误的直接链接")

  * `MsgSeqNum(34)` contains an unexpected value. Expected: '%d'.



### -1180 登陆消息错误[​](/docs/zh-CN/binance-spot-api-docs/errors#-1180-登陆消息错误 "-1180 登陆消息错误的直接链接")

  * [Logon`<A>`](/docs/zh-CN/binance-spot-api-docs/fix-api#logon-main) must be the first message in the session.



### -1181 消息太多[​](/docs/zh-CN/binance-spot-api-docs/errors#-1181-消息太多 "-1181 消息太多的直接链接")

  * Too many messages; current limit is '%d' messages per '%s'.



### -1182 错误的参数组合[​](/docs/zh-CN/binance-spot-api-docs/errors#-1182-错误的参数组合 "-1182 错误的参数组合的直接链接")

  * Conflicting fields: [%s]



### -1183 不允许在 Drop Copy 会话中使用[​](/docs/zh-CN/binance-spot-api-docs/errors#-1183-不允许在-drop-copy-会话中使用 "-1183 不允许在 Drop Copy 会话中使用的直接链接")

  * Requested operation is not allowed in DropCopy sessions.



### -1184 不允许使用 Drop Copy 会话[​](/docs/zh-CN/binance-spot-api-docs/errors#-1184-不允许使用-drop-copy-会话 "-1184 不允许使用 Drop Copy 会话的直接链接")

  * DropCopy sessions are not supported on this server. Please reconnect to a drop copy server.



### -1185 需要使用 Drop Copy 会话[​](/docs/zh-CN/binance-spot-api-docs/errors#-1185-需要使用-drop-copy-会话 "-1185 需要使用 Drop Copy 会话的直接链接")

  * Only DropCopy sessions are supported on this server. Either reconnect to order entry server or send `DropCopyFlag (9406)` field.



### -1186 不允许在订单输入会话中使用[​](/docs/zh-CN/binance-spot-api-docs/errors#-1186-不允许在订单输入会话中使用 "-1186 不允许在订单输入会话中使用的直接链接")

  * Requested operation is not allowed in order entry sessions.



### -1187 不允许在 Market Data 会话中使用[​](/docs/zh-CN/binance-spot-api-docs/errors#-1187-不允许在-market-data-会话中使用 "-1187 不允许在 Market Data 会话中使用的直接链接")

  * Requested operation is not allowed in market data sessions.



### -1188 组计数中的数字不正确[​](/docs/zh-CN/binance-spot-api-docs/errors#-1188-组计数中的数字不正确 "-1188 组计数中的数字不正确的直接链接")

  * Incorrect NumInGroup count for repeating group '%s'.



### -1189 组中包含重复条目[​](/docs/zh-CN/binance-spot-api-docs/errors#-1189-组中包含重复条目 "-1189 组中包含重复条目的直接链接")

  * Group '%s' contains duplicate entries.



### -1190 无效的请求 ID[​](/docs/zh-CN/binance-spot-api-docs/errors#-1190-无效的请求-id "-1190 无效的请求 ID的直接链接")

  * `MDReqID (262)` contains a subscription request id that is already in use on this connection.
  * `MDReqID (262)` contains an unsubscription request id that does not match any active subscription.



### -1191 订阅数量过多[​](/docs/zh-CN/binance-spot-api-docs/errors#-1191-订阅数量过多 "-1191 订阅数量过多的直接链接")

  * Too many subscriptions. Connection may create up to '%s' subscriptions at a time.
  * Similar subscription is already active on this connection. Symbol='%s', active subscription id: '%s'.



### -1194 错误的时间单位[​](/docs/zh-CN/binance-spot-api-docs/errors#-1194-错误的时间单位 "-1194 错误的时间单位的直接链接")

  * Invalid value for time unit; expected either MICROSECOND or MILLISECOND.



### -1196 买方 `OCO` 单的止损限价单必须是上方（`above`） 订单[​](/docs/zh-CN/binance-spot-api-docs/errors#-1196-买方-oco-单的止损限价单必须是上方above-订单 "-1196-买方-oco-单的止损限价单必须是上方above-订单的直接链接")

  * A stop loss order in a buy OCO must be above.



### -1197 卖方 `OCO` 单的止损限价单必须是下方（`below`） 订单[​](/docs/zh-CN/binance-spot-api-docs/errors#-1197-卖方-oco-单的止损限价单必须是下方below-订单 "-1197-卖方-oco-单的止损限价单必须是下方below-订单的直接链接")

  * A stop loss order in a sell OCO must be below.



### -1198 买方 `OCO` 单的止盈单必须是下方（`below`） 订单[​](/docs/zh-CN/binance-spot-api-docs/errors#-1198-买方-oco-单的止盈单必须是下方below-订单 "-1198-买方-oco-单的止盈单必须是下方below-订单的直接链接")

  * A take profit order in a buy OCO must be below.



### -1199 卖方 `OCO` 单的止盈单必须是上方（`above`） 订单[​](/docs/zh-CN/binance-spot-api-docs/errors#-1199-卖方-oco-单的止盈单必须是上方above-订单 "-1199-卖方-oco-单的止盈单必须是上方above-订单的直接链接")

  * A take profit order in a sell OCO must be above.



### -1210 错误的挂钩订单价格类型[​](/docs/zh-CN/binance-spot-api-docs/errors#-1210-错误的挂钩订单价格类型 "-1210 错误的挂钩订单价格类型的直接链接")

  * Invalid pegPriceType.



### -1211 错误的挂钩订单偏移类型[​](/docs/zh-CN/binance-spot-api-docs/errors#-1211-错误的挂钩订单偏移类型 "-1211 错误的挂钩订单偏移类型的直接链接")

  * Invalid pegOffsetType.



### -1220 交易对与状态不匹配[​](/docs/zh-CN/binance-spot-api-docs/errors#-1220-交易对与状态不匹配 "-1220 交易对与状态不匹配的直接链接")

  * The symbol's status does not match the requested symbolStatus.



### -1221 SBE 消息中包含错误的字段[​](/docs/zh-CN/binance-spot-api-docs/errors#-1221-sbe-消息中包含错误的字段 "-1221 SBE 消息中包含错误的字段的直接链接")

  * Invalid/missing field(s) in SBE message.



### -1222 OPO 的生效订单必须是买单[​](/docs/zh-CN/binance-spot-api-docs/errors#-1222-opo-的生效订单必须是买单 "-1222 OPO 的生效订单必须是买单的直接链接")

  * Working order in an OPO list must be a bid.



### -1223 OPO 的待执行订单必须是卖单[​](/docs/zh-CN/binance-spot-api-docs/errors#-1223-opo-的待执行订单必须是卖单 "-1223 OPO 的待执行订单必须是卖单的直接链接")

  * Pending orders in an OPO list must be asks.



### -1224 生效订单缺少必须的 Tag[​](/docs/zh-CN/binance-spot-api-docs/errors#-1224-生效订单缺少必须的-tag "-1224 生效订单缺少必须的 Tag的直接链接")

  * Working order must include the '{param}' tag.



### -1225 待执行订单包含不需要的 Tag[​](/docs/zh-CN/binance-spot-api-docs/errors#-1225-待执行订单包含不需要的-tag "-1225 待执行订单包含不需要的 Tag的直接链接")

  * Pending orders should not include the '%s' tag.



### -2010 新订单被拒绝[​](/docs/zh-CN/binance-spot-api-docs/errors#-2010-新订单被拒绝 "-2010 新订单被拒绝的直接链接")

  * NEW_ORDER_REJECTED



### -2011 撤销订单被拒绝[​](/docs/zh-CN/binance-spot-api-docs/errors#-2011-撤销订单被拒绝 "-2011 撤销订单被拒绝的直接链接")

  * CANCEL_REJECTED



### -2013 不存在的订单[​](/docs/zh-CN/binance-spot-api-docs/errors#-2013-不存在的订单 "-2013 不存在的订单的直接链接")

  * Order does not exist.



### -2014 API Key格式无效[​](/docs/zh-CN/binance-spot-api-docs/errors#-2014-api-key格式无效 "-2014 API Key格式无效的直接链接")

  * API-key format invalid.



### -2015 API Key权限，例如该Key不存在、请求并非来自允许的IP范围、或者该接口对应权限未开放[​](/docs/zh-CN/binance-spot-api-docs/errors#-2015-api-key权限例如该key不存在请求并非来自允许的ip范围或者该接口对应权限未开放 "-2015 API Key权限，例如该Key不存在、请求并非来自允许的IP范围、或者该接口对应权限未开放的直接链接")

  * Invalid API-key, IP, or permissions for action.



### -2016 非交易窗口[​](/docs/zh-CN/binance-spot-api-docs/errors#-2016-非交易窗口 "-2016 非交易窗口的直接链接")

  * No trading window could be found for the symbol. Try ticker/24hrs instead.



### -2026 交易被归档[​](/docs/zh-CN/binance-spot-api-docs/errors#-2026-交易被归档 "-2026 交易被归档的直接链接")

  * Order was canceled or expired with no executed qty over 90 days ago and has been archived.



### -2035 有效的订阅[​](/docs/zh-CN/binance-spot-api-docs/errors#-2035-有效的订阅 "-2035 有效的订阅的直接链接")

  * User Data Stream subscription already active.



### -2036 非有效的订阅[​](/docs/zh-CN/binance-spot-api-docs/errors#-2036-非有效的订阅 "-2036 非有效的订阅的直接链接")

  * User Data Stream subscription not active.



### -2039 ClientOrderId 无效[​](/docs/zh-CN/binance-spot-api-docs/errors#-2039-clientorderid-无效 "-2039 ClientOrderId 无效的直接链接")

  * Client order ID is not correct for this order ID.



### -2042 最大订阅 ID[​](/docs/zh-CN/binance-spot-api-docs/errors#-2042-最大订阅-id "-2042 最大订阅 ID的直接链接")

  * Maximum subscription ID reached for this connection.



## 消息 -1010 收到了错误消息， -2010 新订单被拒绝，-2011 撤销订单被拒绝，还有 -2038 保留优先权的修改订单被拒绝[​](/docs/zh-CN/binance-spot-api-docs/errors#消息--1010-收到了错误消息--2010-新订单被拒绝-2011-撤销订单被拒绝还有--2038-保留优先权的修改订单被拒绝 "消息 -1010 收到了错误消息， -2010 新订单被拒绝，-2011 撤销订单被拒绝，还有 -2038 保留优先权的修改订单被拒绝的直接链接")

这个错误代码是由撮合引擎抛出的。 下面的消息会指明具体的错误：

错误消息| 描述  
---|---  
"Unknown order sent."| 找不到订单， (根据请求里发送的 `orderId`, `clOrdId`, `origClOrdId`)。  
"Duplicate order sent."| 客户自定义的订单号重复了。  
"Market is closed."| 该交易对交易关闭了。  
"Account has insufficient balance for requested action."| 账户金额不足。  
"Market orders are not supported for this symbol."| 该交易对无法发起市价单。  
"Iceberg orders are not supported for this symbol."| 该交易对无法发起冰山订单。  
"Stop loss orders are not supported for this symbol."| 该交易对无法发起止损单。  
"Stop loss limit orders are not supported for this symbol."| 该交易对无法发起止损限价单。  
"Take profit orders are not supported for this symbol."| 该交易对无法发起止盈单。  
"Take profit limit orders are not supported for this symbol."| 该交易对无法发起止盈限价单。  
"Order amend is not supported for this symbol."| 该交易对无法发起保持优先级的修改订单操作。  
"Price * QTY is zero or less."| 订单金额必须大于0。  
"IcebergQty exceeds QTY."| 冰山订单中小订单的Quantity必须小于总的Quantity。  
"This action is disabled on this account."| 联系客户支持； 该账户已禁用了某些操作。  
"This account may not place or cancel orders."| 联系客户支持： 该账户已被禁用了交易操作。  
"Unsupported order combination"| `orderType`, `timeInForce`, `stopPrice`, `icebergQty` 某些参数取某些值的时候另一些参数必须/不得提供。  
"Order would trigger immediately."| 止盈、止损单必须在未来触发，如果条件太弱现在的市场行情就可以触发（通常是误操作填错了条件），就会报这个错误。  
"Cancel order is invalid. Check origClOrdId and orderId."| 撤销订单必须提供 `origClOrdId` 或者 `orderId` 中的一个。  
"Order would immediately match and take."| `LIMIT_MAKER` 订单如果按照规则会成为Taker，就会报此错。  
"The relationship of the prices for the orders is not correct."| `OCO`订单中设置的价格不符合报价规则：  
请参考以下示例：   
`BUY`：`LIMIT_MAKER` `price` < Last Traded Price < `stopPrice`   
`SELL`：`LIMIT_MAKER` `price` > Last Traded Price > `stopPrice`   
  
"OCO orders are not supported for this symbol"| `OCO`订单不支持该交易对。  
"Quote order qty market orders are not support for this symbol."| 这个交易对，市价单不支持参数 `quoteOrderQty`。  
"Trailing stop orders are not supported for this symbol."| 此symbol不支持 `trailingDelta`。  
"Order cancel-replace is not supported for this symbol."| 此symbol不支持 `POST /api/v3/order/cancelReplace` 或者 `order.cancelReplace` (WebSocket API)。  
"This symbol is not permitted for this account."| 账户和交易对的权限不一致 (比如 `SPOT`, `MARGIN` 等)。  
"This symbol is restricted for this account."| 账户没有权限在此交易对交易 (比如账户只拥有 `ISOLATED_MARGIN`权限，则无法下`SPOT` 订单)。  
"Order was not canceled due to cancel restrictions."| `cancelRestrictions` 设置为 `ONLY_NEW` 但订单状态不是 `NEW`   
或   
`cancelRestrictions` 设置为 `ONLY_PARTIALLY_FILLED` 但订单状态不是 `PARTIALLY_FILLED`。  
"Rest API trading is not enabled." / "WebSocket API trading is not enabled."| 下单时，服务器没有设置为允许访问 `TRADE` 的接口。  
"FIX API trading is not enabled.| 订单放置在未启用 TRADE 的 FIX 服务器上.  
"Order book liquidity is less than `LOT_SIZE` filter minimum quantity."| 当订单簿流动性小于 `LOT_SIZE` 过滤器配置的最小数量时，无法提交包含 `quoteOrderQty` 的市价单。  
"Order book liquidity is less than `MARKET_LOT_SIZE` filter minimum quantity."| 当订单簿流动性小于 `MARKET_LOT_SIZE` 过滤器的最小数量时，无法提交包含 `quoteOrderQty` 的市价单。  
"Order book liquidity is less than symbol minimum quantity."| 当订单簿里没有订单时，无法提交包含 `quoteOrderQty` 的市价单。  
"Order amend (quantity increase) is not supported."| `newQty` 必须小于原来订单的数量 (`quantity`)。  
"The requested action would change no state; rejecting".| 发送的请求将不会改变现状；拒绝。  
  
(比如， `newQty` 不能和原来订单的数量 (`quantity`)是一样的。)  
"Pegged orders are not supported for this symbol."| `pegInstructionsAllowed` 还没有启用。  
"This order type may not use pegged price."| 在不被支持的订单类型上使用 `pegPriceType` 参数 (例如， `MARKET`)。  
"This price peg cannot be used with this order type."| 在 `LIMIT_MAKER` 订单上使用 `pegPriceType`=`MARKET_PEG`。  
"Order book liquidity is too low for this pegged order."| 订单簿中没有最佳价格水平可用以固定价格。  
OPO orders are not supported for this symbol.| 该交易对不支持 OPO 订单  
Order amend (pending OPO order) is not supported.| OPO 订单中的待执行订单无法修改数量  
  
## 有关使用 cancelReplace 下订单的错误[​](/docs/zh-CN/binance-spot-api-docs/errors#有关使用-cancelreplace-下订单的错误 "有关使用 cancelReplace 下订单的错误的直接链接")

### -2021 Order cancel-replace partially failed[​](/docs/zh-CN/binance-spot-api-docs/errors#-2021-order-cancel-replace-partially-failed "-2021 Order cancel-replace partially failed的直接链接")

  * 收到该错误码代表撤单**或者** 下单失败。



### -2022 Order cancel-replace failed.[​](/docs/zh-CN/binance-spot-api-docs/errors#-2022-order-cancel-replace-failed "-2022 Order cancel-replace failed.的直接链接")

  * 收到该错误码代表撤单**和** 下单都失败。



## 订单未能通过过滤器[​](/docs/zh-CN/binance-spot-api-docs/errors#订单未能通过过滤器 "订单未能通过过滤器的直接链接")

错误信息| 描述  
---|---  
"Filter failure: PRICE_FILTER"| 检查价格的上限、下限、步进间隔。  
"Filter failure: PERCENT_PRICE"| 检查订单中价格是否相对于过去N分钟的平均价格变动超过了百分之X。  
"Filter failure: LOT_SIZE"| 检查订单中数量的上限、下线、步进间隔。  
"Filter failure: MIN_NOTIONAL"| `price` * `quantity`，也就是订单金额，是否超过了最小值。  
"Filter failure: NOTIONAL"| `price` * `quantity` 不在 `minNotional` 和 `maxNotional` 的范围内  
"Filter failure: ICEBERG_PARTS"| 冰山订单只能被分割成有限个小订单。  
"Filter failure: MARKET_LOT_SIZE"| 与 `LOT_SIZE` 含义一致，只是对市价单生效。  
"Filter failure: MAX_POSITION"| 账户的仓位已达到定义的最大限额。  
它是由基础资产余额的总和以及所有未平仓买入订单的数量之和组成的。  
"Filter failure: MAX_NUM_ORDERS"| 账户在该交易对下最多挂单数。  
"Filter failure: MAX_NUM_ALGO_ORDERS"| 账户在该交易对下最多的止盈/止损挂单数。  
"Filter failure: MAX_NUM_ICEBERG_ORDERS"| 账户在该交易对下最多的冰山订单数。  
"Filter failure: MAX_NUM_ORDER_AMENDS"| 账户在该交易对下针对单一订单的最多修改次数。  
"Filter failure: MAX_NUM_ORDER_LISTS"| 账户在该交易对下最多的订单列表数。  
"Filter failure: TRAILING_DELTA"| `trailingDelta` 不在该订单类型的筛选器的定义范围内。  
"Filter failure: EXCHANGE_MAX_NUM_ORDERS"| 账户在交易所有太多未结订单。  
"Filter failure: EXCHANGE_MAX_NUM_ALGO_ORDERS"| 账户在交易所有太多的未平仓止损和/或止盈订单。  
"Filter failure: EXCHANGE_MAX_NUM_ICEBERG_ORDERS"| 账户在交易所有太多未平仓的冰山订单。  
"Filter failure: EXCHANGE_MAX_NUM_ORDER_LISTS"| 账户在交易所有太多未平仓的订单列表。