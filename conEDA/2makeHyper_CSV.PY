#%%
import numpy as np
import pandas as pd
import os

#전처리 꼭해줘야함
#sed -i '1,3d' * 세번째 줄까지 줄이는 것

#base_file을 작품별로 수정
#%%
base_file = 'C:/inputcsv/20200514/family/3.3.3. VNIR(1000-1600nm) Spectrum'
#3.3.2 VIR(500-900nm) Spectrum
#3.3.3. VNIR(1000-1600nm) Spectrum

files = os.listdir(base_file)
hyper_list = []
df_Hyper = pd.DataFrame(columns=['nm'])


#%%
for file in files:

    path = os.path.join(base_file,file)
    point = 0
    if 'VIR' in file:
        point = file[-20:-17]
    elif 'VNIR' in file:
        point = file[-21:-18]
  
    col_name = ['nm',point]

    # 공백을 구분자로한 csv 파일 읽기 # col_names 명시 
    data = pd.read_table(path,sep="\s+",names= col_name)
    # 전처리가 안되어 있으면 merge에서 메모리 오류남
    df_Hyper = pd.merge(df_Hyper,data,how='outer',on='nm')

df_Hyper.set_index('nm')


import datetime
basename = os.getcwd()+'\\Hyper\\Hyper'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")

df_Hyper.to_csv(basename+'HyperSpectrum.csv')

