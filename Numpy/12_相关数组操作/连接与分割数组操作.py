from array import array
import numpy as np

a = np.array([[10, 20], [30, 40]])
print(a)

b = np.array([[50, 60], [70, 80]])
print(b)
# 沿轴0连接两个数组   axis=0沿着垂直方向
print(np.concatenate((a, b)))
# 沿轴1连接两个数组   axis=1沿着水平方向
print(np.concatenate((a, b), axis=1))
# 数组连接操作至少需要两个维度相同的数组，才允许对它们进行垂直或者水平方向上的操作
# 二维数组相连接生成二维数组

# 垂直堆叠
c = np.stack((a, b))
print(c)
# 二维数组垂直堆叠生成三维数组


aa = np.arange(6)
print(aa)
# 将数组分为二个形状大小相等的子数组
bb = np.split(aa, 2)
print(bb)
# [array([0, 1, 2]), array([3, 4, 5])]
# 将数组在一维数组中标明要位置分割
bb = np.split(aa, [3, 4])
print(bb)
# [array([0, 1, 2]), array([3]), array([4, 5])]


arr1 = np.floor(10*np.random.random((2, 6)))

print(arr1)
# 把每一列分割成新的一维数组的一行，然后装入一个二维数组
print(np.hsplit(arr1, 3))
print(np.random.random((2, 6)))
