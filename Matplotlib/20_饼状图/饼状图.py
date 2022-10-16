# pie()函数 该函数可以生成数组中数据的饼状图

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
# 使得X/Y轴的间距相等
# ax.axis('equal')

langs = ['C', 'C++', 'Java', 'Python', 'PHP']

students = [23, 17, 35, 29, 12]
# 绘制饼状图
# autopct  格式化字符串"fmt%pct"使用百分比的格式设置每个扇形区的标签
#   并将其放置在扇形区内
ax.pie(students, labels=langs, autopct='%1.2f%%')
# pie会根据students来计算各个扇形区域占饼图总和的百分比

plt.show()
