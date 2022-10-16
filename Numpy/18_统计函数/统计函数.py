from calendar import c
import numpy as np
# numpy提供了许多统计功能的函数，比如查找数组元素的最值、百分位数、方差、以及标准差

# 对于二维数组来说，axis=1表示沿着水平方向，axis=0表示沿着垂直方向
# amin()/amax()沿指定的轴，查找数组中元素的最小值或最大值，并以数组形式返回
a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print('数组a是：\n', a)
# [[3 7 5]
#  [8 4 3]
#  [2 4 9]]
print(np.amin(a))
# 2
print(np.amin(a, axis=1))
# [3 3 2]
print(np.amin(a, axis=0))
# [2 4 3]
print(np.amax(a))
# 9
print(np.amax(a, axis=0))
# [8 7 9]


# numpy.ptp()用于计算数组元素中最值之差值  也就是  最大值-最小值
b = np.array([[2, 10, 20], [80, 43, 31], [22, 43, 10]])
print("原数组  \n", a)
# [[3 7 5]
#  [8 4 3]
#  [2 4 9]]
print("沿着axis  1：", np.ptp(a, 1))
# 沿着axis  1： [4 5 7]
print("沿着axis  0：", np.ptp(a, 0))
# 沿着axis  0： [6 3 6]


# percentile()百分位数，是统计学中使用的一种度量单位
# 该函数表示沿指定轴，计算数组中任意百分比分位数

print("沿着axis=0计算百分位数", np.percentile(a, 10, 0))
# 沿着axis = 0计算百分位数[2.2 4.  3.4]
print("沿着axis=1计算百分位数", np.percentile(a, 10, 1))
# 沿着axis=1计算百分位数 [3.4 3.2 2.4]


# median()用于计算a数组元素的中位数（中值）
c = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
print(c)
# [[30 65 70]
#  [80 95 10]
#  [50 90 60]]

print(np.median(c))
# 65.0
print(np.median(c, axis=0))
# [50. 90. 60.]
print(np.median(c, axis=1))
# [65. 80. 60.]


# mean()该函数表示沿指定的轴  计算数组中元素的算数平均值（即元素之总和除以元素数量）
print('我们的数组是： \n', a)
# [[3 7 5]
#  [8 4 3]
#  [2 4 9]]
print('调用mean()函数: ', np.mean(a))
# 5.0
print('沿轴0调用mean()函数： ', np.mean(a, axis=0))
# [4.33333333 5. 5.66666667]
print('沿轴1调用mean()函数: ', np.mean(a, axis=1))
# [5. 5. 5.]


# 加权平均值是将数组中各数值乘以相应的权数  然后在对权重值求总和  最后以权重的总和除以总的单位数  即因子个数
# average()根据在数组中给出的权重，计算数组元素的加权平均值
# 该函数可以接受一个轴参数axis  如果未指定  则数组被展开为一维数组
d = np.array([1, 2, 3, 4])
print('d数组是：', d)

print(np.average(d))
# 2.5
we = np.array([4, 3, 2, 1])

print(np.average(d, weights=we))
# 2.0
print(np.average([1, 2, 3, 4], weights=[4, 3, 2, 1], returned=True))
# 10为所加权重和
# (2.0, 10.0)

# 在多维数组中 可以指定axis轴参数
f = np.arange(6).reshape(3, 2)
print(f)
# [[0 1]
#  [2 3]
#  [4 5]]
wt = np.array([3, 5])
print(np.average(f, axis=1, weights=wt))
# [0.625 2.625 4.625]
print(np.average(f, axis=1, weights=wt, returned=True))
# (array([0.625, 2.625, 4.625]), array([8., 8., 8.]))


# var()求数组方差
# 方差：每个样本值与均值之差的平方和 最后对差的平方和求均值
print(np.var([1, 2, 3, 4]))
# 1.25


# std()求数组的标准差
# 标准差是方差的算术平方根  用来描述一组数据平均值分散程度
# 若一组数据的标准差较大  说明大部分的数值和其平均值之间差异较大
# 若标准差较小   则代表这组数值比较接近平均值
print(np.std([1, 2, 3, 4]))
# 1.118033988749895
