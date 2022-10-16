# 在一个函数图像中  有时自变量x与因变量y是指数对应关系  这时需要将坐标轴刻度
# 设置为对数刻度  Matplotlib通过axes对象的xscale或yscale属性来实现对
# 坐标轴的格式设置


import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
x = np.arange(1, 5)
axes[0].plot(x, np.exp(x), 'gD:')
axes[0].plot(x, x**2, 'r^-.')
axes[0].set_title('Normal scale')
axes[0].set_xlabel("x axis")
axes[0].set_ylabel("y axis")
axes[0].xaxis.labelpad = 10

axes[1].plot(x, np.exp(x))
axes[1].plot(x, x**2)
# 设置y轴
axes[1].set_yscale('log')
axes[1].set_title('Logarithmic scale(y)')


# 设置x、y轴标签
axes[1].set_xlabel('x axis')
axes[1].set_ylabel('y axis')
fig.tight_layout()
plt.show()
