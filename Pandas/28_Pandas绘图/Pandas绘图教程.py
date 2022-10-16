# Pandas之所以能够实现了数据可视化 主要利用了matplotlib库的plot()方法  它对plot()方法做了简单的封装
# 因此可以直接调用该街口

from inspect import stack
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 创建包含时间序列 的数据
df = pd.DataFrame(np.random.randn(8, 4), index=pd.date_range('2/1/2020', periods=8),
                  columns=list('ABCD'))
# df.plot()

df_bar = pd.DataFrame(np.random.rand(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# 或使用df.plot(kind='bar')
# df_bar.plot.bar()

# 通过设置stacked=True可以生成柱状堆叠图
# df.plot(kind='bar', stacked=True)

# 绘制水平柱状图
# df.plot.barh(stacked=True)

# 绘制直方图
df_hist = pd.DataFrame({'A': np.random.randn(100)+2, 'B': np.random.rand(100),
                        'C': np.random.randn(100)-2}, columns=['A', 'B', 'C'])
# print(df_hist)
# df_hist.plot.hist(bins=5)

# 给每一列数据都绘制一个直方图
df_diff = pd.DataFrame({'A': np.random.randn(100)+2, 'B': np.random.rand(100),
                        'C': np.random.randn(100)-2, 'D': np.random.randn(100)+3},
                       columns=['A', 'B', 'C', 'D'])
# df_diff.diff().hist(color='r', alpha=0.5, bins=15)

# 箱型图
df_box = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
# df_box.plot.box()

# 区域图
df_area = pd.DataFrame(np.random.rand(5, 4), columns=['a', 'b', 'c', 'd'])
# df_area.plot.area()

# 散点图
df_scatter = pd.DataFrame(np.random.rand(30, 4), columns=['a', 'b', 'c', 'd'])
# df_scatter.plot.scatter(x='a', y='b')


df_pie = pd.DataFrame(np.random.rand(4),
                      index=['go', 'java', 'C++', 'C'], columns=['L'])
df_pie.plot.pie(subplots=True)
plt.show()
