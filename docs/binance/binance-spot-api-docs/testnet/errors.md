---
exchange: binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/testnet/errors
api_type: REST
updated_at: 2026-01-15T23:36:24.938036
---

# Error codes for Binance SPOT Testnet

Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:
    
    
    {  
        "code": -1121,  
        "msg": "Invalid symbol."  
    }  
    

## 10xx - General Server or Network issues[​](/docs/binance-spot-api-docs/testnet/errors#10xx---general-server-or-network-issues "Direct link to 10xx - General Server or Network issues")

### -1000 UNKNOWN[​](/docs/binance-spot-api-docs/testnet/errors#-1000-unknown "Direct link to -1000 UNKNOWN")

  * An unknown error occurred while processing the request.



### -1001 DISCONNECTED[​](/docs/binance-spot-api-docs/testnet/errors#-1001-disconnected "Direct link to -1001 DISCONNECTED")

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED[​](/docs/binance-spot-api-docs/testnet/errors#-1002-unauthorized "Direct link to -1002 UNAUTHORIZED")

  * You are not authorized to execute this request.



### -1003 TOO_MANY_REQUESTS[​](/docs/binance-spot-api-docs/testnet/errors#-1003-too_many_requests "Direct link to -1003 TOO_MANY_REQUESTS")

  * Too many requests queued.
  * Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.
  * Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.



### -1006 UNEXPECTED_RESP[​](/docs/binance-spot-api-docs/testnet/errors#-1006-unexpected_resp "Direct link to -1006 UNEXPECTED_RESP")

  * An unexpected response was received from the message bus. Execution status unknown.



### -1007 TIMEOUT[​](/docs/binance-spot-api-docs/testnet/errors#-1007-timeout "Direct link to -1007 TIMEOUT")

  * Timeout waiting for response from backend server. Send status unknown; execution status unknown.



### -1008 SERVER_BUSY[​](/docs/binance-spot-api-docs/testnet/errors#-1008-server_busy "Direct link to -1008 SERVER_BUSY")

  * Server is currently overloaded with other requests. Please try again in a few minutes.



### -1013 INVALID_MESSAGE[​](/docs/binance-spot-api-docs/testnet/errors#-1013-invalid_message "Direct link to -1013 INVALID_MESSAGE")

  * The request is rejected by the API. (i.e. The request didn't reach the Matching Engine.)
  * Potential error messages can be found in [Filter Failures](/docs/binance-spot-api-docs/testnet/errors#filter-failures) or [Failures during order placement](/docs/binance-spot-api-docs/testnet/errors#other-errors).



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/binance-spot-api-docs/testnet/errors#-1014-unknown_order_composition "Direct link to -1014 UNKNOWN_ORDER_COMPOSITION")

  * Unsupported order combination.



### -1015 TOO_MANY_ORDERS[​](/docs/binance-spot-api-docs/testnet/errors#-1015-too_many_orders "Direct link to -1015 TOO_MANY_ORDERS")

  * Too many new orders.
  * Too many new orders; current limit is %s orders per %s.



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/binance-spot-api-docs/testnet/errors#-1016-service_shutting_down "Direct link to -1016 SERVICE_SHUTTING_DOWN")

  * This service is no longer available.



### -1020 UNSUPPORTED_OPERATION[​](/docs/binance-spot-api-docs/testnet/errors#-1020-unsupported_operation "Direct link to -1020 UNSUPPORTED_OPERATION")

  * This operation is not supported.



### -1021 INVALID_TIMESTAMP[​](/docs/binance-spot-api-docs/testnet/errors#-1021-invalid_timestamp "Direct link to -1021 INVALID_TIMESTAMP")

  * Timestamp for this request is outside of the recvWindow.
  * Timestamp for this request was 1000ms ahead of the server's time.



### -1022 INVALID_SIGNATURE[​](/docs/binance-spot-api-docs/testnet/errors#-1022-invalid_signature "Direct link to -1022 INVALID_SIGNATURE")

  * Signature for this request is not valid.



### -1033 COMP_ID_IN_USE[​](/docs/binance-spot-api-docs/testnet/errors#-1033-comp_id_in_use "Direct link to -1033 COMP_ID_IN_USE")

  * `SenderCompId(49)` is currently in use. Concurrent use of the same SenderCompId within one account is not allowed.



### -1034 TOO_MANY_CONNECTIONS[​](/docs/binance-spot-api-docs/testnet/errors#-1034-too_many_connections "Direct link to -1034 TOO_MANY_CONNECTIONS")

  * Too many concurrent connections; current limit is '%s'.
  * Too many connection attempts for account; current limit is %s per '%s'.
  * Too many connection attempts from IP; current limit is %s per '%s'.



### -1035 LOGGED_OUT[​](/docs/binance-spot-api-docs/testnet/errors#-1035-logged_out "Direct link to -1035 LOGGED_OUT")

  * Please send [Logout`<5>`](/docs/binance-spot-api-docs/testnet/fix-api#logout) message to close the session.



## 11xx - Request issues[​](/docs/binance-spot-api-docs/testnet/errors#11xx---request-issues "Direct link to 11xx - Request issues")

### -1100 ILLEGAL_CHARS[​](/docs/binance-spot-api-docs/testnet/errors#-1100-illegal_chars "Direct link to -1100 ILLEGAL_CHARS")

  * Illegal characters found in a parameter.
  * Illegal characters found in parameter '%s'; legal range is '%s'.



### -1101 TOO_MANY_PARAMETERS[​](/docs/binance-spot-api-docs/testnet/errors#-1101-too_many_parameters "Direct link to -1101 TOO_MANY_PARAMETERS")

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected '%s' and received '%s'.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/binance-spot-api-docs/testnet/errors#-1102-mandatory_param_empty_or_malformed "Direct link to -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
  * Param '%s' or '%s' must be sent, but both were empty/null!
  * Required tag '%s' missing.
  * Field value was empty or malformed.
  * '%s' contains unexpected value. Cannot be greater than %s.



### -1103 UNKNOWN_PARAM[​](/docs/binance-spot-api-docs/testnet/errors#-1103-unknown_param "Direct link to -1103 UNKNOWN_PARAM")

  * An unknown parameter was sent.
  * Undefined Tag.



### -1104 UNREAD_PARAMETERS[​](/docs/binance-spot-api-docs/testnet/errors#-1104-unread_parameters "Direct link to -1104 UNREAD_PARAMETERS")

  * Not all sent parameters were read.
  * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.



### -1105 PARAM_EMPTY[​](/docs/binance-spot-api-docs/testnet/errors#-1105-param_empty "Direct link to -1105 PARAM_EMPTY")

  * A parameter was empty.
  * Parameter '%s' was empty.



### -1106 PARAM_NOT_REQUIRED[​](/docs/binance-spot-api-docs/testnet/errors#-1106-param_not_required "Direct link to -1106 PARAM_NOT_REQUIRED")

  * A parameter was sent when not required.
  * Parameter '%s' sent when not required.
  * A tag '%s' was sent when not required.



### -1108 PARAM_OVERFLOW[​](/docs/binance-spot-api-docs/testnet/errors#-1108-param_overflow "Direct link to -1108 PARAM_OVERFLOW")

  * Parameter '%s' overflowed.



### -1111 BAD_PRECISION[​](/docs/binance-spot-api-docs/testnet/errors#-1111-bad_precision "Direct link to -1111 BAD_PRECISION")

  * Parameter '%s' has too much precision.



### -1112 NO_DEPTH[​](/docs/binance-spot-api-docs/testnet/errors#-1112-no_depth "Direct link to -1112 NO_DEPTH")

  * No orders on book for symbol.



### -1114 TIF_NOT_REQUIRED[​](/docs/binance-spot-api-docs/testnet/errors#-1114-tif_not_required "Direct link to -1114 TIF_NOT_REQUIRED")

  * TimeInForce parameter sent when not required.



### -1115 INVALID_TIF[​](/docs/binance-spot-api-docs/testnet/errors#-1115-invalid_tif "Direct link to -1115 INVALID_TIF")

  * Invalid timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/binance-spot-api-docs/testnet/errors#-1116-invalid_order_type "Direct link to -1116 INVALID_ORDER_TYPE")

  * Invalid orderType.



### -1117 INVALID_SIDE[​](/docs/binance-spot-api-docs/testnet/errors#-1117-invalid_side "Direct link to -1117 INVALID_SIDE")

  * Invalid side.



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/binance-spot-api-docs/testnet/errors#-1118-empty_new_cl_ord_id "Direct link to -1118 EMPTY_NEW_CL_ORD_ID")

  * New client order ID was empty.



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/binance-spot-api-docs/testnet/errors#-1119-empty_org_cl_ord_id "Direct link to -1119 EMPTY_ORG_CL_ORD_ID")

  * Original client order ID was empty.



### -1120 BAD_INTERVAL[​](/docs/binance-spot-api-docs/testnet/errors#-1120-bad_interval "Direct link to -1120 BAD_INTERVAL")

  * Invalid interval.



### -1121 BAD_SYMBOL[​](/docs/binance-spot-api-docs/testnet/errors#-1121-bad_symbol "Direct link to -1121 BAD_SYMBOL")

  * Invalid symbol.



### -1122 INVALID_SYMBOLSTATUS[​](/docs/binance-spot-api-docs/testnet/errors#-1122-invalid_symbolstatus "Direct link to -1122 INVALID_SYMBOLSTATUS")

  * Invalid symbolStatus.



### -1125 INVALID_LISTEN_KEY[​](/docs/binance-spot-api-docs/testnet/errors#-1125-invalid_listen_key "Direct link to -1125 INVALID_LISTEN_KEY")

  * This listenKey does not exist.



### -1127 MORE_THAN_XX_HOURS[​](/docs/binance-spot-api-docs/testnet/errors#-1127-more_than_xx_hours "Direct link to -1127 MORE_THAN_XX_HOURS")

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 OPTIONAL_PARAMS_BAD_COMBO[​](/docs/binance-spot-api-docs/testnet/errors#-1128-optional_params_bad_combo "Direct link to -1128 OPTIONAL_PARAMS_BAD_COMBO")

  * Combination of optional parameters invalid.
  * Combination of optional fields invalid. Recommendation: '%s' and '%s' must both be sent.
  * Fields [%s] must be sent together or omitted entirely.
  * Invalid `MDEntryType (269)` combination. BID and OFFER must be requested together.
  * Conflicting fields: ['%s'...]



### -1130 INVALID_PARAMETER[​](/docs/binance-spot-api-docs/testnet/errors#-1130-invalid_parameter "Direct link to -1130 INVALID_PARAMETER")

  * Invalid data sent for a parameter.
  * Data sent for parameter '%s' is not valid.



### -1134 BAD_STRATEGY_TYPE[​](/docs/binance-spot-api-docs/testnet/errors#-1134-bad_strategy_type "Direct link to -1134 BAD_STRATEGY_TYPE")

  * `strategyType` was less than 1000000.
  * `TargetStrategy (847)` was less than 1000000.



### -1135 INVALID_JSON[​](/docs/binance-spot-api-docs/testnet/errors#-1135-invalid_json "Direct link to -1135 INVALID_JSON")

  * Invalid JSON Request.
  * JSON sent for parameter '%s' is not valid



### -1139 INVALID_TICKER_TYPE[​](/docs/binance-spot-api-docs/testnet/errors#-1139-invalid_ticker_type "Direct link to -1139 INVALID_TICKER_TYPE")

  * Invalid ticker type.



### -1145 INVALID_CANCEL_RESTRICTIONS[​](/docs/binance-spot-api-docs/testnet/errors#-1145-invalid_cancel_restrictions "Direct link to -1145 INVALID_CANCEL_RESTRICTIONS")

  * `cancelRestrictions` has to be either `ONLY_NEW` or `ONLY_PARTIALLY_FILLED`.



### -1151 DUPLICATE_SYMBOLS[​](/docs/binance-spot-api-docs/testnet/errors#-1151-duplicate_symbols "Direct link to -1151 DUPLICATE_SYMBOLS")

  * Symbol is present multiple times in the list.



### -1152 INVALID_SBE_HEADER[​](/docs/binance-spot-api-docs/testnet/errors#-1152-invalid_sbe_header "Direct link to -1152 INVALID_SBE_HEADER")

  * Invalid `X-MBX-SBE` header; expected `<SCHEMA_ID>:<VERSION>`.
  * Invalid SBE message header.



### -1153 UNSUPPORTED_SCHEMA_ID[​](/docs/binance-spot-api-docs/testnet/errors#-1153-unsupported_schema_id "Direct link to -1153 UNSUPPORTED_SCHEMA_ID")

  * Unsupported SBE schema ID or version specified in the `X-MBX-SBE` header.
  * Invalid SBE schema ID or version specified.



### -1155 SBE_DISABLED[​](/docs/binance-spot-api-docs/testnet/errors#-1155-sbe_disabled "Direct link to -1155 SBE_DISABLED")

  * SBE is not enabled.



### -1158 OCO_ORDER_TYPE_REJECTED[​](/docs/binance-spot-api-docs/testnet/errors#-1158-oco_order_type_rejected "Direct link to -1158 OCO_ORDER_TYPE_REJECTED")

  * Order type not supported in OCO.
  * If the order type provided in the `aboveType` and/or `belowType` is not supported.



### -1160 OCO_ICEBERGQTY_TIMEINFORCE[​](/docs/binance-spot-api-docs/testnet/errors#-1160-oco_icebergqty_timeinforce "Direct link to -1160 OCO_ICEBERGQTY_TIMEINFORCE")

  * Parameter '%s' is not supported if `aboveTimeInForce`/`belowTimeInForce` is not GTC.
  * If the order type for the above or below leg is `STOP_LOSS_LIMIT`, and `icebergQty` is provided for that leg, the `timeInForce` has to be `GTC` else it will throw an error.
  * `TimeInForce (59)` must be `GTC (1)` when `MaxFloor (111)` is used.



### -1161 DEPRECATED_SCHEMA[​](/docs/binance-spot-api-docs/testnet/errors#-1161-deprecated_schema "Direct link to -1161 DEPRECATED_SCHEMA")

  * Unable to encode the response in SBE schema 'x'. Please use schema 'y' or higher.



### -1165 BUY_OCO_LIMIT_MUST_BE_BELOW[​](/docs/binance-spot-api-docs/testnet/errors#-1165-buy_oco_limit_must_be_below "Direct link to -1165 BUY_OCO_LIMIT_MUST_BE_BELOW")

  * A limit order in a buy OCO must be below.



### -1166 SELL_OCO_LIMIT_MUST_BE_ABOVE[​](/docs/binance-spot-api-docs/testnet/errors#-1166-sell_oco_limit_must_be_above "Direct link to -1166 SELL_OCO_LIMIT_MUST_BE_ABOVE")

  * A limit order in a sell OCO must be above.



### -1168 BOTH_OCO_ORDERS_CANNOT_BE_LIMIT[​](/docs/binance-spot-api-docs/testnet/errors#-1168-both_oco_orders_cannot_be_limit "Direct link to -1168 BOTH_OCO_ORDERS_CANNOT_BE_LIMIT")

  * At least one OCO order must be contingent.



### -1169 INVALID_TAG_NUMBER[​](/docs/binance-spot-api-docs/testnet/errors#-1169-invalid_tag_number "Direct link to -1169 INVALID_TAG_NUMBER")

  * Invalid tag number.



### -1170 TAG_NOT_DEFINED_IN_MESSAGE[​](/docs/binance-spot-api-docs/testnet/errors#-1170-tag_not_defined_in_message "Direct link to -1170 TAG_NOT_DEFINED_IN_MESSAGE")

  * Tag '%s' not defined for this message type.



### -1171 TAG_APPEARS_MORE_THAN_ONCE[​](/docs/binance-spot-api-docs/testnet/errors#-1171-tag_appears_more_than_once "Direct link to -1171 TAG_APPEARS_MORE_THAN_ONCE")

  * Tag '%s' appears more than once.



### -1172 TAG_OUT_OF_ORDER[​](/docs/binance-spot-api-docs/testnet/errors#-1172-tag_out_of_order "Direct link to -1172 TAG_OUT_OF_ORDER")

  * Tag '%s' specified out of required order.



### -1173 GROUP_FIELDS_OUT_OF_ORDER[​](/docs/binance-spot-api-docs/testnet/errors#-1173-group_fields_out_of_order "Direct link to -1173 GROUP_FIELDS_OUT_OF_ORDER")

  * Repeating group '%s' fields out of order.



### -1174 INVALID_COMPONENT[​](/docs/binance-spot-api-docs/testnet/errors#-1174-invalid_component "Direct link to -1174 INVALID_COMPONENT")

  * Component '%s' is incorrectly populated on '%s' order. Recommendation: '%s'



### -1175 RESET_SEQ_NUM_SUPPORT[​](/docs/binance-spot-api-docs/testnet/errors#-1175-reset_seq_num_support "Direct link to -1175 RESET_SEQ_NUM_SUPPORT")

  * Continuation of sequence numbers to new session is currently unsupported. Sequence numbers must be reset for each new session.



### -1176 ALREADY_LOGGED_IN[​](/docs/binance-spot-api-docs/testnet/errors#-1176-already_logged_in "Direct link to -1176 ALREADY_LOGGED_IN")

  * [Logon`<A>`](/docs/binance-spot-api-docs/testnet/fix-api#logon-main) should only be sent once.



### -1177 GARBLED_MESSAGE[​](/docs/binance-spot-api-docs/testnet/errors#-1177-garbled_message "Direct link to -1177 GARBLED_MESSAGE")

  * `CheckSum(10)` contains an incorrect value.
  * `BeginString (8)` is not the first tag in a message.
  * `MsgType (35)` is not the third tag in a message.
  * `BodyLength (9)` does not contain the correct byte count.
  * Only printable ASCII characters and SOH (Start of Header) are allowed.
  * Tag specified without a value.
  * Invalid encodingType.



### -1178 BAD_SENDER_COMPID[​](/docs/binance-spot-api-docs/testnet/errors#-1178-bad_sender_compid "Direct link to -1178 BAD_SENDER_COMPID")

  * `SenderCompId(49)` contains an incorrect value. The SenderCompID value should not change throughout the lifetime of a session.



### -1179 BAD_SEQ_NUM[​](/docs/binance-spot-api-docs/testnet/errors#-1179-bad_seq_num "Direct link to -1179 BAD_SEQ_NUM")

  * `MsgSeqNum(34)` contains an unexpected value. Expected: '%d'.



### -1180 EXPECTED_LOGON[​](/docs/binance-spot-api-docs/testnet/errors#-1180-expected_logon "Direct link to -1180 EXPECTED_LOGON")

  * [Logon`<A>`](/docs/binance-spot-api-docs/testnet/fix-api#logon-main) must be the first message in the session.



### -1181 TOO_MANY_MESSAGES[​](/docs/binance-spot-api-docs/testnet/errors#-1181-too_many_messages "Direct link to -1181 TOO_MANY_MESSAGES")

  * Too many messages; current limit is '%d' messages per '%s'.



### -1182 PARAMS_BAD_COMBO[​](/docs/binance-spot-api-docs/testnet/errors#-1182-params_bad_combo "Direct link to -1182 PARAMS_BAD_COMBO")

  * Conflicting fields: [%s]



### -1183 NOT_ALLOWED_IN_DROP_COPY_SESSIONS[​](/docs/binance-spot-api-docs/testnet/errors#-1183-not_allowed_in_drop_copy_sessions "Direct link to -1183 NOT_ALLOWED_IN_DROP_COPY_SESSIONS")

  * Requested operation is not allowed in DropCopy sessions.



### -1184 DROP_COPY_SESSION_NOT_ALLOWED[​](/docs/binance-spot-api-docs/testnet/errors#-1184-drop_copy_session_not_allowed "Direct link to -1184 DROP_COPY_SESSION_NOT_ALLOWED")

  * DropCopy sessions are not supported on this server. Please reconnect to a drop copy server.



### -1185 DROP_COPY_SESSION_REQUIRED[​](/docs/binance-spot-api-docs/testnet/errors#-1185-drop_copy_session_required "Direct link to -1185 DROP_COPY_SESSION_REQUIRED")

  * Only DropCopy sessions are supported on this server. Either reconnect to order entry server or send `DropCopyFlag (9406)` field.



### -1186 NOT_ALLOWED_IN_ORDER_ENTRY_SESSIONS[​](/docs/binance-spot-api-docs/testnet/errors#-1186-not_allowed_in_order_entry_sessions "Direct link to -1186 NOT_ALLOWED_IN_ORDER_ENTRY_SESSIONS")

  * Requested operation is not allowed in order entry sessions.



### -1187 NOT_ALLOWED_IN_MARKET_DATA_SESSIONS[​](/docs/binance-spot-api-docs/testnet/errors#-1187-not_allowed_in_market_data_sessions "Direct link to -1187 NOT_ALLOWED_IN_MARKET_DATA_SESSIONS")

  * Requested operation is not allowed in market data sessions.



### -1188 INCORRECT_NUM_IN_GROUP_COUNT[​](/docs/binance-spot-api-docs/testnet/errors#-1188-incorrect_num_in_group_count "Direct link to -1188 INCORRECT_NUM_IN_GROUP_COUNT")

  * Incorrect NumInGroup count for repeating group '%s'.



### -1189 DUPLICATE_ENTRIES_IN_A_GROUP[​](/docs/binance-spot-api-docs/testnet/errors#-1189-duplicate_entries_in_a_group "Direct link to -1189 DUPLICATE_ENTRIES_IN_A_GROUP")

  * Group '%s' contains duplicate entries.



### -1190 INVALID_REQUEST_ID[​](/docs/binance-spot-api-docs/testnet/errors#-1190-invalid_request_id "Direct link to -1190 INVALID_REQUEST_ID")

  * `MDReqID (262)` contains a subscription request id that is already in use on this connection.
  * `MDReqID (262)` contains an unsubscription request id that does not match any active subscription.



### -1191 TOO_MANY_SUBSCRIPTIONS[​](/docs/binance-spot-api-docs/testnet/errors#-1191-too_many_subscriptions "Direct link to -1191 TOO_MANY_SUBSCRIPTIONS")

  * Too many subscriptions. Connection may create up to '%s' subscriptions at a time.
  * Similar subscription is already active on this connection. Symbol='%s', active subscription id: '%s'.



### -1194 INVALID_TIME_UNIT[​](/docs/binance-spot-api-docs/testnet/errors#-1194-invalid_time_unit "Direct link to -1194 INVALID_TIME_UNIT")

  * Invalid value for time unit; expected either MICROSECOND or MILLISECOND.



### -1196 BUY_OCO_STOP_LOSS_MUST_BE_ABOVE[​](/docs/binance-spot-api-docs/testnet/errors#-1196-buy_oco_stop_loss_must_be_above "Direct link to -1196 BUY_OCO_STOP_LOSS_MUST_BE_ABOVE")

  * A stop loss order in a buy OCO must be above.



### -1197 SELL_OCO_STOP_LOSS_MUST_BE_BELOW[​](/docs/binance-spot-api-docs/testnet/errors#-1197-sell_oco_stop_loss_must_be_below "Direct link to -1197 SELL_OCO_STOP_LOSS_MUST_BE_BELOW")

  * A stop loss order in a sell OCO must be below.



### -1198 BUY_OCO_TAKE_PROFIT_MUST_BE_BELOW[​](/docs/binance-spot-api-docs/testnet/errors#-1198-buy_oco_take_profit_must_be_below "Direct link to -1198 BUY_OCO_TAKE_PROFIT_MUST_BE_BELOW")

  * A take profit order in a buy OCO must be below.



### -1199 SELL_OCO_TAKE_PROFIT_MUST_BE_ABOVE[​](/docs/binance-spot-api-docs/testnet/errors#-1199-sell_oco_take_profit_must_be_above "Direct link to -1199 SELL_OCO_TAKE_PROFIT_MUST_BE_ABOVE")

  * A take profit order in a sell OCO must be above.



### -1210 INVALID_PEG_PRICE_TYPE[​](/docs/binance-spot-api-docs/testnet/errors#-1210-invalid_peg_price_type "Direct link to -1210 INVALID_PEG_PRICE_TYPE")

  * Invalid pegPriceType.



### -1211 INVALID_PEG_OFFSET_TYPE[​](/docs/binance-spot-api-docs/testnet/errors#-1211-invalid_peg_offset_type "Direct link to -1211 INVALID_PEG_OFFSET_TYPE")

  * Invalid pegOffsetType.



### -1220 SYMBOL_DOES_NOT_MATCH_STATUS[​](/docs/binance-spot-api-docs/testnet/errors#-1220-symbol_does_not_match_status "Direct link to -1220 SYMBOL_DOES_NOT_MATCH_STATUS")

  * The symbol's status does not match the requested symbolStatus.



### -1221 INVALID_SBE_MESSAGE_FIELD[​](/docs/binance-spot-api-docs/testnet/errors#-1221-invalid_sbe_message_field "Direct link to -1221 INVALID_SBE_MESSAGE_FIELD")

  * Invalid/missing field(s) in SBE message.



### -1222 OPO_WORKING_MUST_BE_BUY[​](/docs/binance-spot-api-docs/testnet/errors#-1222-opo_working_must_be_buy "Direct link to -1222 OPO_WORKING_MUST_BE_BUY")

  * Working order in an OPO list must be a bid.



### -1223 OPO_PENDING_MUST_BE_SELL[​](/docs/binance-spot-api-docs/testnet/errors#-1223-opo_pending_must_be_sell "Direct link to -1223 OPO_PENDING_MUST_BE_SELL")

  * Pending orders in an OPO list must be asks.



### -1224 WORKING_PARAM_REQUIRED[​](/docs/binance-spot-api-docs/testnet/errors#-1224-working_param_required "Direct link to -1224 WORKING_PARAM_REQUIRED")

  * Working order must include the '{param}' tag.



### -1225 PENDING_PARAM_NOT_REQUIRED[​](/docs/binance-spot-api-docs/testnet/errors#-1225-pending_param_not_required "Direct link to -1225 PENDING_PARAM_NOT_REQUIRED")

  * Pending orders should not include the '%s' tag.



### -2010 NEW_ORDER_REJECTED[​](/docs/binance-spot-api-docs/testnet/errors#-2010-new_order_rejected "Direct link to -2010 NEW_ORDER_REJECTED")

  * NEW_ORDER_REJECTED



### -2011 CANCEL_REJECTED[​](/docs/binance-spot-api-docs/testnet/errors#-2011-cancel_rejected "Direct link to -2011 CANCEL_REJECTED")

  * CANCEL_REJECTED



### -2013 NO_SUCH_ORDER[​](/docs/binance-spot-api-docs/testnet/errors#-2013-no_such_order "Direct link to -2013 NO_SUCH_ORDER")

  * Order does not exist.



### -2014 BAD_API_KEY_FMT[​](/docs/binance-spot-api-docs/testnet/errors#-2014-bad_api_key_fmt "Direct link to -2014 BAD_API_KEY_FMT")

  * API-key format invalid.



### -2015 REJECTED_MBX_KEY[​](/docs/binance-spot-api-docs/testnet/errors#-2015-rejected_mbx_key "Direct link to -2015 REJECTED_MBX_KEY")

  * Invalid API-key, IP, or permissions for action.



### -2016 NO_TRADING_WINDOW[​](/docs/binance-spot-api-docs/testnet/errors#-2016-no_trading_window "Direct link to -2016 NO_TRADING_WINDOW")

  * No trading window could be found for the symbol. Try ticker/24hrs instead.



### -2026 ORDER_ARCHIVED[​](/docs/binance-spot-api-docs/testnet/errors#-2026-order_archived "Direct link to -2026 ORDER_ARCHIVED")

  * Order was canceled or expired with no executed qty over 90 days ago and has been archived.



### -2035 SUBSCRIPTION_ACTIVE[​](/docs/binance-spot-api-docs/testnet/errors#-2035-subscription_active "Direct link to -2035 SUBSCRIPTION_ACTIVE")

  * User Data Stream subscription already active.



### -2036 SUBSCRIPTION_INACTIVE[​](/docs/binance-spot-api-docs/testnet/errors#-2036-subscription_inactive "Direct link to -2036 SUBSCRIPTION_INACTIVE")

  * User Data Stream subscription not active.



### -2039 CLIENT_ORDER_ID_INVALID[​](/docs/binance-spot-api-docs/testnet/errors#-2039-client_order_id_invalid "Direct link to -2039 CLIENT_ORDER_ID_INVALID")

  * Client order ID is not correct for this order ID.



### -2042 MAXIMUM_SUBSCRIPTION_IDS[​](/docs/binance-spot-api-docs/testnet/errors#-2042-maximum_subscription_ids "Direct link to -2042 MAXIMUM_SUBSCRIPTION_IDS")

  * Maximum subscription ID reached for this connection.



## Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, -2011 CANCEL_REJECTED, and -2038 ORDER_AMEND_REJECTED[​](/docs/binance-spot-api-docs/testnet/errors#messages-for--1010-error_msg_received--2010-new_order_rejected--2011-cancel_rejected-and--2038-order_amend_rejected "Direct link to Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, -2011 CANCEL_REJECTED, and -2038 ORDER_AMEND_REJECTED")

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
If the `aboveType` is `LIMIT_MAKER` and the `belowType` is either a `STOP_LOSS` or `STOP_LOSS_LIMIT`:   
`abovePrice` > Last Traded Price > `belowStopPrice`.   
If the `aboveType` is `STOP_LOSS` or `STOP_LOSS_LIMIT`, and the `belowType` is `LIMIT_MAKER`:   
`aboveStopPrice` > Last Traded Price > `belowPrice`.  
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
  
## Errors regarding placing orders via cancelReplace[​](/docs/binance-spot-api-docs/testnet/errors#errors-regarding-placing-orders-via-cancelreplace "Direct link to Errors regarding placing orders via cancelReplace")

### -2021 Order cancel-replace partially failed[​](/docs/binance-spot-api-docs/testnet/errors#-2021-order-cancel-replace-partially-failed "Direct link to -2021 Order cancel-replace partially failed")

  * This code is sent when either the cancellation of the order failed or the new order placement failed but not both.



### -2022 Order cancel-replace failed.[​](/docs/binance-spot-api-docs/testnet/errors#-2022-order-cancel-replace-failed "Direct link to -2022 Order cancel-replace failed.")

  * This code is sent when both the cancellation of the order failed and the new order placement failed.



## Filter failures[​](/docs/binance-spot-api-docs/testnet/errors#filter-failures "Direct link to Filter failures")

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

# Error codes for Binance SPOT Testnet

Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:
    
    
    {  
        "code": -1121,  
        "msg": "Invalid symbol."  
    }  
    

## 10xx - General Server or Network issues[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#10xx---general-server-or-network-issues "10xx - General Server or Network issues的直接链接")

### -1000 UNKNOWN[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1000-unknown "-1000 UNKNOWN的直接链接")

  * An unknown error occurred while processing the request.



### -1001 DISCONNECTED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1001-disconnected "-1001 DISCONNECTED的直接链接")

  * Internal error; unable to process your request. Please try again.



### -1002 UNAUTHORIZED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1002-unauthorized "-1002 UNAUTHORIZED的直接链接")

  * You are not authorized to execute this request.



### -1003 TOO_MANY_REQUESTS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1003-too_many_requests "-1003 TOO_MANY_REQUESTS的直接链接")

  * Too many requests queued.
  * Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.
  * Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.



### -1006 UNEXPECTED_RESP[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1006-unexpected_resp "-1006 UNEXPECTED_RESP的直接链接")

  * An unexpected response was received from the message bus. Execution status unknown.



### -1007 TIMEOUT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1007-timeout "-1007 TIMEOUT的直接链接")

  * Timeout waiting for response from backend server. Send status unknown; execution status unknown.



### -1008 SERVER_BUSY[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1008-server_busy "-1008 SERVER_BUSY的直接链接")

  * Server is currently overloaded with other requests. Please try again in a few minutes.



### -1013 INVALID_MESSAGE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1013-invalid_message "-1013 INVALID_MESSAGE的直接链接")

  * The request is rejected by the API. (i.e. The request didn't reach the Matching Engine.)
  * Potential error messages can be found in [Filter Failures](/docs/zh-CN/binance-spot-api-docs/testnet/errors#filter-failures) or [Failures during order placement](/docs/zh-CN/binance-spot-api-docs/testnet/errors#other-errors).



### -1014 UNKNOWN_ORDER_COMPOSITION[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1014-unknown_order_composition "-1014 UNKNOWN_ORDER_COMPOSITION的直接链接")

  * Unsupported order combination.



### -1015 TOO_MANY_ORDERS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1015-too_many_orders "-1015 TOO_MANY_ORDERS的直接链接")

  * Too many new orders.
  * Too many new orders; current limit is %s orders per %s.



### -1016 SERVICE_SHUTTING_DOWN[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1016-service_shutting_down "-1016 SERVICE_SHUTTING_DOWN的直接链接")

  * This service is no longer available.



### -1020 UNSUPPORTED_OPERATION[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1020-unsupported_operation "-1020 UNSUPPORTED_OPERATION的直接链接")

  * This operation is not supported.



### -1021 INVALID_TIMESTAMP[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1021-invalid_timestamp "-1021 INVALID_TIMESTAMP的直接链接")

  * Timestamp for this request is outside of the recvWindow.
  * Timestamp for this request was 1000ms ahead of the server's time.



### -1022 INVALID_SIGNATURE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1022-invalid_signature "-1022 INVALID_SIGNATURE的直接链接")

  * Signature for this request is not valid.



### -1033 COMP_ID_IN_USE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1033-comp_id_in_use "-1033 COMP_ID_IN_USE的直接链接")

  * `SenderCompId(49)` is currently in use. Concurrent use of the same SenderCompId within one account is not allowed.



### -1034 TOO_MANY_CONNECTIONS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1034-too_many_connections "-1034 TOO_MANY_CONNECTIONS的直接链接")

  * Too many concurrent connections; current limit is '%s'.
  * Too many connection attempts for account; current limit is %s per '%s'.
  * Too many connection attempts from IP; current limit is %s per '%s'.



### -1035 LOGGED_OUT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1035-logged_out "-1035 LOGGED_OUT的直接链接")

  * Please send [Logout`<5>`](/docs/zh-CN/binance-spot-api-docs/testnet/fix-api#logout) message to close the session.



## 11xx - Request issues[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#11xx---request-issues "11xx - Request issues的直接链接")

### -1100 ILLEGAL_CHARS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1100-illegal_chars "-1100 ILLEGAL_CHARS的直接链接")

  * Illegal characters found in a parameter.
  * Illegal characters found in parameter '%s'; legal range is '%s'.



### -1101 TOO_MANY_PARAMETERS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1101-too_many_parameters "-1101 TOO_MANY_PARAMETERS的直接链接")

  * Too many parameters sent for this endpoint.
  * Too many parameters; expected '%s' and received '%s'.
  * Duplicate values for a parameter detected.



### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1102-mandatory_param_empty_or_malformed "-1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED的直接链接")

  * A mandatory parameter was not sent, was empty/null, or malformed.
  * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
  * Param '%s' or '%s' must be sent, but both were empty/null!
  * Required tag '%s' missing.
  * Field value was empty or malformed.
  * '%s' contains unexpected value. Cannot be greater than %s.



### -1103 UNKNOWN_PARAM[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1103-unknown_param "-1103 UNKNOWN_PARAM的直接链接")

  * An unknown parameter was sent.
  * Undefined Tag.



### -1104 UNREAD_PARAMETERS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1104-unread_parameters "-1104 UNREAD_PARAMETERS的直接链接")

  * Not all sent parameters were read.
  * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.



### -1105 PARAM_EMPTY[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1105-param_empty "-1105 PARAM_EMPTY的直接链接")

  * A parameter was empty.
  * Parameter '%s' was empty.



### -1106 PARAM_NOT_REQUIRED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1106-param_not_required "-1106 PARAM_NOT_REQUIRED的直接链接")

  * A parameter was sent when not required.
  * Parameter '%s' sent when not required.
  * A tag '%s' was sent when not required.



### -1108 PARAM_OVERFLOW[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1108-param_overflow "-1108 PARAM_OVERFLOW的直接链接")

  * Parameter '%s' overflowed.



### -1111 BAD_PRECISION[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1111-bad_precision "-1111 BAD_PRECISION的直接链接")

  * Parameter '%s' has too much precision.



### -1112 NO_DEPTH[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1112-no_depth "-1112 NO_DEPTH的直接链接")

  * No orders on book for symbol.



### -1114 TIF_NOT_REQUIRED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1114-tif_not_required "-1114 TIF_NOT_REQUIRED的直接链接")

  * TimeInForce parameter sent when not required.



### -1115 INVALID_TIF[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1115-invalid_tif "-1115 INVALID_TIF的直接链接")

  * Invalid timeInForce.



### -1116 INVALID_ORDER_TYPE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1116-invalid_order_type "-1116 INVALID_ORDER_TYPE的直接链接")

  * Invalid orderType.



### -1117 INVALID_SIDE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1117-invalid_side "-1117 INVALID_SIDE的直接链接")

  * Invalid side.



### -1118 EMPTY_NEW_CL_ORD_ID[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1118-empty_new_cl_ord_id "-1118 EMPTY_NEW_CL_ORD_ID的直接链接")

  * New client order ID was empty.



### -1119 EMPTY_ORG_CL_ORD_ID[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1119-empty_org_cl_ord_id "-1119 EMPTY_ORG_CL_ORD_ID的直接链接")

  * Original client order ID was empty.



### -1120 BAD_INTERVAL[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1120-bad_interval "-1120 BAD_INTERVAL的直接链接")

  * Invalid interval.



### -1121 BAD_SYMBOL[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1121-bad_symbol "-1121 BAD_SYMBOL的直接链接")

  * Invalid symbol.



### -1122 INVALID_SYMBOLSTATUS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1122-invalid_symbolstatus "-1122 INVALID_SYMBOLSTATUS的直接链接")

  * Invalid symbolStatus.



### -1125 INVALID_LISTEN_KEY[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1125-invalid_listen_key "-1125 INVALID_LISTEN_KEY的直接链接")

  * This listenKey does not exist.



### -1127 MORE_THAN_XX_HOURS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1127-more_than_xx_hours "-1127 MORE_THAN_XX_HOURS的直接链接")

  * Lookup interval is too big.
  * More than %s hours between startTime and endTime.



### -1128 OPTIONAL_PARAMS_BAD_COMBO[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1128-optional_params_bad_combo "-1128 OPTIONAL_PARAMS_BAD_COMBO的直接链接")

  * Combination of optional parameters invalid.
  * Combination of optional fields invalid. Recommendation: '%s' and '%s' must both be sent.
  * Fields [%s] must be sent together or omitted entirely.
  * Invalid `MDEntryType (269)` combination. BID and OFFER must be requested together.
  * Conflicting fields: ['%s'...]



### -1130 INVALID_PARAMETER[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1130-invalid_parameter "-1130 INVALID_PARAMETER的直接链接")

  * Invalid data sent for a parameter.
  * Data sent for parameter '%s' is not valid.



### -1134 BAD_STRATEGY_TYPE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1134-bad_strategy_type "-1134 BAD_STRATEGY_TYPE的直接链接")

  * `strategyType` was less than 1000000.
  * `TargetStrategy (847)` was less than 1000000.



### -1135 INVALID_JSON[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1135-invalid_json "-1135 INVALID_JSON的直接链接")

  * Invalid JSON Request.
  * JSON sent for parameter '%s' is not valid



### -1139 INVALID_TICKER_TYPE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1139-invalid_ticker_type "-1139 INVALID_TICKER_TYPE的直接链接")

  * Invalid ticker type.



### -1145 INVALID_CANCEL_RESTRICTIONS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1145-invalid_cancel_restrictions "-1145 INVALID_CANCEL_RESTRICTIONS的直接链接")

  * `cancelRestrictions` has to be either `ONLY_NEW` or `ONLY_PARTIALLY_FILLED`.



### -1151 DUPLICATE_SYMBOLS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1151-duplicate_symbols "-1151 DUPLICATE_SYMBOLS的直接链接")

  * Symbol is present multiple times in the list.



### -1152 INVALID_SBE_HEADER[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1152-invalid_sbe_header "-1152 INVALID_SBE_HEADER的直接链接")

  * Invalid `X-MBX-SBE` header; expected `<SCHEMA_ID>:<VERSION>`.
  * Invalid SBE message header.



### -1153 UNSUPPORTED_SCHEMA_ID[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1153-unsupported_schema_id "-1153 UNSUPPORTED_SCHEMA_ID的直接链接")

  * Unsupported SBE schema ID or version specified in the `X-MBX-SBE` header.
  * Invalid SBE schema ID or version specified.



### -1155 SBE_DISABLED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1155-sbe_disabled "-1155 SBE_DISABLED的直接链接")

  * SBE is not enabled.



### -1158 OCO_ORDER_TYPE_REJECTED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1158-oco_order_type_rejected "-1158 OCO_ORDER_TYPE_REJECTED的直接链接")

  * Order type not supported in OCO.
  * If the order type provided in the `aboveType` and/or `belowType` is not supported.



### -1160 OCO_ICEBERGQTY_TIMEINFORCE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1160-oco_icebergqty_timeinforce "-1160 OCO_ICEBERGQTY_TIMEINFORCE的直接链接")

  * Parameter '%s' is not supported if `aboveTimeInForce`/`belowTimeInForce` is not GTC.
  * If the order type for the above or below leg is `STOP_LOSS_LIMIT`, and `icebergQty` is provided for that leg, the `timeInForce` has to be `GTC` else it will throw an error.
  * `TimeInForce (59)` must be `GTC (1)` when `MaxFloor (111)` is used.



### -1161 DEPRECATED_SCHEMA[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1161-deprecated_schema "-1161 DEPRECATED_SCHEMA的直接链接")

  * Unable to encode the response in SBE schema 'x'. Please use schema 'y' or higher.



### -1165 BUY_OCO_LIMIT_MUST_BE_BELOW[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1165-buy_oco_limit_must_be_below "-1165 BUY_OCO_LIMIT_MUST_BE_BELOW的直接链接")

  * A limit order in a buy OCO must be below.



### -1166 SELL_OCO_LIMIT_MUST_BE_ABOVE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1166-sell_oco_limit_must_be_above "-1166 SELL_OCO_LIMIT_MUST_BE_ABOVE的直接链接")

  * A limit order in a sell OCO must be above.



### -1168 BOTH_OCO_ORDERS_CANNOT_BE_LIMIT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1168-both_oco_orders_cannot_be_limit "-1168 BOTH_OCO_ORDERS_CANNOT_BE_LIMIT的直接链接")

  * At least one OCO order must be contingent.



### -1169 INVALID_TAG_NUMBER[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1169-invalid_tag_number "-1169 INVALID_TAG_NUMBER的直接链接")

  * Invalid tag number.



### -1170 TAG_NOT_DEFINED_IN_MESSAGE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1170-tag_not_defined_in_message "-1170 TAG_NOT_DEFINED_IN_MESSAGE的直接链接")

  * Tag '%s' not defined for this message type.



### -1171 TAG_APPEARS_MORE_THAN_ONCE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1171-tag_appears_more_than_once "-1171 TAG_APPEARS_MORE_THAN_ONCE的直接链接")

  * Tag '%s' appears more than once.



### -1172 TAG_OUT_OF_ORDER[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1172-tag_out_of_order "-1172 TAG_OUT_OF_ORDER的直接链接")

  * Tag '%s' specified out of required order.



### -1173 GROUP_FIELDS_OUT_OF_ORDER[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1173-group_fields_out_of_order "-1173 GROUP_FIELDS_OUT_OF_ORDER的直接链接")

  * Repeating group '%s' fields out of order.



### -1174 INVALID_COMPONENT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1174-invalid_component "-1174 INVALID_COMPONENT的直接链接")

  * Component '%s' is incorrectly populated on '%s' order. Recommendation: '%s'



### -1175 RESET_SEQ_NUM_SUPPORT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1175-reset_seq_num_support "-1175 RESET_SEQ_NUM_SUPPORT的直接链接")

  * Continuation of sequence numbers to new session is currently unsupported. Sequence numbers must be reset for each new session.



### -1176 ALREADY_LOGGED_IN[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1176-already_logged_in "-1176 ALREADY_LOGGED_IN的直接链接")

  * [Logon`<A>`](/docs/zh-CN/binance-spot-api-docs/testnet/fix-api#logon-main) should only be sent once.



### -1177 GARBLED_MESSAGE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1177-garbled_message "-1177 GARBLED_MESSAGE的直接链接")

  * `CheckSum(10)` contains an incorrect value.
  * `BeginString (8)` is not the first tag in a message.
  * `MsgType (35)` is not the third tag in a message.
  * `BodyLength (9)` does not contain the correct byte count.
  * Only printable ASCII characters and SOH (Start of Header) are allowed.
  * Tag specified without a value.
  * Invalid encodingType.



### -1178 BAD_SENDER_COMPID[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1178-bad_sender_compid "-1178 BAD_SENDER_COMPID的直接链接")

  * `SenderCompId(49)` contains an incorrect value. The SenderCompID value should not change throughout the lifetime of a session.



### -1179 BAD_SEQ_NUM[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1179-bad_seq_num "-1179 BAD_SEQ_NUM的直接链接")

  * `MsgSeqNum(34)` contains an unexpected value. Expected: '%d'.



### -1180 EXPECTED_LOGON[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1180-expected_logon "-1180 EXPECTED_LOGON的直接链接")

  * [Logon`<A>`](/docs/zh-CN/binance-spot-api-docs/testnet/fix-api#logon-main) must be the first message in the session.



### -1181 TOO_MANY_MESSAGES[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1181-too_many_messages "-1181 TOO_MANY_MESSAGES的直接链接")

  * Too many messages; current limit is '%d' messages per '%s'.



### -1182 PARAMS_BAD_COMBO[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1182-params_bad_combo "-1182 PARAMS_BAD_COMBO的直接链接")

  * Conflicting fields: [%s]



### -1183 NOT_ALLOWED_IN_DROP_COPY_SESSIONS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1183-not_allowed_in_drop_copy_sessions "-1183 NOT_ALLOWED_IN_DROP_COPY_SESSIONS的直接链接")

  * Requested operation is not allowed in DropCopy sessions.



### -1184 DROP_COPY_SESSION_NOT_ALLOWED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1184-drop_copy_session_not_allowed "-1184 DROP_COPY_SESSION_NOT_ALLOWED的直接链接")

  * DropCopy sessions are not supported on this server. Please reconnect to a drop copy server.



### -1185 DROP_COPY_SESSION_REQUIRED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1185-drop_copy_session_required "-1185 DROP_COPY_SESSION_REQUIRED的直接链接")

  * Only DropCopy sessions are supported on this server. Either reconnect to order entry server or send `DropCopyFlag (9406)` field.



### -1186 NOT_ALLOWED_IN_ORDER_ENTRY_SESSIONS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1186-not_allowed_in_order_entry_sessions "-1186 NOT_ALLOWED_IN_ORDER_ENTRY_SESSIONS的直接链接")

  * Requested operation is not allowed in order entry sessions.



### -1187 NOT_ALLOWED_IN_MARKET_DATA_SESSIONS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1187-not_allowed_in_market_data_sessions "-1187 NOT_ALLOWED_IN_MARKET_DATA_SESSIONS的直接链接")

  * Requested operation is not allowed in market data sessions.



### -1188 INCORRECT_NUM_IN_GROUP_COUNT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1188-incorrect_num_in_group_count "-1188 INCORRECT_NUM_IN_GROUP_COUNT的直接链接")

  * Incorrect NumInGroup count for repeating group '%s'.



### -1189 DUPLICATE_ENTRIES_IN_A_GROUP[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1189-duplicate_entries_in_a_group "-1189 DUPLICATE_ENTRIES_IN_A_GROUP的直接链接")

  * Group '%s' contains duplicate entries.



### -1190 INVALID_REQUEST_ID[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1190-invalid_request_id "-1190 INVALID_REQUEST_ID的直接链接")

  * `MDReqID (262)` contains a subscription request id that is already in use on this connection.
  * `MDReqID (262)` contains an unsubscription request id that does not match any active subscription.



### -1191 TOO_MANY_SUBSCRIPTIONS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1191-too_many_subscriptions "-1191 TOO_MANY_SUBSCRIPTIONS的直接链接")

  * Too many subscriptions. Connection may create up to '%s' subscriptions at a time.
  * Similar subscription is already active on this connection. Symbol='%s', active subscription id: '%s'.



### -1194 INVALID_TIME_UNIT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1194-invalid_time_unit "-1194 INVALID_TIME_UNIT的直接链接")

  * Invalid value for time unit; expected either MICROSECOND or MILLISECOND.



### -1196 BUY_OCO_STOP_LOSS_MUST_BE_ABOVE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1196-buy_oco_stop_loss_must_be_above "-1196 BUY_OCO_STOP_LOSS_MUST_BE_ABOVE的直接链接")

  * A stop loss order in a buy OCO must be above.



### -1197 SELL_OCO_STOP_LOSS_MUST_BE_BELOW[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1197-sell_oco_stop_loss_must_be_below "-1197 SELL_OCO_STOP_LOSS_MUST_BE_BELOW的直接链接")

  * A stop loss order in a sell OCO must be below.



### -1198 BUY_OCO_TAKE_PROFIT_MUST_BE_BELOW[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1198-buy_oco_take_profit_must_be_below "-1198 BUY_OCO_TAKE_PROFIT_MUST_BE_BELOW的直接链接")

  * A take profit order in a buy OCO must be below.



### -1199 SELL_OCO_TAKE_PROFIT_MUST_BE_ABOVE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1199-sell_oco_take_profit_must_be_above "-1199 SELL_OCO_TAKE_PROFIT_MUST_BE_ABOVE的直接链接")

  * A take profit order in a sell OCO must be above.



### -1210 INVALID_PEG_PRICE_TYPE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1210-invalid_peg_price_type "-1210 INVALID_PEG_PRICE_TYPE的直接链接")

  * Invalid pegPriceType.



### -1211 INVALID_PEG_OFFSET_TYPE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1211-invalid_peg_offset_type "-1211 INVALID_PEG_OFFSET_TYPE的直接链接")

  * Invalid pegOffsetType.



### -1220 SYMBOL_DOES_NOT_MATCH_STATUS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1220-symbol_does_not_match_status "-1220 SYMBOL_DOES_NOT_MATCH_STATUS的直接链接")

  * The symbol's status does not match the requested symbolStatus.



### -1221 INVALID_SBE_MESSAGE_FIELD[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1221-invalid_sbe_message_field "-1221 INVALID_SBE_MESSAGE_FIELD的直接链接")

  * Invalid/missing field(s) in SBE message.



### -1222 OPO_WORKING_MUST_BE_BUY[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1222-opo_working_must_be_buy "-1222 OPO_WORKING_MUST_BE_BUY的直接链接")

  * Working order in an OPO list must be a bid.



### -1223 OPO_PENDING_MUST_BE_SELL[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1223-opo_pending_must_be_sell "-1223 OPO_PENDING_MUST_BE_SELL的直接链接")

  * Pending orders in an OPO list must be asks.



### -1224 WORKING_PARAM_REQUIRED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1224-working_param_required "-1224 WORKING_PARAM_REQUIRED的直接链接")

  * Working order must include the '{param}' tag.



### -1225 PENDING_PARAM_NOT_REQUIRED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-1225-pending_param_not_required "-1225 PENDING_PARAM_NOT_REQUIRED的直接链接")

  * Pending orders should not include the '%s' tag.



### -2010 NEW_ORDER_REJECTED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2010-new_order_rejected "-2010 NEW_ORDER_REJECTED的直接链接")

  * NEW_ORDER_REJECTED



### -2011 CANCEL_REJECTED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2011-cancel_rejected "-2011 CANCEL_REJECTED的直接链接")

  * CANCEL_REJECTED



### -2013 NO_SUCH_ORDER[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2013-no_such_order "-2013 NO_SUCH_ORDER的直接链接")

  * Order does not exist.



### -2014 BAD_API_KEY_FMT[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2014-bad_api_key_fmt "-2014 BAD_API_KEY_FMT的直接链接")

  * API-key format invalid.



### -2015 REJECTED_MBX_KEY[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2015-rejected_mbx_key "-2015 REJECTED_MBX_KEY的直接链接")

  * Invalid API-key, IP, or permissions for action.



### -2016 NO_TRADING_WINDOW[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2016-no_trading_window "-2016 NO_TRADING_WINDOW的直接链接")

  * No trading window could be found for the symbol. Try ticker/24hrs instead.



### -2026 ORDER_ARCHIVED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2026-order_archived "-2026 ORDER_ARCHIVED的直接链接")

  * Order was canceled or expired with no executed qty over 90 days ago and has been archived.



### -2035 SUBSCRIPTION_ACTIVE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2035-subscription_active "-2035 SUBSCRIPTION_ACTIVE的直接链接")

  * User Data Stream subscription already active.



### -2036 SUBSCRIPTION_INACTIVE[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2036-subscription_inactive "-2036 SUBSCRIPTION_INACTIVE的直接链接")

  * User Data Stream subscription not active.



### -2039 CLIENT_ORDER_ID_INVALID[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2039-client_order_id_invalid "-2039 CLIENT_ORDER_ID_INVALID的直接链接")

  * Client order ID is not correct for this order ID.



### -2042 MAXIMUM_SUBSCRIPTION_IDS[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2042-maximum_subscription_ids "-2042 MAXIMUM_SUBSCRIPTION_IDS的直接链接")

  * Maximum subscription ID reached for this connection.



## Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, -2011 CANCEL_REJECTED, and -2038 ORDER_AMEND_REJECTED[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#messages-for--1010-error_msg_received--2010-new_order_rejected--2011-cancel_rejected-and--2038-order_amend_rejected "Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, -2011 CANCEL_REJECTED, and -2038 ORDER_AMEND_REJECTED的直接链接")

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
If the `aboveType` is `LIMIT_MAKER` and the `belowType` is either a `STOP_LOSS` or `STOP_LOSS_LIMIT`:   
`abovePrice` > Last Traded Price > `belowStopPrice`.   
If the `aboveType` is `STOP_LOSS` or `STOP_LOSS_LIMIT`, and the `belowType` is `LIMIT_MAKER`:   
`aboveStopPrice` > Last Traded Price > `belowPrice`.  
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
  
## Errors regarding placing orders via cancelReplace[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#errors-regarding-placing-orders-via-cancelreplace "Errors regarding placing orders via cancelReplace的直接链接")

### -2021 Order cancel-replace partially failed[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2021-order-cancel-replace-partially-failed "-2021 Order cancel-replace partially failed的直接链接")

  * This code is sent when either the cancellation of the order failed or the new order placement failed but not both.



### -2022 Order cancel-replace failed.[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#-2022-order-cancel-replace-failed "-2022 Order cancel-replace failed.的直接链接")

  * This code is sent when both the cancellation of the order failed and the new order placement failed.



## Filter failures[​](/docs/zh-CN/binance-spot-api-docs/testnet/errors#filter-failures "Filter failures的直接链接")

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