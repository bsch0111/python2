import pandas as pd

com_csv_path = "C:/inputcsv/200407_142743.csv"
org_csv_path = "C:/inputcsv/200407_134425.csv"

data1 = pd.read_csv(com_csv_path)
data2 = pd.read_csv(org_csv_path)

data3 = pd.merge(data1,data2,on='파일명')

data3['Match'] = (data3['원소명_x'] == data3['원소명_y'])
data3.to_csv("match.csv")
