#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# %%
# 시분초까지 입력 가능
today = datetime(2019,1,24)
# %%
print(today.year)
print(today.month)
print(today.day)


# %%
dates = [datetime(2019,1,23),datetime(2019,1,24)]

# %%
#datetime index를 만드는 방법
dt_index = pd.DatetimeIndex(dates)
dt_index
#%%
data = np.random.randn(2,2)
cols = ['A','B']
# %%
#datetime을 인덱스로 가지는 dataframe 생성
df = pd.DataFrame(data=data, index=dt_index,columns=cols)

# %%
#index reset
#해당 경우 numeric으로 기본 인덱스가됨
pd.DataFrame(data=data, index=dt_index, columns=cols).reset_index()

# %%
# index와 관련된 연산 확인
print(df.index)
print(df.index.max())
print(df.index.min())
print(df.index.argmax()) #max값의 인덱스를 사용 (Serise의 index 사용)

# %%
