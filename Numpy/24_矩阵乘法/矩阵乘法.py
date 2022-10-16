# 矩阵乘法运算被称为向量化操作   向量化的主要目的是减少使用的for循环次数或者根本不适用
# 这样做的目的是为了加速程序的计算


# NumPy提供的三种矩阵乘法
from unittest import result
import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ndmin=3)
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]], ndmin=3)
# 逐元素矩阵乘法
result = np.multiply(array1, array2)
print(result)
# [[[9 16 21]
#   [24 25 24]
#   [21 16  9]]]


# 矩阵乘积运算
result1 = np.matmul(array1, array2)
print(result1)
# [[[30  24  18]
#   [84  69  54]
#   [138 114  90]]]


# 矩阵点积运算
result3 = np.dot(array1, array2)
print(result3)
# [[[[30  24  18]]
#   [[84  69  54]]
#   [[138 114  90]]]]
