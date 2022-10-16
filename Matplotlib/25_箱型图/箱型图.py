# 箱型图它能显示出一组数据的最大值、最小值、中位数、及上下四分位数

import matplotlib.pyplot as plt
import numpy as np
# 利用随机数种子使每次生成的随机数相同
np.random.seed(10)

# 可以使用np.random.normal函数来创建一组基于正态分布的随机数据、该函数有三个参数
# 分别是正态分布的平均值、标准差以及期望值的数量
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
# 创建箱型图
bp = ax.boxplot(data_to_plot)

plt.show()
