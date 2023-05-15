
import asyncio, json, time, websockets

from dydx3 import Client
from dydx3.helpers.request_helpers import generate_now_iso
from web3 import Web3
from dydx3.constants import *


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



# order_response = private_client.private.create_order(**order_params)
# order_id = order_response['order']['id']
