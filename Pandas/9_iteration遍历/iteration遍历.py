import pandas as pd
import numpy as np
N = 20
df = pd.DataFrame({'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
                   'x': np.linspace(0, stop=N-1, num=N),
                   'y': np.random.rand(N),
                   'C': np.random.choice(['low', 'Medium', 'High'], N).tolist(),
                   'D': np.random.normal(100, 10, size=(N)).tolist()})
# print(df)
for col in df:
    print(col)
# A
# x
# y
# C
# D

# 内置迭代方法
# 如果想要遍历DataFrame的每一行  下列函数
# 1、iteritems()   以键值对(key,value)的形式遍历
# 2、iterrows()    以(row_index,row)的形式遍历行
# 3、itertuples()   使用已命名元祖的方式对行遍历
df1 = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])
# 以键值对的形式遍历DataFrame对象   以列标签为键  以对应列的元素为值
for key, value in df1.iteritems():
    print(key, '  qq', value)
print('-----------------------')
# 按行遍历  返回一个迭代器  以行索引标签为键  以每一行数据为值
for row_index, row in df1.iterrows():
    print(row_index, row)

print('-----------------------')
# itertuples()返回一个迭代器  该方法会把DataFrame的每一行生成一个元祖
df2 = pd.DataFrame(np.random.rand(3, 3), columns=['c1', 'c2', 'c3'])
for row in df2.itertuples():
    print(row)

# 迭代返回副本
# 迭代器返回的是原对象的副本  所以  如果在迭代过程中修改元素值  不会影响原对象
for index, row in df2.iterrows():
    row['a'] = 15
print(df2)
# 原对象df2没有受到任何影响
