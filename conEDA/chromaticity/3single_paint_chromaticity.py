#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
# %%
# 실험 대상이 될 작품 Chromaticity 폴더 지정

base_dir = "C:/inputcsv/painting/conUNSOUNG/BABY(PAI, UN-SOUNG)/3. Material Analysis/3.2 Basic Analysis/3.2.2 Chromaticity"

#%%
# Chromaticity 폴더 내부의 파일 이름에서 포인트 추출
'''
예시
파일 명 : PAINTING_BABY_058-Chromaticity.xlsx
추출 포인트 : 058
'''
files=os.listdir(base_dir)
points = []
for file in files:
    point = file[-21:-18]
    points.append(point)

# %%
# Chromaticity 데이터프레임 생성
# point 열 인덱스
chromaticity_df = pd.DataFrame()
chromaticity_df['point'] = points

# %%
# Chromaticity excel Sheet1 구성 :  point, L, a*, b*
p_df = pd.DataFrame(columns=['Sample Name','L', 'a*','b*'])
for file in files:
    path = os.path.join(base_dir,file)
    # 데이터 프레임에 행 추가
    p_df = p_df.append(pd.read_excel(path, sheet_name='Sheet1'),ignore_index=True) 

# %%
'''
chromaticity_df
columns : 
  point
  L
  a*
  b*
'''
chromaticity_df['L'] = p_df['L']
chromaticity_df['a*'] = p_df['a*']
chromaticity_df['b*'] = p_df['b*']
#chromaticity_df = chromaticity_df.set_index('point')

# %%
# df_dist : 포인트 간의 거리를 squareform으로 표현
from scipy.spatial.distance import squareform, pdist
dist = pdist(chromaticity_df[['L','a*','b*']],'euclidean')
df_dist = pd.DataFrame(squareform(dist),columns = chromaticity_df['point'], index=chromaticity_df['point'])
# %%
# df_dist를 heatmap 형태로 시각화
import seaborn as sns
sns.heatmap(df_dist, cmap = 'RdYlGn', linewidths = 0.2)

# %%
# chromaticity 거리가 n 아래인 것들을 추출
n = 1
chromaticity_n_under = df_dist[(df_dist< n) & (df_dist != 0)]

# %%
chromaticity_n_under_pointpair = pd.DataFrame(columns=['match'],index=chromaticity_n_under.columns)

# %%
for co in chromaticity_n_under.columns:
    matching = []
    # Series 나 Dataframe의 데이터를 조회할 때 dtype과 Name를 출력하고 싶지 않다면, 배열에 넣은후 출력하는 방법 사용 
    for var in (chromaticity_n_under[chromaticity_n_under[co] > 0].index) :
        matching.append(var)
    chromaticity_n_under_pointpair.loc[co,'match'] = matching
# %%
# 출력하고 싶은 데이터 csv 형태로 출력
import datetime
basename1 = os.getcwd()+'\\Chromaticity\\Chromaticity_3under_match'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
basename2 = os.getcwd()+'\\Chromaticity\\Chromaticity_dist'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")

chromaticity_n_under_pointpair.to_csv(basename1+'_Chromaticity.csv')
df_dist.to_csv(basename2+'.csv')