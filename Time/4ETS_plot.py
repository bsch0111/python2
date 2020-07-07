#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# %%
# y_t = Level + Trend + Seaseonality + Noise (Error)
# y_t = Trend + Seaseonality + Noise (Error) Level 데이터는 Decomposition으로 포함되지 못하기 때문에 Noise에 포함됨

from statsmodels.tsa.seasonal import seasonal_decompose
# 임의로 상향트렌드를 가진 데이터 만들기
# [i for i in range(1,100) ]

# 이런식으로도 리스트 반복문을 표현할수 있구나
# 상향트렌드를 가지도록 노이즈 추가
# [i+np.random.randint(10) for i in range(1,100) ]

series = pd.Series([i+np.random.randint(10) for i in range(1,100) ])    

# %%
# 기본 모델이 additive지만 여기선 명시함(그냥)
result = seasonal_decompose(series, model='additive', freq=1)
# %%
# 트렌드만 존재함을 확인할 수 있음
result.plot();=
# %%
# residual 도 없음을 확인할 수 있음
result.resid

# %%
# 조금 더 보기좋게 다듬기
def plot_decompose(decomposeresult):
    #fig는 4개의 그래프 전체 그림을 의미하고 ax1, ax2, ax3, ax4는 각각의 슬롯을 의미함
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4,1, figsize=(15,8))
    decomposeresult.observed.plot(legend=False, ax=ax1)
    # 위에서 입력이 시리즈니까 결과도 시리즈로 나옴, 리스트로 들어오면 결과가 리스트로 나옴
    # 시리즈기 떄문에 plot을 그릴 수 있음
    ax1.set_ylabel('Observed')

    decomposeresult.trend.plot(legend=False, ax=ax2)
    ax2.set_ylabel('Trend')

    decomposeresult.seasonal.plot(legend=False, ax=ax3)
    ax2.set_ylabel('seasonal')

    decomposeresult.resid.plot(legend=False, ax=ax4)
    ax2.set_ylabel('Resid')


# %%
plot_decompose(result)

# %%
# y-t = Level * Error * Trend * Seasonality 로 표현되는 모델
# 앞에다 Log만 씌워주면 +로 풀림
# log(y-t) = Level + Error + Trend + Seasonality

series = pd.Series([ i**2 for i in range(1,100)])

# %%
# 지수형이기 때문에 커브형으로 올라가는것을 확인할 수  있음
series.plot()


# %%
# 모델만 multiplicative로 바꿈
result = seasonal_decompose(series, model='multiplicative', freq=1)

# %%
plot_decompose(result)

# %%
# airline_passengers를 이용해서 multiplicative 활용해보기
airline = pd.read_csv('C:/inputcsv/tsa_tutorial_data/airline_passengers.csv', index_col = 'Month')

# %%
airline.plot()
#%%
airline.index = pd.to_datetime(airline.index)

# %%
result_addivive = seasonal_decompose(airline['Thousands of Passengers'], freq=1)
result_multi = seasonal_decompose(airline['Thousands of Passengers'],model='multiplicative', freq=1)

# %%
plot_decompose(result_addivive)

# %%
plot_decompose(result_multi)

# %%
