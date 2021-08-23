import numpy as np 
import pandas as pd 
import statsmodels.api as sm; 

df = pd.read_csv('./house_price_area_only.csv') 

# 우선, intercept(절편) column을 추가해줘야 합니다. 거의 모든 회귀 모델에서 intercept column을 추가해야 합니다.
df['intercept'] = 1

lm = sm.OLS(df['price'], df[['intercept', 'area']])
results = lm.fit()
results.summary()
