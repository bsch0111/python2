#%%
import numpy as np
import pandas as pd
import os

#%%
#base_file을 작품별로 수정
base_file = 'C:/inputcsv/20200514/family/3.3.1 Terahertz Spectrum'

#%%
Absorbance_list = []
Imaginary_Refractive_Index_list = []
Real_Refractive_Index_list = []
Reflectance_list = []

#base_file의 모든 파일을 기준으로 THz Absorbance, THz Imaginary Refractive Index ,THz Real Refractive Index, THz Reflectance 파일을 구분함
#%%
files = os.listdir(base_file)

for file in files:
    path = os.path.join(base_file,file)
    if 'Absorbance' in file and ('png' in file) == False:
      Absorbance_list.append(path)
    if 'Imaginary Refractive Index' in file and ('png' in file) == False:
      Imaginary_Refractive_Index_list.append(path)
    if 'Real Refractive Index' in file and ('png' in file) == False:
      Real_Refractive_Index_list.append(path)
    if 'Reflectance' in file and ('png' in file) == False:
      Reflectance_list.append(path)


#index 생성
#%%
index_Absorbance = pd.read_excel(Absorbance_list[0],sheet_name='Sheet1')
index_Absorbance = index_Absorbance.drop('Absorbance',1)
index_Imaginary_Refractive_Index = pd.read_excel(Imaginary_Refractive_Index_list[0],sheet_name='Sheet1')
index_Imaginary_Refractive_Index = index_Imaginary_Refractive_Index.drop('Imaginary Refractive Index',1)
index_Real_Refractive_Index = pd.read_excel(Real_Refractive_Index_list[0],sheet_name='Sheet1')
index_Real_Refractive_Index = index_Real_Refractive_Index.drop('Real Refractive Index',1)
index_Reflectance = pd.read_excel(Reflectance_list[0],sheet_name='Sheet1')
index_Reflectance = index_Reflectance.drop('Reflectance',1)


#index 데이터 프레임 생성
df_absorbance = pd.DataFrame(index_Absorbance)
df_Imaginary_Refractive_Index = pd.DataFrame(index_Imaginary_Refractive_Index)
df_Real_Refractive_Index = pd.DataFrame(index_Real_Refractive_Index)
df_Reflectance = pd.DataFrame(index_Reflectance)


def point_merge(df, file_list, col_name): 
    for file in file_list:
        # 긴 이름 중에서 포인트만 추출 https://dongdongfather.tistory.com/74
        point = 0
        if col_name in 'Absorbance':
            point = file[-23:-20]
        elif col_name in 'Imaginary Refractive Index':
            point = file[-39:-36]
        elif col_name in 'Real Refractive Index':
            point = file[-34:-31]
        elif col_name in 'Reflectance':
            point = file[-24:-21]
        df_t = pd.read_excel(file,sheet_name='Sheet1')
        # col 명 변경 
        df_t.rename(columns={col_name:point}, inplace=True)
        # outer join  https://rfriend.tistory.com/258
        df = pd.merge(df,df_t,how='outer',on='wavenumber(cm^-^1)')

    df.set_index('wavenumber(cm^-^1)')
    return df 

df_absorbance = point_merge(df_absorbance, Absorbance_list,'Absorbance')
df_Imaginary_Refractive_Index = point_merge(df_Imaginary_Refractive_Index, Imaginary_Refractive_Index_list, 'Imaginary Refractive Index')
df_Real_Refractive_Index = point_merge(df_Real_Refractive_Index, Real_Refractive_Index_list, 'Real Refractive Index')
df_Reflectance = point_merge(df_Reflectance, Reflectance_list, 'Reflectance')

import datetime
basename = os.getcwd()+'\\THz\\THz'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")

#현재 실행경로 구하기 https://wikidocs.net/3716
df_absorbance.to_csv(basename+'_Absorbance.csv')
df_Imaginary_Refractive_Index.to_csv(basename+'_Imaginary_Refractive_Index.csv')
df_Real_Refractive_Index.to_csv(basename+'_Real_Refractive_Index.csv')
df_Reflectance.to_csv(basename+'_Reflectance.csv')
