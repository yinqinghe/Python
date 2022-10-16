import numpy as np
a = np.arange(12).reshape(3, 4)

print(a)
# [[0  1  2  3]
#  [4  5  6  7]
#  [8  9 10 11]]

# axis：沿着哪条轴删除子数组
# 不提供axis参数情况
print(np.delete(a, 5))
# [0  1  2  3  4  6  7  8  9 10 11]

# 删除第二列
print(np.delete(a, 1, axis=1))
# [[0  2  3]
#  [4  6  7]
#  [8 10 11]]

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 删除经切片后的数组
print(np.delete(a, np.s_[::2]))
# [ 2  4  6  8 10]

print()
# argwhere该函数返回数组中非0元素的索引，若是多维数组则返回行 列索引组成的索引坐标
x = np.arange(6).reshape(2, 3)
print(x)
# 返回所有大于1的元素索引
y = np.argwhere(x > 1)
print(y)
# [[0 2]
#  [1 0]
#  [1 1]
#  [1 2]]

print()
aa = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print(aa)

# unique()用删除数组中重复的元素
# 1.return_index：如果TRUE 则返回新数组元素在原数组的位置（索引）
# 2.return_inverse：如果TRUE 则返回原数组元素在新数组的位置（索引）
# 3.return_counts：如果TRUE 则返回去重后的数组元素在原数组中出现的次数

# 对a数组的去重   排序
uq = np.unique(aa)
print(uq)
# [2 5 6 7 8 9]

# 数组去重后的索引数组
u, indices = np.unique(aa, return_index=True)
print(u)
# [2 5 6 7 8 9]
# 打印索引
print(indices)
# [1 0 2 4 7 9]

# 去重数组的下标
ui, indices = np.unique(aa, return_inverse=True)
print(ui)
# [2 5 6 7 8 9]
print(indices)
# [1 0 2 0 3 1 2 4 0 5]

uc, indices = np.unique(aa, return_counts=True)
print(uc)
# 返回去重元素的重复数量
# [2 5 6 7 8 9]
print(indices)
# 统计重复元素出现次数
# [3 2 2 1 1 1]
