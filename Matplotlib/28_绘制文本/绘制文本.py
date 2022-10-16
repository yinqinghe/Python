

from symbol import factor
from tkinter.ttk import Style
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.set_title('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

# 3,8表示x,y的坐标点;style设置字体样式为斜体   bbox用来设置盒子的属性  比如背景色
ax.text(3, 8, r'编程爱好者都喜欢的网站:', Style='italic',
        bbox={'facecolor': 'yellow'}, fontsize=15)

# 绘制数学表达式  用$符包裹
ax.text(2, 6, r'an equation:  $E=mc^2$', fontsize=15)

# 添加文字设置样式
ax.text(4, 0.05, r'网站：www', verticalalignment='bottom',
        color='green', fontsize=15)

ax.plot([2], [1], 'o')

# xy为点的坐标  xytext为注释内容坐标  始坐标
# arrowprops设置箭头的属性
ax.annotate('C语言中文网', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='blue', shrink=0.0))
# 设置坐标轴x,y
ax.axis([0, 10, 0, 10])


plt.show()
