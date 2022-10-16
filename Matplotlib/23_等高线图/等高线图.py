# 等高线图  也称水平图  是一种在二维平面上显示3D图像的方法
# 等高线有时也被称为  Z切片  如果想要查看因变量Z与自变量X、Y之间的函数图像变化
# 采用等高线最为直观


import matplotlib.pyplot as plt
import numpy as np
# 绘制等高线  contour     填充等高线contourf

xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
# 将上述数据变成网格数据形式
X, Y = np.meshgrid(xlist, ylist)

Z = np.sqrt(X**2+Y**2)

fig, ax = plt.subplots(1, 1)
# 填充等高线颜色
cp = ax.contourf(X, Y, Z)
fig.colorbar(cp)
ax.set_title('Filled Contours Plot')
ax.set_xlabel('x(cm)')
ax.set_ylabel('y(cm)')


# plt.contour(X, Y, Z)

plt.show()
