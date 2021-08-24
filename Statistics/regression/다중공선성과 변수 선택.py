from statsmodels.stats.outliers_influence import variance_inflation_factor
from matplotlib import pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from statsmodels.datasets.longley import load_pandas

# pairplot (scatter plot) 확인하기
dfy = load_pandas().endog
dfX = load_pandas().exog
df = pd.concat([dfy, dfX], axis=1)
sns.pairplot(dfX)
plt.show()

# 상관관계 행렬
dfX.corr()

# heat map
cmap = sns.light_palette("darkgray", as_cmap=True)
sns.heatmap(dfX.corr(), annot=True, cmap=cmap)
plt.show()

# 다중공선성 때문에 condition number가 높음
def get_model1(seed):
    df_train, df_test = train_test_split(df, test_size=0.5, random_state=seed)
    model = sm.OLS.from_formula(
        "TOTEMP ~ GNPDEFL + POP + GNP + YEAR + ARMED + UNEMP", data=df_train
    )
    return df_train, df_test, model.fit()


df_train, df_test, result1 = get_model1(3)
print(result1.summary())


# 학습용 데이터와 검증용 데이터로 나누어 회귀분석 성능을 비교하면 과최적화가 발생하였음을 알 수 있다.


def calc_r2(df_test, result):
    target = df.loc[df_test.index].TOTEMP
    predict_test = result.predict(df_test)
    RSS = ((predict_test - target) ** 2).sum()
    TSS = ((target - target.mean()) ** 2).sum()
    return 1 - RSS / TSS


test1 = []
for i in range(10):
    df_train, df_test, result = get_model1(i)
    test1.append(calc_r2(df_test, result))

test1

# VIF를 계산

vif = pd.DataFrame()
vif["VIF Factor"] = [
    variance_inflation_factor(dfX.values, i) for i in range(dfX.shape[1])
]
vif["features"] = dfX.columns
vif

# 상관계수와 VIF를 사용하여 독립 변수를 선택하면 GNP, ARMED, UNEMP 세가지 변수만으로도 비슷한 수준의 성능이 나온다는 것을 알 수 있다.


def get_model2(seed):
    df_train, df_test = train_test_split(df, test_size=0.5, random_state=seed)
    model = sm.OLS.from_formula(
        "TOTEMP ~ scale(GNP) + scale(ARMED) + scale(UNEMP)", data=df_train
    )
    return df_train, df_test, model.fit()


df_train, df_test, result2 = get_model2(3)
print(result2.summary())

# 다중공선성을 제거한 경우에는 학습 성능과 검증 성능간의 차이가 줄어들었음을 확인할 수 있다.

test2 = []
for i in range(10):
    df_train, df_test, result = get_model2(i)
    test2.append(calc_r2(df_test, result))

test2


plt.subplot(121)
plt.plot(test1, "ro", label="검증 성능")
plt.hlines(result1.rsquared, 0, 9, label="학습 성능")
plt.legend()
plt.xlabel("시드값")
plt.ylabel("성능(결정계수)")
plt.title("다중공선성 제거 전")
plt.ylim(0.5, 1.2)

plt.subplot(122)
plt.plot(test2, "ro", label="검증 성능")
plt.hlines(result2.rsquared, 0, 9, label="학습 성능")
plt.legend()
plt.xlabel("시드값")
plt.ylabel("성능(결정계수)")
plt.title("다중공선성 제거 후")
plt.ylim(0.5, 1.2)

plt.suptitle("다중공선성 제거 전과 제거 후의 성능 비교", y=1.04)
plt.tight_layout()
plt.show()


## 보스턴 집값 예측 문제에 응용
from sklearn.datasets import load_boston
import numpy as np

boston = load_boston()

dfX0 = pd.DataFrame(boston.data, columns=boston.feature_names)

from patsy import dmatrix

formula = (
    "scale(CRIM) + scale(I(CRIM ** 2)) + "
    + "scale(ZN) + scale(I(ZN ** 2)) + scale(INDUS) + "
    + "scale(NOX) + scale(RM) + scale(AGE) + "
    + "scale(np.log(DIS)) + scale(RAD) + scale(TAX) + "
    + "scale(np.log(PTRATIO)) + scale(B) + scale(np.log(LSTAT)) + CHAS"
)
dfX = dmatrix(formula, dfX0, return_type="dataframe")
dfy = pd.DataFrame(boston.target, columns=["MEDV"])

idx_outlier = np.array(
    [
        7,
        54,
        148,
        152,
        160,
        214,
        253,
        267,
        364,
        365,
        367,
        368,
        369,
        371,
        372,
        374,
        380,
        385,
        397,
        398,
        399,
        400,
        401,
        405,
        409,
        410,
        412,
        413,
        414,
        415,
        416,
        418,
        419,
        426,
        445,
        489,
        490,
        492,
        505,
        161,
        162,
        163,
        166,
        186,
        195,
        204,
        225,
        257,
        267,
        283,
        368,
        369,
        370,
        371,
        372,
    ]
)

idx = list(set(range(len(dfX))).difference(idx_outlier))
dfX = dfX.iloc[idx, :].reset_index(drop=True)
dfy = dfy.iloc[idx, :].reset_index(drop=True)

# correlation heatmap 그리기

cmap = sns.light_palette("black", as_cmap=True)
sns.heatmap(dfX.corr(), annot=True, fmt="3.1f", cmap=cmap)
plt.show()

# vif 확인

vif = pd.DataFrame()
vif["VIF Factor"] = [
    variance_inflation_factor(dfX.values, i) for i in range(dfX.shape[1])
]
vif["features"] = dfX.columns
vif = vif.sort_values("VIF Factor").reset_index(drop=True)
vif

model_boston1 = sm.OLS(np.log(dfy), dfX)
result_boston1 = model_boston1.fit()
print(result_boston1.summary())
