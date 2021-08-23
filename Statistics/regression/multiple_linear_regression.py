import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("house_prices.csv")
df.head()
df["intercept"] = 1

# 단순선형회귀
lm_bed = sm.OLS(df["price"], df[["intercept", "bedrooms"]])
results_bed = lm_bed.fit()
results_bed.summary()

# 다중선형회귀
mlr = sm.OLS(df["price"], df[["intercept", "area", "bedrooms", "bathrooms"]])
results_mlr = mlr.fit()
results_mlr.summary()
