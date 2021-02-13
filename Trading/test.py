# # Rest API
# import requests

# url = "http://api.upbit.com/v1/market/all"
# params = {"isDetails":"True"}
# resp = requests.get(url, params=params)
# data = resp.json()
# print(data)

# 마켓 코드 조회
import pyupbit

tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)

# 시세 캔들 조회
# ohlcv: open, high, low, close, volume

import pyupbit

# 최대 200개 받아오기
df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
# 일봉 받아오기
df = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=100)
df

# 현재가 가져오기
price = pyupbit.get_current_price("KRW-BTC")
price

# 여러종목 현재가
tickers = ["KRW-BTC", "KRW-XRP"]
price = pyupbit.get_current_price(tickers)
price


# 호가정보
# 매수, 매도 15호가 제공
import pprint as pprint

orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint(orderbooks)

