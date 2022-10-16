from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
#  创建一个空白画布
fig = plt.figure()
# 序列中的4个数字分别对应图形的左侧  底部  宽度  高毒  且每个数字必须介于0于1之间
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_title('sine wave')
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()
