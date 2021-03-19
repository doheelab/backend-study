import pandas as pd

data = pd.read_csv("./Sales_Transactions_Dataset_Weekly.csv")
data = data.filter(regex="Product|W").copy()  # Product 혹은 W로 시작하는 것만 남기기
data["Product_Code_NUM"] = data["Product_Code"].str.extract("(\d+)").astype(int)

print(data.shape)
data.head()

import numpy as np

X_train = []
Y_train = []

X_test = []
Y_test = []

for ix, row in data.iterrows():
    for w in range(8, 50):
        x = row.iloc[w - 7 : w].values.astype(int)
        y = row.iloc[w : w + 3].values.astype(int)
        if w < 30:
            X_train.append(x)
            Y_train.append(y)
        else:
            X_test.append(x)
            Y_test.append(y)

X_train = np.array(X_train)
Y_train = np.array(Y_train)

X_test = np.array(X_test)
Y_test = np.array(Y_test)

print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)


from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
print("변경 전 :", X_train)
X_train = scaler.fit_transform(X_train)
print("변경 후 :", X_train)
X_test = scaler.transform(X_test)


print(
    "변경 전 :", X_train.shape, X_train,
)
X_train = np.expand_dims(X_train, axis=2)
print(
    "변경 후 :", X_train.shape, X_train,
)

from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras import optimizers
from keras.callbacks import LearningRateScheduler


def deep_lstm():
    model = Sequential()
    model.add(LSTM(4, input_shape=(7, 1), return_sequences=True))
    model.add(LSTM(4, return_sequences=False))
    model.add(Dense(3))
    # model.add(Activation('softmax'))

    adam = optimizers.Adam(lr=0.001)
    model.compile(loss="mse", optimizer=adam)

    return model


model = deep_lstm()


def scheduler(epoch):
    if epoch < 10:
        return 0.01
    else:
        return 0.001


callback = LearningRateScheduler(scheduler)

model.fit(X_train, Y_train, epochs=20, callbacks=[callback], verbose=1)
