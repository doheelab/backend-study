import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv("house_prices.csv")
df.head()


df["intercept"] = 1
df_new = df.join(pd.get_dummies(df.neighborhood))

# 잘못된 예시 (다중공선성 발생)
sm.OLS(df_new["price"], df_new[["A", "B", "C", "intercept"]]).fit().summary()

# 올바른 예시 (column 하나를 drop)
sm.OLS(df_new["price"], df_new[["B", "C", "intercept"]]).fit().summary()
