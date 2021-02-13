import pyupbit
from pprint import pprint

f = open("../save/upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1]
f.close()

upbit = pyupbit.Upbit(access, secret)
ticker = "KRW-XRP"  # 리플

# 호가정보
orderbooks = pyupbit.get_orderbook(ticker)
pprint(orderbooks)


# 지정가 매수
resp = upbit.buy_limit_order(ticker, 200, 10)  # 티커, 주문가격, 주문량
uuid = resp["uuid"]
pprint(resp)

# 지정가 매도
xrp_balance = upbit.get_balance(ticker)
resp = upbit.sell_limit_order(ticker, 265, xrp_balance)  # 티커, 주문가격, 주문량
pprint(resp)

# 시장가 매수 (매도 1호가)
resp = upbit.buy_market_order(ticker, 10000)  # 티커, 매수가격
uuid = resp["uuid"]
pprint(resp)

# 시장가 매도 (매수 1호가)
balance = upbit.get_balance(ticker)
resp = upbit.buy_market_order(ticker, balance)  # 티커, 잔고
pprint(resp)

params = {"state": "wait"}
upbit.get_order(ticker)

# 주문 취소
resp = upbit.cancel_order(uuid=uuid)
print(resp)
