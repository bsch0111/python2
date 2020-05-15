import numpy as np
import pandas as pd
import os
import string as str


#hyper_cor.exe [저장소의 hyper 데이터 디렉토리명] [비교대상의 hyper 데이터 디렉토리명]
base_file = 'C:/inputcsv/3.3.2 VIR(500-900nm) Spectrum/PAINTING_BABY_071-VIR Spectrum.txt' #sys[1]로 대체해야함
target_file = 'C:/inputcsv/3.3.2 VIR(500-900nm) Spectrum/PAINTING_BABY_072-VIR Spectrum.txt' #sys[2]로 대체해야함
#파일이름에서 point가 어딘지 추출
if 'VIR' in base_file:
    point = base_file[-20:-17]
elif 'VNIR' in base_file:
    point = base_file[-21:-18]
col_name = ['nm',point]
# 세번째 줄까지 삭제(상관계수를 비교하기에 불필요한 문장)
#base
with open(base_file, 'r') as base_f:
       base_lines = base_f.readlines()
with open(os.getcwd()+'/temp_base_file.txt', 'w') as base_f:
       base_f.writelines(base_lines[3:])

base_data = pd.read_table(os.getcwd()+'/temp_base_file.txt',sep='\s+',names=col_name)

#target
with open(target_file, 'r') as target_f:
       target_lines = target_f.readlines()
with open(os.getcwd()+'temp_target_file.txt', 'w') as target_f:
       target_f.writelines(target_lines[3:])
target_data = pd.read_table(os.getcwd()+'temp_target_file.txt',sep='\s+',names=col_name)

#상관계수(pearson, spearman, kendall)
pearson = base_data[point].corr(target_data[point], method="pearson")
spearman = base_data[point].corr(target_data[point], method="spearman")
kendall = base_data[point].corr(target_data[point], method="kendall")


print("{")
print(' "pearson" : "%f"' % pearson)
print(' "spearman" :"%f"' % spearman)
print(' "kendall" : "%f"' % kendall)
print("}")
