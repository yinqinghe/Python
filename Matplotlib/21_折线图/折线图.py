# Matplotlib并没有直接提供绘制折线图的函数

from cProfile import label
import matplotlib.pyplot as plt
x = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
y = [20, 40, 35, 55, 42, 80, 50]

# markersize用来设置'D'菱形的大小
plt.plot(x, y, 'g', marker='D', markersize=5, label='周活')
plt.xlabel('登录时间')
plt.ylabel('用户活跃度')
plt.title('C语言中文网活跃度')

# 显示图裂
plt.legend(loc='lower right')
# 调用  text()在图像上绘制注释文本   x1,y1表示文本所处坐标位置
# ha参数控制水平对齐方式   va控制垂直对齐方式  str(y1)表示要绘制的文本

for x1, y1 in zip(x, y):
    plt.text(x1, y1, str(y1), ha='center', va='bottom', fontsize='20')

plt.savefig('1.jpg')


plt.show()
