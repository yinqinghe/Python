# Series结构  也称Series序列  是Pandas常用的数据结构之一  它是一种类似于一维数组的结构
# 有一组数据值(value)和一组标签组成   其中标签与数据值是一一对应的关系
# Series可以保存任何数据类型  比如整数  字符串  浮点数  Python对象

import numpy as np
import pandas as pd
s = pd.Series()
print(s)

data = np.array(['a', 'b', 'c', 'd'])
ss = pd.Series(data)
print(ss)
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object

# 自定义索引标签(即显示索引)
sss = pd.Series(data, index=[98, 101, 102, 103])
print(sss)
# 100    a
# 101    b
# 102    c
# 103    d
# dtype: object

# 用dict创建series对象
data1 = {'a': 0., 'b': 1, 'c': 2}
print(pd.Series(data1))
# a    0
# b    1
# c    2
# dtype: int64


print(pd.Series(data1, index=['b', 'c', 'd', 'a']))
# b    1.0
# c    2.0
# d    NaN
# a    0.0
# dtype: float64


# 标量创建Series对象
# 如果data是标量值  则必须提供索引
s1 = pd.Series(5, index=[0, 1, 2, 3])
print(s1)
# 0    5
# 1    5
# 2    5
# 3    5
# dtype: int64


s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s2[0], '   ', s2['a'])  # 位置下标   标签下标
# 1     1
# 通过切片的方式访问数据
print(s2[:3])
# a    1
# b    2
# c    3
# dtype: int64

print(s2[-3:])
# c    3
# d    4
# e    5
# dtype: int64

# 索引标签访问
s3 = pd.Series([6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e'])
print(s3['a'])
print(s3[['a', 'c', 'd']])
# 6
# a    6
# c    8
# d    9
# dtype: int64
# 如果使用了index中不包含的标签  则会触发异常
print(s3['f'])
# KeyError: 'f'
