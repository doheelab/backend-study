import pandas as pd
import numpy as np
import seaborn as sns
from patsy import dmatrices
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv("house_prices.csv")
df["intercept"] = 1
df.head()

# scatter plot을 통해 다중공선성 파악하기
sns.pairplot(df[["bedrooms", "bathrooms", "area"]])

# VIF Factor 계산하기
y, X = dmatrices("price ~ area + bedrooms + bathrooms", df, return_type="dataframe")

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns

# VIF 10 이상 변수 drop을 통한 다중공선성 해결 실습

# bathrooms 변수를 제거하고 OLS
lm = sm.OLS(df["price"], df[["intercept", "bedrooms", "area"]])
results = lm.fit()
results.summary()

# bathrooms 변수를 제거하고 VIF Factor 구하기
y, X = dmatrices("price ~ area + bedrooms", df, return_type="dataframe")

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns
vif
