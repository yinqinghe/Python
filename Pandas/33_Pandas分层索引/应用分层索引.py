import pandas as pd
import numpy as np
arrays = [[0, 0, 1, 1], ['A', 'B', 'C', 'B']]

index = pd.MultiIndex.from_arrays(arrays, names=('number', 'letter'))

print(index)
# MultiIndex([(0, 'A'),
#             (0, 'B'),
#             (1, 'C'),
#             (1, 'B')],
#            names=['number', 'letter'])
# 第一层为number  该层有0 1两个元素  第二层为letter  有两个字母A和B
df = pd.DataFrame([{'a': 11, 'b': 22}], index=index)
print(df)

df1 = pd.DataFrame({'a': range(5), 'b': range(5, 0, -1),
                    'c': ['one', 'one', 'one', 'two', 'two'], 'd': [0, 1, 2, 0, 1]})
print(df1)
# 通过set_index()可以将DataFrame的已有列的标索设置为index行索引
df2 = df1.set_index(['a', 'd'], drop=False)
print(df2)
df3 = df1.set_index(['a', 'd'], drop=False, append=True)
print(df3)
# 通过set_index()将列索引转换为了分层行索引  其中drop=False表示更新索引的同时  不删除a、d列
# 同时  该函数还提供了一个append=True参数表示不添加默认的整数索引值(0到4)

# 分层索引切片取值
tuple = [('湖人', 2008), ('步行者', 2007), ('湖人', 2007), ('凯尔特人', 2007),
         ('蓝网', 2007), ('热火', 2008)]
salary = [10000, 20000, 11000, 30000, 19000, 22000]
index1 = pd.MultiIndex.from_tuples(tuple)
s = pd.Series(salary, index=index1)
print(s)
# 切片取值
# 湖人队的工资
print(s['湖人', 2007], '\n')
# 湖人队的工资
print(s['湖人'], '\n')
# 2008年所有队伍工资
print(s[:, 2007], '\n')
# 比较value
# 小于等于20000的年份和队伍
print(s[s <= 20000], '\n')


# 行、列多层索引操作
df_df = pd.DataFrame(np.arange(1, 13).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Jack', 'Jack', 'Helen'], ['Python', 'Java', 'Python']])
# 选择同一层级的索引切记不要写成
# ['Jack','Helen']
print(df_df[['Jack', 'Helen']])
# 在不同层级分别选择索引
print(df_df['Jack', 'Python'])
# iloc整数索引
print(df_df.iloc[:3, :2])
# loc列标签索引
print(df_df.loc[:, ('Helen', 'Python')])
