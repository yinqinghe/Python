# 在一个给定的画布(figure)中可以包含多个axes对象  但是同一个axes对象只能在一个画布中使用
# 2D绘图区域(axes) 包含两个轴(axis)对象   如果是3D绘图区域  则包含三个
# 通过调用add_axes()方法能够将axes对象添加到画布中  该方法用来生成一个axes轴域对象
# 对象的位置由参数rect决定

# rect是位置参数  接受一个由4个元素组成的浮点数列表  [left,bottom,width,height]
# 它表示添加到画布中的矩形区域的左下角坐标(x,y),以及宽度和高度
# 列如  ax=fig.add_axes([0.1,0.1.0.8,0.8])
# 每个元素的值是百分制   它代表着从画布10%的位置开始绘制  宽高是画布的80%


import matplotlib.pyplot as plt
y = [1, 4, 9, 16, 25, 36, 49, 64]
x1 = [1, 16, 30, 42, 55, 68, 77, 88]
x2 = [1, 6, 12, 18, 28, 40, 52, 65]
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
# 使用简写的形式color/标签符/线型
l1 = ax.plot(x1, y, 'ys-')
l2 = ax.plot(x2, y, 'go--')
ax.legend(labels=('tv', 'Sarmtphone'), loc='lower right')

ax.set_title('Advertisement effect at lower rihgt')
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()
