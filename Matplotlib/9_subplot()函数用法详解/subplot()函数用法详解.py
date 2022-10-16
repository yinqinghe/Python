# 在使用Matplotlib绘图时  我们大多数情况下  需要将一张画布划分为若干个子区域
# 之后  我们就可以在这些区域上绘制不用的图形  学习如何在同一画布上绘制多个子图

# subplot(233)表示在当前画布的右上角创建一个两行三列的绘图区域  同时  选择在第3个位置绘制子图
import matplotlib.pyplot as plt
import numpy as np
import math
plt.plot([1, 2, 3])
# 现在创建一个子图  它表示一个有2行1列的网格的顶部图
# 因为这个子图将与第一个重叠  所以之前创建的图将被删除

# plt.subplot(211)
# plt.plot(range(12))

# plt.subplot(212, facecolor='y')
# # 创建带有黄色背景的第二个子图
# plt.plot(range(12))


# # 如果不想覆盖之前的图  需要使用add_subplot()函数
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot([1, 2, 3])
# ax2 = fig.add_subplot(221, facecolor='y')
# ax2.plot([1, 2, 3])


# 通过给画布添加axes对象可以实现在同一画布中插入另外的图像
x = np.arange(0, math.pi*2, 0.05)
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 1, 0.8])
axes2 = fig.add_axes([0.65, 0.55, 0.4, 0.2])
y = np.sin(x)
axes1.plot(x, y, 'b')
axes2.plot(x, np.cos(x), 'r')
axes1.set_title('sine')
axes2.set_title('cosine')
plt.show()
