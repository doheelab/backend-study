import time
import pyupbit
import numpy as np
import copy
import datetime

from pprint import pprint

from collections import deque

ask_history = deque([])
bid_history = deque([])

f = open("./save/upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)
# ticker = "KRW-XRP"  # 리플
# ticker = "KRW-CVC"  # 시빅
# ticker = "KRW-ZIL"  # 질리카
# ticker = "KRW-NPXS"  # 펀디엑스
# ticker = "KRW-SAND"  # 샌드박스
# ticker = "KRW-ARDR"  # 아더
# ticker = "KRW-EMC2"  # 아인스타이늄
# ticker = "KRW-SNT"  # 스테이터스네트워크토큰
ticker = "KRW-XRP"  # 리플


tick = 1
coin_num = 40

buy_list = []
sell_list = []

# 지정가 매수
def buy_coin(ticker, price, coin_num):
    resp = upbit.buy_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량
    if "error" in resp:
        resp2 = upbit.buy_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량
        print("매수 오류:", resp["error"], "error" in resp2)
        return False
    else:
        buy_message = "매수:" + str(resp["price"])
        print(buy_message)
        write_record(buy_message)
        return True


# 지정가 매도
def sell_coin(ticker, price, coin_num):
    resp = ["error"]
    resp = upbit.sell_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량

    if "error" in resp:
        resp2 = upbit.sell_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량
        print("매도 오류:", resp["error"], "error" in resp2)
        return False
    else:
        sell_message = "매도:" + str(resp["price"])
        print(sell_message)
        write_record(sell_message)
        return True


def sell_all(ticker):
    balance = upbit.get_balance(ticker)
    resp = upbit.sell_market_order(ticker, balance)  # 티커, 잔고
    print(resp)


def check_decrease(recent_prices):
    intensity = 0
    for i in range(5 - 1):
        if 0.9 * recent_prices[i] > recent_prices[i + 1]:
            intensity += 1
        elif recent_prices[i] < 0.9 * recent_prices[i + 1]:
            intensity -= 1
    if intensity > 0:
        return intensity
    else:
        return 0


def main(ticker):
    idx = 0
    initialized = 0
    save_benefit = 0
    recent_ask_size = []
    recent_bid_size = []
    trend = 1
    init = 0

    def transaction(
        idx, ticker, recent_ask_size, recent_bid_size, trend, save_benefit, init
    ):

        # 호가정보
        orderbooks = pyupbit.get_orderbook(ticker)
        if not orderbooks:
            return False
        orderbook_units = orderbooks[0]["orderbook_units"]
        ask_price = orderbook_units[0]["ask_price"]
        bid_price = orderbook_units[0]["bid_price"]
        ask_size_1 = orderbook_units[0]["ask_size"]
        bid_size_1 = orderbook_units[0]["bid_size"]
        ask_size_2 = orderbook_units[1]["ask_size"]
        bid_size_2 = orderbook_units[1]["bid_size"]
        recent_ask_size.append(int(ask_size_1))
        recent_bid_size.append(int(bid_size_1))

        if len(recent_ask_size) > 5:
            recent_ask_size = recent_ask_size[1:]
            recent_bid_size = recent_bid_size[1:]

        if idx > 25:
            # sell
            sell_intensity = check_decrease(recent_bid_size)
            buy_intensity = check_decrease(recent_ask_size)
            sell_condition = (
                ask_size_1 > bid_size_1 * 5 + bid_size_2 * 2
                and ask_size_1 * 0.5 < ask_size_2
                and sell_intensity
            )

            buy_condition = (
                ask_size_1 * 5 + ask_size_2 * 2 < bid_size_1
                and bid_size_1 * 0.5 < bid_size_2
                and buy_intensity
            )

            if sell_condition:
                if sell_intensity > 2:
                    multiplier = 2
                else:
                    multiplier = 1
                amount = int(coin_num * multiplier)
                if sell_coin(ticker, bid_price, amount):
                    buy_coin(ticker, bid_price - tick, amount)
                idx = 0
            if buy_condition:
                if buy_intensity > 2:
                    multiplier = 2
                else:
                    multiplier = 1
                multiplier *= trend
                amount = int(coin_num * multiplier)
                if buy_coin(ticker, ask_price, amount):
                    sell_coin(ticker, ask_price + tick, amount)
                idx = 0

        if idx % 50 == 0:
            orders = upbit.get_order(ticker)
            to_bid = [
                float(order["volume"]) * bid_price
                for order in orders
                if order["side"] == "bid"
            ]
            to_ask = [
                float(order["volume"]) * bid_price
                for order in orders
                if order["side"] == "ask"
            ]
            money = int(
                upbit.get_balance(ticker="KRW")
                + (upbit.get_balance(ticker=ticker)) * bid_price
                + np.sum(to_ask)
                + np.sum(to_bid)
            )

            benefit = money - init
            message = f"{money}, {bid_price}, {benefit}, {trend} \n"
            print(message)
            write_record(message)
            if abs(benefit - save_benefit) < 1000:
                diff = benefit - save_benefit
            else:
                diff = 0
            trend = np.clip(np.round(1.5 ** (diff / bid_price), 2), 0.9, 2)
            save_benefit = copy.copy(benefit)
        elif idx == 3000:
            idx = 0
        time.sleep(0.3)
        idx += 1
        return (
            idx,
            bid_price,
            recent_ask_size,
            recent_bid_size,
            trend,
            save_benefit,
        )

    while True:
        try:
            (
                idx,
                bid_price,
                recent_ask_size,
                recent_bid_size,
                trend,
                save_benefit,
            ) = transaction(
                idx, ticker, recent_ask_size, recent_bid_size, trend, save_benefit, init
            )
        except Exception as e:
            print(e)
            pass
        if not initialized:
            orders = upbit.get_order(ticker)
            to_bid = [
                float(order["volume"]) * bid_price
                for order in orders
                if order["side"] == "bid"
            ]

            to_ask = [
                float(order["volume"]) * bid_price
                for order in orders
                if order["side"] == "ask"
            ]

            init = int(
                upbit.get_balance(ticker="KRW")
                + (upbit.get_balance(ticker=ticker)) * bid_price
                + np.sum(to_ask)
                + np.sum(to_bid)
            )

            write_record("-----" + str(bid_price) + "원" + "----- \n")
            initialized = 1


def write_record(message):
    now = datetime.datetime.now()
    today = now.strftime("%m%d")
    f = open(f"./record/{ticker}-{today}.txt", "a")
    f.write(message)
    f.close()


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
    main(ticker)
