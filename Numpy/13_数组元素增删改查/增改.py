# Numpy数组元素的增删改查操作,主要有
# 1.resize()
# 2.append()
# 3.insert()
# 4.delete()
# 5.argwhere()
# 6.unique()

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
# [[1 2 3]
#  [4 5 6]]
# 这里resize没有修改a数组
b = np.resize(a, (3, 2))
print(b)
print(b.shape)
# [[1 2]
#  [3 4]
#  [5 6]]
b = np.resize(a, (3, 3))
print(b)
# [[1 2 3]
#  [4 5 6]
#  [1 2 3]]
# resize仅对原数组进行修改，没有返回值
# 而reshape不仅对原数组进行修改，同时返回修改后的结果

# x = np.arange(12)
# x_resize = x.resize(2, 3, 2)
# print(x)
# print(x_resize)
# [[[0  1]
#   [2  3]
#   [4  5]]

#  [[6  7]
#   [8  9]
#   [10 11]]]
# None
# x_shape = x.reshape(2, 3, 2)
# print(x_shape)
# print(x)
# [[[ 0  1]
#   [ 2  3]
#   [ 4  5]]
#  [[ 6  7]
#   [ 8  9]
#   [10 11]]]

# [[[ 0  1]
#   [ 2  3]
#   [ 4  5]]
#  [[ 6  7]
#   [ 8  9]
#   [10 11]]]
print()
# 向数组a添加元素
# 向arr数组中添加的值，需要和arr数组的形状保持一致
# 默认为None，返回的是一维数组
# 当axis=0时，追加的植被添加到行，而列数保持不变，若axis=1则与其恰好相反
print(np.append(a, [7, 8, 9]))
# [1 2 3 4 5 6 7 8 9]

# 沿轴0添加元素
print(np.append(a, [[7, 8, 9]], axis=0))
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 沿轴1添加元素
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))
# [[1 2 3 5 5 5]
#  [4 5 6 7 8 9]]

print()
aa = np.array([[1, 2], [3, 4], [5, 6]])
# 不提供axis的情况，会将数组展开
print(np.insert(a, 3, [11, 12]))
# [1  2  3 11 12  4  5  6]

# 沿轴0垂直方向
print(np.insert(a, 1, 11, axis=0))
# [[1  2  3]
#  [11 11 11]
#  [4  5  6]]

# 沿轴1水平方向
print(np.insert(a, 1, 11, axis=1))
# [[ 1 11  2  3]
#  [ 4 11  5  6]]
