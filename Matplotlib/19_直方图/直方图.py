# 直方图又称质量分布图  它是一种条形图的一种  有一系列高度不等待纵向线段来表示数据
# 分布的情况   直方图的横轴表示数据类型   纵轴表示分布情况

# 直方图用于概率分布  它显示了一组数值序列在给定的数值范围内出现的概率
# 而柱状图则用于展示各个类别的频数


from matplotlib import pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])

# 通常将bin指定为连续且不重叠的数值区间  而bin值指区间开始和结束的数值
# density = True 返回概率密度直方图  默认False  返回相应区间元素的个数的直方图
ax.hist(a, bins=[0, 25, 50, 75, 100], histtype='barstacked')

ax.set_title('histogram of result')
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xlabel('marks')
ax.set_ylabel('no.of students')

plt.show()
