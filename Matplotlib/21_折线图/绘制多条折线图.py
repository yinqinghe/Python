import matplotlib.pyplot as plt

x = [5, 8, 12, 14, 16, 18, 20]
y1 = [18, 21, 29, 31, 26, 24, 20]
y2 = [15, 18, 24, 30, 31, 25, 24]


plt.plot(x, y1, 'r', marker='*', markersize=10)

plt.plot(x, y2, 'b', marker='*', markersize=10)

plt.title('温度对比折线图')
plt.xlabel('时间(h)')
plt.ylabel('温度(C)')

# 给图像添加注释  并设置样式
for a, b in zip(x, y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)


plt.legend(['第一天', '第二天'])

plt.show()
