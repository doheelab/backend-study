import pandas as pd
import statsmodels.api as sm

df_mtcars = pd.read_csv("mtcars.csv")
df_mtcars = df_mtcars.iloc[:, 1:]
col_list = list(df_mtcars.columns)

y = df_mtcars[col_list[:1]]
x = df_mtcars[col_list[1:]]

# Let's start with ["wt"]

x_data = sm.add_constant(x["wt"], has_constant="add")
multi_model = sm.OLS(y, x_data)
fitted_multi_model = multi_model.fit()
fitted_multi_model.summary()

# Go with ["wt", "hp"]

x_data = sm.add_constant(x[["wt", "hp"]], has_constant="add")
multi_model = sm.OLS(y, x_data)
fitted_multi_model = multi_model.fit()
fitted_multi_model.summary()


# Go with ["wt", "hp", "qsec"]
# "hp", "qsec" are insignificant

x_data = sm.add_constant(x[["wt", "hp", "qsec"]], has_constant="add")
multi_model = sm.OLS(y, x_data)
fitted_multi_model = multi_model.fit()
fitted_multi_model.summary()

# Go with all variables
#

x_data = sm.add_constant(x, has_constant="add")
multi_model = sm.OLS(y, x_data)
fitted_multi_model = multi_model.fit()
fitted_multi_model.summary()

# 예측하기
fitted_multi_model.predict(x_data)
