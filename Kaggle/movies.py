#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

mpl.rcParams['axes.unicode_minus'] = False

# %%
print('버전: ',mpl.__version__)
print('설치 위치: ', mpl.__file__)
print('설정 위치: ', mpl.get_configdir())
print('캐시 위치: ',mpl.get_cachedir())
# %%
movies_test = pd.read_csv('C:\inputcsv\movies\movies_test.csv')
movies_train = pd.read_csv('C:\inputcsv\movies\movies_train.csv')
# %%
movies_train.head(3)
movies_train.info()
# %%
movies_train.isnull().sum()
# %%
# dir_prev_bfnum : 해당 감독이 이 영화를 만들기 전 제작에 참여한 영화에서의 평균 관객수(단 관객수가 알려지지 않은 영화 제외)
# dir_prev_bfnum이 null 이면 감독의 이전작이 없음  
movies_train.isnull().any()

# %%
movies_train = movies_train.fillna(0)
#%%
movies_train.isnull().any()

# %%
#divived by objecy, int64, and float64
movies_tr_obj = movies_train.select_dtypes(include=['object']).copy()
movies_tr_num = movies_train.select_dtypes(include=['int64']).copy()
movies_tr_float64 = movies_train.select_dtypes(include=['float64']).copy()

# %%
g = sns.pairplot(movies_train, hue="screening_rat")
sns.pairplot(movies_tr_num)
sns.pairplot(movies_tr_float64)

# %%
from sklearn.manifold import TSNE
m = TSNE(learning_rate = 50)
# %%
tsne_feature = m.fit_transform(movies_tr_num)
# %%
df = pd.DataFrame()
df['x'] = tsne_feature[:,0]
df['y'] = tsne_feature[:,1]
# %%
df = pd.concat([movies_tr_num, df], axis=1)
# %%
fig, ax = plt.subplots()
ax = sns.pointplot(x = 'x',y = 'y', hue='time', data=df)
plt.show()

# %%
df.head()

# %%
# Import train_test_split()
from sklearn.model_selection import train_test_split

# Select the Gender column as the feature to be predicted (y)
y = df['box_off_num'].values

# Remove the Gender column to create the training data
X = df.drop('box_off_num', axis=1).values

# Perform a 70% train and 30% test data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)

print("{} rows in test set vs. {} in training set. {} Features.".format(X_test.shape[0], X_train.shape[0], X_test.shape[1]))

# %%

y
# %%
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
svc = SVC()

# %%
svc.fit(X,y)

# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%
