#%%
import numpy as np
import pandas as pd
import os
 # %%
base_dir = "C:/inputcsv/20200514/mother1/3.2.2 Chromaticity"
# 최종 결과물 속성
# point, L, a*, b*
#%%
# Chromaticity 파일리스트
files=os.listdir(base_dir)
# 포인트 배열
points = []
# %%
# 포인트 추출
for file in files:
    point = file[-21:-18]
    points.append(point)
# %%
# 데이터프레임 생성
# point 열을 인덱스화
chromaticity_df = pd.DataFrame()
chromaticity_df['point'] = points
# %%

# %%
p_df = pd.DataFrame(columns=['Sample Name','L', 'a*','b*'])
for file in files:
    path = os.path.join(base_dir,file)
    # 데이터 프레임에 행 추가
    p_df = p_df.append(pd.read_excel(path, sheet_name='Sheet1'),ignore_index=True) 

# %%
chromaticity_df['L'] = p_df['L']
chromaticity_df['a*'] = p_df['a*']
chromaticity_df['b*'] = p_df['b*']
#chromaticity_df = chromaticity_df.set_index('point')
#index를 point로 여기서 하면 추후에 squreform할 때 index로 사용할 컬럼이 부족
# %%

'''
import datetime
basename = os.getcwd()+'\\Chromaticity\\Chromaticity'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
chromaticity_df.to_csv(basename+'_Chromaticity.csv')
'''

# %%
# 포인트 간의 거리를 squareform으로 출력
from scipy.spatial.distance import squareform, pdist
dist = pdist(chromaticity_df[['L','a*','b*']],'euclidean')
df_dist = pd.DataFrame(squareform(dist),columns = chromaticity_df['point'], index=chromaticity_df['point'])
# %%
import seaborn as sns
sns.heatmap(df_dist, cmap = 'RdYlGn', linewidths = 0.2)

# %%
# chromaticity 거리가 3 아래인 것들을 추출
chromaticity_3under = df_dist[(df_dist<3) & (df_dist != 0)]
# %%

import datetime
basename = os.getcwd()+'\\Chromaticity\\Chromaticity_3under'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
chromaticity_3under.to_csv(basename+'_Chromaticity.csv')

# %%
chromaticity_3under_match = pd.DataFrame(columns=['match'],index=chromaticity_3under.columns)

# %%
for co in chromaticity_3under.columns:
    chromaticity_3under_match.loc[co,'match'] = chromaticity_3under[chromaticity_3under[co] > 0].index
# %%
chromaticity_3under_match['match'].apply(str)

import datetime
basename = os.getcwd()+'\\Chromaticity\\Chromaticity_3under_match'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
chromaticity_3under_match.to_csv(basename+'_Chromaticity.csv')

#%%
#정규표현식을 이용한 삭제
'''
import re
i = "Index(['057', '058'], dtype='object', name='po.'"
test = re.sub('[a-zA-Z]',' ',i).strip()
'''

# %%
'''
for co in chromaticity_3under.columns:
    chromaticity_3under_match.loc[co,'match_point'] = re.sub('[a-zA-Z]',' ',chromaticity_3under_match[co]).strip()
'''

