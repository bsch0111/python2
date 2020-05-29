#%%
import numpy as np
import pandas as pd
import os



# %%
base_dir = 'C:/bsch0111/Chromaticity'
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
chromaticity_df.set_index('point')
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
# %%
import datetime
basename = os.getcwd()+'\\Chromaticity\\Chromaticity'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")
chromaticity_df.to_csv(basename+'_Chromaticity.csv')
# %%


# %%
