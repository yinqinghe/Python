# 在数据分析过程中 很多时候需要从数据表中提取出相应的数据  而这么做的前提是需要先“索引”
# 出这一部分数据  虽然通过Python提供的索引操作符[]和属性操作符.可以访问Series 或者 DataFrame中的数据
# 但这种方式只适应与少量的数据  为了解决这一问题  Pandas提供了两种类型的索引方式来实现数据的访问

# .loc[]  基于标签索引选取数据
# .iloc[] 基于整数索引选取数据
from textwrap import indent
import numpy as np
import pandas as pd

data = {'name': ['John', 'Mike', 'Mozla', 'Rose', 'David', 'Marry', 'Wansi', 'Sidy', 'Jack', 'Alic'],
        'age': [20, 32, 29, np.nan, 15, 28, 21, 30, 37, 25],
        'gender': [0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
        'isMarried': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=label)
print(df)
# loc[]只能使用标签索引  不能使用整数索引  当通过标签索引的切片方式来筛选数据时  它的取值前闭后闭
# 也就是只包括边界值标签
# loc[]接受两个参数  并','分隔  第一个位置表示行  第二个位置表示列
# 对行操作
print(df.loc['a':'d', :])  # 等同于df.loc['a':'d']

#  对列操作
print(df.loc[:, 'name'])

df1 = pd.DataFrame(np.random.randn(8, 4), index=[
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
                   columns=['A', 'B', 'C', 'D'])
# 对列和行同时操作
print(df1.loc[['a', 'b', 'f', 'h'], ['A', 'C']])
#            A         C
# a - 1.052020 - 0.711093
# b - 1.049226  0.456114
# f  0.137049  2.118239
# h  0.023661 - 0.794804

df2 = pd.DataFrame(np.random.randn(4, 4), index=[
                   'a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
# 返回一组布尔值
print(df2.loc['b'] > 0)
# A     True
# B    False
# C    False
# D    False
# Name: b, dtype: bool

# iloc[]只能使用整数索引  不能使用标签索引  通过整数索引切片选择数据时  前闭后开  不包含边界结束值
# 同Python和NumPy一样  他们的索引都是从0开始

print(df.iloc[2:, ])


df3 = pd.DataFrame(np.random.rand(8, 4), columns=['A', 'B', 'C', 'D'])
print(df3.iloc[[1, 3, 5], [1, 3]])
#          B         D
# 1  0.340296  0.995686
# 3  0.197879  0.264485
# 5  0.324358  0.300123
print(df3.iloc[1:3, :])
#           A         B         C         D
# 1  0.437392  0.340296  0.408733  0.995686
# 2  0.522093  0.765369  0.140646  0.784172
print(df3.iloc[:, 1:3])
#           B         C
# 0  0.362703  0.454457
# 1  0.340296  0.408733
# 2  0.765369  0.140646
# 3  0.197879  0.414294
# 4  0.384466  0.352376
# 5  0.324358  0.387305
# 6  0.702719  0.987517
# 7  0.829875  0.104194
