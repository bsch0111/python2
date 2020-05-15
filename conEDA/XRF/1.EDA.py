import numpy as np
import pandas as pd

# 첫행 삭제
data=pd.read_csv("C:/result.csv")
data.drop([0],inplace=True)

# 원소명 컬럼 삭제
# 인덱스랑 첫번째 컬럼이랑 겹치기 떄문에 첫번쨰 컬럼 삭제
data = data.drop('원소명',1)
data = data.drop(' ',1)

#자료형 숫자로 변경
data = data.apply(pd.to_numeric)

#Ba 평균계산
data['Ba_average'] = (data['Ba_start']+data['Ba_end'])/2

#Ba 처리 방법 (2)
data.loc[data['Ba_average'] > (data['Ba_middle']/3), 'Ba'] = 0


# 15Kev(1~10 컬럼), 40Kev(11~27), Ba(28~30) 구분
data_spit=np.split(data, [10], axis=1)
data_15Kev = data_spit[0] #15Kev
data_spit2=np.split(data_spit[1], [17], axis=1)
data_40Kev = data_spit2[0] #40Kev
data_Ba = data_spit2[1] #Ba

# 행과 열을 치환한 뒤 각 포인터 별 15Kev 에너지 높은 순으로 정렬 후 상위 5개 추출
# 정렬 참조 : https://wordbe.tistory.com/entry/Pandas-Part-1-DataFrame-Series-Rename-Remove-Sort-Filter

data_15Kev = data_15Kev.transpose()
#for column in data_15Kev:
#    print(data_15Kev[column].sort_values(ascending=False).head(5))

# 40Kev 에너지 높은 순으로 정렬
data_40Kev = data_40Kev.transpose()
#for column in data_40Kev:
#    print(data_40Kev[column].sort_values(ascending=False).head(5))


# 빈 데이터 프레임 선언 후 정렬된 15Kev, 40Kev 삽입
# 참조 : https://shydev.tistory.com/29

# 빈 리스트 선언 후 정렬된 15Kev, 40Kev 삽입
data_sorted =  []
data_sorted_keys =  []

for column in data_15Kev:
    data_sorted.append(data_15Kev[column].sort_values(ascending=False).head(5).append(data_40Kev[column].sort_values(ascending=False).head(5)))

# 리스트에서 인덱스 값만 추출
for column in data_15Kev:
    data_sorted_keys.append(data_15Kev[column].sort_values(ascending=False).head(5).append(data_40Kev[column].sort_values(ascending=False).head(5)).keys())

for i in data_sorted_keys:
    print(i)

data_sorted[72]
data_sorted_keys[72]