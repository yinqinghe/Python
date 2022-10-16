import numpy as np
a = np.array([1, 2, 3])

print(a)
print(type(a))
# [1 2 3]
# //<class 'numpy.ndarray'>

arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 0, 11, 23]])
print(arr.ndim)  # 查看数组维数  2

# aa = np.array([1, 2, 3, 4, 5, 6], ndim=2)
# print(aa)

c = np.array([2, 3, 4, 5], dtype="complex")
print(c)
