
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
#           0         1         2
# a  1.096919  1.379960  2.464926
# b       NaN       NaN       NaN
# c  1.342381  0.937952 -0.121757
# d       NaN       NaN       NaN
# e  0.810705 -0.290036 -0.434172
# f -1.905765  0.330294  1.209485
# g       NaN       NaN       NaN
# h -2.586861  0.119788  0.616345
# 通过使用reindex(重构索引)  我们创建了一个存在缺少值的DataFrame对象


# 检查缺失值
# print(df[1].isnull())
# a    False
# b     True
# c    False
# d     True
# e    False
# f    False
# g     True
# h    False
# Name: 1, dtype: bool
# print(df[1].notnull())

# 缺失数据计算
# 计算缺失数据时  需要注意两点  首先数据求和时  将NA值视为0  其次 如果要计算的数据为NA  那么结果就是NA
print(df[1].sum())


# 清理并填充缺失值
# fillna()函数可以实现用非空数据"填充"NAN值
# 用标量值替换NAN值
# print(df.fillna('a'))

# 向前和向后填充NA
# print(df.fillna(method='bfill'))

# 使用replace替换通用值
df1 = pd.DataFrame({'one': [10, 20, 30, 40, 50, 6661],
                   'two': [99, 0, 30, 40, 50, 60]})
print(df1.replace({99: 10, 666: 60, 0: 20}))

# 删除缺失值
# dropna()函数与参数axis可以实现  在默认情况下  按照axis=0来按行处理
# 这意味着如果某一行中存在NaN值将会删除整行数据
print(df.dropna(axis=1))
# axis=1表示按列处理  处理结果是一个空的DataFrame对象
