---
exchange: binance
source_url: https://developers.binance.com/docs/margin_trading/market-data
api_type: Market Data
updated_at: 2026-01-15T23:48:27.731784
---

# Cross margin collateral ratio (MARKET_DATA)

## API Description[​](/docs/margin_trading/market-data#api-description "Direct link to API Description")

Cross margin collateral ratio

## HTTP Request[​](/docs/margin_trading/market-data#http-request "Direct link to HTTP Request")

GET `/sapi/v1/margin/crossMarginCollateralRatio`

## Request Weight[​](/docs/margin_trading/market-data#request-weight "Direct link to Request Weight")

**100(IP)**

## Request Parameters[​](/docs/margin_trading/market-data#request-parameters "Direct link to Request Parameters")

None

## Response Example[​](/docs/margin_trading/market-data#response-example "Direct link to Response Example")
    
    
    [  
      {  
        "collaterals": [  
          {  
            "minUsdValue": "0",  
            "maxUsdValue": "13000000",  
            "discountRate": "1"  
          },  
          {  
            "minUsdValue": "13000000",  
            "maxUsdValue": "20000000",  
            "discountRate": "0.975"  
          },  
          {  
            "minUsdValue": "20000000",  
            "discountRate": "0"  
          }  
        ],  
        "assetNames": [  
          "BNX"  
        ]  
      },  
      {  
        "collaterals": [  
          {  
            "minUsdValue": "0",  
            "discountRate": "1"  
          }  
        ],  
        "assetNames": [  
          "BTC",  
          "BUSD",  
          "ETH",  
          "USDT"  
        ]  
      }  
    ]

---

# 全仓币种质押率 (MARKET_DATA)

## 接口描述[​](/docs/zh-CN/margin_trading/market-data#接口描述 "接口描述的直接链接")

全仓币种质押率

## HTTP请求[​](/docs/zh-CN/margin_trading/market-data#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/margin/crossMarginCollateralRatio`

## 请求权重[​](/docs/zh-CN/margin_trading/market-data#请求权重 "请求权重的直接链接")

**100(IP)**

## 请求参数[​](/docs/zh-CN/margin_trading/market-data#请求参数 "请求参数的直接链接")

None

## 响应示例[​](/docs/zh-CN/margin_trading/market-data#响应示例 "响应示例的直接链接")
    
    
    [  
      {  
        "collaterals": [  
          {  
            "minUsdValue": "0",  
            "maxUsdValue": "13000000",  
            "discountRate": "1"  
          },  
          {  
            "minUsdValue": "13000000",  
            "maxUsdValue": "20000000",  
            "discountRate": "0.975"  
          },  
          {  
            "minUsdValue": "20000000",  
            "discountRate": "0"  
          }  
        ],  
        "assetNames": [  
          "BNX"  
        ]  
      },  
      {  
        "collaterals": [  
          {  
            "minUsdValue": "0",  
            "discountRate": "1"  
          }  
        ],  
        "assetNames": [  
          "BTC",  
          "BUSD",  
          "ETH",  
          "USDT"  
        ]  
      }  
    ]