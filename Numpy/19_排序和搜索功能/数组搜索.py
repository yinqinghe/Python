import numpy as np

b = np.array([12, 90, 380, 12, 211])
print("原数组  :", b)

# nonzero()从函数中查找非零元素的索引位置
print("打印非0元素的索引位置 :", b.nonzero())
# (array([0, 1,2, 3, 4], dtype=int64),)


print(np.where(b > 12))
# (array([1, 2, 4], dtype=int64),)
c = np.array([[20, 24], [21, 23]])

print(np.where(c > 20))
# 第一个数组是行坐标  第二个数组是列坐标
# (array([0, 1, 1], dtype=int64), array([1, 0, 1], dtype=int64))


x = np.arange(9.).reshape(3, 3)
print(x)
# 设置条件选择偶数元素
condition = np.mod(x, 2) == 0

print(condition)
# [[True False  True]
#  [False  True False]
#  [True False  True]]
# 按condition提取满足条件的元素值
print(np.extract(condition, x))
# [0. 2. 4. 6. 8.]


tt = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
print(tt)

# argmax()该函数返回最大值的索引，与其相反的函数是argmin()求最小值索引
print(np.argmax(tt))
# 7
# 将数组以一维数组展开
print(tt.flatten())
# [30 40 70 80 20 10 50 90 60]
maxindex = np.argmax(tt, axis=0)
print(maxindex)
# [1 2 0]
maxindex = np.argmax(tt, axis=1)
print(maxindex)
# [2 0 1]


pp = np.array([[3, 4, 7], [8, 2, 1], [5, 9, 6]])
print('数组pp  :\n', pp)

minindex = np.argmin(pp)
print(minindex)
# 5
print(pp.flatten()[minindex])  # 展示数组最小的值
# 1
minindex = np.argmin(pp, axis=0)

print(minindex)
# [0 1 1]
minindex = np.argmin(pp, axis=1)
print(minindex)
# [0 2 0]
