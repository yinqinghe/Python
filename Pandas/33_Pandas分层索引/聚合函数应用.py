import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(1, 13).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=[['Jack', 'Jack', 'Helen'], ['Python', 'Java', 'Python']])
df.index.names = ['key1', 'key2']
df.columns.names = ['name', 'course']
# 通过给level传递参数值  可以指定在那个层上进行聚合操作  比如求和  求均值
print(df.sum(level='key2'))
print(df.mean(level='course', axis=1))

info = pd.Series([11, 14, 17, 24, 19, 32, 34, 27], index=[['x', 'x', 'x', 'x', 'y', 'y', 'y', 'y', ],
                                                          ['obj1', 'obj2', 'obj3', 'obj4', 'obj1', 'obj2', 'obj3', 'obj4']])
print(info)
# 创建了两个层级的索引  你可以使用'index'命令查看索引
print(info.index)
print(info[:, 'obj2'])
# x    14
# y    32
# dtype: int64

# 局部索引  可以理解为  从分层索引中选择特定索引层的一种方法
print(info['y'])
# obj1    19
# obj2    32
# obj3    34
# obj4    27
# dtype: int64
# 可以基于内层索引选择数据

# 行索引层转换为列索引
# unstack()用来将行索引转变成列索引  相当于转置操作
# 通过unstack()可以将Series(一维序列)转变为DataFrame(二维序列)
# 行索引标签默认是最外层的x,y   0代表第一层索引  而1代表第二层
print(info.unstack(0))
# unstack(0)表示选择第一层索引作为列
#        x   y
# obj1  11  19
# obj2  14  32
# obj3  17  34
# obj4  24  27
print(info.unstack(1))
# unstack(1)表示选择第二层索引作为列

#    obj1  obj2  obj3  obj4
# x    11    14    17    24
# y    19    32    34    27


# 列索引实现分层
infos = pd.DataFrame(np.arange(12).reshape(4, 3),
                     index=[['a', 'a', 'b', 'b'], [
                         'one', 'two', 'three', 'four']],
                     columns=[['num1', 'num2', 'num3'], ['x', 'x', 'y']])

print(infos)
print(infos.columns)
# MultiIndex([('num1', 'x'),
#             ('num2', 'x'),
#             ('num3', 'y')],
#            )
print(infos.index)

# 交换层和层排序
# 交换层  swaplevel()方法轻松地实现索引层交换
frame = pd.DataFrame(np.arange(12).reshape(4, 3),
                     index=[['a', 'a', 'b', 'b'], ['1', '2', '1', '2']],
                     columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
# 设置index的levels名称   key1与key2分别对应不同的层
frame.index.names = ['key1', 'key2']
#  设置columns的levels名称
frame.columns.names = ['state', 'color']
print(frame.swaplevel('key1', 'key2'))


# 层排序
# sort_index()的level参数实现对层的排序     按key1的字母顺序重新排序
print(frame.sort_index(level='key1'))
