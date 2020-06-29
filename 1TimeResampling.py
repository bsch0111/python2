#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# %%
# 시분초까지 입력 가능
'''1강 
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
'''
'''
# %% 2강 애플 주식을 이용 Resample
#date를 index로 하지 않음 
df = pd.read_csv('C:/inputcsv/tsa_tutorial_data/apple_stock.csv')

# %%
df.info()
# pandas에서 object 타입은 integer,float 가 아니면 object라고 나옴
# Date 컬럼이 object 
# %%
# Date 컬럼을 Date 타입으로 변경
df['Date'] = df['Date'].apply(pd.to_datetime)

# %%
df.info()
# %%
#Date 컬럼을 인덱스로 사용
df.set_index('Date', inplace=True)

# %%
# pandas의 Resampling 기능을 사용하지 않는 경우 
# %%
# pandas 의 Resampling을 몰랐을때, Month 별로 합계를 구하는 방법
df['month'] = df.index.month

#%%
df.groupby('month').agg(sum)
# 년도가 달라지는 걸 확인 못하고 단지 달 별로 합계를 구함
# %%
# 년도별로 다라지는 문제를 해결
df.groupby(df.index.year).sum()
#%%
df['year'] = df.index.year
# %%
#index를 통해서 두개의 groupby할 때는 이름 레벨차이가 난다고 실행이 안됨 
#df.groupby([df.index.year,df.index.month]).agg(sum)
df.groupby(['year','month']).agg(sum)
# 문제를 멀티인덱스, groupby로 해결할 수 있지만 쉬운 방법이 아님
# %%
# pandas의 Resampling 기능을 사용하는 경우
# time series offset strings 개념을 꼭 알아야함! pandas documnetation을 봐야함
# 년도별로 Resampling A
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

df.resample(rule='A').mean()
# 년도 별로 12월 31일을 기준으로 mean, sum, 등 사용가능

# %%
# 다시 인덱싱을 할 필요가 없음
df.resample(rule='A').mean()['2009']


# %%
# 기본 제공되는 alliase가 없더라도 커스텀 핤 ㅜ잇음
# 매년 첫날에 대한 자료를 뽑고 싶음
def first_day(sample):
    return sample[0]

df.resample(rule='A').apply(first_day)

# %%
# 차트만들기도 매우 편리함
# 년도 별 종가(마지막 판매가)의 연 평균을 차트로 그려라
df['Close'].resample('A').mean().plot(kind='bar')
# %%
# 오픈가격의 월별 최대 값
df['Open'].resample('M').max().plot(kind='bar', figsize=(15,8))

# %%
# 오픈가격의 월별 최대 값(2015년 이후)
df['Open']['2015':].resample('M').max().plot(kind='bar', figsize=(15,8))
# %%
# 오픈가격의 월별 최대 값(2015년 8월 이후 )
df['Open']['2015-8':].resample('M').max().plot(kind='bar', figsize=(15,8))


# %%
# 오픈가격의 월별 최대 값(2015년 8월부터 2015년 12월)
# 범위 셀렉션이 쉽다.
df['Open']['2015-8':'2015-12'].resample('M').max().plot(kind='bar', figsize=(15,8))

# %%
# date range index 생성
# freq = 'B' Business day .. 토일 제외 
pd.date_range(start=datetime(2018,9,1), end=datetime(2019,1,24), freq='B')
daily_daterange = pd.date_range(start=datetime(2018,9,1), end=datetime(2019,1,24), freq='B')

# %%
daily_dataset = \
    pd.DataFrame(
        data = {'value' : np.random.rand(len(daily_daterange))},
        index=daily_daterange)


# %%
# 주의 월요일 최소 값 (Weekly Monday)
daily_dataset.resample('W-MON').max()

# %%
daily_dataset.resample('M').min()
'''
'''
# %% 2강 Shifting
# read csv 할때 index를 잡아줌
df = pd.read_csv('C:/inputcsv/tsa_tutorial_data/apple_stock.csv', index_col='Date')

# %%
df.index
# df['2009'] 안됨
# 확인해보니 df의 index 타입이 object로 되어있음
# index를 datetime으로 수정해보자
df.index = pd.to_datetime(df.index)
# %%
df.index
# datetime index로 바뀌어 있음
# df['2009'] 됨
# %%
# 아래와 같이 shfting 할수 있지만 모든 컬럼에 적용하기엔 번거로움 번거로움
temp = np.asarray(df['Close'])
temp
# %%
# 마지막 한개 전까지
temp[:-1]
# %%
# 두번째부터 마지막가지
temp[1:]

#%%
df.head()
#%%
df.tail()
#%%
# dataframe의 shift 방법 
# 첫번째 행이 없어졌지만 채워줘야함
df.shift(1).head()
# %%
df.shift(1).tail()
# %%
# 두 번째 행이 첫번째로
df.shift(-1).tail()
# %%
df.shift(-1).head()
# %%
# lagging lag lagged : shift 이외에 여러 작업을 한 데이터를 lagged 데이터
# 이전 마지막 달 데이터가 자기 데이터가 됨
df.tshift(freq='M', periods=1).head()
'''

# %%
# 2강 Rolling & Expanding
# parse_date : 컬럼을 검사해서 parsing할수 있는 컬럼이 발견되면 datetype으로 변경
df = pd.read_csv('C:/inputcsv/tsa_tutorial_data/apple_stock.csv',\
    index_col='Date',parse_dates=True)
df.index
# index가 datetime으로 변경되어 있음
# 하고싶은 컬럼만 적어줄 수 있음
#df = pd.read_csv('C:/inputcsv/tsa_tutorial_data/apple_stock.csv',\
#    index_col='Date',parse_dates=['',''])
# %%
# 파싱이 안되는 경우에는 파싱함수를 만들어 줘야함
# 19-01-11, 19-JAN-11 이런 경우는 파싱이 안됨

def dateparser(str_dt):
    return pd.datetime.strptime(str_dt, "%Y-%m-%d")
#%%
df = pd.read_csv('C:/inputcsv/tsa_tutorial_data/apple_stock.csv',\
    index_col='Date',parse_dates=['Date'], date_parser = dateparser)

#strptime ( string parser time)

# %%
dateparser('2019-01-01')
# %%
def dateparser2(str_dt):
    return pd.datetime.strptime(str_dt, "%d-%m-%Y")
# %%
dateparser2('01-01-2019')
# %%
df.head(10)
# %%
# rolling 은 트렌드를 보기위해 사용됨 
df.rolling(7).mean().head(10)

# %%
# 파랑색은 원래 데이터, 주황색은 트렌드
df['Close'].plot()
df.rolling(window=30).mean()['Close'].plot()

# %%
df['2018':]['Close'].plot()
df['2018':].rolling(window=30).mean()['Close'].plot()
# window size가 커질수록 실제를 반영못함
# 여기서는 30일을 한번에 트렌드에 반영함
# %%
df['Close : 30 Day Mean'] = df['Close'].rolling(30).mean()
# %%
df[['Close','Close : 30 Day Mean']].plot(figsize=(15,7))

# %%
# Expandings
# Rolling은 window size만큼 움직이면서 트렌드 반영
# Expand는 시점이 고정된 채로 트렌드 반영 (Rolling 보다 잘 쓰이진 않음)
list(range(10))
#%%
#누적평균을 트렌드로 
df['Close'].expanding(min_periods=1).mean().plot(figsize=(15,8))

# %%
# 볼린저 밴드
# 주식높으면 사고 낮으면 안된다 같은의미 
# 20일 단위의 종가의 평균 트렌트 값과
df['Close: 20Day Mean'] = df['Close'].rolling(20).mean()
# %%
df['Upper'] = df['Close: 20Day Mean'] + 2*df['Close'].rolling(20).std()
#%%
df['Lower'] = df['Close: 20Day Mean'] - 2*df['Close'].rolling(20).std()
#%%
df[['Close','Close: 20Day Mean','Upper','Lower']].plot(figsize=(15,8))

# %%
df[2018:][['Close','Close: 20Day Mean','Upper','Lower']].plot(figsize=(15,8))
