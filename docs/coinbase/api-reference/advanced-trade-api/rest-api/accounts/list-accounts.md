---
exchange: coinbase
source_url: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/accounts/list-accounts
api_type: Account
updated_at: 2026-06-26 18:37:12.455639
---

# List Accounts

**Endpoint:** `GET https://api.coinbase.com/api/v3/brokerage/accounts`


# List Accounts

Get a list of authenticated accounts for the current user.
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/accounts \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "has_next": true,
      "accounts": [
        {
          "uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
          "name": "BTC Wallet",
          "currency": "BTC",
          "available_balance": {
            "value": "1.23",
            "currency": "BTC"
          },
          "default": false,
          "active": true,
          "created_at": "2021-05-31T09:59:59.000Z",
          "updated_at": "2021-05-31T09:59:59.000Z",
          "deleted_at": "2021-05-31T09:59:59.000Z",
          "type": "FIAT",
          "ready": true,
          "hold": {
            "value": "1.23",
            "currency": "BTC"
          },
          "retail_portfolio_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
          "platform": "ACCOUNT_PLATFORM_CONSUMER"
        }
      ],
      "cursor": "789100",
      "size": 123
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

limit

integer<int32>

The number of accounts to display per page. By default, displays 49 (max 250). If `has_next` is true, additional pages of accounts are available to be fetched. Use the `cursor` parameter to start on a specified page.

cursor

string

For paginated responses, returns all responses that come after this value.

retail_portfolio_id

string

(Deprecated) Only returns the accounts matching the portfolio ID. Only applicable for legacy keys. CDP keys will default to the key's permissioned portfolio.

#### Response

A successful response.

has_next

boolean

required

Whether there are additional pages for this query.

Example:

`true`

accounts

object[]

cursor

string

For paginated responses, returns all responses that come after this value.

Example:

`"789100"`

size

integer<int32>

Number of accounts returned

Convert

# Create Convert Quote

Create a convert quote with a specified source account, target account, and amount. Convert is applicable for USDC-USD, PYUSD-USD, EURC-EUR conversion, and PYUSD-USDC conversion

POST

/

api

/

v3

/

brokerage

/

convert

/

quote

Create Convert Quote
    
    
    curl --request POST \
      --url https://api.coinbase.com/api/v3/brokerage/convert/quote \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '
    {
      "from_account": "<string>",
      "to_account": "<string>",
      "amount": "<string>",
      "trade_incentive_metadata": {
        "user_incentive_id": "<string>",
        "code_val": "<string>"
      }
    }
    '
    
    
    {
      "trade": {
        "id": "<string>",
        "status": "TRADE_STATUS_UNSPECIFIED",
        "user_entered_amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "amount": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "subtotal": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "total": {
          "value": "<string>",
          "currency": "<string>",
          "cbrn": "<string>"
        },
        "fees": [
          {
            "title": "<string>",
            "description": "<string>",
            "amount": {
              "value": "<string>",
              "currency": "<string>",
              "cbrn": "<string>"
            },
            "label": "<string>",
            "disclosure": {
              "title": "<string>",
              "description": "<string>",
              "link": {
                "text": "<string>",
                "url": "<string>"
              }
            },
            "waived_details": {
              "amount": {
                "value": "<string>",
                "currency": "<string>",
                "cbrn": "<string>"
              },
              "source": "WAIVED_FEE_SOURCE_UNSPECIFIED"
            },
            "metadata": {
              "netburn": {
                "threshold": {
                  "value": "<string>",
                  "currency": "<string>",
                  "cbrn": "<string>"
                },
                "netburn_value": {
                  "value": "<string>",
                  "currency": "<string>",
                  "cbrn": "<string>"
                }
              }
            }
          }
        ],
        "total_fee": {
          "title": "<string>",
          "description": "<string>",
          "amount": {
            "value": "<string>",
            "currency": "<string>",
            "cbrn": "<string>"
          },
          "label": "<string>",
          "disclosure": {
            "title": "<string>",
            "description": "<string>",
            "link": {
              "text": "<string>",
              "url": "<string>"
            }
          },
          "waived_details": {
            "amount": {
              "value": "<string>",
              "currency": "<string>",
              "cbrn": "<string>"
            },
            "source": "WAIVED_FEE_SOURCE_UNSPECIFIED"
          },
          "metadata": {
            "netburn": {
              "threshold": {
                "value": "<string>",
                "currency": "<string>",
                "cbrn": "<string>"
              },
              "netburn_value": {
                "value": "<string>",
                "currency": "<string>",
                "cbrn": "<string>"
              }
            }
          }
        },
        "source": {
          "type": "INVALID",
          "network": "<string>",
          "payment_method_id": "<string>",
          "payment_method_type_string": "<string>",
          "blockchain_address": {
            "address": "<string>",
            "destination_tag": "<string>"
          },
          "coinbase_account": {
            "account_id": "<string>"
          },
          "blockchain_transaction": {
            "hsh": "<string>",
            "height": 123,
            "normalized_hash": "<string>"
          },
          "fedwire": {
            "routing_number": "<string>",
            "account_holder": {
              "legal_name": "<string>",
              "account_number": "<string>",
              "address": {
                "lines": [
                  "<string>"
                ],
                "country_code": "<string>",
                "city": "<string>",
                "state": "<string>",
                "postal_code": "<string>"
              }
            },
            "bank": {
              "name": "<string>",
              "address": {
                "lines": [
                  "<string>"
                ],
                "country_code": "<string>",
                "city": "<string>",
                "state": "<string>",
                "postal_code": "<string>"
              },
              "identifier": "<string>",
              "type": "CHIPS_IDENTIFIER",
              "identifier_code": "<string>"
            },
            "intermediary_bank": {
              "name": "<string>",
              "address": {
                "lines": [
                  "<string>"
                ],
                "country_code": "<string>",
                "city": "<string>",
                "state": "<string>",
                "postal_code": "<string>"
              },
              "identifier": "<string>",
              "type": "CHIPS_IDENTIFIER",
              "identifier_code": "<string>"
            },
            "currency": "<string>",
            "fiat_id": "<string>",
            "rejection_count_v2": 123
          },
          "swift": {
            "account_holder": {
              "legal_name": "<string>",
              "iban": "<string>",
              "bban": "<string>",
              "domestic_account_id": "<string>",
              "customer_payment_address1": "<string>",
              "customer_payment_address2": "<string>",
              "customer_payment_address3": "<string>",
              "customer_payment_country_code": "<string>",
              "iban_generated": true
            },
            "institution": {
              "bic": "<string>",
              "name": "<string>",
              "bank_address1": "<string>",
              "bank_address2": "<string>",
              "bank_address3": "<string>",
              "bank_country_code": "<string>",
              "domestic_bank_id": "<string>",
              "international_bank_id": "<string>"
            },
            "intermediary": {
              "bic": "<string>",
              "name": "<string>",
              "bank_address1": "<string>",
              "bank_address2": "<string>",
              "bank_address3": "<string>",
              "bank_country_code": "<string>",
              "domestic_bank_id": "<string>",
              "international_bank_id": "<string>"
            },
            "currency": "<string>",
            "rejection_count": 123
          },
          "card": {
            "first_data_token": {
              "value": "<string>",
              "store_id": "<string>",
              "id": "<string>"
            },
            "merchant": {
              "mid": "<string>"
            },
            "vault_token": {
              "value": "<string>",
              "vault_id": "<string>",
              "attempted_at": "<string>",
              "encrypted_data": "<string>",
              "encrypted_cvv": "<string>"
            },
            "worldpay_params": {
              "token_value": "<string>",
              "token_event": "<string>",
              "uses_merchant_token": true,
              "accept_header": "<string>",
              "user_agent_header": "<string>",
              "shopper_ip": "<string>",
              "shopper_session_id": "<string>"
            },
            "checkout_token": {
              "source_id": "<string>"
            },
            "stripe_params": {
              "stripe_id": "<string>",
              "radar_session_id": "<string>",
              "address_line1_check": "STRIPE_CARD_CHECK_STATUS_UNKNOWN",
              "address_postal_code_check": "STRIPE_CARD_CHECK_STATUS_UNKNOWN",
              "cvc_check": "STRIPE_CARD_CHECK_STATUS_UNKNOWN"
            },
            "six_digit_bin": "<string>",
            "last_four": "<string>",
            "eight_digit_bin": "<string>",
            "card_sub_brand": "<string>",
            "card_brand": "<string>",
            "obfuscated_pan": "<string>",
            "bin_info": {
              "match_found": true,
              "type": "UNKNOWN",
              "issuer": "<string>",
              "issuer_country_code": "<string>",
              "prepaid": true,
              "corporate": true,
              "consumer": true,
              "visa": {
                "oct_supported": true,
                "fast_funds_supported": true
              },
              "mastercard": {
                "fast_funds_supported": true
              },
              "use_3ds": true
            },
            "scheme": "UNKNOWN",
            "issuer": "<string>",
            "issuer_country_code": "<string>",
            "address": {
              "address1": "<string>",
              "address2": "<string>",
              "city": "<string>",
              "state": "<string>",
              "postal_code": "<string>",
              "country": "<string>",
              "uuid": "<string>",
              "id": "<string>"
            },
            "phone_number": "<string>",
            "user_id": "<string>",
            "postal_code": "<string>",
            "customer_info": {
              "full_name": "<string>",
              "first_name": "<string>",
              "last_name": "<string>",
              "dob": {
                "month": "<string>",
                "day": "<string>",
                "year": "<string>"
              },
              "nationality": "<string>",
              "email": "<string>"
            },
            "expiry_date": {
              "month": "<string>",
              "year": "<string>"
            },
            "cdv_method": "<string>",
            "cdv_amount_1": {
              "amount": "<string>",
              "currency": "<string>"
            },
            "cdv_amount_2": {
              "amount": "<string>",
              "currency": "<string>"
            },
            "worldpay_card_cdv_status": {
              "cdv_required": true,
              "cdv_failed": true
            },
            "previous_scheme_tx_id": "<string>",
            "initial_scheme_tx_id": "<string>",
            "rejected": true,
            "rejected_at": "<string>",
            "rejection_count": 123,
            "rejected_via_purchase": true,
            "account_updater_updated_at": "<string>",
            "account_updater_reason": "<string>",
            "account_updater_status": "<string>",
            "almost_expired_notified": true,
            "is_migrated_card": true,
            "migrated_created_at": "<string>",
            "card_source": "SOURCE_UNKNOWN",
            "added_via_buy_widget": true,
            "encrypted_data": "<string>",
            "verification_method": "<string>",
            "coinbase_credit_card_params": {
              "credit_card_account_id": "<string>"
            },
            "address_verification_info": {
              "source": "<string>",
              "avs_street_address": "ADDRESS_VERIFICATION_STATUS_UNSPECIFIED",
              "avs_postal_code": "ADDRESS_VERIFICATION_STATUS_UNSPECIFIED"
            },
            "account_name_inquiry": {
              "first_name_match": "MATCH_RESULT_UNSPECIFIED",
              "middle_name_match": "MATCH_RESULT_UNSPECIFIED",
              "last_name_match": "MATCH_RESULT_UNSPECIFIED",
              "name_match_indicator": "NAME_MATCH_INDICATOR_UNSPECIFIED"
            },
            "customer_name": "<string>",
            "customer_first_name": "<string>",
            "customer_last_name": "<string>",
            "customer_dob": {
              "month": "<string>",
              "day": "<string>",
              "year": "<string>"
            }
          },
          "zengin": {
            "account_holder": {
              "legal_name": "<string>",
              "identifier": "<string>",
              "type": "<string>"
            },
            "institution": {
              "bank_code": "<string>",
              "branch_code": "<string>"
            }
          },
          "uk": {
            "account_holder": {
              "legal_name": "<string>",
              "bban": "<string>",
              "sort_code": "<string>",
              "account_number": "<string>",
              "address": {
                "address1": "<string>",
                "address2": "<string>",
                "city": "<string>",
                "state": "<string>",
                "postal_code": "<string>",
                "country": "<string>",
                "uuid": "<string>",
                "id": "<string>"
              },
              "account_type": "UK_ACCOUNT_TYPE_UNSPECIFIED"
            },
            "institution": {
              "name": "<string>"
            },
            "customer_first_name": "<string>",
            "customer_last_name": "<string>",
            "email": "<string>",
            "phone_number": "<string>",
            "currency": "<string>",
            "open_banking_details": {
              "true_layer_bank_provider_id": "<string>",
              "open_banking_provider_id": "<string>"
            }
          },
          "sepa": {
            "account_holder": {
              "legal_name": "<string>",
              "iban": "<string>",
              "bban": "<string>"
            },
            "institution": {
              "bic": "<string>",
              "name": "<string>",
              "bank_country_code": "<string>",
              "bank_country_name": "<string>",
              "bank_address": "<string>"
            },
            "customer_first_name": "<string>",
            "customer_last_name": "<string>",
            "email": "<string>",
            "phone_number": "<string>"
          },
          "paypal": {
            "account_holder": {
              "paypal_id": "<string>",
              "paypal_pm_id": "<string>",
              "paypal_verified": true,
              "account_type": "<string>",
              "account_age": "<string>"
            },
            "merchant": {
              "merchant_account_id": "<string>"
            },
            "metadata": {
              "paypal_correlation_id": "<string>",
              "authorization_code": "<string>"
            },
            "email": "<string>",
            "owner_name": "<string>",
            "birth_date": "<string>",
            "phone_number": "<string>",
            "phone_type": "<string>",
            "billing_address": {
              "address1": "<string>",
              "address2": "<string>",
              "city": "<string>",
              "state": "<string>",
              "postal_code": "<string>",
              "country": "<string>",
              "uuid": "<string>",
              "id": "<string>"
            },
            "braintree_customer_id": "<string>",
            "payment_method_nonce": "<string>",
            "payer_id": "<string>"
          },
          "ledger_account": {
            "account_id": "<string>",
            "currency": "<string>",
            "owner": {
              "id": "<string>",
              "uuid": "<string>",
              "user_uuid": "<string>",
              "type": "UNKNOWN"
            },
            "account_uuid": "<string>",
            "account_name": "<string>"
          },
          "external_payment_method": {
            "payment_method_id": "<string>"
          },
          "pro_account": {
            "account_id": "<string>",
            "coinbase_account_id": "<string>",
            "user_id": "<string>",
            "currency": "<string>",
            "portfolio_id": "<string>"
          },
          "rtp": {
            "account_holder": {
              "legal_name": "<string>",
              "identifier": "<string>",
              "bank_account_id": "<string>"
            },
            "institution": {
              "routing_number": "<string>"
            },
            "currency": "<string>"
          },
          "venue": {
            "name": "<string>"
          },
          "ledger_named_account": {
            "name": "<string>",
            "currency": "<string>",
            "foreign_network": "<string>"
          },
          "custodial_pool": {
            "name": "<string>",
            "network": "<string>",
            "fiat_id": "<string>"
          },
          "apple_pay": {
            "braintree": {
              "nonce": "<string>",
              "correlation_id": "<string>"
            },
            "apple_pay": {
              "nonce": "<string>",
              "correlation_id": "<string>",
              "version": "<string>"
            },
            "user_id": "<string>",
            "postal_code": "<string>",
            "customer_name": "<string>",
            "address": {
              "address1": "<string>",
              "address2": "<string>",
              "city": "<string>",
              "state": "<string>",
              "postal_code": "<string>",
              "country": "<string>",
              "uuid": "<string>",
              "id": "<string>"
            },
            "six_digit_bin": "<string>",
            "last_four": "<string>",
            "issuing_country": "<string>",
            "issuing_bank": "<string>",
            "product_id": "<string>",
            "customer_dob": "<string>",
            "billing_address_id": "<string>",
            "currency": "<string>",
            "scheme": "UNKNOWN",
            "prepaid": "UNCERTAIN",
            "debit": "UNCERTAIN"
          },
          "default_account": {
            "user_uuid": "<string>",
            "currency": "<string>"
          },
          "remitly": {
            "account_holder": {
              "recipient_id": "<string>",
              "payout_method_type": "<string>",
              "recipient_version": "<string>",
              "currency": "<string>"
            }
          },
          "pro_internal_account": {
            "user_id": "<string>",
            "currency": "<string>"
          },
          "dapp_wallet_account": {
            "user_uuid": "<string>",
            "network": "<string>",
            "cohort_id": "<string>",
            "signing_backend": "<string>",
            "currency": "<string>"
          },
          "google_pay": {
            "braintree": {
              "nonce": "<string>",
              "correlation_id": "<string>"
            },
            "google_pay": {
              "nonce": "<string>",
              "correlation_id": "<string>",
              "version": "<string>"
            },
            "user_id": "<string>",
            "postal_code": "<string>",
            "customer_name": "<string>",
            "address": {
              "address1": "<string>",
              "address2": "<string>",
              "city": "<string>",
              "state": "<string>",
              "postal_code": "<string>",
              "country": "<string>",
              "uuid": "<string>",
              "id": "<string>"
            },
            "six_digit_bin": "<string>",
            "last_four": "<string>",
            "issuing_country": "<string>",
            "issuing_bank": "<string>",
            "product_id": "<string>",
            "customer_dob": "<string>",
            "billing_address_id": "<string>",
            "currency": "<string>",
            "scheme": "UNKNOWN",
            "prepaid": "UNCERTAIN",
            "debit": "UNCERTAIN"
          },
          "dapp_wallet_blockchain_address": {
            "network": "<string>",
            "address": "<string>",
            "cohort_id": "<string>",
            "user_uuid": "<string>",
            "pool": "<string>"
          },
          "zaakpay_mobikwik": {
            "phone_number": "<string>"
          },
          "deneb_upi": {
            "vpa_id": "<string>",
            "customer_first_name": "<string>",
            "customer_last_name": "<string>",
            "email": "<string>",
            "phone_number": "<string>",
            "pan": "<string>",
            "address": {
              "address1": "<string>",
              "address2": "<string>",
              "city": "<string>",
              "state": "<string>",
              "postal_code": "<string>",
              "country": "<string>",
              "uuid": "<string>",
              "id": "<string>"
            }
          },
          "bank_account": {
            "customer_account_type": "<string>",
            "customer_account_number": "<string>",
            "customer_routing_number": "<string>",
            "customer_name": "<string>",
            "currency": "<string>",
            "bank_name": "<string>",
            "ach_entry_class": "<string>",
            "verification_method": "<string>",
            "cdv_amount_1": {
              "amount": "<string>",
              "currency": "<string>"
            },
            "cdv_amount_2": {
              "amount": "<string>",
              "currency": "<string>"
            },
            "ach_invalid_account": true,
            "ach_bad_account": true,
            "received_non_nsf_return": true,
            "giactInfo": {
              "giact_item_id": "<string>",
              "giact_bank_result": "Get a list of authenticated accounts for the current user.
    
    GET
    
    /
    
    api
    
    /
    
    v3
    
    /
    
    brokerage
    
    /
    
    accounts
    
    List Accounts
    
    
    curl --request GET \
      --url https://api.coinbase.com/api/v3/brokerage/accounts \
      --header 'Authorization: Bearer <token>'
    
    
    {
      "has_next": true,
      "accounts": [
        {
          "uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
          "name": "BTC Wallet",
          "currency": "BTC",
          "available_balance": {
            "value": "1.23",
            "currency": "BTC"
          },
          "default": false,
          "active": true,
          "created_at": "2021-05-31T09:59:59.000Z",
          "updated_at": "2021-05-31T09:59:59.000Z",
          "deleted_at": "2021-05-31T09:59:59.000Z",
          "type": "FIAT",
          "ready": true,
          "hold": {
            "value": "1.23",
            "currency": "BTC"
          },
          "retail_portfolio_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
          "platform": "ACCOUNT_PLATFORM_CONSUMER"
        }
      ],
      "cursor": "789100",
      "size": 123
    }

#### Authorizations

Authorization

string

header

required

A JWT signed using your CDP API Key Secret, encoded in base64. Refer to the [Creating API Keys](/coinbase-app/authentication-authorization/api-key-authentication) section of our Coinbase App Authentication docs for information on how to generate your Bearer Token.

#### Query Parameters

limit

integer<int32>

The number of accounts to display per page. By default, displays 49 (max 250). If `has_next` is true, additional pages of accounts are available to be fetched. Use the `cursor` parameter to start on a specified page.

cursor

string

For paginated responses, returns all responses that come after this value.

retail_portfolio_id

string

(Deprecated) Only returns the accounts matching the portfolio ID. Only applicable for legacy keys. CDP keys will default to the key's permissioned portfolio.

#### Response

A successful response.

has_next

boolean

required

Whether there are additional pages for this query.

Example:

`true`

<string>", "giact_customer_result": "<string>", "giact_status": "<string>", "giact_last_updated_at": "<string>", "giact_account_added_date": "<string>", "giact_account_last_updated_date": "<string>" }, "vendor_verification_status": { "iav_status": "<string>", "md_status": "<string>", "email_verification_status": "<string>" }, "plaid_verification_info": { "plaid_bank_name": "<string>", "plaid_access_token": "<string>", "plaid_item_id": "<string>", "plaid_old_access_token": "<string>", "plaid_response": "<string>", "plaid_info": "<string>", "plaid_account_id": "<string>", "plaid_test_account": true, "plaid_link_account": true, "plaid_link_bank_name": "<string>", "balance": { "amount": "<string>", "currency": "<string>" }, "balance_updated_at": "<string>", "plaid_name_check": true, "plaid_public_token": "<string>", "account_number_mask": "<string>", "plaid_persistent_account_id": "<string>", "is_tokenized_account_number": true, "is_plaid_supported": true }, "stripe_verification_info": { "stripe_response": "<string>", "stripe_info": "<string>", "stripe_financial_connections_id": "<string>", "stripe_payment_method_id": "<string>", "stripe_test_account": true, "stripe_link_account": true, "stripe_link_bank_name": "<string>", "stripe_institution_id": "<string>", "balance": { "amount": "<string>", "currency": "<string>" }, "balance_updated_at": "<string>", "stripe_name_check": true } }, "identity_contract_call": { "network": "<string>", "address": "<string>" }, "deneb_imps": { "ifsc_code": "<string>", "account_number": "<string>", "customer_first_name": "<string>", "customer_last_name": "<string>", "email": "<string>", "phone_number": "<string>", "pan": "<string>", "address": { "address1": "<string>", "address2": "<string>", "city": "<string>", "state": "<string>", "postal_code": "<string>", "country": "<string>", "uuid": "<string>", "id": "<string>" } }, "allocation": { "id": "<string>", "legs": [ { "id": "<string>", "movements": [ { "id": "<string>", "source_account": { "account_id": "<string>", "currency": "<string>", "owner": { "id": "<string>", "uuid": "<string>", "user_uuid": "<string>", "type": "UNKNOWN" }, "account_uuid": "<string>", "account_name": "<string>" }, "destination_account": { "account_id": "<string>", "currency": "<string>", "owner": { "id": "<string>", "uuid": "<string>", "user_uuid": "<string>", "type": "UNKNOWN" }, "account_uuid": "<string>", "account_name": "<string>" }, "source_currency": "<string>", "target_currency": "<string>", "amount": { "amount": "<string>", "currency": "<string>" }, "fee": { "amount": "<string>", "currency": "<string>" } } ], "is_netted": true } ], "is_netted": true }, "liquidity_pool": { "network": "<string>", "pool": "<string>", "currency": "<string>", "account_id": "<string>", "from_address": "<string>" }, "zengin_v2": { "account_holder": { "legal_name": "<string>", "identifier": "<string>", "type": "<string>" }, "institution": { "bank_code": "<string>", "branch_code": "<string>" } }, "direct_deposit": { "direct_deposit_account": "<string>" }, "sepa_v2": { "account": { "legal_name": "<string>", "iban": "<string>", "bban": "<string>", "account_address": "<string>" }, "customer_first_name": "<string>", "customer_last_name": "<string>", "email": "<string>", "phone_number": "<string>", "customer_country": "<string>", "address": { "address1": "<string>", "address2": "<string>", "city": "<string>", "state": "<string>", "postal_code": "<string>", "country": "<string>", "uuid": "<string>", "id": "<string>" }, "supports_open_banking": true, "banking_circle_token": { "mandate_id": "<string>", "active": true, "balance_check_supported": true, "hosted_page_id": "<string>" }, "institution": { "bic": "<string>", "name": "<string>", "bank_country_code": "<string>", "bank_country_name": "<string>accounts

object[]

cursor

string

For paginated responses, returns all responses that come after this value.

Example:

`"789100"`

size

integer<int32>

Number of accounts returned