# 分层索引(Multiple index)是Pandas中非常重要的索引类型  它指的是在一个轴上拥有多个(即两个以上)
# 索引层数  这使得我们可以用低纬度的结构来处理更高维的数据
# 比如  当想要处理三维以上的高维数据时  就需要用到分层索引

# 分层索引的目的是用低纬度的结构(Series 或者DataFrame)更好地处理高位数据  通过分层索引
# 我们可以象处理二维数据一样  处理三维及以上的数据  分层索引的存在使得分析高维数据变得简单
# 让抽象的高维数据变得容易理解  同时它比废弃的Panel结构更容易使用

# Panel可以通过Multindex()方法来创建分层索引对象
# 该对象本质上是一个元祖序列  序列中每一个元祖都是唯一的


import pandas as pd
import numpy as np
# 为leves传递一个1行5列的二维数组
df = pd.MultiIndex(levels=[[np.nan, 2, pd.NaT, None, 5]], codes=[
                   [4, -1, 1, 2, 3, 4]])
print(df.levels)
print(df)
# levls参数用来创建层级索引  这里只有一层  该层的索引值分别是nan, 2, NaT, None, 5
# codes表示按参数值对层级索引值排序(levels中的值相对应)  也就说codes中数值是leves序列的下标索引
# 需要注意  这里的-1代表NAN


# 从元祖创建
arrays = [['it', 'it', 'of', 'of', 'for', 'for', 'then', 'then'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
# 使用zip()函数创建元祖
tuples = list(zip(*arrays))
print(tuples)
# [('it', 'one'), ('it', 'two'), ('of', 'one'), ('of', 'two'), ('for', 'one'), ('for', 'two'), ('then', 'one'),
#  ('then', 'two')]

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
# MultiIndex([('it', 'one'),
#             ('it', 'two'),
#             ('of', 'one'),
#             ('of', 'two'),
#             ('for', 'one'),
#             ('for', 'two'),
#             ('then', 'one'),
#             ('then', 'two')],
#            names=['first', 'second'])


# 从DataFrame对象创建
df_data = pd.DataFrame([['bar', 'one'], ['bar', 'two'],
                        ['foo', 'one'], ['foo', 'two']], columns=['first', 'second'])
# 然后使用  from_frame()创建分层索引
index = pd.MultiIndex.from_frame(df_data)
# 将index应用于Series
s = pd.Series(np.random.randn(4), index=index)
print(s)

# 笛卡尔积创建   使用from_product()笛卡尔积创建分层索引
numbers = [0, 1, 2]
language = ['Python', 'Java']

index = pd.MultiIndex.from_product(
    [numbers, language], names=['number', 'language'])
# 将分层索引对象应用于series
dk_er = pd.Series(np.random.randn(6), index=index)
print(dk_er)


# 数组创建分层索引
df_arr = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
print(df_arr)
