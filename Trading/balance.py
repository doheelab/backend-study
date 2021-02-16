import pyupbit

f = open("../save/upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1]
f.close()


# 잔고조회
# 원화 "KRW", 비트코인 "KRW-BTC"
upbit = pyupbit.Upbit(access, secret)
balance = upbit.get_balance("KRW")
print(balance)
