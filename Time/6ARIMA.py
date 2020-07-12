#%%
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
%matplotlib inline

# %%
df = pd.read_csv('C:/inputcsv/tsa_tutorial_data/monthly-milk-production.csv', index_col='Month', parse_dates=True)

# %%
df.info()

# %%
# trend와 seasonality가 있는 것을 확인
df.plot()
#%%
df.columns
# %%
# 이것은 stationaliy 하게 만든다면 ploting을 통해 trend와 seasonality를 확인하지 못함
timeseries = df['pounds per cow']

# %%
timeseries.rolling(12).mean().plot()
# seasonality 지움, trend만 남겨져 잇음
# %%
timeseries.rolling(12).std().plot()
#trend 지움

# %%
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(df['pounds per cow'])

# %%
fig = plt.figure(figsize=(15,7))
fig = decomposition.plot()
fig.set_size_inches(15,7)
# %%
# stationalary 한지 검사
from statsmodels.tsa.stattools import adfuller
result = adfuller(df['pounds per cow'])
# 두번째 항목이 p-value.. 0.5보다 작으면 stationalary 하다고 말할 수 있음
# 현재 stationalary 하지 않음 
# %%
def adf_check(ts):
    result = adfuller(ts)
    if result[1] <= 0.05:
        print('Stationary {}'.format(result[1]))
    else:
        print('Non-Stationary {}'.format(result[1]))

# %%
adf_check(df['pounds per cow'])

# %%
df['1st diff'] = df['pounds per cow'] - df['pounds per cow'].shift(1)

# %%
df.head()

#%%
df['1st diff'].isna().sum()
# %%
adf_check(df['1st diff'].dropna())
# 이제는 stationnary하다고 말할 수 있음
# %%
df['1st diff'].plot()

# %%
# 혹시 모르니까 한번더 differencing을 수행
df['2nd diff'] = df['1st diff'] - df['1st diff'].shift(1)

# %%
df['2nd diff'].plot()
#%%
adf_check(df['2nd diff'].dropna())
# 엄청 stationary 하게 변했음
# %%
# seasonal diferencing 
df['seasonal diff'] = df['pounds per cow'] - df['pounds per cow'].shift(12)

# %%
df['seasonal diff'].plot()
# 노이즈 같기는 한데, varience 가 생김
# %%
adf_check(df['seasonal diff'].dropna())

# %%
df['seasonal 1st diff'] = df['1st diff'] - df['1st diff'].shift(12)

# %%
df['seasonal 1st diff'].plot()

# %%
adf_check(df['seasonal 1st diff'].dropna())

# %%
# d = 1, D = 1


#%%
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# %%
plot_acf(df['1st diff'].dropna())

# %%
plot_acf(df['seasonal 1st diff'].dropna());
# 만약 두개씩 다온다면 에러, 뒤에 ; 추가
# %%
model = sm.tsa .statespace.SARIMAX(df['pounds per cow'], order=(0,1,0), seasonal_order=(1,1,1,12))

# %%
result = model.fit()

# %%
print(result.summary())

# %%
result.resid.plot()

# %%
result.resid.plot(kind='kde')

# %%
len(df['pounds per cow'])
#%%
df['forecast'] = result.forecast(len(df['pounds per cow']))
#%%
df[['pounds per cow', 'forecast']].plot(figsize=(12,8))
#%%
df['forecast'].plot(figsize=(12,8))

#%%
df['predict'] = result.predict(start=150, end= 168, dynamic=True)

# %%
df[['pounds per cow', 'predict']].plot(figsize=(12,8))


# %%
