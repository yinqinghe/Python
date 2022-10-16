# Matplotlib默认不支持中文字体  这因为Matplotlib只支持ASCLL字符


# 重写配置文件
from turtle import color
import matplotlib.pyplot as plt
# 设置字体
# plt.rcParams['font.sans-serif'] = ['SimHei']
# # 该语句解决图像中的"-"负号的乱码问题
# plt.rcParams['axes.unicode_minus'] = False

year = [2017, 2018, 2019, 2020]
people = [20, 40, 60, 70]

plt.plot(year, people)
plt.xlabel('年份')
plt.ylabel('人口')
plt.title('人口增长')
# 设置纵坐标刻度
plt.yticks([0, 20, 40, 60, 80])


plt.fill_between(year, people, 20, color='green')
plt.show()
