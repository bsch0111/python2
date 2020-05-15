#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# %%
df = pd.DataFrame(columns=('x','y'))
# %%
df.loc[0] = [7,1]
df.loc[1] = [2,1]
df.loc[2] = [4,2]
df.loc[3] = [9,4]
df.loc[4] = [10,5]
df.loc[5] = [10,6]
df.loc[6] = [12,3]
df.loc[7] = [14,9]
df.loc[8] = [23,1]
df.loc[9] = [8,11]
df.loc[10] = [12,3]
df.loc[11] = [17,14]

# %%
sns.lmplot('x','y',data=df,fit_reg=False, scatter_kws={"s":200})
plt.title('K-means plot')
plt.xlabel('x')
plt.ylabel('y')
# %%
data_points = df.values
kmeans = KMeans(n_clusters=3).fit(data_points)

# %%
df['cluster_id'] = kmeans.labels_

# %%
sns.lmplot('x','y',data=df, fit_reg= False, scatter_kws={"s":150},hue="cluster_id")
plt.title("kmean plot ver2")
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
