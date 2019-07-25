import pandas as pd

broad_df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.

print(broad_df.loc[2012:,'KBS':'JTBC'])

