# 使用SQL语句能够完成对table的增删改查操作  Pandas同样也可以实现SQL语句
# 的基本功能   pandas如何执行SQL操作


import pandas as pd
url = 'D:\C#\VSCODE\python\Pandas\website.xlsx'
coffee_df = pd.read_excel(url)
coffee_df.head()
print(coffee_df.head())

print(coffee_df[['name', 'rank', 'language', 'url']])

print(coffee_df.groupby('rank').size())

print(coffee_df[['name', 'rank']].head(3))
