#%%
import pandas as pd
import numpy as np
# %%
basefile500_900 = "C:/inputcsv/Hyper_result/baby/VIR(500-900nm) Spectrum/Hyper200514_174439HyperSpectrum.csv"
basefile1000_1600 = "C:/inputcsv/Hyper_result/baby/VNIR(1000-1600nm) Spectrum/Hyper200514_174418HyperSpectrum.csv"
# %%
vir500_900 = pd.read_csv(basefile500_900)
vir1000_1600 = pd.read_csv(basefile1000_1600)
# %%
vir500_900 = vir500_900.drop(['Unnamed: 0'], axis=1)
vir1000_1600 = vir1000_1600.drop(['Unnamed: 0'], axis=1)
# %%
vir500_900
# %%
print("vir500_900 : [059 099]",vir500_900['059'].corr(vir500_900['099'], method="pearson"))
print("vir500_900 : [062 064]",vir500_900['062'].corr(vir500_900['064'], method="pearson"))
print("vir500_900 : [066 072]",vir500_900['066'].corr(vir500_900['072'], method="pearson"))
print("vir500_900 : [081 082]",vir500_900['081'].corr(vir500_900['082'], method="pearson"))
print("vir500_900 : [094 096]",vir500_900['094'].corr(vir500_900['096'], method="pearson"))
print("vir500_900 : [094 097]",vir500_900['094'].corr(vir500_900['097'], method="pearson"))
print("vir500_900 : [096 097]",vir500_900['096'].corr(vir500_900['097'], method="pearson"))

print("vir1000_1600 : [059 099]",vir1000_1600['059'].corr(vir1000_1600['099'], method="pearson"))
print("vir1000_1600 : [062 064]",vir1000_1600['062'].corr(vir1000_1600['064'], method="pearson"))
print("vir1000_1600 : [066 072]",vir1000_1600['066'].corr(vir1000_1600['072'], method="pearson"))
print("vir1000_1600 : [081 082]",vir1000_1600['081'].corr(vir1000_1600['082'], method="pearson"))
print("vir1000_1600 : [094 096]",vir1000_1600['094'].corr(vir1000_1600['096'], method="pearson"))
print("vir1000_1600 : [094 097]",vir1000_1600['094'].corr(vir1000_1600['097'], method="pearson"))
print("vir1000_1600 : [096 097]",vir1000_1600['096'].corr(vir1000_1600['097'], method="pearson"))


# %%
print("vir500_900 : [059 099]",vir500_900['059'].corr(vir500_900['099'], method="spearman"))
print("vir500_900 : [062 064]",vir500_900['062'].corr(vir500_900['064'], method="spearman"))
print("vir500_900 : [066 072]",vir500_900['066'].corr(vir500_900['072'], method="spearman"))
print("vir500_900 : [081 082]",vir500_900['081'].corr(vir500_900['082'], method="spearman"))
print("vir500_900 : [094 096]",vir500_900['094'].corr(vir500_900['096'], method="spearman"))
print("vir500_900 : [094 097]",vir500_900['094'].corr(vir500_900['097'], method="spearman"))
print("vir500_900 : [096 097]",vir500_900['096'].corr(vir500_900['097'], method="spearman"))

print("vir1000_1600 : [059 099]",vir1000_1600['059'].corr(vir1000_1600['099'], method="spearman"))
print("vir1000_1600 : [062 064]",vir1000_1600['062'].corr(vir1000_1600['064'], method="spearman"))
print("vir1000_1600 : [066 072]",vir1000_1600['066'].corr(vir1000_1600['072'], method="spearman"))
print("vir1000_1600 : [081 082]",vir1000_1600['081'].corr(vir1000_1600['082'], method="spearman"))
print("vir1000_1600 : [094 096]",vir1000_1600['094'].corr(vir1000_1600['096'], method="spearman"))
print("vir1000_1600 : [094 097]",vir1000_1600['094'].corr(vir1000_1600['097'], method="spearman"))
print("vir1000_1600 : [096 097]",vir1000_1600['096'].corr(vir1000_1600['097'], method="spearman"))

# %%
print("vir500_900 : [059 099]",vir500_900['059'].corr(vir500_900['099'], method="kendall"))
print("vir500_900 : [062 064]",vir500_900['062'].corr(vir500_900['064'], method="kendall"))
print("vir500_900 : [066 072]",vir500_900['066'].corr(vir500_900['072'], method="kendall"))
print("vir500_900 : [081 082]",vir500_900['081'].corr(vir500_900['082'], method="kendall"))
print("vir500_900 : [094 096]",vir500_900['094'].corr(vir500_900['096'], method="kendall"))
print("vir500_900 : [094 097]",vir500_900['094'].corr(vir500_900['097'], method="kendall"))
print("vir500_900 : [096 097]",vir500_900['096'].corr(vir500_900['097'], method="kendall"))

print("vir1000_1600 : [059 099]",vir1000_1600['059'].corr(vir1000_1600['099'], method="kendall"))
print("vir1000_1600 : [062 064]",vir1000_1600['062'].corr(vir1000_1600['064'], method="kendall"))
print("vir1000_1600 : [066 072]",vir1000_1600['066'].corr(vir1000_1600['072'], method="kendall"))
print("vir1000_1600 : [081 082]",vir1000_1600['081'].corr(vir1000_1600['082'], method="kendall"))
print("vir1000_1600 : [094 096]",vir1000_1600['094'].corr(vir1000_1600['096'], method="kendall"))
print("vir1000_1600 : [094 097]",vir1000_1600['094'].corr(vir1000_1600['097'], method="kendall"))
print("vir1000_1600 : [096 097]",vir1000_1600['096'].corr(vir1000_1600['097'], method="kendall"))

# %%
