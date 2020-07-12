#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# %%
airline = pd.read_csv('C:/inputcsv/time_data/airline_passengers.csv', index_col='Month', parse_dates=True)

# %%

# %%
# Simple Moving Average
# 6 month moving average
airline['6M_SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()
# 12 month moving average
airline['12M_SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()

# %%
# 그래프 그려서 확인
# 녹색은 트렌드만 따라가고 고저가 없음, 
# 주황색에 비해 녹색이 residual(잔차가)이 큼
# 이것도 일종의 예측모델이라고 하는구나
airline.plot()
#%%
# 잔차 구하기
airline['Thousands of Passengers'] - airline['6M_SMA']

#%%
residual = airline['Thousands of Passengers'] - airline['6M_SMA']
# %%

from sklearn.metrics import mean_squared_error
#%%
# mean_squared_error(실제값, 예측한 값 )
mean_squared_error(airline['Thousands of Passengers'],airline['6M_SMA'].fillna(123))
# %%
# Weighted Moving Average
airline['6M_EMA'] = airline['Thousands of Passengers'].ewm(span=6).mean()
airline['12M_EMA'] = airline['Thousands of Passengers'].ewm(span=12).mean()

# %%
mean_squared_error(airline['Thousands of Passengers'],airline['6M_EMA'])
#%%
airline.plot()

# %%
# Simple Exponential Smoothing, Holt's, Holt_winter's
# trend와 seasonality 반영 X,   trend 반영, trend와 seasonality 반영 성능 좋음
from statsmodels.tsa.api import SimpleExpSmoothing
#%%
train = airline[:'1959']
test = airline['1960':]
# %%

train['Thousands of Passengers'].plot()
test['Thousands of Passengers'].plot()
# 색깔이 분리되어서 보임
# %%
ses_model = SimpleExpSmoothing(train['Thousands of Passengers'])
# %%
#SimpleExpSmoothing(np.asarray(train['Thousands of Passengers']))

#%%
ses_result = ses_model.fit()

# %%
#테스트 데이터를 오염시키지 않기위해서
y_hat = test.copy()


# %%
y_hat['SES'] = ses_result.forecast(len(test))

# %%

plt.plot(train['Thousands of Passengers'], label='Train')
plt.plot(test['Thousands of Passengers'], label='Test')
plt.plot(y_hat['SES'], label='Simple Exp Smoothing')
# 트렌드와 패턴이 반영안된 걸 확인할 수 있음
# %%
# mse가 너무커서 루트를 씌워줌
rmse_ses = np.sqrt(mean_squared_error(test['Thousands of Passengers'],y_hat['SES'])
)
# %%
from statsmodels.tsa.api import Holt

# %%
holt_model = Holt(train['Thousands of Passengers'])

# %%
holt_result = holt_model.fit()

# %%
y_hat['Holt'] = holt_result.forecast(len(test))

# %%
plt.plot(train['Thousands of Passengers'], label='Train')
plt.plot(test['Thousands of Passengers'], label='Test')
plt.plot(y_hat['Holt'], label='Simple Exp Smoothing')
# 트렌드는 반영된 것을 확인할 수 있음
# %%
rmse_holt = np.sqrt(mean_squared_error(test['Thousands of Passengers'],y_hat['Holt'])
)
#ses보다 줄어들었음을 확인
# %%
# Holt_winters
from statsmodels.tsa.api import ExponentialSmoothing
# %%
winter_model = ExponentialSmoothing(train['Thousands of Passengers'],seasonal_periods=12,trend="add",seasonal="add")

# %%
winter_result = winter_model.fit()

# %%
y_hat['Winter'] = winter_result.forecast(len(train))

# %%
plt.plot(train['Thousands of Passengers'])
plt.plot(test['Thousands of Passengers'])
plt.plot(y_hat['Winter'])
# 거의 유사한걸 확인할 수 있음
# %%
rmse_winter = np.sqrt(mean_squared_error(test['Thousands of Passengers'], y_hat['Winter']))
# 아주 많이 줄어든 것을 확인할 수 있음
# %%
# ARIMA
# Holt와 Winter's에 비해서 이해하기 어려움
# 알고리즘을 이해하고 파라미터를 구할 필요는 없음
# grid search 방식으로 파라미터를 구함. 그러나 약간은 이해하는게 필요

import statsmodels.api as sm

# %%
# ARIMA(p,d,q)(P,D,Q)m
# 트렌드만 있으면 앞에 파라미터 3개, seasonality가 있으면 4개 추가
arima = sm.tsa.statespace.SARIMAX(
    train['Thousands of Passengers'],
    order=[2,1,1], # 첫번째 p,d,q
    seasonal_order = [0,1,0,12], # 첫번쨰 seasonal 파라미터
    #경험상 에러를 낼 수 있기떄문에 바꾸는 것을 끄고 함
    enforce_stationarity = False,
    enforce_invertibility = False
)
#%%
arima_result = arima.fit()

# %%
#forecast 는 예측할 데이터의 개수를 파라미터로 받음
#predict 는 예측할 데이터의 index를 파라미터로 받음
y_hat['arima'] = arima_result.predict(start = '1960-01-01', end='1960-12-01', dynamic=True)
#dynamic으로 해야 여러개의 데이터를 예측할 수 있음, 원래 arima는 특정 시즌만 예측함
# %%
plt.plot(train['Thousands of Passengers'])
plt.plot(test['Thousands of Passengers'])
plt.plot(y_hat['arima'])
  
# %%
rmse_winter
# %%
np.sqrt(mean_squared_error(test['Thousands of Passengers'], y_hat['arima']))


# %%
