import numpy as np
a = np.arange(9).reshape(3, 3)
for row in a:
    print(row)
# 返回一个数组迭代器
for ele in a.flat:
    print(ele, end=" , ")

print()
# flatten返回一份数组副本，对副本修改不会影响原始数组
aa = np.arange(8).reshape(2, 4)
print(aa)
# 默认按行C风格展开的数组
print(aa.flatten())
# 以F风格顺序展开的数组
print(aa.flatten(order='f'))
# [[0 1 2 3]
#  [4 5 6 7]]
# [0 1 2 3 4 5 6 7]
# [0 4 1 5 2 6 3 7]

# ravel返回数组的视图，如果修改，则会影响原始数组
# 将多维数组的元素以一维数组的形式展开
print('调用ravel函数后')
print(aa.ravel())

print('F风格顺序调用ravel函数之后')
print(aa.ravel(order='F'))

# 数组转置操作
# 二维数组使用此方法可以实现矩阵转置   与ndarray.T使用方法相似
b = np.arange(12).reshape(3, 4)
print(b)
print(np.transpose(a))
# [[0  1  2  3]
#  [4  5  6  7]
#  [8  9 10 11]]
# [[0 3 6]
#  [1 4 7]
#  [2 5 8]]

# bb = np.arange(27).reshape(3, 3, 3)
# print(bb)
# # 该方法用于交换数组的两个轴         ？？？？？不懂
# print(np.swapaxes(bb, 2, 0))
# 三维数组的第一个二维数组的每一列分到每一个二维数组的第一列  (二维数组的第一列分到第一个二维数组的第一列，第二列分到第二个二维数组的第一列。。。)
# 第二个二维数组的每一列分到每一个二维数组的第二列  。。。


# 修改数组维度操作
# broadcast：返回值是数组被广播后的对象
# 该函数以两个数组作为输入参数
m = np.array([[1], [2], [3]])
n = np.array([4, 5, 6])


p = np.broadcast(n, m)
# p它拥有iterator属性
print(p)
w, v = p.iters
print(next(w), next(v))
print(next(w), next(v))
print(next(w), next(v))
print(next(w), next(v))

e = np.broadcast(m, n)  # broadcast只提供了一个shape参数
print(e.shape)
f = np.empty(e.shape)
f.flat = [x+y for (x, y) in e]
print(f)
print(m+n)

to = np.arange(4).reshape(1, 4)
print("原数组", to)
print('调用broadcast_to函数之后')
# 该函数将数组广播到新形状中，它在原始数组的基础上返回一个只读视图
# 如果新性状不符合Numpy的广播规则，则会抛出ValueError异常
print(np.broadcast_to(to, (4, 4)))
# 原数组[[0 1 2 3]]
# 调用broadcast_to函数之后
# [[0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]
#  [0 1 2 3]]

# 在指定位置插入新的轴，从而扩展数组的维度
x_dims = np.array(([1, 2], [3, 4]))
print('数组x_dims : \n', x_dims)
y_dims = np.expand_dims(x_dims, axis=0)
print('数组y_dim : \n', y_dims)

print('数组x和y的形状：\n', x_dims.shape, y_dims.shape)

# squeeze删除数组中纬度为1的项，列如，一个数组的shape是（5,1）经此函数后，shape变为（5）
squeeze = np.array([[[0], [1], [2]], [[0], [1], [2]]])
print(squeeze.shape)
print(np.squeeze(squeeze).shape)
# axis用于指定需要删除的维度所在轴，指定的维度值必须为1，否则将会报错
# 若为None，则删除数组维度中所有为1的项
print(np.squeeze(squeeze, axis=(2,)).shape)


a_squeeze = np.arange(9).reshape(1, 3, 3)
print(a_squeeze)
b_squeeze = np.squeeze(a_squeeze)
print(b_squeeze)
print('数组a_squeeze 和b_squeeze 的形状：', a_squeeze.shape, b_squeeze.shape)
