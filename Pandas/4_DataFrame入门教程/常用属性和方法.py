import pandas as pd
import numpy as np
d = {'Name': pd.Series(['c语言中文网', '编程帮', '百度', '360搜索', '谷歌', '微学苑', 'Bing搜索']),
     'year': pd.Series([5, 6, 15, 28, 3, 19, 23]), 'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.20, 4.6, 3.8])}
df = pd.DataFrame(d)
print(df)
# 返回DataFrame的转置  也就是把行和列进行交换
# print(df.T)
#                  0    1     2      3     4     5       6    7    8
# Name    c语言中文网  编程帮    百度  360搜索    谷歌   微学苑  Bing搜索  NaN  NaN
# year       5.0  6.0  15.0   28.0   3.0  19.0    23.0  NaN  NaN
# Rating    4.23  3.0  24.0    3.0  98.0  2.56     3.2  4.6  3.8

# 返回一个行标签、列标签组成的列表
print(df.axes)
# [3 rows x 9 columns]
# [RangeIndex(start=0, stop=9, step=1), Index(
#     ['Name', 'year', 'Rating'], dtype='object')]

# 返回每一列的数据类型
print(df.dtypes)
# Name       object
# year      float64
# Rating    float64
# dtype: object


# 判断输入数据是否为空
print(df.empty)
# False

# DataFrame的维度
print(df.ndim)
# 2

# DataFrame的形状
print(df.shape)
# (9, 3)

# DataFrame的中元素个数
print(df.size)
# 27

# DataFrame的数据
print(df.values)
# [['c语言中文网' 5.0 4.23]
#  ['编程帮' 6.0 3.0]
#  ['百度' 15.0 24.0]
#  ['360搜索' 28.0 3.0]
#  ['谷歌' 3.0 98.0]
#  ['微学苑' 19.0 2.56]
#  ['Bing搜索' 23.0 3.2]
#  [nan nan 4.6]
#  [nan nan 3.8]]

# 获取前3行数据
print(df.head(3))
#          Name  year  Rating
# 0  c语言中文网   5.0    4.23
# 1     编程帮   6.0    3.00
# 2      百度  15.0   24.00

# 获取后2行数据
print(df.tail(2))
#         Name  year  Rating
# 5     微学苑    19     4.6
# 6  Bing搜索    23     3.8

info = pd.DataFrame({'a_data': [40, 28, 39, 32, 18], 'b_data': [
                    20, 37, 41, 35, 45], 'c_data': [22, 17, 11, 25, 15]})
# 移动幅度为3   不对原DataFrame修改   修改产生副本
inf = info.shift(periods=3)
print(info)
print(inf)
#      a_data  b_data  c_data
# 0     NaN     NaN     NaN
# 1     NaN     NaN     NaN
# 2     NaN     NaN     NaN
# 3    40.0    20.0    22.0
# 4    28.0    37.0    17.0

print(info.shift(periods=3))
# 将缺失值和原数值替换为52
print(info.shift(periods=3, axis=1, fill_value=52))
#    a_data  b_data  c_data
# 0      52      52      52
# 1      52      52      52
# 2      52      52      52
# 3      52      52      52
# 4      52      52      52
# fill_value参数不仅可以填充缺失值  还也可以对原数据进行替换
