# 振动图也叫磁场图  或量场图  其图像的表现形式是一组适量箭头
# 其数学含义是在点(x,y)处具有分向量(u,v)

import matplotlib.pyplot as plt
import numpy as np
x, y = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.25))

z = x*np.exp(-x**2-y**2)
# 计算数组中元素的梯度
v, u = np.gradient(z, 0.2, 0.2)
fig, ax = plt.subplots()

q = ax.quiver(x, y, u, v)
plt.show()
