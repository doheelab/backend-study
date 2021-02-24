import time
import pyupbit
import numpy as np
import copy
import datetime

from pprint import pprint

from collections import deque

# import datetime
# datetime.datetime.strptime(orders[0]['created_at'],)

ask_history = deque([])
bid_history = deque([])

f = open("./save/upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)
ticker = "KRW-XRP"  # 리플
ticker = "KRW-NPXS"  # Paycoin


tick = 0.01
coin_num = 50000

buy_list = []
sell_list = []

# 지정가 매수
def buy_coin(ticker, price, coin_num):
    resp = upbit.buy_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량
    if "error" in resp:
        resp2 = upbit.buy_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량
        print("매수 오류:", resp["error"], "error" in resp2)
        return False or ("error" not in resp2)
    else:
        buy_message = "매수:" + str(resp["price"])
        print(buy_message)
        return True


# 지정가 매도
def sell_coin(ticker, price, coin_num):
    resp = ["error"]
    resp = upbit.sell_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량

    if "error" in resp:
        resp2 = upbit.sell_limit_order(ticker, price, coin_num)  # 티커, 주문가격, 주문량
        print("매도 오류:", resp["error"], "error" in resp2)
        return False or ("error" not in resp2)
    else:
        sell_message = "매도:" + str(resp["price"])
        print(sell_message)
        write_record(sell_message)
        return True


def sell_all(orders, ticker):
    balance = upbit.get_balance(ticker)
    resp = upbit.sell_market_order(ticker, balance)  # 티커, 잔고
    print(resp)


def check_ask_price(recent_prices):
    # 감소하지 않았음을 확인
    intensity = 0
    if len(recent_prices) < 5:
        return 0

    for i in range(5 - 1):
        if recent_prices[i] > recent_prices[i + 1]:
            intensity = 1
    if intensity > 0:
        return 0
    else:
        return 1


def check_ask_size(recent_prices):
    # 감소했음을 확인
    intensity = 0
    if len(recent_prices) < 5:
        return 0

    for i in range(5 - 1):
        if 0.8 * recent_prices[i] > recent_prices[i + 1]:
            intensity += 1
        elif recent_prices[i] < 0.9 * recent_prices[i + 1]:
            intensity -= 1
    if intensity > 0:
        return intensity
    else:
        return 0


def main(ticker):
    recent_ask_size = []
    recent_ask_size_2 = []
    recent_ask_price = []
    saved_price = 0
    bought = 0

    def transaction(
        idx,
        saved_idx,
        recent_ask_size,
        recent_ask_size_2,
        recent_ask_price,
        bought,
        saved_price,
        coin_num,
    ):
        # 호가정보
        orderbooks = pyupbit.get_orderbook(ticker)
        if not orderbooks:
            return False
        orderbook_units = orderbooks[0]["orderbook_units"]
        ask_price = orderbook_units[0]["ask_price"]
        ask_size_1 = orderbook_units[0]["ask_size"]
        bid_size_1 = orderbook_units[0]["bid_size"]
        ask_size_2 = orderbook_units[1]["ask_size"]
        bid_size_2 = orderbook_units[1]["bid_size"]
        recent_ask_size.append(int(ask_size_1))
        recent_ask_size_2.append(int(ask_size_2))
        recent_ask_price.append(ask_price)

        if len(recent_ask_size) > 5:
            recent_ask_size = recent_ask_size[1:]
            recent_ask_size_2 = recent_ask_size_2[1:]
            recent_ask_price = recent_ask_price[1:]

        orders = upbit.get_order(ticker)
        amount = upbit.get_balance(ticker)
        if len(orders) == 0 and ask_price > 1:
            if bought == 1:

                print("saved_price:", np.round(saved_price + tick, 2))
                sell_coin(ticker, np.round(saved_price + tick, 2), amount)
                bought = 0

            elif bought == 0:
                buy_intensity = (
                    check_ask_size(recent_ask_size)
                    # and check_ask_size(recent_ask_size_2)
                    and check_ask_price(recent_ask_price)
                )
                buy_condition = (
                    (ask_size_1 * 3 + ask_size_2 < bid_size_1)
                    # and bid_size_1 * 0.5 < bid_size_2
                    and buy_intensity
                )
                if ask_size_1 * 3 + ask_size_2 < bid_size_1:
                    print(
                        ask_price,
                        bid_size_1 * 0.5 < bid_size_2,
                        check_ask_size(recent_ask_size),
                        check_ask_size(recent_ask_size_2),
                        check_ask_price(recent_ask_price),
                    )

                if buy_condition:
                    buy_coin(ticker, ask_price, coin_num)
                    bought = 1
                    saved_price = ask_price
                    saved_idx = idx
                    idx = 0

        if len(orders) > 0 and (saved_price - ask_price > 5 * tick):
            clear_bid(orders, all=True)
            clear_ask(orders, all=True)
            sell_all(orders, ticker)
            print(f"실패: {saved_price}에 사서 {ask_price} 이하에 팜")
            bought = 0
        time.sleep(0.2)

        return (
            saved_idx,
            recent_ask_size,
            recent_ask_size_2,
            recent_ask_price,
            bought,
            saved_price,
        )

    idx = 0
    saved_idx = 0

    orders = upbit.get_order(ticker)

    # if len(orders) > 0:
    clear_bid(orders, all=True)
    clear_ask(orders, all=True)
    sell_all(orders, ticker)

    while True:
        try:
            (
                saved_idx,
                recent_ask_size,
                recent_ask_size_2,
                recent_ask_price,
                bought,
                saved_price,
            ) = transaction(
                idx,
                saved_idx,
                recent_ask_size,
                recent_ask_size_2,
                recent_ask_price,
                bought,
                saved_price,
                coin_num,
            )
        except Exception as e:
            print(e)
            pass
        idx += 1
        if idx == 1000:
            idx = 0


def write_record(message):
    now = datetime.datetime.now()
    today = now.strftime("%m%d")
    f = open(f"./record/{ticker}-{today}.txt", "a")
    f.write(message)
    f.close()


def clear_bid(orders, all=False):
    bid_orders = [order for order in orders if order["side"] == "bid"]
    bid_orders = sorted(bid_orders, key=lambda x: x["remaining_fee"], reverse=True)
    # if len(bid_orders) < 2:
    #     return

    if all == False:
        bid_orders = bid_orders[-1:]
    for order in bid_orders:
        upbit.cancel_order(uuid=order["uuid"])


def clear_ask(orders, all=False):
    ask_orders = [order for order in orders if order["side"] == "ask"]
    ask_orders = sorted(ask_orders, key=lambda x: x["remaining_fee"])
    # if len(ask_orders) < 2:
    #     return
    if all == False:
        ask_orders = ask_orders[-1:]
    for order in ask_orders:
        upbit.cancel_order(uuid=order["uuid"])


if __name__ == "__main__":
    main(ticker)
