import pandas as pd

iphone_df = pd.read_csv("data/iphone.csv", index_col=0)

print(iphone_df)

print(iphone_df.loc['iPhone 8','메모리'])      # 데이터 가져오기

print(iphone_df.loc['iPhone X', :])