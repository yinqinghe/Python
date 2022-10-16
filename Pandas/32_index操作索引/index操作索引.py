import pandas as pd
import numpy as np
data = pd.read_csv(r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv')
print(data)

# 设置 "Name"  为行索引
data = pd.read_csv(
    r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv', index_col="Name")
# 通过列标签选取多列数据
a = data[["City", "Salary"]]
print(a)

# 获取单列数据  或者以列表的形式传入["Salary"]
a = data['Salary']
print(a)

# 设置索引
info = pd.DataFrame({'Name': ['Parker', 'Terry', 'Smith', 'William'],
                     'Year': [2011, 2009, 2014, 2010], 'Leaves': [10, 15, 9, 4]})
# set_index()除了可以添加索引外  也可以替换已经存在的索引
# 也可以把Series 或者一个DataFrame设置成另一个DataFrame的索引
# 设置Name为行索引
print(info.set_index('Name'))

# 重置索引
infos = pd.DataFrame([('William', 'C'), ('Smith', 'Java'), ('Parker', 'Python'),
                      ('Phill', np.nan)], index=[1, 2, 3, 4], columns=('name', 'Language'))

print(infos)
print(infos.reset_index())
