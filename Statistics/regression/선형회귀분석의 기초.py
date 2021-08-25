import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


# 데이터 생성
bias = 100
X0, y, w = make_regression(
    n_samples=200, n_features=1, bias=bias, noise=10, coef=True, random_state=1
)
# 상수항 추가
X = sm.add_constant(X0)
y = y.reshape(len(y), 1)

# x_new, y_new 생성 생성
x_new = np.linspace(np.min(X0), np.max(X0), 10)
X_new = sm.add_constant(x_new)  # 상수항 결합
w = np.linalg.inv(X.T @ X) @ X.T @ y
y_new = np.dot(X_new, w)

# NumPy를 이용한 선형 회귀 분석

model = LinearRegression(fit_intercept=True)
model = model.fit(X, y)
y_new = model.predict(X_new)

plt.scatter(X0, y, label="원래 데이터")
plt.plot(x_new, y_new, "rs-", label="회귀분석 예측")
plt.xlabel("x")
plt.ylabel("y")
plt.title("선형 회귀분석의 예")
plt.legend()
plt.show()

# (Type 1) OLS 명령으로 선형회귀
df = pd.DataFrame({"x": X0[:, 0], "y": y[:, 0]})
dfy = df[["y"]]
dfX = sm.add_constant(df[["x"]])
model = sm.OLS(dfy, dfX)
result = model.fit()

# (Type 2) formula 문자열을 사용하여 모형을 만들기
model = sm.OLS.from_formula("y ~ x", data=df)
result = model.fit()
print(result.summary())

#######################################

# 보스턴 집값 예측 (P값이 높은 변수 존재)

from sklearn.datasets import load_boston

boston = load_boston()

dfX0 = pd.DataFrame(boston.data, columns=boston.feature_names)
dfX = sm.add_constant(dfX0)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])

model_boston2 = sm.OLS(dfy, dfX)
result_boston2 = model_boston2.fit()
print(result_boston2.summary())
