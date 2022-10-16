# subplot2grid()  该函数能够在画布的特定位置创建axes对象(即绘图区域)
# 它还可以使用不同数量的行、列来创建跨度不同的绘图区域
# 与subplot()和subplots()函数不同   subplot2grid()函数以非等分的形式对画布进行切分

# 在画布(figure)中添加了行、列跨度均不相同的绘图子区域
# 然后在每个绘图区上   绘制不同的图形

import numpy as np
import matplotlib.pyplot as plt
# 使用colspan指定列   使用rowspan指定行
a1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
a2 = plt.subplot2grid((3, 3), (0, 2), rowspan=3)
a3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2, colspan=2)
x = np.arange(1, 10)
a2.plot(x, x*x)
a2.set_title('square')
a1.plot(x, np.exp(x))
a1.set_title('exp')
a3.plot(x, np.log(x))
a3.set_title('log')
plt.tight_layout()
plt.show()
