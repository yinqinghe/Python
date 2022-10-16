# from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x**2+y**2))


x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')

# ax.contour(X, Y, Z, 50, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# ax.set_title('3D contour')

# 绘制线框图   线框图可以将数据投影到指定的三维表面上  并输出可视化程度较高的三维效果图
# ax.plot_wireframe(X, Y, Z, color='black')
# ax.set_title('wireframe')


# 绘制曲面图   曲面图是一个三维图形  它非常类似于线框图
# 不同之处  线框图的每个面都由多边形填充而成
# 求向量积(outre()方法又称外积)
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
# 矩阵转置
y = x.copy().T
z = np.cos(x**2+y**2)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')

plt.show()
