import numpy as np
arr = np.array([0, 30, 60, 90, 120, 150, 180])

# 计算arr数组中给定角度的三角函数值
# 通过乘以np.pi/180将其转换为弧度
print(np.sin(arr*np.pi/180))
print(np.cos(arr*np.pi/180))
print(np.tan(arr*np.pi/180))
print(np.pi)


# arr1 = np.array([0, 30, 60, 90])
# # 正弦值数组
# sinval = np.sin(arr*np.pi/180)
# print(sinval)
# # 计算角度反正弦，返回值以弧度为单位
# cosec = np.arcsin(arr*np.pi/180)
# print(cosec)
# # 通过degrees函数转化为角度进行验证
# print(np.degrees(cosec))

# # 余弦值数组
# cosval = np.cos(arr*np.pi/180)
# print(cosval)
# # 计算反余弦值，以弧度为单位
# sec = np.arccos(cosval)
# print(sec)
# # 通过degrees函数转化为角度进行验证
# print(np.degrees(sec))

# # 下面是tan（）正切函数
# tanval = np.tan(arr*np.pi/180)
# print(tanval)
# cot = np.arctan(tanval)
# print(cot)
# print(np.degrees(cot))


# numpy提供了三个舍入函数
a = np.array([12.202, 90.23120, 123.020, 23.202])
print(a)
# decimals：要舍入到的小数位数。它的默认值为0，如果为负数，则小数点将移到整数左侧
print("数组值四舍五入到小数点后两位：", np.around(a, 2))
print("数组值四舍五入到小数点后-1位：", np.around(a, -1))

# floor()该函数表示对数组中个每个元素向下取整数，即返回不大于数组中每个元素值的最大整数
b = np.array([-1.8, 1.1, -0.4, 0.9, 18])
# 对数组a 向下取整
print(np.floor(b))
# [-2.  1. - 1.  0. 18.]

# 对数组a 向上取整
print(np.ceil(b))
# [-1.  2. -0.  1. 18.]
