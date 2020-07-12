#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
%matplotlib inline


# %%
df = pd.read_csv("C:/inputcsv/tsa_tutorial_data/sales-of-shampoo.csv", index_col = 'Month',parse_dates=True)

# Month 형식이 일반적으로 쓰이지 않아서 parse_date가 적용안됨
# parser 함수만들어줘야함
#%%
df.index
# index가 object로 되어 있는것을 확인할 수 있음

#%%
from datetime import datetime

def dateparser(x):
    return datetime.strptime('190'+x, "%Y-%m")

# %%
shampoo = pd.read_csv("C:/inputcsv/tsa_tutorial_data/sales-of-shampoo.csv", index_col = 'Month',parse_dates=True, date_parser=dateparser)

# %%
shampoo.index
# index가 datetime64로 되어잇는것을 확인할 수 있음
# %%
shampoo.head()

#%%
def adf_check(ts):
    result = adfuller(ts)
    if result[1] <= 0.05:
        print('Stationary {}'.format(result[1]))
    else:
        print('Non-Stationary {}'.format(result[1]))


# %%
adf_check(shampoo['Sales of shampoo'])
# Non-Stationary 1.0 확인

# %%
shampoo['1st diff'] = shampoo['Sales of shampoo'] - shampoo['Sales of shampoo'].shift(1)

# %%
adf_check(shampoo['1st diff'].dropna())
# %%
shampoo['1st diff'].plot()

# %%
shampoo['2nd diff'] = shampoo['1st diff'] - shampoo['1st diff'].shift(1)
adf_check(shampoo['2nd diff'].dropna())

# %%
shampoo['2nd diff'].plot()
# 눈으로 봐서는 잘 모르겠음
# %%
from statsmodels.tsa.arima_model import ARIMA
# %%

p = list(range(0,5)) # grid search
d = [1,2] # 1,2차에서 stationlary 했기 떄문에
q = [0]

import itertools

# %%
pdq = list(itertools.product(p,d,q))

# %%
for param in pdq:
    model = ARIMA(shampoo['Sales of shampoo'], order=param)
    result = model.fit()
    print('ARIMA{} - AIC:{}'.format(param, result.aic))
# AIC가 작을수록 좋은거
# %%
X = shampoo['Sales of shampoo'].values

# train과 test 나눔
# %%
size = int(len(X)*0.66)
size
# 우선 2: 1로 나눔
#%%
train, test = X[:size], X[size:]

# %%
len(train)
len(test)

# %%
#window를 옮겨가면서 하나씩 prict, 예측 => 모델링 => 예측 => 모델링

history = [x for x in train] 

# %%
predictions = []

# %%
for t in range(len(test)):
    model = ARIMA(history, order=(2,1,0))
    result = model.fit(disp=0) #display =0 로그데이터 안보이게 하기 .. 아닐수도 있음
    output = result.forecast() # 매개변수 없으면 기본이 1
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t] 
    history.append(obs)
# %%
predictions

# %%
from sklearn.metrics import mean_squared_error
# %%
error = mean_squared_error(test, predictions)

# %%
rmse = np.sqrt(error)

# %%
rmse

# %%
shampoo['Sales of shampoo'].describe()

# %%
plt.plot(test)
plt.plot(predictions, color='red')


# %%


# %%
