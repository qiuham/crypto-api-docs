---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/websocket-v1/editorder
api_type: WebSocket
updated_at: 2026-05-31 19:27:21.418845
---

# Heartbeat

CHANNEL
**Endpoint:** `wss://ws.kraken.com`
    heartbeat

Server heartbeat sent if no subscription traffic within approximately 1 second.

## Payload

  * Response Schema
  * Example

### MESSAGE BODY

**event** `string`

heartbeat
    
    
    {  
      "event": "heartbeat"  
    }