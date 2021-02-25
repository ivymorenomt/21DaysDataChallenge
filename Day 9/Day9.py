import pandas as pd

df = pd.read_csv('milk_2.csv')
df.head()

df_median = df['Monthly milk production: pounds per cow'].median()

df['Monthly milk production: pounds per cow'] = df['Monthly milk production: pounds per cow'].fillna(value = df_median)
df.head(100)
# df.isnull().sum(axis = 0)
df['Number of Cows'] = df['Number of Cows'].fillna(method='ffill')
df.head()
# df.isnull().sum(axis = 0)


#Q1
df['Monthly milk production: pounds per cow'] = df['Monthly milk production: pounds per cow'].mean()

#Q2
df['Monthly milk production: pounds per cow'] = df['Monthly milk production: pounds per cow'].std()
df

#Q3

df['Number of Cows'] = df['Number of Cows'].mean()
df