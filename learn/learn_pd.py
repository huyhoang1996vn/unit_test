print("===============")

import pandas as pd
print("===============")

df = pd.read_csv("ca-covid.csv")

print(df.info())


print(df.head(10))

df.set_index('date', inplace=True, drop=False)
print(df.loc['31.12.20'])
# same
print(df.iloc[1])

print('index')
# print(df.head(10))
print(df.iloc[:3])
# df.drop('state', axis=1, inplace=True)
df.drop(index='31.12.20', inplace=True)
df['month'] = pd.to_datetime(df['date'], format="%d.%m.%y").dt.month_name()

print(df.tail(10))
print(df.iloc[-3:])

print(df['month'].value_counts())
print(df.groupby('month')['cases'].sum())

# Elastic Search



