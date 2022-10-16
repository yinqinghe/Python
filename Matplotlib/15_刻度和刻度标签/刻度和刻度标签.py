# xticks()函数接受一个列表对象作为参数  列表中的元素表示对应数轴上要显示的刻度
# set_xticklabels()函数设置与刻度线相对应的刻度标签


import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
# 生成画布对象
fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
y = np.sin(x)
ax.plot(x, y)
# 设置x轴标签
ax.set_xlabel('angle')
ax.set_title('sine')
# 设置x轴刻度标签
ax.set_xticklabels(['zero', 'two', 'four', 'six'])
ax.set_xticks([0, 2, 4, 6])

# 设置y轴刻度
ax.set_yticks([-1, 0, 1])
