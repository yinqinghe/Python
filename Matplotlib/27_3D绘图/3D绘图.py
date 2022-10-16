

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
# 创建3d绘图区域
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
x = z*np.sin(20*z)
y = z*np.cos(20*z)

# 调用 ax.plot3D创建三维线图
# ax.plot3D(x, y, z, 'gray')
# ax.set_title('3D line plot')

# 绘制3D散点图
c=x+y
ax.scatter3D(x,y,z,c=c)
ax.set_title('3d Scatter plot')


plt.show()
