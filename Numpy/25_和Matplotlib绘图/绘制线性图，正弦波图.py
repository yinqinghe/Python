import numpy as np
from matplotlib import pyplot as plt
# 绘制线性图
# x = np.arange(1, 11)
# y = x*2+5

# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.plot(x, y, "ob")
# plt.show()


# 绘制正弦波图
# x = np.arange(0, 3*np.pi, 0.1)
# y = np.sin(x)
# plt.title("sine wave image")
# # 使用matplotlib制图
# plt.plot(x, y)
# plt.show()

# 计算正弦和余弦曲线上的点的x和y坐标
x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 绘制subplot网格为2行1列
# 激活第一个subplot
plt.subplot(2, 1, 1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')

# 将第二个subplot 激活  并绘制第二个图像
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()
