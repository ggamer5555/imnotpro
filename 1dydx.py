
#{"0xA5f51a1A61D374dd97a51e946F9aB9e16Af0f0E3":{"walletAddress":"0xA5f51a1A61D374dd97a51e946F9aB9e16Af0f0E3","secret":"nNUX8jGxtsQqCSQPxAC607Z0KJKSEAE8r7zxZdfc","key":"6193757d-d7ec-faf9-2894-15fc7238284d","passphrase":"AjdZhHPKcZlku4_018mh","legacySigning":false,"walletType":"WALLET_CONNECT"}}
#{"0xA5f51a1A61D374dd97a51e946F9aB9e16Af0f0E3":{"walletAddress":"0xA5f51a1A61D374dd97a51e946F9aB9e16Af0f0E3","publicKey":"05140c18366f41ceef44f489485ca398d01f1037dd1e9f3bee24cab7dd3c610d","publicKeyYCoordinate":"01cc79c58fa55e345ec0586989a5454ea6b97eac296fc4dcc7abd5f19397b840","privateKey":"02b4c1d091e9545eae9fbbe964e24ff659c615fd4ce046db04fcac7a94d8c679","legacySigning":false,"walletType":"WALLET_CONNECT"}}

import asyncio, json, time, websockets
from sortedcontainers import SortedDict

from dydx3 import Client
from dydx3.helpers.request_helpers import generate_now_iso
from web3 import Web3
from dydx3.constants import *

# from dydx3 import Client
# from web3 import Web3

# from dydx3 import Client
# from dydx3.constants import API_HOST_GOERLI
# from dydx3.constants import NETWORK_ID_GOERLI
# from web3 import Web3

# # Ganache test address.
# ETHEREUM_ADDRESS = '0xA5f51a1A61D374dd97a51e946F9aB9e16Af0f0E3'

# # Ganache node.
# WEB_PROVIDER_URL = 'http://localhost:8545'

# client = Client(
#     network_id=NETWORK_ID_GOERLI,
#     host=API_HOST_GOERLI,
#     default_ethereum_address=ETHEREUM_ADDRESS,
#     web3=Web3(Web3.HTTPProvider(WEB_PROVIDER_URL)),
# )

# # Set STARK key.
# stark_key_pair_with_y_coordinate = client.onboarding.derive_stark_key()
# client.stark_private_key = stark_key_pair_with_y_coordinate['private_key']
# (public_x, public_y) = (
#     stark_key_pair_with_y_coordinate['public_key'],
#     stark_key_pair_with_y_coordinate['public_key_y_coordinate'],
# )

# # Onboard the account.
# onboarding_response = client.onboarding.create_user(
#     stark_public_key=public_x,
#     stark_public_key_y_coordinate=public_y,
# )
# print('onboarding_response', onboarding_response)

# # Query a private endpoint.
# accounts_response = client.private.get_accounts()
# print('accounts_response', accounts_response)



#
# Access public API endpoints.
client = Client(
    host=API_HOST_MAINNET,
)
client.public.get_markets()

price=client.public.get_candles(MARKET_BTC_USD, resolution="5MINS")


candles = client.public.get_candles(
  market=MARKET_BTC_USD,
  resolution='1DAY',
)
candles

from datetime import datetime
import matplotlib.pyplot as plt

now = datetime.now().isoformat()

historical_funding = client.public.get_historical_funding(
  market=MARKET_BTC_USD,
    effective_before_or_at = now
)

historical_funding
# from dydx3.constants import MARKET_BTC_USD

# orderbook = client.public.get_orderbook(
#   market=MARKET_BTC_USD,
# )


# ETHEREUM_ADDRESS = '0xA5f51a1A61D374dd97a51e946F9aB9e16Af0f0E3'
# private_client = Client(
#       host='https://api.dydx.exchange',
#       api_key_credentials={ 'key': '6193757d-d7ec-faf9-2894-15fc7238284d',
#                             'secret': 'nNUX8jGxtsQqCSQPxAC607Z0KJKSEAE8r7zxZdfc',
#                             'passphrase': 'AjdZhHPKcZlku4_018mh'},
#       stark_private_key='02b4c1d091e9545eae9fbbe964e24ff659c615fd4ce046db04fcac7a94d8c679',
#       default_ethereum_address=ETHEREUM_ADDRESS
# )

# # Get our position ID.
# account_response = private_client.private.get_account()
# position_id = account_response['account']['positionId']


# # Post an bid at a price that is unlikely to match.
# order_params = {
#     'position_id': position_id,
#     'market': MARKET_BTC_USD,
#     'side': ORDER_SIDE_BUY,
#     'order_type': ORDER_TYPE_LIMIT,
#     'post_only': True,
#     'size': '0.0777',
#     'price': '20',
#     'limit_fee': '0.0015',
#     'expiration_epoch_seconds': time.time() + 5,
# }
# order_response = private_client.private.create_order(**order_params)
# order_id = order_response['order']['id']
