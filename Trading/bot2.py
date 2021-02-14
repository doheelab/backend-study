import time
import pyupbit
import numpy as np
import copy
from pprint import pprint

from collections import deque

ask_history = deque([])
bid_history = deque([])

ask_history.append(2)

ask_history[0]


f = open("../save/upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1]
f.close()

upbit = pyupbit.Upbit(access, secret)
# ticker = "KRW-XRP"  # 리플
# ticker = "KRW-CVC"  # 시빅
# ticker = "KRW-ZIL"  # 질리카
# ticker = "KRW-NPXS"  # 펀디엑스
ticker = "KRW-SAND"  # 샌드박스
tick = 1
stock_num = 4

buy_list = []
sell_list = []

# 지정가 매수
def buy(ticker, price, stock_num):
    resp = upbit.buy_limit_order(ticker, price, stock_num)  # 티커, 주문가격, 주문량
    if "error" in resp:
        resp2 = upbit.buy_limit_order(ticker, price, stock_num)  # 티커, 주문가격, 주문량
        print("매수 오류:", resp["error"], "error" in resp2)


# 지정가 매도
def sell(ticker, price, stock_num):
    resp = ["error"]
    resp = upbit.sell_limit_order(ticker, price, stock_num)  # 티커, 주문가격, 주문량

    if "error" in resp:
        resp2 = upbit.sell_limit_order(ticker, price, stock_num)  # 티커, 주문가격, 주문량
        print("매도 오류:", resp["error"], "error" in resp2)
        return False
    else:
        return True


def sell_all(ticker):
    balance = upbit.get_balance(ticker)
    resp = upbit.sell_market_order(ticker, balance)  # 티커, 잔고
    print(resp)


def practice(ticker):
    ask_price = 0
    can_buy = 1
    idx = 0
    ratio = 8
    initialized = 0
    benefit = 0
    save_benefit = 0

    while True:
        changed = 0
        will_change = 0

        # 호가정보
        orderbooks = pyupbit.get_orderbook(ticker)
        units = orderbooks[0]["orderbook_units"][0]
        max_bid = np.max(
            [order["bid_size"] for order in orderbooks[0]["orderbook_units"]]
        )
        if ask_price > units["ask_price"]:
            ask_price = units["ask_price"]
            bid_price = units["bid_price"]
            changed = "went down"
            if can_buy > 0:
                can_buy = 0
            else:
                can_buy = 1
        elif ask_price < units["ask_price"]:
            ask_price = units["ask_price"]
            bid_price = units["bid_price"]
            changed = "went up"
            if can_buy > 0:
                can_buy = 0
            else:
                can_buy = 1
        if not initialized:
            init = int(
                upbit.get_balance(ticker="KRW")
                + upbit.get_balance(ticker=ticker) * bid_price
            )
            initialized = 1
        ask_size = units["ask_size"]
        bid_size = units["bid_size"]

        if ask_size / bid_size < 1 / ratio and can_buy and idx > 10:
            if upbit.get_balance("KRW") > ask_price * stock_num:
                will_change = "up"
                can_buy += 1
                if can_buy > 1:
                    buy(ticker, ask_price, stock_num)
                    sell(ticker, ask_price + tick, stock_num)
                    can_buy = 1
                    idx = 0
        message = f"{ask_price}, {bid_price}, {np.round(ask_size, 2)}, {np.round(bid_size, 2)} "
        if changed:
            message += changed

        if will_change:
            message += " " + will_change

        idx += 1
        if idx % 20 == 0:
            orders = upbit.get_order(ticker)
            to_bid = [order["price"] for order in orders if order["side"] == "bid"]
            to_ask = [order["price"] for order in orders if order["side"] == "ask"]
            money = int(
                upbit.get_balance(ticker="KRW")
                + upbit.get_balance(ticker=ticker) * bid_price
                + len(to_ask) * bid_price * stock_num
                + np.sum(np.array(to_bid, dtype=float)) * stock_num
            )
            benefit = money - init

            print(money, benefit)
        time.sleep(0.1)

        # 일정 이상의 손실
        if 100 < save_benefit - benefit:
            clear_ask(orders, all=True)
            sell_all(ticker)
            save_benefit = benefit
        elif idx == 600:
            save_benefit = copy.copy(benefit)
        elif idx == 3000:
            clear_bid(orders)
            clear_ask(orders)
            save_benefit = copy.copy(benefit)
            idx = 0


def clear_bid(orders, all=False):
    bid_orders = [order for order in orders if order["side"] == "bid"]
    bid_orders = sorted(bid_orders, key=lambda x: x["remaining_fee"], reverse=True)
    if len(bid_orders) < 2:
        return

    if all == False:
        bid_orders = bid_orders[-1:]
    for order in bid_orders:
        upbit.cancel_order(uuid=order["uuid"])


def clear_ask(orders, all=False):
    ask_orders = [order for order in orders if order["side"] == "ask"]
    ask_orders = sorted(ask_orders, key=lambda x: x["remaining_fee"])
    if len(ask_orders) < 2:
        return

    if all == False:
        ask_orders = ask_orders[-1:]
    for order in ask_orders:
        upbit.cancel_order(uuid=order["uuid"])


if __name__ == "__main__":
    practice(ticker)
