### 참고자료: https://datascienceschool.net/03%20machine%20learning/04.02%20%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D%EC%9D%98%20%EA%B8%B0%EC%B4%88.html


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

# 보스턴 집값 예측 (조건수가 매우 높다는 경고 메시지 나옴)

from sklearn.datasets import load_boston

boston = load_boston()

dfX0 = pd.DataFrame(boston.data, columns=boston.feature_names)
dfX = sm.add_constant(dfX0)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])

model_boston2 = sm.OLS(dfy, dfX)
result_boston2 = model_boston2.fit()
print(result_boston2.summary())

# scale() 명령을 사용하여 스케일링하기

dfX2 = dfX.copy()
dfX2["TAX"] *= 1e13
df2 = pd.concat([dfX2, dfy], axis=1)

feature_names = list(boston.feature_names)
feature_names.remove("CHAS")
feature_names = ["scale({})".format(name) for name in feature_names] + ["CHAS"]
model3 = sm.OLS.from_formula("MEDV ~ " + "+".join(feature_names), data=df2)
result3 = model3.fit()
print(result3.summary())
