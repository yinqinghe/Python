import numpy as np
a = np.array([[2, 4, 6], [3, 5, 7]])

# 输出数组的维度
print(a.shape)

a.shape = (3, 2)
print(a)
print(a.shape)


b = a.reshape(2, 3)
print(a)
print(b)
print(a.shape)
print(b.shape)
