import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

# 코드를 작성하세요.
date = samsong_df['요일']
s_culturePay = samsong_df['문화생활비']
h_culturePay = hyundee_df['문화생활비']

dict1 = {
    'day': date,
    'samsong': s_culturePay,
    'hyundee': h_culturePay
}

df = pd.DataFrame(dict1)

print(df)