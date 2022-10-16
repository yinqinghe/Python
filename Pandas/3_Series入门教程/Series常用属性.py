import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(5))
print(s)
# 0 - 0.270465
# 1 - 0.723973
# 2    0.368155
# 3 - 0.631662
# 4    0.064093
# dtype: float64

# axes以列表的形式返回所有行索引标签
print("The axes are: ", s.axes)
# The axes are:  [RangeIndex(start=0, stop=5, step=1)]

print("The dtype is: ", s.dtype)
# The dtype is:  float64
print("是否为空对象: ", s.empty)
# 是否为空对象:  False
# 返回输入数据的维数
print("The ndim are: ", s.ndim)
# The ndim are:  1
print("The values are: ", s.values)
# The values are:  [-0.17810276  0.89293748  1.43497686  0.23042512 - 2.24934245]
# 返回输入数据的元素数量
print("The size are: ", s.size)
# The size are:  5
print("The index are: ", s.index)
# The index are:  RangeIndex(start=0, stop=5, step=1)
s1 = pd.Series([1, 2, 5, 8], index=['a', 'b', 'c', 'd'])
# 隐式索引
print(s.index)
# RangeIndex(start=0, stop=4, step=1)

# 显示索引
print(s1.index)
# Index(['a', 'b', 'c', 'd'], dtype='object')

# 返回前三行数据
print(s.head(3))
# 返回后两行数据
print(s.tail(2))
# 3 - 0.977336
# 4    0.051889
# dtype: float64


# isnull()和 notnull()用于检测series中的缺失值  所谓缺失值  顾名思义就是值不存在  丢失  缺少

s_null = pd.Series([1, 2, 5, None])
print(pd.isnull(s_null))  # 是空值返回True
# 0    False
# 1    False
# 2    False
# 3     True
# dtype: bool
print(pd.notnull(s_null))  # 空值返回False
# 0     True
# 1     True
# 2     True
# 3    False
# dtype: bool
