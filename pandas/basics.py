import pandas as pd
# s = pd.Series([10, 20, 30, 40])
# print(s)

#dataframe
# data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
# df = pd.DataFrame(data)
# print(df)

data = {'Name': ['Alice', 'Bob','Charlie','David','Eve','Frank'],
        'age': [25, 30, 35, 40, None, 33],
        'Score': [85, 90, None, 92, 88, 75]}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e', 'f'])
# print(df.head())
# print(df.head(3))
# print(df.tail(2))
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.shape)
# print(df.loc['a'])
# print(df.loc['b', 'Name'])
# print(df.loc[:,['Name', 'Score']])
# print(df.iloc[2])
# print(df.iloc[1, 0])
# print(df.iloc[:, [0, 2]])
# print(df.isnull())
# print(df.dropna())
# print(df.fillna(0))
df['age'] = df['age'].fillna(df['age'].mean())
print(df)  