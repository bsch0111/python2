#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
 # %%
base_dir = "C:/inputcsv/painting/conUNSOUNG/BABY(PAI, UN-SOUNG)/3. Material Analysis/3.2 Basic Analysis/3.2.2 Chromaticity"
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
#index를 point로 여기서 하면 추후에 squreform할 때 index로 사용할 컬럼이 부족
#chromaticity_df = chromaticity_df.set_index('point')

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
# 실험 중 1로 수정
chromaticity_3under = df_dist[(df_dist< 1) & (df_dist != 0)]

# %%
chromaticity_3under_match = pd.DataFrame(columns=['match'],index=chromaticity_3under.columns)

# %%
for co in chromaticity_3under.columns:
    matching = []
    # Series 나 Dataframe의 데이터를 조회할 때 dtype과 Name를 출력하고 싶지 않다면, 배열에 넣은후 출력하는 방법 사용 
    for var in (chromaticity_3under[chromaticity_3under[co] > 0].index) :
        matching.append(var)
    chromaticity_3under_match.loc[co,'match'] = matching
# %%
import datetime
basename1 = os.getcwd()+'\\Chromaticity\\Chromaticity_3under_match'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
basename2 = os.getcwd()+'\\Chromaticity\\Chromaticity_dist'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")

chromaticity_3under_match.to_csv(basename1+'_Chromaticity.csv')
df_dist.to_csv(basename2+'.csv')
#plt = sns.get_figure()
#plt.savefig(basename2 +'_output.png')

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

# %%
# 데이터 output 저장용 코드
'''
import datetime
basename = os.getcwd()+'\\Chromaticity\\Chromaticity_3under'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
chromaticity_3under.to_csv(basename+'_Chromaticity.csv')
'''