# subplots()函数  它的使用方法和subplot()函数类似  其不同之处在于
# subplots()即创建了一个包含子图区域的画布  又创建了一个figure图形对象
# 而subplot()只是创建一个包含子图区域的画布

# subplot()函数的返回值是一个元组
import numpy as np
import matplotlib.pyplot as plt
fig, a = plt.subplots(2, 2)
x = np.arange(1, 5)
# 绘制平方函数
a[0][0].plot(x, x*x)
a[0][0].set_title('square')
# 绘制平方根函数
a[0][1].plot(x, np.sqrt(x))
a[0][1].set_title('square root')
# 绘制指数函数
a[1][0].plot(x, np.exp(x))
a[1][0].set_title('exp')
# 绘制对数函数
a[1][1].plot(x, np.log10(x))
a[1][1].set_title('log')
plt.show()
