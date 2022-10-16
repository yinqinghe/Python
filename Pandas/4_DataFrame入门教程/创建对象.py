# DataFrame 是Pandas的重要数据结构之一  也是在使用Pandas进行数据分析过程中最常用的结构之一
# 可以这么说  掌握了DataFrame的用法  你就拥有了学习数据分析的基本能力

# DataFrame一个表格型的数据结构  既有行标签(index)  又有列标签(columns)
# 它也被称异构数据表  所谓异构  指的是表格中每列的数据类型可以不同
# 比如可以是字符串  整数或者浮点型

from cmath import nan
import pandas as pd
df = pd.DataFrame()
# 创建空的DataFrame对象
print(df)
# Empty DataFrame
# Columns: []
# Index: []
data = [1, 2, 3, 4, 5]
# 列表创建DataFrame对象
df = pd.DataFrame(data)
print(df)
#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5

# 使用嵌套列表创建DataFrame对象
data1 = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df1 = pd.DataFrame(data1, columns=['Name', 'Age'])
print(df1)
# Name  Age
# 0    Alex   10
# 1     Bob   12
# 2  Clarke   13
# 指定数值元素的数据类型为float
df2 = pd.DataFrame(data1, columns=['Name', 'Age'], dtype=float)
print(df2)
# Name   Age
# 0    Alex  10.0
# 1     Bob  12.0
# 2  Clarke  13.0


# 字典嵌套列表创建
data2 = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
df3 = pd.DataFrame(data2)
print(df3)
#      Name  Age
# 0    Tom   28
# 1   Jack   34
# 2  Steve   29
# 3  Ricky   42
# 给上述事例添加自定义的行标签
df4 = pd.DataFrame(data2, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df4)
#         Name  Age
# rank1    Tom   28
# rank2   Jack   34
# rank3  Steve   29
# rank4  Ricky   42
# 注意  index参数为每行分配了一个索引


# 列表嵌套字典创建DataFrame对象
data5 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df5 = pd.DataFrame(data5)
print(df5)
#    a   b     c
# 0  1   2   NaN
# 1  5  10  20.0
# 注意  如果其中某个元素值缺失  也就是字典的key无法找到对应的value  将使用NaN代替
# 给上述事例添加自定义的行标签
df6 = pd.DataFrame(data5, index=['frist', 'second'])
print(df6)
#         a   b     c
# frist   1   2   NaN
# second  5  10  20.0

# 如何使用字典嵌套列表以及行、列索引表创建一个DataFrame对象
df_1 = pd.DataFrame(data5, index=['frist', 'second'], columns=['a', 'b'])
df_2 = pd.DataFrame(data5, index=['frist', 'second'], columns=['a', 'b1'])
print(df_1)
#         a   b
# frist   1   2
# second  5  10
print(df_2)
#         a  b1
# frist   1 NaN
# second  5 NaN
# 因为b1在字典键中不存在  所以对应值为NaN


# Series创建DataFrame对象
pdd = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series(
    [1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df_3 = pd.DataFrame(pdd)
print(df_3)
#    one  two
# a  1.0    1
# b  2.0    2
# c  3.0    3
# d  NaN    4
# 注意  对于one列而言  此处虽然现实了行索引'd'  但由于没有与其对应的值  所以它的值为NaN
