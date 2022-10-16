# NumPy提供了多种排序函数  这些排序函数可以实现不同的排序算法
# 排序算法特征主要体现在以下四个方面：执行速度  最坏情况下的复杂度  所需的工作空间以及算法的稳定性

import numpy as np
a = np.array([[3, 7], [9, 1]])
print('a数组是：\n', a)
# [[3 7]
#  [9 1]]
print(np.sort(a))
# [[3 7]
#  [1 9]]
# 按列排序
print(np.sort(a, axis=0))
# [[3 1]
#  [9 7]]
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25),
             ("ravi", 17), ("amar", 27)], dtype=dt)

print(a)
# [(b'raju', 21)(b'anil', 25)(b'ravi', 17)(b'amar', 27)]
# 按name字段排序
print(np.sort(a, order='name'))
# [(b'amar', 27)(b'anil', 25)(b'raju', 21)(b'ravi', 17)]


# argsor()沿着指定的轴  对输入数组的元素值进行排序  并返回排序后的元素索引数组
b = np.array([90, 29, 89, 12])
print("原数组: ", b)
sort_ind = np.argsort(b)
print("打印排序元素索引值", sort_ind)
# [3 1 2 0]
# 使用索引数组对原数组排序
sort_a = b[sort_ind]
print("打印排序数组")
for i in sort_ind:
    print(b[i], end="  ")
# 12  29  89  90
print(sort_a)

# lexsort()按键序列对数组进行排序   它返回一个已排序的索引数组   类似于numpy.argsirt()
m = np.array(['a', 'b', 'c', 'd', 'e'])
n = np.array([12, 90, 380, 12, 211])
ind = np.lexsort((m, n))
# [0 3 1 4 2]
# 打印排序元素的索引数组
print(ind)
# 使用索引数组对数组进行排序
for i in ind:
    print(m[i], n[i])
# a 12
# d 12
# b 90
# e 211
# c 380
