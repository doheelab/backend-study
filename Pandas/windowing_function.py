import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

gld = pdr.get_data_yahoo("GLD", "2016-11-08")
gld.head()

gld_close = pd.DataFrame(gld.Close)


# pd.Series([1, 2, 3, 4, 5, 7, 8, 9, 10])
# interval = 3
# rolling_max = pd.Series([1, 2, 3, 4, 5, 7, 8, 9, 10]).rolling(interval).max()
# rolling_max = pd.Series([1, 2, 3, 4, 5, 7, 8, 9, 10]).rolling(interval).min()


gld_close.Close.rolling(9).mean().iloc[10]


gld_close["MA_9"] = gld_close.Close.rolling(9).mean().shift()
gld_close["MA_21"] = gld_close.Close.rolling(21).mean()

gld_close["MA_9"].head(12)

plt.figure(figsize=(15, 10))
plt.grid(True)
plt.plot(gld_close["Close"], label="GLD")
plt.plot(gld_close["MA_9"], label="MA 9 day")
plt.plot(gld_close["MA_21"], label="MA 21 day")
plt.legend(loc=2)


gld_close["change"] = np.log(gld_close["Close"] / gld_close["Close"].shift())


plt.plot(gld_close.change)

gld_close["Volatility"] = gld_close.change.rolling(21).std().shift()
gld_close["Volatility"].plot()


# offset expected change 1-day
gld_close["exp_chng"] = gld_close["Volatility"] * gld_close["Close"].shift()
gld_close["actual_chng"] = gld_close["Close"] - gld_close["Close"].shift()

# running more than once will
gld_close = pd.DataFrame(gld_close.iloc[22:])

gld_close["Magnitude"] = gld_close["actual_chng"] / gld_close["exp_chng"]

gld_close["abs_magni"] = np.abs(gld_close["Magnitude"])
gld_close.head()

plt.scatter(gld_close["actual_chng"], gld_close["abs_magni"])

