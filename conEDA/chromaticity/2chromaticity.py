# 두 다른 그림의 포인트 비교
# baby(아기초상), family(가족초상)
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
 # %%
base_dir1 = "C:/inputcsv/painting/conUNSOUNG/BABY(PAI, UN-SOUNG)/3. Material Analysis/3.2 Basic Analysis/3.2.2 Chromaticity"
base_dir2 = "C:/inputcsv/painting/conUNSOUNG/FAMILY(PAI, UN-SOUNG)/3. Material Analysis/3.2 Basic Analysis/3.2.2 Chromaticity"
# 최종 결과물 속성
# point, L, a*, b*
#%%
# Chromaticity 파일리스트
files1=os.listdir(base_dir1)
files2=os.listdir(base_dir2)

# 포인트 배열
points1 = []
points2 = []
# %%
# 포인트 추출
for file in files1:
    point = file[-21:-18]
    points1.append(point)

for file in files2:
    point = file[-21:-18]
    points2.append(point)    
# %%
# 데이터프레임 생성
# point 열을 인덱스화
chromaticity_df1 = pd.DataFrame()
chromaticity_df1['point'] = points1

chromaticity_df2 = pd.DataFrame()
chromaticity_df2['point'] = points2
# %%
p_df1 = pd.DataFrame(columns=['Sample Name','L', 'a*','b*'])
for file in files1:
    path = os.path.join(base_dir1,file)
    # 데이터 프레임에 행 추가
    p_df1 = p_df1.append(pd.read_excel(path, sheet_name='Sheet1'),ignore_index=True) 

p_df2 = pd.DataFrame(columns=['Sample Name','L', 'a*','b*'])
for file in files2:
    path = os.path.join(base_dir2,file)
    # 데이터 프레임에 행 추가
    p_df2 = p_df2.append(pd.read_excel(path, sheet_name='Sheet1'),ignore_index=True) 

# %%
chromaticity_df1['L'] = p_df1['L']
chromaticity_df1['a*'] = p_df1['a*']
chromaticity_df1['b*'] = p_df1['b*']

chromaticity_df2['L'] = p_df2['L']
chromaticity_df2['a*'] = p_df2['a*']
chromaticity_df2['b*'] = p_df2['b*']
#index를 point로 여기서 하면 추후에 squreform할 때 index로 사용할 컬럼이 부족
#chromaticity_df = chromaticity_df.set_index('point')

#%%
# index를 chromaticity_df1 의 point로 columns 를 chromaticity_df2의 point로
# columns = chromaticity_df2
# index = chromaticity_df1
chromaticity_df1 = chromaticity_df1.apply(pd.to_numeric)
chromaticity_df2 = chromaticity_df2.apply(pd.to_numeric)
df_dist = pd.DataFrame(columns= chromaticity_df2['point'],index=chromaticity_df1['point'])
#%%
#df_dist[컬럼][인덱스]


#%%
#A = chromaticity_df1[chromaticity_df1['point']==103][['L','a*','b*']]
#B = chromaticity_df2[chromaticity_df2['point']==51][['L','a*','b*']]
from scipy.spatial import distance
for ch1_point in chromaticity_df1.point:
    column = chromaticity_df1[chromaticity_df1['point']==ch1_point][['L','a*','b*']]
    for ch2_point in chromaticity_df2.point:
        index = chromaticity_df2[chromaticity_df2['point']==ch2_point][['L','a*','b*']]
        df_dist[ch2_point][ch1_point] = distance.euclidean(column,index)
        df_dist.to_csv('df_distsdfsdf.csv')

        
#%%
for ch1_point in chromaticity_df1.point:
    for ch2_point in chromaticity_df2.point:
        print(ch1_point,'--------',ch2_point)
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
chromaticity_3under = df_dist[(df_dist< 4) & (df_dist != 0)]

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