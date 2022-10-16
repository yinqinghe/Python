import pandas as pd
pdd = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series(
    [1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(pdd)
# 使用列索引
print(df['one'])
# a    1.0
# b    2.0
# c    3.0
# d    NaN
# Name: one, dtype: float64

# 列索引添加数据列
df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df)
#    one  two  three
# a  1.0    1   10.0
# b  2.0    2   20.0
# c  3.0    3   30.0
# d  NaN    4    NaN

df['four'] = df['one']+df['three']
print(df)
#    one  two  three  four
# a  1.0    1   10.0  11.0
# b  2.0    2   20.0  22.0
# c  3.0    3   30.0  33.0
# d  NaN    4    NaN   NaN


info = [['Jack', 18], ['Helen', 19], ['John', 17]]
df_1 = pd.DataFrame(info, columns=['name', 'age'])
print(df_1)
#     name  age
# 0   Jack   18
# 1  Helen   19
# 2   John   17
df_1.insert(1, column='score', value=[91, 90, 75])
print(df_1)
#     name  score  age
# 0   Jack     91   18
# 1  Helen     90   19
# 2   John     75   17


# 列索引删除数据列
df_2 = pd.DataFrame(pdd)
print("Our dataframe is:\n", df_2)
#    one  two
# a  1.0    1
# b  2.0    2
# c  3.0    3
# d  NaN    4
# 使用del删除
del df_2['one']
print(df_2)
#    two
# a    1
# b    2
# c    3
# d    4
# 使用pop方法删除
df_2.pop('two')
print(df_2)
# Empty DataFrame
# Columns: []
# Index: [a, b, c, d]


# 行索引操作DataFrame
# 标签索引选取   loc允许接两个参数分别是行和列  参数之间需要使用 逗号  隔开   但该函数只能接受标签索引
df_3 = pd.DataFrame(pdd)
print(df_3.loc['b', 'one'])
# one    2.0
# two    2.0
# Name: b, dtype: float64

# 整数索引选取
# 通过将数据行所在的索引位置传递给iloc函数  也可以实现数据行选取
print(df_3.iloc[2])
# one    3.0
# two    3.0
# Name: c, dtype: float64

# 切片操作多行选取
print(df_3[2:4])
#    one  two
# c  3.0    3
# d  NaN    4

# 添加数据行
app = pd.DataFrame([[22, 22], [22, 22]], columns=['one', 'two'])
# 在行末追加新数据行
df_3 = df_3.append(app)
print(df_3)
#     one  two
# a   1.0    1
# b   2.0    2
# c   3.0    3
# d   NaN    4
# 0  22.0   22
# 1  22.0   22

# 删除数据行
# 可以使用行索引标签  从DataFrame中删除某一行数据  如果索引标签存在重复  那么它们将被一起删除
df_3 = df_3.drop('a')
print(df_3)
#     one  two
# b   2.0    2
# c   3.0    3
# d   NaN    4
# 0  22.0   22
# 1  22.0   22
