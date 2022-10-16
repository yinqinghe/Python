# Matplotlib可以根据自变量与因变量的取值范围  自动设定x轴与y 轴的数值大小
# 也可以用自定义的方式  通过set_xlim()和set_ylim()对x、y轴的数值范围进行设置

import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
# 添加绘图区域
a1 = fig.add_axes([0, 0, 1, 1])
# 准备数据
x = np.arange(1, 10)

a1.plot(x, np.exp(x))

a1.set_title('exp')


# 自定义设置
# 设置x轴
# a1.set_xlim(0, 10)
# # 设置y轴
# a1.set_ylim(0, 10000)

plt.show()
