# PyLab是一个面向Matplotlib的绘图接口  其语法和MATLAB十分相近
# 它和Pyplot模块都能实现Matplotlib的绘图功能  PyLab是一个单独的模块
# 随Matplotlib软件包一起安装  该模块的导包方式和Pyplot不同

from matplotlib import pyplot as plt
import pylab
from pylab import *


from numpy import *
from pylab import *
x = linspace(-3, 3, 30)
y = x**2
# 在同一绘图区域内绘制多个图形
plot(x, y, 'r.')
plot(x, sin(x))
plot(x, cos(x), '1')
plot(x, -sin(x), 'g--')
show()
clf()
