import numpy as np
# 整数数组索引
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)
# [1 4 5]

b = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])
r = np.array([[0, 0], [3, 3]])
c = np.array([[0, 2], [0, 2]])
# 获取四个角的元素
c = b[r]
print(c)
# [[ 0  2]
#  [ 9 11]]
x_shi = np.array([[1, 2], [1, 2]])
y_shi = np.array([[1, 2], [1, 2]])
print(b[x_shi, y_shi])

# e = b[1:4, 1:3]
# print(e)
# f = b[1:4, [1, 2]]
# print(f)
# h = b[..., 1:]
# print(h)


# 布尔数组索引
a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# 比较运算
print(a[a > 6])
# [ 7  8  9 10 11]
aa = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

aaa = np.array([[1, 2+6j, 5, 3.5+5j]])
print(aaa[np.iscomplex(aaa)])
# 是筛选出复数

xx = np.arange(32).reshape((8, 4))
print(xx)
# print(xx[[4, 2, 1, 7]])
# print(xx[[-4, -2, -1, -7]])
print(xx[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
# [[4  7  5  6]
#  [20 23 21 22]
#  [28 31 29 30]
#  [8 11  9 10]]
# 第一行的匹配规则：[(1,0)(1,3)(1,1)(1,2)]
# 第二行的匹配规则：[(5,0)(5,3)(5,1)(5,2)]
