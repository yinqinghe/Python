# 在一些应用场景中  有时需要绘制两个x轴或两个y轴  这样可以更直观地显现图像
# 从而获取更有效的数据  Matplotlib提供的twinx()和twiny()函数
# 除了可以实现绘制双轴的功能外  还可以使用不同的单位来绘制曲线
# 比如一个轴绘制对函数  另外一个轴绘制指数函数

from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

a1 = fig.add_axes([0, 0, 1, 1])

x = np.arange(1, 11)

a1.plot(x, np.exp(x))
a1.set_ylabel('exp')

a2 = a1.twinx()

a2.plot(x, np.log(x), 'ro-')

a2.set_ylabel('log')

fig.legend(labels=('exp', 'log'), loc='upper left')

plt.show()
