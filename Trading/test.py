import time
import pyupbit
import numpy as np
from pprint import pprint
from price import log_price

f = open("../save/upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1]
f.close()

upbit = pyupbit.Upbit(access, secret)
ticker = "KRW-XRP"  # 리플

log_price(ticker)
