

from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

langs = ['C', 'C++', 'Java', 'Python', 'PHP']

students = [23, 17, 35, 29, 12]

# ax.bar(langs,students)


data = [[30, 25, 50, 20],
        [40, 23, 51, 17],
        [35, 22, 45, 19]]
X = np.arange(4)
# 通过调整柱状图的宽度  可以实现在同一x轴位置绘制多个柱状图
# ax.bar(X+0.00, data[0], color='b', width=0.25)
# ax.bar(X+0.25, data[1], color='g', width=0.25)
# ax.bar(X+0.50, data[2], color='r', width=0.35)


# 堆叠柱状图  所谓堆叠柱状图就是将不同数组别的柱状图堆叠在一起
# 堆叠后的柱状图高度显示了两者相加的结果值
countries = ['USA', 'India', 'China', 'Russia', 'Germany']
bronzes = np.array([38, 17, 26, 19, 15])
silvers = np.array([37, 23, 18, 18, 10])
golds = np.array([46, 27, 26, 19, 17])

ind = [x for x, _ in enumerate(countries)]
print(ind)
# bottom该参数  可以指定柱状图开始堆叠的起始值  一般从底部柱状图的最大值开始
plt.bar(ind, golds, width=0.5, label='golds',
        color='gold', bottom=silvers+bronzes)
plt.bar(ind, silvers, width=0.5, label='silvers',
        color='silver', bottom=bronzes)
plt.bar(ind, bronzes, width=0.5, label='bronzes', color='#CD853F')

# 设置坐标轴
plt.xticks(ind, countries)
plt.ylabel('Medals')
plt.xlabel('Countries')
plt.legend(loc='upper right')
plt.title('2019 Olympics Top Scorers')

plt.show()
