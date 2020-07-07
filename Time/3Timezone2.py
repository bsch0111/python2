#%%
from datetime import datetime
from datetime import timezone
# %%
timezone.utc
# python 안에는 utc라는 timezone 밖에 없음. 해당 타임존을 수정해서 다른 타임존을 만드는데
# 매우 불편함
datetime(2019,1,1) # timezone unawared datetime
# %%
datetime(2019,1,1,tzinfo=timezone.utc) # timezone awared datetime
# 다른 타임존으로 데이터타임 저장하기
#%%
# 별도의 패키지를 통해서 타임존 추가를 많이함 (pytz)
import pytz
# %%
#pytz가 확인할 수 있는 모든 timezone출력
pytz.all_timezones
# %%
KST = pytz.timezone('Asia/Seoul')
#datetime(2019,1,1,tzinfo=timezion.utc) == pytz.UTC.localize(datetime(2019,1,1)) True!
KST.localize(datetime(2019,1,1))
#%%
datetime(2019,1,1,tzinfo=timezone.utc) == KST.localize(datetime(2019,1,1))
# False
# %%
mydate = datetime(2019,1,1)
mydate.replace(year=2018) #날짜를 변경할때 replace 를 많이 사용함
#%%
mydate.replace(tzinfo=KST)
#변경이 안됨 (에러인지 뭔지 모르겠음)
mydate = KST.localize(mydate) # 이렇게 해야함

# %%
# timezone만 바꾸는게 아니라 시간까지도 맞추어 바꾸어주는 것
mydate.astimezone(pytz.utc)
#%%
mydate.astimezone(pytz.utc) == mydate #utc 시간과 kst 시간이 같은지 확인 
# True
# %%
# strftime 내 datetime을 다음 형식으로 저장해달라
# strftime.org 가면 시간 형식을 확인할 수 있음
mydate.strftime ("%Y-%m-%d %H:%M:%S:%Z")
#%%
mydate.astimezone(pytz.utc).strftime ("%Y-%m-%d %H:%M:%S:%Z")
#%%
#시스템의 지금 시간을 알아보는 것
#환경설정에서 변경했다면 다른 시간이 나옴, 편리하면서도 위험함
datetime.today()
#%%
#전세계 어디에서도 해당 코드의 결과를 동일하게 하려면
datetime.utcnow().astimezone(KST)
#오늘의 요일 알기
#  %%
# 월 : 0, 화 : 1, .... 일 : 6
today = datetime.today()
today.weekday()
# %%
# 가장 최근 금요일을 구하라
def last_friday():
    today = KST.localize(datetime.today())
    offset = 4 - today.weekday()
    aweekago = today.replace(day=today.day-7)
    last_friday = aweekago.replace(day=aweekago.day+offset)
    return  last_friday

# %%
last_friday()
# 하지만 월초, 월말에 문제가 일어남 (month의 범위에 맞지 않아서)
# %%
# 상대적인 날짜, 시간의 델타 값을 저장하기위함
# from datetime import timedelta
pytz.utc.localize(mydate) - KST.localize(mydate)
# 월이 넘어가던가하는 것도 알아서 계산해줌
pytz.utc.localize(mydate) + timedalta(seconds=32400)

def last_friday():
    today = KST.localize(datetime.today())
    offset = 4 - today.weekday()
#    aweekago = today.replace(day=today.day-7)
    aweekago = today - timedelta(weeks=1)
    last_friday = aweekago + timedelta(days=offset)
#    last_friday = aweekago.replace(day=aweekago.day+offset)
    return  last_friday


#
#%%
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
# %%
# 시계열 데이터 visualization할 때 쓰는 함수들
df_apple = pd.read_csv('C:/inputcsv/tsa_tutorial_data/apple_stock.csv', index_col = 'Date', parse_dates =True)

# %%
df_apple[['Volume','Adj Close']].plot()
# 문제점 : Volume 과 Adj Close의 변화량이 같지 않기 때문에 상대적으로 작은 변화량을 가진
# Adj Close가 변하지 않는 것처럼 보인다.
# %%
df_apple['Adj Close'].plot()
# %%
# 데이터 왜곡 삭제
df_apple[['Volume','Adj Close']].plot(secondary_y=['Volume'])

# %%
# 12인치, 8이니로 그림 확대
# 실행되는 한 셀에는 데코레이션을 할 수 있음
df_apple['Adj Close'].plot(figsize=(12,8))
plt.ylabel('Close Price')
plt.xlabel('Overwrite Date')
plt.title('APPL')
# %%
# 범위지정 할수 있음
df_apple['Adj Close']['2015-01-01':'2018-01-01']
df_apple['Adj Close']['2015-01-01':'2018-01-01'].plot()

# %%
# 위 범위 지정이랑 같지만 x limited 방법 사용
# : 는 pandas에서만 읽히는 문법이고, 그 외 (plot포함)은 ,으로 표현
df_apple['Adj Close'].plot(xlim=['2015-01-01','2018-01-01'])

# %%
# y 범위 제한 
df_apple['Adj Close'].plot(xlim=['2015-01-01','2018-01-01'],ylim=[70,180])

# %%
# x축의 값이 겹쳐서 변경해야하는 경우 (예제에서는 겹치지 않았음)
index = df_apple['2015-01-01':'2018-01-01'].index
stock = df_apple['2015-01-01':'2018-01-01']['Adj Close']

#%%
import matplotlib.dates as dates # 축 값의 포맷 변경 가능

# %%
fig, ax = plt.subplots(figsize=(15,3))
# subplot 한개짜리가 만들어짐
ax.plot_date(index, stock, '-')
# - 는 line으로 그리라는 뜻, 눕히지 말고 
# 이렇게 하면 겹침
ax.xaxis.set_major_locator(dates.MonthLocator()) # 축 보이는 것을 변경
ax.xaxis.set_major_formatter(dates.DateFormatter('%b\n%Y')) # 평상시에는 이런방식안쓰고 이미지 편집 쓰기도 함

plt.tight_layout() #1차적인 해결방법, 꼭 써주는게 좋음
fig.autofmt_xdate() #알아서 포맷을 수정해서 잘 보이게끔 수정

# %%
# 3강 끝

# %%
