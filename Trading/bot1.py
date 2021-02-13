import time
import pyupbit
import numpy as np
from pprint import pprint


f = open("../save/upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1]
f.close()

upbit = pyupbit.Upbit(access, secret)
ticker = "KRW-XRP"  # 리플
# ticker = "KRW-CVC"  # 시빅
buy_list = []
sell_list = []

# 지정가 매수
def buy(ticker, price, stock_num):
    resp = upbit.buy_limit_order(ticker, price, stock_num)  # 티커, 주문가격, 주문량
    buy_list.append(price)
    # pprint(resp)


# 지정가 매도
def sell(ticker, price, stock_num):
    # xrp_balance = upbit.get_balance(ticker)
    resp = ["error"]
    resp = upbit.sell_limit_order(ticker, price, stock_num)  # 티커, 주문가격, 주문량
    # pprint(resp)

    if "error" in resp:
        return False
    else:
        return True


# 주문내역
upbit.get_order(ticker)


def practice(ticker):
    ask_price = 0
    can_buy = 1
    idx = 0
    rate = 10
    stock_num = 2
    bought = 0
    sold = 0
    while True:
        changed = 0
        will_change = 0

        # 호가정보
        orderbooks = pyupbit.get_orderbook(ticker)
        units = orderbooks[0]["orderbook_units"][0]
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

        ask_size = units["ask_size"]
        bid_size = units["bid_size"]

        if ask_size / bid_size > rate and can_buy and idx > 10 and sold == 0:
            will_change = "down"
            can_buy += 1
            if can_buy == 3:
                if not sell(ticker, bid_price, stock_num):
                    can_buy = 0
                    continue
                if upbit.get_balance("KRW") > ask_price * stock_num:
                    buy(ticker, bid_price - 1, stock_num)
                can_buy = 0
                bought = 1
                idx = 0

        elif ask_size / bid_size < 1 / rate and can_buy and idx > 10 and bought == 0:
            balance = upbit.get_balance(ticker)
            if balance < 5 and upbit.get_balance("KRW") > ask_price * stock_num:
                will_change = "up"
                can_buy += 1
                if can_buy == 3:
                    buy(ticker, ask_price, stock_num)
                    sell(ticker, ask_price + 1, stock_num)
                    can_buy = 0
                sold = 1
                idx = 0
        message = f"{ask_price}, {bid_price}, {np.round(ask_size, 2)}, {np.round(bid_size, 2)} "
        if changed:
            message += changed

        if will_change:
            message += " " + will_change

        idx += 1
        if idx % 50 == 0:
            orders = upbit.get_order(ticker)
            to_bid = [order["price"] for order in orders if order["side"] == "bid"]
            to_ask = [order["price"] for order in orders if order["side"] == "ask"]
            bought = 0
            sold = 0

            print(
                "현재자산:",
                int(
                    upbit.get_balance(ticker="KRW")
                    + upbit.get_balance(ticker=ticker) * bid_price
                    + len(to_ask) * bid_price * 2
                    + np.sum(np.array(to_bid, dtype=float)) * 2
                ),
            )
        time.sleep(0.2)

        if idx == 600:

            clear_bid(orders)
            clear_ask(orders)
            idx = 0


def clear_bid(orders):
    bid_orders = [order for order in orders if order["side"] == "bid"]
    bid_orders = sorted(bid_orders, key=lambda x: x["remaining_fee"], reverse=True)
    if len(bid_orders) < 2:
        return
    for order in bid_orders[1:]:
        upbit.cancel_order(uuid=order["uuid"])


def clear_ask(orders):
    bid_orders = [order for order in orders if order["side"] == "ask"]
    bid_orders = sorted(bid_orders, key=lambda x: x["remaining_fee"])
    if len(bid_orders) < 2:
        return
    for order in bid_orders[-1:]:
        upbit.cancel_order(uuid=order["uuid"])


if __name__ == "__main__":
    practice(ticker)
