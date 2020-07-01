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


#25분까지 봄
# %%
