import numpy as np
import random
a = np.arange(10)
s = slice(2, 9, 3)

print(a[s])
print(a)
# [2 5 8]
# [0 1 2 3 4 5 6 7 8 9]

print(a[3])
print(a[2:])
print(a[2:5])
# 3
# [2 3 4 5 6 7 8 9]
# [2 3 4]
# 多维数组切片
two = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print(two[..., 1])
print(two[1, ...])
print(two[..., 1:])
print(two[1:])
print(two[1:, ...], '\n')
print(two[1:, 1:])
