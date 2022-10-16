# 我们知道  窗口函数可以与聚合函数一起使用
# 聚合函数指的是对一组数据求总和  最大值  最小值  以及平均值的操作

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(9, 4), index=pd.date_range('12/14/2020', periods=9),
                  columns=['A', 'B', 'C', 'D'])
print(df)
# 窗口大小为3  min_periods最小观测值为1
print(df.rolling(window=3, min_periods=1))
# Rolling [window = 3, min_periods = 1, center = False, axis = 0, method = single]

# 1对整体聚合
r = df.rolling(window=3, min_periods=1)
print(r.aggregate(np.sum))

# 2对A列聚合
print(r['A'].aggregate(np.sum))
# 2020-12-14 - 0.311834
# 2020-12-15 - 0.087557
# 2020-12-16 - 1.188383
# 2020-12-17 - 2.288973
# 2020-12-18 - 0.750136
# Freq: D, Name: A, dtype: float64

# 3对多列数据聚合
print(r['A', 'B'].aggregate(np.sum))
#                     A         B
# 2020-12-14 - 1.107004  1.490831
# 2020-12-15 - 2.698877  1.757200
# 2020-12-16 - 2.889885  1.911870
# 2020-12-17 - 1.529668  1.193490
# 2020-12-18  0.785975  1.331653

# 4对单列应用多个函数
print(r['A'].aggregate([np.sum, np.mean]))

# 5对不同列应用多个函数
print(r['A', 'B'].aggregate([np.sum, np.mean]))

# 6对不同列应用不同函数
print(r.aggregate({'A': np.sum, 'B': np.mean}))
#                    A         B
# 2020-12-14 -0.276254  1.709550
# 2020-12-15 -2.095820  1.022048
# 2020-12-16 -3.911497  0.078798
# 2020-12-17 -2.698175 -0.363717
# 2020-12-18  0.883839 -0.090587
