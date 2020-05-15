#MATPLOTLIBDATA Warning 무시
import warnings
warnings.filterwarnings("ignore", "(?s).*MATPLOTLIBDATA.*", category=UserWarning)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import string
import sys
import xlrd


# XRF 데이터 읽어오기
pwd=sys.argv[1]

#파일명(확장자까지), 폴더경로
filename = os.path.basename(pwd)
dirname = os.path.dirname(pwd)
data=pd.read_excel(pwd,sheet_name='Sheet1')
# energy, 40KeV, 15KeV
plt.plot(data['energy'],data['40KeV'],color='r',)
plt.plot(data['energy'],data['15KeV '],color='b')

#단위는 5단위로 ~ 40까지
plt.title(filename)
#확장자
gls = os.path.splitext(filename)
#범례지정하기
plt.legend(['40KeV','15KeV'])
plt.xlabel("Energy(KeV)",labelpad=5)
plt.ylabel("CPS")
plt.xticks([0,5,10,15,20,25,30,35,40])
plt.savefig(dirname+'/'+gls[0]+'.png',dpi=300)
