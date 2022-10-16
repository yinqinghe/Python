# 描述性统计学  是一门统计学领域的学科  主要研究如何取得反映客观现象的数据  并以图表形式对所搜集的数据
# 进行处理和显示  最终对数据的规律、特征做出综合性的描述分析

# 对行操作  默认使用axis=0或者使用“index”
# 对列操作  默认使用axis=1或者使用“columns”

import pandas as pd
import numpy as np
d = {'Name': pd.Series(['小明', '小亮', '小红', '小华', '老赵', '小曹', '小陈', '老李', '老王', '小冯', '小何', '老张']),
     'Age': pd.Series([25, 26, 25, 23, 30, 29, 23, 34, 40, 30, 51, 46]),
     'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8, 3.78, 2.98, 4.80, 4.10, 3.65])}
df = pd.DataFrame(d)
print(df)

# 默认axis=0或者使用sum("index")
print(df.sum())
# Name      小明小亮小红小华老赵小曹小陈老李老王小冯小何老张
# Age                            382
# Rating                       44.92
# dtype: object
# sum() 和cumsum()函数可以同时处理数字和字符串数据  虽然字符聚合通常不被使用 但使用这两个函数并不会抛出异常
# 而对于abs()  cumprod()函数则会抛出异常  因为它们无法操作字符串数据

# print(df.sum(axis=1))
# 0     29.23
# 1     29.24
# 2     28.98
# 3     25.56
# 4     33.20
# 5     33.60
# 6     26.80
# 7     37.78
# 8     42.98
# 9     34.80
# 10    55.10
# 11    49.65
# dtype: float64

# mean()求平均值
# print(df.mean())
# Age       31.833333
# Rating     3.743333
# dtype: float64

# std()求标准差
# print(df.std())
# Age       9.232682
# Rating    0.661628
# dtype: float64

# 数据汇总描述
# describe()函数显示与DataFrame数据列相关的统计信息摘要

# print(df.describe())
#              Age     Rating
# count  12.000000  12.000000
# mean   31.833333   3.743333
# std     9.232682   0.661628
# min    23.000000   2.560000
# 25 % 25.000000   3.230000
# 50 % 29.500000   3.790000
# 75 % 35.500000   4.132500
# max    51.000000   4.800000

print(df.describe(include=["object"]))
#        Name
# count    12
# unique   12
# top      小明
# freq      1

print(df.describe(include="all"))
#        Name        Age     Rating
# count    12  12.000000  12.000000
# unique   12        NaN        NaN
# top      小明        NaN        NaN
# freq      1        NaN        NaN
# mean    NaN  31.833333   3.743333
# std     NaN   9.232682   0.661628
# min     NaN  23.000000   2.560000
# 25 % NaN  25.000000   3.230000
# 50 % NaN  29.500000   3.790000
# 75 % NaN  35.500000   4.132500
# max     NaN  51.000000   4.800000
