import pyupbit
from pprint import pprint

orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint(orderbooks)

pyupbit.get_orderbook()[0]["orderbook_units"]

