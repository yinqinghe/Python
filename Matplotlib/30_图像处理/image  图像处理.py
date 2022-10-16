import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread(r'../pillow/ss.jpg')


# 将imsave()方法 的origin参数设置为lower实现了原始图像的垂直翻转
# plt.imsave('logo.jpg', img, cmap='gray', origin='lower')


# plt.imshow(img)
fig = plt.figure()


points = np.arange(-5, 5, 0.01)
# meshgrid接受两个一维数组  然后产生两个二维矩阵
xs, ys = np.meshgrid(points, points)

z = np.sqrt(xs**2+ys**2)
# 绘制图像
ax = fig.add_subplot(221)
ax.imshow(z)
ax = fig.add_subplot(222)
ax.imshow(z, cmap='gray')
ax = fig.add_subplot(223)
ax.imshow(z, cmap='cool')
ax = fig.add_subplot(224)
ax.imshow(z, cmap='hot')
# 显示图像
plt.show()
