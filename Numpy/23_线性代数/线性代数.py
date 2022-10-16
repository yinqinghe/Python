# Numpy提供了numpy.linalg模块   该模块中包含了一些常用的线性代数计算方法

from re import X
from tkinter import Y
import numpy as np
A = [1, 2, 3]
B = [4, 5, 6]
# 按照矩阵的乘法规则  计算两个矩阵的点积运算结果
# 当输入一维数组时返回一个结果值   若输入的多维数组则同样返回一个多维数组结果
# 输入一维数组
print(np.dot(A, B))
# 32

# 输入二维数组时
a = np.array([[100, 200], [23, 12]])
b = np.array([[10, 20], [12, 21]])
dot = np.dot(a, b)
print(dot)
# [[3400 6200]
#  [ 374  712]]
# 点积运算就是将a数组的每一行元素与b数组的每一列元素相乘再相加


# vdot()该函数用于计算两个向量的点积结果  与dot()函数不同
aa = np.array([[100, 200], [23, 12]])
bb = np.array([[10, 20], [12, 21]])
vdot = np.vdot(a, b)
print(vdot)
# 5528


# inner()方法用于计算数组之间的内积  当计算的数组是一维数组  它与dot()函数相同
# 若输入的是多维数组则两者存在不同
AA = [[1, 10], [100, 1000]]
BB = [[1, 2], [3, 4]]

print(np.inner(AA, BB))
# inner()函数的计算过程是A数组的每一行与B数组的每一行相乘再相加
# [[21   43]
#  [2100 4300]]
print(np.dot(AA, BB))
# dot()则表示是A数组每一行与B数组的每一列相乘
# [[31   42]
#  [3100 4200]]


# matmul()该函数返回两个矩阵的乘积   假如两个矩阵的维度不一致
a_matmul = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b_matmul = np.array([[23, 23, 12], [2, 1, 2]])
mul = np.matmul(a, b)
print(mul)
# [[3400 6200]
#  [ 374  712]]


# linalg.det()该函数使用对角线元素来计算矩阵的行列式
a_det = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a_det))
# -2.0000000000000004


# linalg.solve()该函数用于求解线性矩阵方程组  并以矩阵的形式表示线性方程的解
# 3X+2Y+Z=10
# X+Y+Z=6
# X+2Y-Z=2

# 方程系数矩阵
# 3    2    1
# 1    1    1
# 1    2   -1
# 方程变量矩阵
# X
# Y
# Z
# 方程结果矩阵
# 10
# 6
# 2
# 如果m、x、n分别代表上述三个矩阵  其表示结果如下
# m*x=n   或  x=n/m

mm = np.array([[3, 2, 1], [1, 1, 1], [1, 2, -1]])
print('数组 mm:\n', mm)
# [[3  2  1]
#  [1  1  1]
#  [1  2 - 1]]
nn = np.array([[10], [6], [2]])
print('矩阵 n: \n', nn)
# [[10]
#  [6]
#  [2]]
# 将系数矩阵与结果矩阵传递给numpy.solve()函数   即可求出线程方程的解
x = np.linalg.solve(mm, nn)
print('计算： m^(-1)n:\n ', x)
# [[1.]
#  [2.]
#  [3.]]


# linalg.inv()该函数用于计算矩阵的逆矩阵  逆矩阵与原矩阵相乘得到单位矩阵
a_inv = np.array([[1, 2], [3, 4]])
# [[1 2]
#  [3 4]]
print("原数组 :\n", a_inv)
b_inv = np.linalg.inv(a_inv)
print("求逆  :\n", b_inv)
#  [[-2.   1. ]
#  [ 1.5 -0.5]]
