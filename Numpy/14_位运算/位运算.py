from calendar import c
from pickletools import uint8
import numpy as np

# 1、bitwise_and   &   计算数组元素之间的按位与运算
# 2、bitwise_or ！ 计算数组元素之间的按位或运算
# 3、invert ~ 计算数组元素之间的按位取反运算
# 5、left_shift << 将二进制数的位数向左移
# 6、right_shift >> 将二进制数的位数向右移
# 演示的是单个元素的位运算

a = 10
b = 12
print("a的二进制数：", bin(a))
print("b的二进制数：", bin(b))
print("将a和b执行按位与操作 ", np.bitwise_and(a, b))
# 将a和b执行按位与操作  8

print()
m, n = 13, 17
print('13和17的二进制：')
print(bin(a), bin(b))
print('13和17的位或：', np.bitwise_or(13, 17))
# 13和17的位或： 29

print()
# 数据类型为无符号整型uint8
arr = np.array([20], dtype=np.uint8)
# np.binary_repr函数用来设置二进制数的位数
# 20数的二进制取八位
print("二进制表示：", np.binary_repr(20, 8))
# 二进制表示： 00010100
print(np.invert(arr))
# 11101011  ->
# 对数组中整数做按位取反运算 ，也就是0变成1   1变为0
# 若是有符号的负整数，取其二进制数的补码，并执行+1操作
# [235]
print("二进制表示：", np.binary_repr(235, 8))
# 二进制表示： 11101011

print()
# left_shift方法把数组元素的二进制数向左移动到指定位置
print(np.left_shift(20, 3))
# 160
print(np.binary_repr(20, width=8))
# 00010100
print(np.binary_repr(160, width=8))
# 10100000

print()
# 将40右移两位后返回值
# right_shift将数组中元素的二进制数向右移动到指定位置
print(np.right_shift(40, 2))
# 将40右移两位后返回值
# 10
# 移动后40的二进制数：
print(np.binary_repr(40, width=8))
# 00101000
# 移动后返回值的二进制数：
print(np.binary_repr(10, width=8))
# 00001010
