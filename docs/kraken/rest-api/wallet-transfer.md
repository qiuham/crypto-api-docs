---
exchange: kraken
source_url: https://docs.kraken.com/api/docs/rest-api/wallet-transfer
api_type: REST
updated_at: 2026-06-05 19:42:28.983362
---

# Request Wallet Transfer

POST 
    
    ## /private/WalletTransfer

Transfer from a Kraken spot wallet to a Kraken Futures wallet. Note that a transfer in the other direction must be requested via the Kraken Futures API endpoint for [withdrawals to Spot wallets](/api/docs/futures-api/trading/withdrawal).

**API Key Permissions Required:** `Funds permissions - Query`

## Request

## Responses

  * 200

Transfer created.