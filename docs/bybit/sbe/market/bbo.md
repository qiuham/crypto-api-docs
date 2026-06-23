---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/sbe/market/bbo
api_type: Market Data
updated_at: 2026-06-23 19:18:49.898433
---

# Fast Order Response SBE

MMWS only

This channel is available **only** via your **dedicated Market Maker WebSocket (MMWS)** host. It is not accessible from standard WebSocket endpoints.

## Overview

The Fast Order SBE channel provides ultra-low-latency order push updates for HFT clients through the Market Maker WebSocket (MMWS). It delivers binary-encoded SBE messages directly from the matching engine for fast order submission, amendment, and cancellation acknowledgements.

This channel is designed for speed and efficiency. For details on which events trigger a push, see the Push Logic section below.

## Release Schedule

Product| Testnet| Mainnet  
---|---|---  
Spot| May 27, 2026| June 23, 2026  
Futures (linear & inverse)| June 10, 2026| July 9, 2026  
Options| June 16, 2026| July 21, 2026  
  
## Connection

Environment| URL  
---|---  
Testnet| `wss://stream-testnet.bybits.org/v5/private-sbe`  
Mainnet| `wss://<your-dedicated-MMWS-host>.bybit-aws.com/v5/private-sbe`  
  
  * SBE messages are sent as **binary frames** (`opcode = 2`).
  * Control frames (auth, ping/pong, subscribe/unsubscribe) use the standard **Bybit V5 API JSON format**.



## Authentication

Authentication is required immediately after establishing a connection.

### Auth Request
    
    
    {  
        "req_id": "10001",  
        "op": "auth",  
        "args": [  
            "api_key",  
            1662350400000,  
            "signature"  
        ]  
    }  
    

Field| Description  
---|---  
req_id| Optional client identifier  
args[1]| Timestamp — must be greater than current time  
args[2]| Generated using the [Bybit API signing algorithm](/docs/v5/guide#authentication)  
  
### Auth Success Response
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "op": "auth",  
        "conn_id": "cejreaspqfh3sjdnldmg-p"  
    }  
    

## Heartbeat

### Send Ping
    
    
    {"req_id": "100001", "op": "ping"}  
    

### Receive Pong
    
    
    {  
        "success": true,  
        "ret_msg": "pong",  
        "conn_id": "465772b1-7630-4fdc-a492-e003e6f0f260",  
        "req_id": "100001",  
        "op": "ping"  
    }  
    

## Subscription

### Available Topics

Topic| Description  
---|---  
`order.sbe.resp.spot`| Spot fast order response  
`order.sbe.resp.linear`| Linear (USDT/USDC) fast order response  
`order.sbe.resp.inverse`| Inverse fast order response  
`order.sbe.resp.option`| Options fast order response  
  
### Subscribe Example
    
    
    {  
        "op": "subscribe",  
        "args": ["order.sbe.resp.linear", "order.sbe.resp.spot", "order.sbe.resp.option"]  
    }  
    

### Subscription Acknowledgment
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "conn_id": "d30fdpbboasp1pjbe7r0",  
        "req_id": "abc123",  
        "op": "subscribe"  
    }  
    

## Push Logic

`fast.resp.order` messages are actively pushed to clients when the order is initiated by the user (active trading actions: place, amend, cancel).

info

Upon channel restart or re-subscription, pushes start from the latest matching event — the focus is **speed** , not backfill.

Scenario / Event| Push via Fast Order Channel| Notes  
---|---|---  
Maker order new (accepted / ack)| ✅ Yes| All active actions initiated by client (place / amend / cancel / reject).  
Maker order filled / partial filled| ✅ Yes| All active actions initiated by client (place / amend / cancel / reject).  
Taker order (active side)| ✅ Yes| All active actions initiated by client (place / amend / cancel / reject).  
COT (CloseOnTrigger) order| ✅ Yes (for triggered order)| Triggered COT order acts like a new taker order; if it opens opposite side, `orderLinkId=""`.  
RO / ReduceOnly order| ✅ Yes| Normal push; if rejected due to cost or position box, `rejectReason` populated.  
Condition / TP-SL triggered order| ✅ Yes| Once condition triggers and order becomes active, it's pushed. `orderLinkId=""` (empty).  
DCP (Disconnect All Protection)| ✅ Yes| Pushes when DCP forcibly cancels orders on disconnect.  
SMP cancel-taker / Cancel Both (Self Match Protection)| ✅ Yes| Both taker/maker side cancellations will be pushed.  
SMP cancel-maker| ✅ Yes| Both taker/maker side cancellations will be pushed.  
MMP (Market Maker Protection)| ✅ Yes| MMP trigger cancels also pushed in fast order channel.  
Delist / Contract expiry / Option delivery| ❌ No| System-initiated close; no fast order push.  
Order reject (matching / validation reject)| ✅ Yes| Pushed immediately with `rejectReason`.  
Amend success / reject| ✅ Yes| Active amend ack / reject are pushed.  
Cancel success / reject| ✅ Yes| Active cancel ack / reject are pushed.  
  
## Differences from Standard WebSocket Order Channel

The table below highlights behavioral differences between the Fast Order SBE channel (`order.sbe.resp.*`) and the standard private WebSocket [Order](/docs/v5/websocket/private/order) channel.

Scenario| Fast Order Channel| Standard WS Order Channel| Notes  
---|---|---|---  
Conditional order — place / amend / cancel (before trigger)| ❌ No push| ✅ Push| Conditional orders are not sent to the matching engine before being triggered; the matching engine has no pre-trigger order state to push.  
TP/SL order — place / amend / cancel (before trigger)| ❌ No push| ✅ Push| Same reason as above.  
Trailing stop order — place / amend / cancel (before trigger)| ❌ No push| ✅ Push| Same reason as above.  
Position liquidation order| ❌ No push| ✅ Push| Note: liquidation-triggered cancellations are consistent between both channels.  
Contract delist cancellation| ❌ No push| ✅ Push| Delist cancellations are handled internally and not forwarded to the matching engine.  
Amend / cancel an order that was fully filled before the request arrived| Fast Order: `orderStatus=Rejected`| Standard WS: `orderStatus=Filled`| e.g. qty=10, amend to 12, but 10 lots already filled — Fast Order returns the amend/cancel as `Rejected`; Standard WS returns `Filled`.  
Normal place / amend / cancel — `leavesValue` field| No value (`0`)| Has value| Fast Order always returns `0` for `leavesValue` on non-spot-market-buy-order-by-value orders.  
Pre-market call auction — cancel rejected| `orderStatus=Rejected`| `orderStatus=New`| During the pre-market call auction phase, cancel requests are rejected; Fast Order reflects `Rejected` while Standard WS reflects `New`.  
  
## OrderLinkId Behavior by Version

Scenario| 2026 Testnet / Mainnet| Notes  
---|---|---  
Active new order (user-initiated)| ✅ Present| Client-initiated place includes user's `orderLinkId`.  
Amend / Cancel (user-initiated)| ✅ Present| Client-initiated place includes user's `orderLinkId`.  
Maker→Taker transition (e.g. price amend crosses book)| ✅ Present| Client-initiated place includes user's `orderLinkId`.  
Active new conditional order (user-initiated)| ✅ Present| Client-initiated place includes user's `orderLinkId`.  
Position set trading stop order| ❌ Empty| System-created, no `orderLinkId`.  
  
## Message Structure (SBE)

`templateId = 21000` (`FastOrderResp`)

### Message Header (8 bytes)

Field| Type| Size (bytes)| Description  
---|---|---|---  
blockLength| uint16| 2| Message body length  
templateId| uint16| 2| Fixed = `21000`  
schemaId| uint16| 2| Fixed = `1`  
version| uint16| 2| Fixed = `0`  
  
### Message Body

ID| Field| Type| Description  
---|---|---|---  
1| category| uint8| `1`=spot, `2`=linear, `3`=inverse, `4`=option  
2| side| uint8| `1`=Buy, `2`=Sell  
3| orderStatus| uint8| Order state enum. `0`=Others, `4`=PartiallyFilledAndCancelled, `5`=Rejected, `6`=New, `7`=Cancelled, `8`=PartiallyFilled, `9`=Filled  
4| priceExponent| int8| Decimal places for price. `price = mantissa / 10^priceExponent`  
5| sizeExponent| int8| Decimal places for size  
6| valueExponent| int8| Decimal places for value  
7| rejectReason| uint16| `0` if N/A. See rejectReason mapping  
8| price| int64| Price mantissa (apply `priceExponent`)  
9| leavesQty| int64| Remaining quantity mantissa (apply `sizeExponent`)  
10| leavesValue| int64| Spot market buy only; otherwise `0` (apply `valueExponent`)  
11| creationTime| int64| Order creation timestamp in Fast Order channel (microseconds)  
12| updatedTime| int64| Matching timestamp (microseconds)  
13| seq| int64| Cross sequence ID  
14| symbolID| int32| Symbol ID  
100| orderId| varString8| Order ID (UUID)  
101| orderLinkId| varString8| Optional; present for user-initiated orders  
  
## rejectReason Mapping

Code| Name  
---|---  
0| EC_NoError  
1| EC_Others  
2| EC_UnknownMessageType  
3| EC_MissingClOrdID  
4| EC_MissingOrigClOrdID  
5| EC_ClOrdIDOrigClOrdIDAreTheSame  
6| EC_DuplicatedClOrdID  
7| EC_OrigClOrdIDDoesNotExist  
8| EC_TooLateToCancel  
9| EC_UnknownOrderType  
10| EC_UnknownSide  
11| EC_UnknownTimeInForce  
12| EC_WronglyRouted  
13| EC_MarketOrderPriceIsNotZero  
14| EC_LimitOrderInvalidPrice  
15| EC_NoEnoughQtyToFill  
16| EC_NoImmediateQtyToFill  
17| EC_QtyCannotBeZero  
18| EC_PerCancelRequest  
19| EC_MarketOrderCannotBePostOnly  
20| EC_PostOnlyWillTakeLiquidity  
21| EC_CancelReplaceOrder  
22| EC_InvalidSymbolStatus  
23| EC_MarketOrderNoSupportTIF  
24| EC_ReachMaxTradeNum  
25| EC_InvalidPriceScale  
26| EC_BitIndexInvalid  
27| EC_StopBySelfMatch  
28| EC_BySelfMatch  
29| EC_InvalidSmpType  
30| EC_CancelByMMP  
31| EC_InCallAuctionStatus  
34| EC_InvalidUserType  
35| EC_InvalidMirrorOid  
36| EC_InvalidMirrorUid  
37| EC_SymbolNotExist  
38| EC_CancelNoActiveOrders  
39| EC_MissingUID  
100| EC_EcInvalidQty  
101| EC_InvalidAmount  
102| EC_LoadOrderCancel  
103| EC_CancelForNoFullFill  
104| EC_MarketQuoteNoSuppSell  
105| EC_DisorderOrderID  
106| EC_InvalidBaseValue  
107| EC_LoadOrderCanMatch  
108| EC_SecurityStatusFail  
110| EC_ReachRiskPriceLimit  
111| EC_OrderNotExist  
112| EC_CancelByOrderValueZero  
113| EC_CancelByMatchValueZero  
200| EC_ReachMarketPriceLimit  
  
## SBE XML Template (Fast Order Response)
    
    
    <?xml version="1.0" encoding="UTF-8"?>  
    <sbe:messageSchema xmlns:sbe="http://fixprotocol.io/2016/sbe"  
                       xmlns:mbx="https://bybit-exchange.github.io/docs/v5/intro"  
                       package="order.fast.sbe"  
                       id="1"  
                       version="0"  
                       semanticVersion="1.0.0"  
                       description="Bybit fast order response SBE schema"  
                       byteOrder="littleEndian"  
                       headerType="messageHeader">  
      <types>  
        <composite name="messageHeader" description="Template ID and length of message root">  
          <type name="blockLength" primitiveType="uint16"/>  
          <type name="templateId" primitiveType="uint16"/>  
          <type name="schemaId" primitiveType="uint16"/>  
          <type name="version" primitiveType="uint16"/>  
        </composite>  
        <composite name="varString8" description="Variable length UTF-8 string">  
          <type name="length" primitiveType="uint8"/>  
          <type name="varData" length="0" primitiveType="uint8" semanticType="String" characterEncoding="UTF-8"/>  
        </composite>  
      </types>  
      <!-- Fast order response: active place/cancel/amend acknowledgements -->  
      <sbe:message name="FastOrderResp" id="21000">  
        <!-- Routing / classification -->  
        <field id="1" name="category" type="uint8" description="1=spot, 2=linear, 3=inverse, 4=option"/>  
        <!-- Side / status / rejection -->  
        <field id="2" name="side" type="uint8" description="1=Buy, 2=Sell"/>  
        <field id="3" name="orderStatus" type="uint8" description="Order state enum"/>  
        <!-- Price / size (mantissas) with exponents -->  
        <field id="4" name="priceExponent" type="int8" description="Decimal places for price"/>  
        <field id="5" name="sizeExponent" type="int8" description="Decimal places for size"/>  
        <field id="6" name="valueExponent" type="int8" description="Decimal places for value"/>  
        <field id="7" name="rejectReason" type="uint16" description="0 if N/A"/>  
        <field id="8" name="price" type="int64" mbx:exponent="priceExponent" description="Price mantissa"/>  
        <field id="9" name="leavesQty" type="int64" mbx:exponent="sizeExponent" description="Remaining quantity mantissa"/>  
        <field id="10" name="leavesValue" type="int64" mbx:exponent="valueExponent" description="Spot market buy only; otherwise 0"/>  
        <!-- Timing -->  
        <field id="11" name="creationTime" type="int64" description="Order creation timestamp in Fast order channel(microseconds)"/>  
        <field id="12" name="updatedTime" type="int64" description="Matching timestamp (microseconds)"/>  
        <field id="13" name="seq" type="int64" description="Cross sequence ID"/>  
        <!-- SymbolID -->  
        <field id="14" name="symbolID" type="int32" description="Symbol ID"/>  
        <!-- Order identifiers -->  
        <data id="100" name="orderId" type="varString8" description="Order ID"/>  
        <data id="101" name="orderLinkId" type="varString8" description="Optional; present for user-initiated orders"/>  
      </sbe:message>  
    </sbe:messageSchema>  
    

## Code Example

  * Go
  * Python


    
    
    package main  
      
    import (  
        "context"  
        "crypto/hmac"  
        "crypto/sha256"  
        "encoding/binary"  
        "encoding/hex"  
        "encoding/json"  
        "flag"  
        "fmt"  
        "log"  
        "math"  
        "os"  
        "os/signal"  
        "time"  
      
        "github.com/gorilla/websocket"  
    )  
      
    // ---------- Config ----------  
      
    const (  
        MMWSURLTestnetBybits = "wss://stream-testnet.bybits.org/v5/private-sbe"  
        MMWSURLTestnetBybit  = "wss://stream-testnet.bybit.com/v5/private-sbe"  
        MMWSURLMainnet       = "wss://stream.bybit.com/v5/private-sbe"  
    )  
      
    // TODO: fill in your real keys  
    const (  
        APIKey    = "YOUR_API_KEY"  
        APISecret = "YOUR_API_SECRET"  
    )  
      
    var subTopics = []string{  
        "order.sbe.resp.spot",  
    }  
      
    // ---------- SBE helpers ----------  
      
    func readU8(buf []byte, off *int) (uint8, error) {  
        if *off+1 > len(buf) {  
            return 0, fmt.Errorf("readU8: out of range")  
        }  
        v := buf[*off]  
        *off++  
        return v, nil  
    }  
      
    func readI8(buf []byte, off *int) (int8, error) {  
        if *off+1 > len(buf) {  
            return 0, fmt.Errorf("readI8: out of range")  
        }  
        v := int8(buf[*off])  
        *off++  
        return v, nil  
    }  
      
    func readU16LE(buf []byte, off *int) (uint16, error) {  
        if *off+2 > len(buf) {  
            return 0, fmt.Errorf("readU16LE: out of range")  
        }  
        v := binary.LittleEndian.Uint16(buf[*off : *off+2])  
        *off += 2  
        return v, nil  
    }  
      
    func readI32LE(buf []byte, off *int) (int32, error) {  
        if *off+4 > len(buf) {  
            return 0, fmt.Errorf("readI32LE: out of range")  
        }  
        v := int32(binary.LittleEndian.Uint32(buf[*off : *off+4]))  
        *off += 4  
        return v, nil  
    }  
      
    func readI64LE(buf []byte, off *int) (int64, error) {  
        if *off+8 > len(buf) {  
            return 0, fmt.Errorf("readI64LE: out of range")  
        }  
        v := int64(binary.LittleEndian.Uint64(buf[*off : *off+8]))  
        *off += 8  
        return v, nil  
    }  
      
    func readVarString8(buf []byte, off *int) (string, error) {  
        if *off+1 > len(buf) {  
            return "", fmt.Errorf("readVarString8: no length byte")  
        }  
        ln := int(buf[*off])  
        *off++  
        if ln == 0 {  
            return "", nil  
        }  
        if *off+ln > len(buf) {  
            return "", fmt.Errorf("readVarString8: length out of range")  
        }  
        s := string(buf[*off : *off+ln])  
        *off += ln  
        return s, nil  
    }  
      
    func applyExp(mantissa int64, exp int8) float64 {  
        e := int(exp)  
        if e >= 0 {  
            return float64(mantissa) / math.Pow10(e)  
        }  
        return float64(mantissa) * math.Pow10(-e)  
    }  
      
    // ---------- Fast Order SBE decode ----------  
      
    type FastOrderSBEResp struct {  
        SBEHeader struct {  
            BlockLength uint16 `json:"blockLength"`  
            TemplateID  uint16 `json:"templateId"`  
            SchemaID    uint16 `json:"schemaId"`  
            Version     uint16 `json:"version"`  
        } `json:"_sbe_header"`  
      
        Category      uint8  `json:"category"`  
        Side          uint8  `json:"side"`  
        OrderStatus   uint8  `json:"orderStatus"`  
        PriceExponent int8   `json:"priceExponent"`  
        SizeExponent  int8   `json:"sizeExponent"`  
        ValExponent   int8   `json:"valueExponent"`  
        RejectReason  uint16 `json:"rejectReason"`  
      
        PriceMantissa       int64 `json:"priceMantissa"`  
        LeavesQtyMantissa   int64 `json:"leavesQtyMantissa"`  
        LeavesValueMantissa int64 `json:"leavesValueMantissa"`  
      
        CreationTime int64 `json:"creationTime"`  
        UpdatedTime  int64 `json:"updatedTime"`  
        Seq          int64 `json:"seq"`  
      
        SymbolID    int32  `json:"symbolID"`  
        OrderID     string `json:"orderId"`  
        OrderLinkID string `json:"orderLinkId"`  
      
        Price       float64 `json:"price"`  
        LeavesQty   float64 `json:"leavesQty"`  
        LeavesValue float64 `json:"leavesValue"`  
      
        RawOffsetEnd int `json:"_raw_offset_end"`  
    }  
      
    func decodeFastOrderResp(payload []byte, debug bool) (*FastOrderSBEResp, error) {  
        if len(payload) < 8 {  
            return nil, fmt.Errorf("payload too short for SBE header")  
        }  
        off := 0  
        blockLen := binary.LittleEndian.Uint16(payload[off : off+2])  
        templateID := binary.LittleEndian.Uint16(payload[off+2 : off+4])  
        schemaID := binary.LittleEndian.Uint16(payload[off+4 : off+6])  
        version := binary.LittleEndian.Uint16(payload[off+6 : off+8])  
        off += 8  
      
        if debug {  
            log.Printf("HEADER: block_len=%d, template_id=%d, schema_id=%d, version=%d",  
                blockLen, templateID, schemaID, version)  
        }  
      
        if templateID != 21000 {  
            return nil, fmt.Errorf("unexpected templateId: %d", templateID)  
        }  
      
        var err error  
        resp := &FastOrderSBEResp{}  
        resp.SBEHeader.BlockLength = blockLen  
        resp.SBEHeader.TemplateID = templateID  
        resp.SBEHeader.SchemaID = schemaID  
        resp.SBEHeader.Version = version  
      
        if resp.Category, err = readU8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.Side, err = readU8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.OrderStatus, err = readU8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.PriceExponent, err = readI8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.SizeExponent, err = readI8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.ValExponent, err = readI8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.RejectReason, err = readU16LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.PriceMantissa, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.LeavesQtyMantissa, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.LeavesValueMantissa, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.CreationTime, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.UpdatedTime, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.Seq, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.SymbolID, err = readI32LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.OrderID, err = readVarString8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.OrderLinkID, err = readVarString8(payload, &off); err != nil {  
            return nil, err  
        }  
      
        resp.Price = applyExp(resp.PriceMantissa, resp.PriceExponent)  
        resp.LeavesQty = applyExp(resp.LeavesQtyMantissa, resp.SizeExponent)  
        resp.LeavesValue = applyExp(resp.LeavesValueMantissa, resp.ValExponent)  
        resp.RawOffsetEnd = off  
      
        return resp, nil  
    }  
      
    // ---------- WebSocket helpers ----------  
      
    func sendJSON(conn *websocket.Conn, v any) error {  
        data, err := json.Marshal(v)  
        if err != nil {  
            return err  
        }  
        return conn.WriteMessage(websocket.TextMessage, data)  
    }  
      
    func signAuth(secret, value string) string {  
        h := hmac.New(sha256.New, []byte(secret))  
        h.Write([]byte(value))  
        return hex.EncodeToString(h.Sum(nil))  
    }  
      
    func heartbeat(ctx context.Context, conn *websocket.Conn) {  
        ticker := time.NewTicker(10 * time.Second)  
        defer ticker.Stop()  
        for {  
            select {  
            case <-ctx.Done():  
                return  
            case <-ticker.C:  
                reqID := fmt.Sprintf("%d", time.Now().UnixMilli())  
                err := sendJSON(conn, map[string]any{  
                    "req_id": reqID,  
                    "op":     "ping",  
                })  
                if err != nil {  
                    log.Printf("[heartbeat] error sending ping: %v", err)  
                    return  
                }  
            }  
        }  
    }  
      
    // ---------- Main run ----------  
      
    func run(ctx context.Context, url string) error {  
        dialer := websocket.Dialer{  
            HandshakeTimeout:  10 * time.Second,  
            EnableCompression: false,  
        }  
      
        conn, _, err := dialer.Dial(url, nil)  
        if err != nil {  
            return fmt.Errorf("dial error: %w", err)  
        }  
        defer conn.Close()  
        log.Printf("Connected to %s", url)  
      
        expires := (time.Now().Unix() + 10000) * 1000  
        val := fmt.Sprintf("GET/realtime%d", expires)  
        sig := signAuth(APISecret, val)  
      
        authMsg := map[string]any{  
            "req_id": "10001",  
            "op":     "auth",  
            "args":   []any{APIKey, expires, sig},  
        }  
        if err := sendJSON(conn, authMsg); err != nil {  
            return fmt.Errorf("send auth error: %w", err)  
        }  
      
        if _, msg, err := conn.ReadMessage(); err != nil {  
            return fmt.Errorf("read auth ack error: %w", err)  
        } else {  
            log.Printf("auth-ack: %s", string(msg))  
        }  
      
        subMsg := map[string]any{  
            "op":   "subscribe",  
            "args": subTopics,  
        }  
        if err := sendJSON(conn, subMsg); err != nil {  
            return fmt.Errorf("send subscribe error: %w", err)  
        }  
      
        hbCtx, hbCancel := context.WithCancel(ctx)  
        defer hbCancel()  
        go heartbeat(hbCtx, conn)  
      
        for {  
            select {  
            case <-ctx.Done():  
                log.Printf("context canceled, exit read loop")  
                return nil  
            default:  
            }  
      
            mt, data, err := conn.ReadMessage()  
            if err != nil {  
                return fmt.Errorf("read message error: %w", err)  
            }  
      
            switch mt {  
            case websocket.BinaryMessage:  
                resp, err := decodeFastOrderResp(data, false)  
                if err != nil {  
                    log.Printf("binary decode error: %v", err)  
                } else {  
                    j, _ := json.Marshal(resp)  
                    log.Printf("FAST_ORDER_SBE: %s", string(j))  
                }  
            case websocket.TextMessage:  
                var obj map[string]any  
                if err := json.Unmarshal(data, &obj); err != nil {  
                    log.Printf("text-nonjson: %s", string(data))  
                    continue  
                }  
                if op, ok := obj["op"].(string); ok && op == "pong" {  
                    continue  
                }  
                j, _ := json.Marshal(obj)  
                log.Printf("control: %s", string(j))  
            default:  
                log.Printf("unknown message type %d", mt)  
            }  
        }  
    }  
      
    // ---------- Entry ----------  
      
    func main() {  
        url := flag.String("url", MMWSURLTestnetBybits, "WebSocket URL")  
        flag.Parse()  
      
        if APIKey == "YOUR_API_KEY" || APISecret == "YOUR_API_SECRET" {  
            log.Println("⚠️ Please set APIKey and APISecret in the source before running.")  
        }  
      
        ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)  
        defer cancel()  
      
        if err := run(ctx, *url); err != nil {  
            log.Fatalf("run error: %v", err)  
        }  
    }  
    
    
    
    #!/usr/bin/env python3  
    import asyncio  
    import json  
    import hmac  
    import time  
    import struct  
    from typing import Tuple, Dict, Any  
    import websockets  
      
    MMWS_URL_TESTNET = "wss://stream-testnet.bybits.org/v5/private-sbe"  
    # MMWS_URL_MAINNET = "wss://stream.bybit.com/v5/private-sbe"  
      
    # TODO: fill in your real keys  
    API_KEY = "YOUR_API_KEY"  
    API_SECRET = "YOUR_API_SECRET"  
    SUB_TOPICS = ["order.sbe.resp.spot"]  
      
      
    def read_u8(buf: memoryview, off: int) -> Tuple[int, int]:  
        return buf[off], off + 1  
      
    def read_i8(buf: memoryview, off: int) -> Tuple[int, int]:  
        b = struct.unpack_from("<b", buf, off)[0]  
        return b, off + 1  
      
    def read_u16_le(buf: memoryview, off: int) -> Tuple[int, int]:  
        v = struct.unpack_from("<H", buf, off)[0]  
        return v, off + 2  
      
    def read_i32_le(buf: memoryview, off: int) -> Tuple[int, int]:  
        v = struct.unpack_from("<i", buf, off)[0]  
        return v, off + 4  
      
    def read_i64_le(buf: memoryview, off: int) -> Tuple[int, int]:  
        v = struct.unpack_from("<q", buf, off)[0]  
        return v, off + 8  
      
    def read_varstring8(buf: memoryview, off: int) -> Tuple[str, int]:  
        ln = buf[off]  
        off += 1  
        if ln == 0:  
            return "", off  
        s = bytes(buf[off: off + ln]).decode("utf-8", "replace")  
        return s, off + ln  
      
    def apply_exp(mantissa: int, exp: int) -> float:  
        if exp >= 0:  
            return mantissa / (10 ** exp)  
        else:  
            return mantissa * (10 ** (-exp))  
      
    def decode_fast_order_resp(payload: bytes, debug: bool = False) -> Dict[str, Any]:  
        mv = memoryview(payload)  
        off = 0  
        if len(mv) < 8:  
            raise ValueError("payload too short for SBE header")  
        block_len, template_id, schema_id, version = struct.unpack_from("<HHHH", mv, off)  
        off += 8  
      
        if debug:  
            print(f"HEADER: block_len={block_len}, template_id={template_id}, schema_id={schema_id}, version={version}")  
      
        if template_id != 21000:  
            return {"_warn": f"unexpected_template_id:{template_id}", "_raw": payload.hex()}  
      
        category, off = read_u8(mv, off)  
        side, off = read_u8(mv, off)  
        order_status, off = read_u8(mv, off)  
        price_exp, off = read_i8(mv, off)  
        size_exp, off = read_i8(mv, off)  
        value_exp, off = read_i8(mv, off)  
        reject_reason, off = read_u16_le(mv, off)  
      
        price, off = read_i64_le(mv, off)  
        leaves_qty, off = read_i64_le(mv, off)  
        leaves_value, off = read_i64_le(mv, off)  
        creation_time_us, off = read_i64_le(mv, off)  
        updated_time_us, off = read_i64_le(mv, off)  
        seq, off = read_i64_le(mv, off)  
        symbol_id, off = read_i32_le(mv, off)  
      
        order_id, off = read_varstring8(mv, off)  
        order_link_id, off = read_varstring8(mv, off)  
      
        return {  
            "_sbe_header": {  
                "blockLength": block_len,  
                "templateId": template_id,  
                "schemaId": schema_id,  
                "version": version,  
            },  
            "category": category,  
            "side": side,  
            "orderStatus": order_status,  
            "priceExponent": price_exp,  
            "sizeExponent": size_exp,  
            "valueExponent": value_exp,  
            "rejectReason": reject_reason,  
            "priceMantissa": price,  
            "leavesQtyMantissa": leaves_qty,  
            "leavesValueMantissa": leaves_value,  
            "price": apply_exp(price, price_exp),  
            "leavesQty": apply_exp(leaves_qty, size_exp),  
            "leavesValue": apply_exp(leaves_value, value_exp),  
            "creationTime": creation_time_us,  
            "updatedTime": updated_time_us,  
            "seq": seq,  
            "symbolID": symbol_id,  
            "orderId": order_id,  
            "orderLinkId": order_link_id,  
            "_raw_offset_end": off  
        }  
      
    async def send_json(ws, obj):  
        await ws.send(json.dumps(obj, separators=(",", ":")))  
      
    async def heartbeat(ws):  
        while True:  
            await asyncio.sleep(10)  
            try:  
                await send_json(ws, {"req_id": str(int(time.time() * 1000)), "op": "ping"})  
            except Exception:  
                return  
      
    async def run(url: str):  
        async with websockets.connect(url, max_size=None) as ws:  
            expires = int((time.time() + 10000) * 1000)  
            val = f'GET/realtime{expires}'  
            signature = hmac.new(  
                bytes(API_SECRET, 'utf-8'),  
                bytes(val, 'utf-8'),  
                digestmod='sha256'  
            ).hexdigest()  
            await send_json(ws, {"req_id": "10001", "op": "auth", "args": [API_KEY, expires, signature]})  
      
            ack = await ws.recv()  
            print("auth-ack:", ack)  
      
            await send_json(ws, {"op": "subscribe", "args": SUB_TOPICS})  
            asyncio.create_task(heartbeat(ws))  
      
            while True:  
                frame = await ws.recv()  
                if isinstance(frame, (bytes, bytearray)):  
                    try:  
                        decoded = decode_fast_order_resp(frame)  
                        print(json.dumps(decoded, ensure_ascii=False))  
                    except Exception as e:  
                        print("binary-decode-error:", e)  
                else:  
                    try:  
                        obj = json.loads(frame)  
                        if obj.get("op") != "pong":  
                            print(obj)  
                    except Exception:  
                        print("text-nonjson:", frame)  
      
      
    if __name__ == "__main__":  
        asyncio.run(run(MMWS_URL_TESTNET))

---

# Fast Order Response SBE

僅限 MMWS

此頻道**僅** 可透過您的**專屬 Market Maker WebSocket（MMWS）** 主機訪問，標準 WebSocket 端點無法使用。

## 概述

Fast Order SBE 頻道透過 Market Maker WebSocket（MMWS）為高頻交易（HFT）客戶提供超低延遲的訂單推送。它直接從撮合引擎推送 SBE（Simple Binary Encoding）二進位編碼訊息，用於下單、改單和撤單的確認回執。

本頻道以速度和效率為核心設計。詳細推送觸發邏輯，請參閱下方推送邏輯章節。

## 上線時間表

產品| 測試網| 主網  
---|---|---  
現貨| 2026年5月27日| 2026年6月23日  
期貨（線性 & 反向）| 2026年6月10日| 2026年7月9日  
期權| 2026年6月16日| 2026年7月21日  
  
## 連接

環境| URL  
---|---  
測試網| `wss://stream-testnet.bybits.org/v5/private-sbe`  
主網| `wss://<your-dedicated-MMWS-host>.bybit-aws.com/v5/private-sbe`  
  
  * SBE 訊息以**二進位幀** （`opcode = 2`）發送。
  * 控制幀（鑒權、ping/pong、訂閱/取消訂閱）使用標準 **Bybit V5 API JSON 格式** 。



## 鑒權

建立連接後必須立即進行鑒權。

### 鑒權請求
    
    
    {  
        "req_id": "10001",  
        "op": "auth",  
        "args": [  
            "api_key",  
            1662350400000,  
            "signature"  
        ]  
    }  
    

欄位| 說明  
---|---  
req_id| 可選的客戶端標識符  
args[1]| 時間戳，必須大於當前時間  
args[2]| 使用 [Bybit API 簽名算法](/docs/zh-TW/v5/guide#authentication) 生成  
  
### 鑒權成功響應
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "op": "auth",  
        "conn_id": "cejreaspqfh3sjdnldmg-p"  
    }  
    

## 心跳

### 發送 Ping
    
    
    {"req_id": "100001", "op": "ping"}  
    

### 接收 Pong
    
    
    {  
        "success": true,  
        "ret_msg": "pong",  
        "conn_id": "465772b1-7630-4fdc-a492-e003e6f0f260",  
        "req_id": "100001",  
        "op": "ping"  
    }  
    

## 訂閱

### 可用 Topic

Topic| 說明  
---|---  
`order.sbe.resp.spot`| 現貨快速訂單響應  
`order.sbe.resp.linear`| 線性合約（USDT/USDC）快速訂單響應  
`order.sbe.resp.inverse`| 反向合約快速訂單響應  
`order.sbe.resp.option`| 期權快速訂單響應  
  
### 訂閱示例
    
    
    {  
        "op": "subscribe",  
        "args": ["order.sbe.resp.linear", "order.sbe.resp.spot", "order.sbe.resp.option"]  
    }  
    

### 訂閱確認
    
    
    {  
        "success": true,  
        "ret_msg": "",  
        "conn_id": "d30fdpbboasp1pjbe7r0",  
        "req_id": "abc123",  
        "op": "subscribe"  
    }  
    

## 推送邏輯

當用戶主動發起操作（下單、改單、撤單）時，`fast.resp.order` 訊息將主動推送給客戶端。

信息

頻道重啟或重新訂閱後，推送從最新的撮合事件開始——核心是**速度** ，不支持補發歷史數據。

場景 / 事件| 是否推送| 備註  
---|---|---  
Maker 訂單新建（已接受 / ack）| ✅ 是| 所有由客戶端主動發起的操作（下單 / 改單 / 撤單 / 拒絕）。  
Maker 訂單成交 / 部分成交| ✅ 是| 所有由客戶端主動發起的操作（下單 / 改單 / 撤單 / 拒絕）。  
Taker 訂單（主動方）| ✅ 是| 所有由客戶端主動發起的操作（下單 / 改單 / 撤單 / 拒絕）。  
COT（CloseOnTrigger）訂單| ✅ 是（針對觸發後訂單）| 觸發的 COT 訂單行為類似新的 Taker 訂單；若開反向倉位，`orderLinkId=""`。  
RO / ReduceOnly 訂單| ✅ 是| 正常推送；若因保證金不足或倉位限制被拒絕，`rejectReason` 將有值。  
條件單 / TP-SL 觸發訂單| ✅ 是| 條件觸發且訂單變為活躍後推送，`orderLinkId=""` （為空）。  
DCP（斷線全部保護）| ✅ 是| DCP 在斷線時強制撤單時推送。  
SMP 撤 Taker / 同時撤兩方（自成交保護）| ✅ 是| Taker / Maker 兩側撤單均會推送。  
SMP 撤 Maker| ✅ 是| Taker / Maker 兩側撤單均會推送。  
MMP（做市商保護）| ✅ 是| MMP 觸發的撤單也會在 Fast Order 頻道推送。  
下架 / 合約到期 / 期權交割| ❌ 否| 系統主動平倉，不推送 Fast Order。  
訂單被拒（撮合 / 驗證拒絕）| ✅ 是| 立即推送，附帶 `rejectReason`。  
改單成功 / 拒絕| ✅ 是| 主動改單的 ack / 拒絕均推送。  
撤單成功 / 拒絕| ✅ 是| 主動撤單的 ack / 拒絕均推送。  
  
## 与标准 WebSocket 订单频道的差异

下表列出了 Fast Order SBE 频道（`order.sbe.resp.*`）与标准私有 WebSocket [订单](/docs/zh-TW/v5/websocket/private/order)频道在行为上的差异。

场景| Fast Order 频道| 标准 WS 订单频道| 说明  
---|---|---|---  
条件单下改撤（触发前）| ❌ 无推送| ✅ 有推送| 条件单在触发前不会发送到撮合引擎，撮合引擎无法获取触发前的订单状态。  
TP/SL 订单下改撤（触发前）| ❌ 无推送| ✅ 有推送| 原因同上。  
Trailing Stop 订单下改撤（触发前）| ❌ 无推送| ✅ 有推送| 原因同上。  
仓位强平订单| ❌ 无推送| ✅ 有推送| 注：强平触发的撤单两者推送一致。  
合约下架撤单| ❌ 无推送| ✅ 有推送| 下架撤单由内部处理，不发送到撮合引擎。  
改单/撤单请求到达前订单已完全成交| `orderStatus=Rejected`| `orderStatus=Filled`| 例如 qty=10，改成 12，但 10 手已成交 — Fast Order 返回 `Rejected`，标准 WS 返回 `Filled`。  
正常下改撤 — `leavesValue` 字段| 无值（`0`）| 有值| Fast Order 对非现货市价按金额买单（non-spot-market-buy-order-by-value）的 `leavesValue` 始终返回 `0`。  
盘前集合竞价阶段 — 撤单被拒| `orderStatus=Rejected`| `orderStatus=New`| 盘前集合竞价阶段不允许撤单，Fast Order 返回 `Rejected`，标准 WS 返回 `New`。  
  
## OrderLinkId 各版本行為說明

場景| 2026 測試網 / 主網| 備註  
---|---|---  
主動新建訂單（用戶發起）| ✅ 有值| 客戶端發起的下單包含用戶的 `orderLinkId`。  
改單 / 撤單（用戶發起）| ✅ 有值| 客戶端發起的下單包含用戶的 `orderLinkId`。  
Maker→Taker 轉變（如價格改單穿越盤口）| ✅ 有值| 客戶端發起的下單包含用戶的 `orderLinkId`。  
主動新建條件單（用戶發起）| ✅ 有值| 客戶端發起的下單包含用戶的 `orderLinkId`。  
倉位設置止盈止損訂單| ❌ 為空| 系統創建，無 `orderLinkId`。  
  
## 消息結構（SBE）

`templateId = 21000`（`FastOrderResp`）

### 消息頭（8 字節）

欄位| 類型| 大小（字節）| 說明  
---|---|---|---  
blockLength| uint16| 2| 消息體長度  
templateId| uint16| 2| 固定 = `21000`  
schemaId| uint16| 2| 固定 = `1`  
version| uint16| 2| 固定 = `0`  
  
### 消息體

ID| 欄位| 類型| 說明  
---|---|---|---  
1| category| uint8| `1`=現貨, `2`=線性, `3`=反向, `4`=期權  
2| side| uint8| `1`=買, `2`=賣  
3| orderStatus| uint8| 訂單狀態枚舉。`0`=Others, `4`=PartiallyFilledAndCancelled, `5`=Rejected, `6`=New, `7`=Cancelled, `8`=PartiallyFilled, `9`=Filled  
4| priceExponent| int8| 價格小數位數。`price = mantissa / 10^priceExponent`  
5| sizeExponent| int8| 數量小數位數  
6| valueExponent| int8| 金額小數位數  
7| rejectReason| uint16| 無拒絕時為 `0`，詳見 rejectReason 映射  
8| price| int64| 價格尾數（需應用 `priceExponent`）  
9| leavesQty| int64| 剩餘數量尾數（需應用 `sizeExponent`）  
10| leavesValue| int64| 僅現貨市價買單有效，其他情況為 `0`（需應用 `valueExponent`）  
11| creationTime| int64| 訂單在 Fast Order 頻道的創建時間戳（微秒）  
12| updatedTime| int64| 撮合時間戳（微秒）  
13| seq| int64| 跨序列 ID  
14| symbolID| int32| 交易對 ID  
100| orderId| varString8| 訂單 ID（UUID）  
101| orderLinkId| varString8| 可選；用戶主動操作時存在  
  
## rejectReason 映射

代碼| 名稱  
---|---  
0| EC_NoError  
1| EC_Others  
2| EC_UnknownMessageType  
3| EC_MissingClOrdID  
4| EC_MissingOrigClOrdID  
5| EC_ClOrdIDOrigClOrdIDAreTheSame  
6| EC_DuplicatedClOrdID  
7| EC_OrigClOrdIDDoesNotExist  
8| EC_TooLateToCancel  
9| EC_UnknownOrderType  
10| EC_UnknownSide  
11| EC_UnknownTimeInForce  
12| EC_WronglyRouted  
13| EC_MarketOrderPriceIsNotZero  
14| EC_LimitOrderInvalidPrice  
15| EC_NoEnoughQtyToFill  
16| EC_NoImmediateQtyToFill  
17| EC_QtyCannotBeZero  
18| EC_PerCancelRequest  
19| EC_MarketOrderCannotBePostOnly  
20| EC_PostOnlyWillTakeLiquidity  
21| EC_CancelReplaceOrder  
22| EC_InvalidSymbolStatus  
23| EC_MarketOrderNoSupportTIF  
24| EC_ReachMaxTradeNum  
25| EC_InvalidPriceScale  
26| EC_BitIndexInvalid  
27| EC_StopBySelfMatch  
28| EC_BySelfMatch  
29| EC_InvalidSmpType  
30| EC_CancelByMMP  
31| EC_InCallAuctionStatus  
34| EC_InvalidUserType  
35| EC_InvalidMirrorOid  
36| EC_InvalidMirrorUid  
37| EC_SymbolNotExist  
38| EC_CancelNoActiveOrders  
39| EC_MissingUID  
100| EC_EcInvalidQty  
101| EC_InvalidAmount  
102| EC_LoadOrderCancel  
103| EC_CancelForNoFullFill  
104| EC_MarketQuoteNoSuppSell  
105| EC_DisorderOrderID  
106| EC_InvalidBaseValue  
107| EC_LoadOrderCanMatch  
108| EC_SecurityStatusFail  
110| EC_ReachRiskPriceLimit  
111| EC_OrderNotExist  
112| EC_CancelByOrderValueZero  
113| EC_CancelByMatchValueZero  
200| EC_ReachMarketPriceLimit  
  
## SBE XML 模板（Fast Order Response）
    
    
    <?xml version="1.0" encoding="UTF-8"?>  
    <sbe:messageSchema xmlns:sbe="http://fixprotocol.io/2016/sbe"  
                       xmlns:mbx="https://bybit-exchange.github.io/docs/v5/intro"  
                       package="order.fast.sbe"  
                       id="1"  
                       version="0"  
                       semanticVersion="1.0.0"  
                       description="Bybit fast order response SBE schema"  
                       byteOrder="littleEndian"  
                       headerType="messageHeader">  
      <types>  
        <composite name="messageHeader" description="Template ID and length of message root">  
          <type name="blockLength" primitiveType="uint16"/>  
          <type name="templateId" primitiveType="uint16"/>  
          <type name="schemaId" primitiveType="uint16"/>  
          <type name="version" primitiveType="uint16"/>  
        </composite>  
        <composite name="varString8" description="Variable length UTF-8 string">  
          <type name="length" primitiveType="uint8"/>  
          <type name="varData" length="0" primitiveType="uint8" semanticType="String" characterEncoding="UTF-8"/>  
        </composite>  
      </types>  
      <!-- Fast order response: active place/cancel/amend acknowledgements -->  
      <sbe:message name="FastOrderResp" id="21000">  
        <!-- Routing / classification -->  
        <field id="1" name="category" type="uint8" description="1=spot, 2=linear, 3=inverse, 4=option"/>  
        <!-- Side / status / rejection -->  
        <field id="2" name="side" type="uint8" description="1=Buy, 2=Sell"/>  
        <field id="3" name="orderStatus" type="uint8" description="Order state enum"/>  
        <!-- Price / size (mantissas) with exponents -->  
        <field id="4" name="priceExponent" type="int8" description="Decimal places for price"/>  
        <field id="5" name="sizeExponent" type="int8" description="Decimal places for size"/>  
        <field id="6" name="valueExponent" type="int8" description="Decimal places for value"/>  
        <field id="7" name="rejectReason" type="uint16" description="0 if N/A"/>  
        <field id="8" name="price" type="int64" mbx:exponent="priceExponent" description="Price mantissa"/>  
        <field id="9" name="leavesQty" type="int64" mbx:exponent="sizeExponent" description="Remaining quantity mantissa"/>  
        <field id="10" name="leavesValue" type="int64" mbx:exponent="valueExponent" description="Spot market buy only; otherwise 0"/>  
        <!-- Timing -->  
        <field id="11" name="creationTime" type="int64" description="Order creation timestamp in Fast order channel(microseconds)"/>  
        <field id="12" name="updatedTime" type="int64" description="Matching timestamp (microseconds)"/>  
        <field id="13" name="seq" type="int64" description="Cross sequence ID"/>  
        <!-- SymbolID -->  
        <field id="14" name="symbolID" type="int32" description="Symbol ID"/>  
        <!-- Order identifiers -->  
        <data id="100" name="orderId" type="varString8" description="Order ID"/>  
        <data id="101" name="orderLinkId" type="varString8" description="Optional; present for user-initiated orders"/>  
      </sbe:message>  
    </sbe:messageSchema>  
    

## 代碼示例

  * Go
  * Python


    
    
    package main  
      
    import (  
        "context"  
        "crypto/hmac"  
        "crypto/sha256"  
        "encoding/binary"  
        "encoding/hex"  
        "encoding/json"  
        "flag"  
        "fmt"  
        "log"  
        "math"  
        "os"  
        "os/signal"  
        "time"  
      
        "github.com/gorilla/websocket"  
    )  
      
    // ---------- Config ----------  
      
    const (  
        MMWSURLTestnetBybits = "wss://stream-testnet.bybits.org/v5/private-sbe"  
        MMWSURLTestnetBybit  = "wss://stream-testnet.bybit.com/v5/private-sbe"  
        MMWSURLMainnet       = "wss://stream.bybit.com/v5/private-sbe"  
    )  
      
    // TODO: 填入您的真實密鑰  
    const (  
        APIKey    = "YOUR_API_KEY"  
        APISecret = "YOUR_API_SECRET"  
    )  
      
    var subTopics = []string{  
        "order.sbe.resp.spot",  
    }  
      
    // ---------- SBE helpers ----------  
      
    func readU8(buf []byte, off *int) (uint8, error) {  
        if *off+1 > len(buf) {  
            return 0, fmt.Errorf("readU8: out of range")  
        }  
        v := buf[*off]  
        *off++  
        return v, nil  
    }  
      
    func readI8(buf []byte, off *int) (int8, error) {  
        if *off+1 > len(buf) {  
            return 0, fmt.Errorf("readI8: out of range")  
        }  
        v := int8(buf[*off])  
        *off++  
        return v, nil  
    }  
      
    func readU16LE(buf []byte, off *int) (uint16, error) {  
        if *off+2 > len(buf) {  
            return 0, fmt.Errorf("readU16LE: out of range")  
        }  
        v := binary.LittleEndian.Uint16(buf[*off : *off+2])  
        *off += 2  
        return v, nil  
    }  
      
    func readI32LE(buf []byte, off *int) (int32, error) {  
        if *off+4 > len(buf) {  
            return 0, fmt.Errorf("readI32LE: out of range")  
        }  
        v := int32(binary.LittleEndian.Uint32(buf[*off : *off+4]))  
        *off += 4  
        return v, nil  
    }  
      
    func readI64LE(buf []byte, off *int) (int64, error) {  
        if *off+8 > len(buf) {  
            return 0, fmt.Errorf("readI64LE: out of range")  
        }  
        v := int64(binary.LittleEndian.Uint64(buf[*off : *off+8]))  
        *off += 8  
        return v, nil  
    }  
      
    func readVarString8(buf []byte, off *int) (string, error) {  
        if *off+1 > len(buf) {  
            return "", fmt.Errorf("readVarString8: no length byte")  
        }  
        ln := int(buf[*off])  
        *off++  
        if ln == 0 {  
            return "", nil  
        }  
        if *off+ln > len(buf) {  
            return "", fmt.Errorf("readVarString8: length out of range")  
        }  
        s := string(buf[*off : *off+ln])  
        *off += ln  
        return s, nil  
    }  
      
    func applyExp(mantissa int64, exp int8) float64 {  
        e := int(exp)  
        if e >= 0 {  
            return float64(mantissa) / math.Pow10(e)  
        }  
        return float64(mantissa) * math.Pow10(-e)  
    }  
      
    // ---------- Fast Order SBE decode ----------  
      
    type FastOrderSBEResp struct {  
        SBEHeader struct {  
            BlockLength uint16 `json:"blockLength"`  
            TemplateID  uint16 `json:"templateId"`  
            SchemaID    uint16 `json:"schemaId"`  
            Version     uint16 `json:"version"`  
        } `json:"_sbe_header"`  
      
        Category      uint8  `json:"category"`  
        Side          uint8  `json:"side"`  
        OrderStatus   uint8  `json:"orderStatus"`  
        PriceExponent int8   `json:"priceExponent"`  
        SizeExponent  int8   `json:"sizeExponent"`  
        ValExponent   int8   `json:"valueExponent"`  
        RejectReason  uint16 `json:"rejectReason"`  
      
        PriceMantissa       int64 `json:"priceMantissa"`  
        LeavesQtyMantissa   int64 `json:"leavesQtyMantissa"`  
        LeavesValueMantissa int64 `json:"leavesValueMantissa"`  
      
        CreationTime int64 `json:"creationTime"`  
        UpdatedTime  int64 `json:"updatedTime"`  
        Seq          int64 `json:"seq"`  
      
        SymbolID    int32  `json:"symbolID"`  
        OrderID     string `json:"orderId"`  
        OrderLinkID string `json:"orderLinkId"`  
      
        Price       float64 `json:"price"`  
        LeavesQty   float64 `json:"leavesQty"`  
        LeavesValue float64 `json:"leavesValue"`  
      
        RawOffsetEnd int `json:"_raw_offset_end"`  
    }  
      
    func decodeFastOrderResp(payload []byte, debug bool) (*FastOrderSBEResp, error) {  
        if len(payload) < 8 {  
            return nil, fmt.Errorf("payload too short for SBE header")  
        }  
        off := 0  
        blockLen := binary.LittleEndian.Uint16(payload[off : off+2])  
        templateID := binary.LittleEndian.Uint16(payload[off+2 : off+4])  
        schemaID := binary.LittleEndian.Uint16(payload[off+4 : off+6])  
        version := binary.LittleEndian.Uint16(payload[off+6 : off+8])  
        off += 8  
      
        if debug {  
            log.Printf("HEADER: block_len=%d, template_id=%d, schema_id=%d, version=%d",  
                blockLen, templateID, schemaID, version)  
        }  
      
        if templateID != 21000 {  
            return nil, fmt.Errorf("unexpected templateId: %d", templateID)  
        }  
      
        var err error  
        resp := &FastOrderSBEResp{}  
        resp.SBEHeader.BlockLength = blockLen  
        resp.SBEHeader.TemplateID = templateID  
        resp.SBEHeader.SchemaID = schemaID  
        resp.SBEHeader.Version = version  
      
        if resp.Category, err = readU8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.Side, err = readU8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.OrderStatus, err = readU8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.PriceExponent, err = readI8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.SizeExponent, err = readI8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.ValExponent, err = readI8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.RejectReason, err = readU16LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.PriceMantissa, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.LeavesQtyMantissa, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.LeavesValueMantissa, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.CreationTime, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.UpdatedTime, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.Seq, err = readI64LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.SymbolID, err = readI32LE(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.OrderID, err = readVarString8(payload, &off); err != nil {  
            return nil, err  
        }  
        if resp.OrderLinkID, err = readVarString8(payload, &off); err != nil {  
            return nil, err  
        }  
      
        resp.Price = applyExp(resp.PriceMantissa, resp.PriceExponent)  
        resp.LeavesQty = applyExp(resp.LeavesQtyMantissa, resp.SizeExponent)  
        resp.LeavesValue = applyExp(resp.LeavesValueMantissa, resp.ValExponent)  
        resp.RawOffsetEnd = off  
      
        return resp, nil  
    }  
      
    // ---------- WebSocket helpers ----------  
      
    func sendJSON(conn *websocket.Conn, v any) error {  
        data, err := json.Marshal(v)  
        if err != nil {  
            return err  
        }  
        return conn.WriteMessage(websocket.TextMessage, data)  
    }  
      
    func signAuth(secret, value string) string {  
        h := hmac.New(sha256.New, []byte(secret))  
        h.Write([]byte(value))  
        return hex.EncodeToString(h.Sum(nil))  
    }  
      
    func heartbeat(ctx context.Context, conn *websocket.Conn) {  
        ticker := time.NewTicker(10 * time.Second)  
        defer ticker.Stop()  
        for {  
            select {  
            case <-ctx.Done():  
                return  
            case <-ticker.C:  
                reqID := fmt.Sprintf("%d", time.Now().UnixMilli())  
                err := sendJSON(conn, map[string]any{  
                    "req_id": reqID,  
                    "op":     "ping",  
                })  
                if err != nil {  
                    log.Printf("[heartbeat] error sending ping: %v", err)  
                    return  
                }  
            }  
        }  
    }  
      
    // ---------- Main run ----------  
      
    func run(ctx context.Context, url string) error {  
        dialer := websocket.Dialer{  
            HandshakeTimeout:  10 * time.Second,  
            EnableCompression: false,  
        }  
      
        conn, _, err := dialer.Dial(url, nil)  
        if err != nil {  
            return fmt.Errorf("dial error: %w", err)  
        }  
        defer conn.Close()  
        log.Printf("Connected to %s", url)  
      
        expires := (time.Now().Unix() + 10000) * 1000  
        val := fmt.Sprintf("GET/realtime%d", expires)  
        sig := signAuth(APISecret, val)  
      
        authMsg := map[string]any{  
            "req_id": "10001",  
            "op":     "auth",  
            "args":   []any{APIKey, expires, sig},  
        }  
        if err := sendJSON(conn, authMsg); err != nil {  
            return fmt.Errorf("send auth error: %w", err)  
        }  
      
        if _, msg, err := conn.ReadMessage(); err != nil {  
            return fmt.Errorf("read auth ack error: %w", err)  
        } else {  
            log.Printf("auth-ack: %s", string(msg))  
        }  
      
        subMsg := map[string]any{  
            "op":   "subscribe",  
            "args": subTopics,  
        }  
        if err := sendJSON(conn, subMsg); err != nil {  
            return fmt.Errorf("send subscribe error: %w", err)  
        }  
      
        hbCtx, hbCancel := context.WithCancel(ctx)  
        defer hbCancel()  
        go heartbeat(hbCtx, conn)  
      
        for {  
            select {  
            case <-ctx.Done():  
                log.Printf("context canceled, exit read loop")  
                return nil  
            default:  
            }  
      
            mt, data, err := conn.ReadMessage()  
            if err != nil {  
                return fmt.Errorf("read message error: %w", err)  
            }  
      
            switch mt {  
            case websocket.BinaryMessage:  
                resp, err := decodeFastOrderResp(data, false)  
                if err != nil {  
                    log.Printf("binary decode error: %v", err)  
                } else {  
                    j, _ := json.Marshal(resp)  
                    log.Printf("FAST_ORDER_SBE: %s", string(j))  
                }  
            case websocket.TextMessage:  
                var obj map[string]any  
                if err := json.Unmarshal(data, &obj); err != nil {  
                    log.Printf("text-nonjson: %s", string(data))  
                    continue  
                }  
                if op, ok := obj["op"].(string); ok && op == "pong" {  
                    continue  
                }  
                j, _ := json.Marshal(obj)  
                log.Printf("control: %s", string(j))  
            default:  
                log.Printf("unknown message type %d", mt)  
            }  
        }  
    }  
      
    // ---------- Entry ----------  
      
    func main() {  
        url := flag.String("url", MMWSURLTestnetBybits, "WebSocket URL")  
        flag.Parse()  
      
        if APIKey == "YOUR_API_KEY" || APISecret == "YOUR_API_SECRET" {  
            log.Println("⚠️ Please set APIKey and APISecret in the source before running.")  
        }  
      
        ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)  
        defer cancel()  
      
        if err := run(ctx, *url); err != nil {  
            log.Fatalf("run error: %v", err)  
        }  
    }  
    
    
    
    #!/usr/bin/env python3  
    import asyncio  
    import json  
    import hmac  
    import time  
    import struct  
    from typing import Tuple, Dict, Any  
    import websockets  
      
    MMWS_URL_TESTNET = "wss://stream-testnet.bybits.org/v5/private-sbe"  
    # MMWS_URL_MAINNET = "wss://stream.bybit.com/v5/private-sbe"  
      
    # TODO: 填入您的真實密鑰  
    API_KEY = "YOUR_API_KEY"  
    API_SECRET = "YOUR_API_SECRET"  
    SUB_TOPICS = ["order.sbe.resp.spot"]  
      
      
    def read_u8(buf: memoryview, off: int) -> Tuple[int, int]:  
        return buf[off], off + 1  
      
    def read_i8(buf: memoryview, off: int) -> Tuple[int, int]:  
        b = struct.unpack_from("<b", buf, off)[0]  
        return b, off + 1  
      
    def read_u16_le(buf: memoryview, off: int) -> Tuple[int, int]:  
        v = struct.unpack_from("<H", buf, off)[0]  
        return v, off + 2  
      
    def read_i32_le(buf: memoryview, off: int) -> Tuple[int, int]:  
        v = struct.unpack_from("<i", buf, off)[0]  
        return v, off + 4  
      
    def read_i64_le(buf: memoryview, off: int) -> Tuple[int, int]:  
        v = struct.unpack_from("<q", buf, off)[0]  
        return v, off + 8  
      
    def read_varstring8(buf: memoryview, off: int) -> Tuple[str, int]:  
        ln = buf[off]  
        off += 1  
        if ln == 0:  
            return "", off  
        s = bytes(buf[off: off + ln]).decode("utf-8", "replace")  
        return s, off + ln  
      
    def apply_exp(mantissa: int, exp: int) -> float:  
        if exp >= 0:  
            return mantissa / (10 ** exp)  
        else:  
            return mantissa * (10 ** (-exp))  
      
    def decode_fast_order_resp(payload: bytes, debug: bool = False) -> Dict[str, Any]:  
        mv = memoryview(payload)  
        off = 0  
        if len(mv) < 8:  
            raise ValueError("payload too short for SBE header")  
        block_len, template_id, schema_id, version = struct.unpack_from("<HHHH", mv, off)  
        off += 8  
      
        if debug:  
            print(f"HEADER: block_len={block_len}, template_id={template_id}, schema_id={schema_id}, version={version}")  
      
        if template_id != 21000:  
            return {"_warn": f"unexpected_template_id:{template_id}", "_raw": payload.hex()}  
      
        category, off = read_u8(mv, off)  
        side, off = read_u8(mv, off)  
        order_status, off = read_u8(mv, off)  
        price_exp, off = read_i8(mv, off)  
        size_exp, off = read_i8(mv, off)  
        value_exp, off = read_i8(mv, off)  
        reject_reason, off = read_u16_le(mv, off)  
      
        price, off = read_i64_le(mv, off)  
        leaves_qty, off = read_i64_le(mv, off)  
        leaves_value, off = read_i64_le(mv, off)  
        creation_time_us, off = read_i64_le(mv, off)  
        updated_time_us, off = read_i64_le(mv, off)  
        seq, off = read_i64_le(mv, off)  
        symbol_id, off = read_i32_le(mv, off)  
      
        order_id, off = read_varstring8(mv, off)  
        order_link_id, off = read_varstring8(mv, off)  
      
        return {  
            "_sbe_header": {  
                "blockLength": block_len,  
                "templateId": template_id,  
                "schemaId": schema_id,  
                "version": version,  
            },  
            "category": category,  
            "side": side,  
            "orderStatus": order_status,  
            "priceExponent": price_exp,  
            "sizeExponent": size_exp,  
            "valueExponent": value_exp,  
            "rejectReason": reject_reason,  
            "priceMantissa": price,  
            "leavesQtyMantissa": leaves_qty,  
            "leavesValueMantissa": leaves_value,  
            "price": apply_exp(price, price_exp),  
            "leavesQty": apply_exp(leaves_qty, size_exp),  
            "leavesValue": apply_exp(leaves_value, value_exp),  
            "creationTime": creation_time_us,  
            "updatedTime": updated_time_us,  
            "seq": seq,  
            "symbolID": symbol_id,  
            "orderId": order_id,  
            "orderLinkId": order_link_id,  
            "_raw_offset_end": off  
        }  
      
    async def send_json(ws, obj):  
        await ws.send(json.dumps(obj, separators=(",", ":")))  
      
    async def heartbeat(ws):  
        while True:  
            await asyncio.sleep(10)  
            try:  
                await send_json(ws, {"req_id": str(int(time.time() * 1000)), "op": "ping"})  
            except Exception:  
                return  
      
    async def run(url: str):  
        async with websockets.connect(url, max_size=None) as ws:  
            expires = int((time.time() + 10000) * 1000)  
            val = f'GET/realtime{expires}'  
            signature = hmac.new(  
                bytes(API_SECRET, 'utf-8'),  
                bytes(val, 'utf-8'),  
                digestmod='sha256'  
            ).hexdigest()  
            await send_json(ws, {"req_id": "10001", "op": "auth", "args": [API_KEY, expires, signature]})  
      
            ack = await ws.recv()  
            print("auth-ack:", ack)  
      
            await send_json(ws, {"op": "subscribe", "args": SUB_TOPICS})  
            asyncio.create_task(heartbeat(ws))  
      
            while True:  
                frame = await ws.recv()  
                if isinstance(frame, (bytes, bytearray)):  
                    try:  
                        decoded = decode_fast_order_resp(frame)  
                        print(json.dumps(decoded, ensure_ascii=False))  
                    except Exception as e:  
                        print("binary-decode-error:", e)  
                else:  
                    try:  
                        obj = json.loads(frame)  
                        if obj.get("op") != "pong":  
                            print(obj)  
                    except Exception:  
                        print("text-nonjson:", frame)  
      
      
    if __name__ == "__main__":  
        asyncio.run(run(MMWS_URL_TESTNET))