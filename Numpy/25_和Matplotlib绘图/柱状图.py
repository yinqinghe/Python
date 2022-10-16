from turtle import color
from matplotlib import pyplot as plt
import numpy as np
# # 第一组数据
# x1 = [5, 8, 10]
# y1 = [12, 16, 6]
# # 第二组数据
# x2 = [6, 9, 11]
# y2 = [6, 15, 7]
# plt.bar(x1, y1, align='center')
# plt.bar(x2, y2, color='g', align='center')

# plt.title('Bar graph')
# # 设置x轴与y轴刻度
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()


# NumPy提供了histogram()函数  它以直方图的形式表示一组数据的概率分布值
# histogram()函数有两个返回值  分别是hist与bin_edges   分别代表直方图高度值与bin数值区间范围
a = np.arange(8)
hist, bin_edges = np.histogram(a, density=True)
print(hist)
# [0.17857143 0.17857143 0.17857143 0. 0.17857143 0.17857143 0.         0.17857143 0.17857143 0.17857143]
print(bin_edges)
# [0.  0.7 1.4 2.1 2.8 3.5 4.2 4.9 5.6 6.3 7.]


aa = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
hist, bins = np.histogram(aa, bins=[0, 20, 40, 60, 80, 100])
print(hist, '\n', bins)
# [3 4 5 2 1]
#  [  0  20  40  60  80 100]


plt.hist(aa, bins=[0, 20, 40, 60, 80, 100])
plt.title("histogram")
plt.show()
