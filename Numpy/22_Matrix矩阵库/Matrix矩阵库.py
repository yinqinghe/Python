import numpy.matlib
import numpy as np
# Numpy提供了一个矩阵库模块 numpy.matlib  该模块中的函数返回的是一个matrix对象  而非ndarray对象
# 矩阵由m行n列(m*n)元素排列而成，矩阵中的元素可以是数字、符号或数学公式

# 矩阵中会填充无意义的随机值
print(np.matlib.empty((2, 2)))
# [[1.20160711e-306 7.56570609e-307]
#  [1.37961913e-306 9.34609790e-307]]
# metlib.empty()返回一个空矩阵  所以它的创建速度非常快

# matlib.zeros()创建一个以0填充的矩阵
print(np.matlib.zeros((2, 2)))
# [[0. 0.]
#  [0. 0.]]


# matlib.ones()创建一个以1填充的矩阵
print(np.matlib.ones((2, 2)))
# [[1. 1.]
#  [1. 1.]]


# matlib.eye()返回一个对角线元素为1  而其他元素为0的矩阵
print(np.matlib.eye(n=3, M=4, k=0, dtype=float))
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]]


# matlib.identity()返回一个给定大小的单位矩阵  矩阵的对角线元素为1  而其他元素均为0
print(np.matlib.identity(5, dtype=float))


# matlib.rand()创建一个以随机数填充  并给定维度的矩阵
print(np.matlib.rand(3, 3))
# [[0.84793905 0.47674339 0.81235432]
#  [0.12107075 0.50879149 0.06175782]
#  [0.66240132 0.39670945 0.21464615]]

# 这里需要注意  因为matrix只能表示二维数据  而ndarray也可以是二维数组  所以两者可以互相转换
i = np.matrix('1,2;3,4')
print(type(i))
print(i)
# <class 'numpy.matrix' >
# [[1 2]
#  [3 4]]

# 实现matrix与 ndarray之间的转换
j = np.array(i)
print(type(j))
print(j)
# <class 'numpy.ndarray' >
# [[1 2]
#  [3 4]]
k = np.asmatrix(j)
print(type(k))
print(k)
# <class 'numpy.matrix' >
# [[1 2]
#  [3 4]]
