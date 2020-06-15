#%%
import numpy as np
import pandas as pd
#%%
# 첫행 삭제
data=pd.read_csv("C:\\inputcsv\\result_csv\\PAINTING_FAMILY_result.csv")
#%%
data.rename(columns = data.loc[0],inplace=True)
data.drop([0],inplace=True)
#%%
# 원소명 컬럼 삭제
# 인덱스랑 첫번째 컬럼이랑 겹치기 떄문에 첫번쨰 컬럼 삭제
data = data.drop('원소명',1)
data = data.set_index(' ')
#data = data.drop(' ',1)
#%%
#자료형 숫자로 변경
data = data.apply(pd.to_numeric)
#%%
#Ba처리
#Ba 평균계산
data['Ba_average'] = (data['Ba_start']+data['Ba_end'])/2
#Ba 처리 방법 (2)
data.loc[data['Ba_average'] > (data['Ba_middle']/3), 'Ba'] = 0
#%%
# 15Kev(1~10 컬럼), 40Kev(11~27), Ba(28~30) 구분
data_spit=np.split(data, [10], axis=1)
data_15Kev = data_spit[0] #15Kev
data_spit2=np.split(data_spit[1], [17], axis=1)
data_40Kev = data_spit2[0] #40Kev
data_Ba = data_spit2[1] #Ba
#%%
# 행과 열을 치환한 뒤 각 포인터 별 15Kev 에너지 높은 순으로 정렬 후 상위 5개 추출
# 정렬 참조 : https://wordbe.tistory.com/entry/Pandas-Part-1-DataFrame-Series-Rename-Remove-Sort-Filter
data_15Kev = data_15Kev.transpose()
data_40Kev = data_40Kev.transpose()


#%%
# 빈 데이터 프레임 선언 후 정렬된 15Kev, 40Kev 삽입
# 참조 : https://shydev.tistory.com/29

# 빈 리스트 선언 후 정렬된 15Kev, 40Kev 삽입
data_sorted =  pd.Series()
data_sorted_keys =  pd.Series()

#%%
# 데이터를 Series에 저장

for column in data_15Kev:
    data_sorted[column] = data_15Kev[column].sort_values(ascending=False).head(5).append(data_40Kev[column].sort_values(ascending=False).head(5))

#%%
# 리스트에서 인덱스 값만 추출
for column in data_15Kev:
    p_keys = data_15Kev[column].sort_values(ascending=False).head(5).append(data_40Kev[column].sort_values(ascending=False).head(5)).keys()
    keys = []
    for key in p_keys :
        keys.append(key)
    data_sorted_keys[column] = keys

#%%
'''
import datetime
import os
basename1 = os.getcwd()+'\\XRF\\XRF_all_'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
basename2 = os.getcwd()+'\\XRF\\XRF_Keys_'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")

data_sorted.to_csv(basename1+'.csv')
data_sorted_keys.to_csv(basename2+'.csv')
'''

# %%
# index 다루기

data_count = pd.DataFrame()
data_count['points'] = data_sorted_keys.index
#%%

#for index in range(0,data_sorted_keys.size):   
#    data_sorted_keys

for point in data_sorted_keys.index :
    data_count[point] = 0
data_count = data_count.set_index('points')

# %%
#data_count['PAINTING_BABY_001-XRF.csv']['PAINTING_BABY_002-XRF.csv'] = 0


# %%
for point1 in data_sorted_keys.index:
    for point2 in data_sorted_keys.index:
        p_sum = 0
        
        for index in range(0,10):
            if data_sorted_keys[point1][index] == data_sorted_keys[point2][index] :
                p_sum = p_sum + 1
        
        data_count[point1][point2] = p_sum
#색조에 57번 포인트까지 데이트가 없음..
#포인트가 확인하는거 중요!
data_count = data_count.iloc[57:,57:] 
# %%
import datetime
import os
print(os.getcwd())
basename3 = os.getcwd()+'\\XRF\\XRF_ordering_matching_'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
data_count.to_csv(basename3+'.csv')


#data_count.iloc[57:,57:].to_csv(basename3+'.csv')


# %%
