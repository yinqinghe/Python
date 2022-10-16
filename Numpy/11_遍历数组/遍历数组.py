import numpy as np
# Numpy提供了一个nditer迭代器对象，它可以配合for循环完成对数组元素的遍历

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)
# 使用nditer迭代器，并使用for进行遍历
for x in np.nditer(a):
    print(x)

# a的转置数组
b = a.T
print(b)
for x in np.nditer(b):
    print(x, end=",")
# a和a.T的遍历顺序是一样的，也就是说，它们在内存中的存储顺序是一样的
print("\n")
for x in np.nditer(a.T.copy(order='C')):
    print(x, end=",")
# 0,5,10,15,20,25,30,35,40,45,50,55,
# 0,20,40,5,25,45,10,30,50,15,35,55,
# 数组遍历结果不一样，就是因为它们在内存中的存储方式不一样

print("\n")

# 制定遍历顺序
# for x in np.nditer(a, order='C'):
#     print(x, end=",")
# print()
# for x in np.nditer(a, order='F'):
#     print(x, end=",")

# [[0  5 10 15]
#  [20 25 30 35]
#  [40 45 50 55]]
# c=order行顺序
# 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
# F-order列顺序
# 0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,


# 修改数组元素值
# nditer对象提供了一个可选参数op_flags,它表示能否在遍历数组时对元素进行修改
# 提供了三种模式：1.read-only  只读
#               2.read-write  读写模式
#               3.write-only  只写模式
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...] = 2*x
# print("修改后的数组是：\n", a)


# 外部循环使用
# flags参数有：1.c_index      可以跟踪C顺序的索引
#             2.f_index      可以跟踪Fortran顺讯的索引
#             3.multi_index  每次迭代都会跟踪一种索引类型
#             4.external_loop 返回的遍历结构是具有多个值的一维数组
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x)


# 迭代多个数组
# 条件：如果两个数组都能够被广播，那么nditer对象就可以同时对它们迭代
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
# 广播迭代
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=" , ")
