# 想要应用自定义的函数  或者把其他库中的函数应用到Pandas对象
# 1、操作整个DataFrame的函数:pipe()
# 2、操作行或者列的函数:apply()
# 3、操作单一元素的的函数:applymap()
import pandas as pd
import numpy as np


def adder(ele1, ele2):
    return ele1+ele2


df = pd.DataFrame(np.random.randn(4, 3), columns=['c1', 'c2', 'c3'])
# 传入自定义函数以及要想加的数值3
# df.pipe(adder, 3)
# 相加前
print(df)
#           c1        c2        c3
# 0  1.197367  1.437869  2.533781
# 1  1.155949 - 0.806421  0.318679
# 2 - 2.264498 - 0.834694  1.059298
# 3  2.413083  0.645846  1.634408
# 相加后
# print(df.pipe(adder, 3))
#          c1        c2        c3
# 0  4.197367  4.437869  5.533781
# 1  4.155949  2.193579  3.318679
# 2  0.735502  2.165306  4.059298
# 3  5.413083  3.645846  4.634408

# 操作行或列
print(df.apply(np.mean))
# c1    0.318607
# c2    0.197055
# c3 - 0.182600
# dtype: float64

print(df.apply(np.mean, axis=1))


# 求每一列中  最大值与最小值之差
df_1 = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print(df_1.apply(lambda x: x.max()-x.min()))
# col1    2.822396
# col2    3.086726
# col3    2.331633
# dtype: float64


# 操作单一元素
print(df_1['col1'].map(lambda x: x*100))
# 0 - 57.430186
# 1    132.311287
# 2 - 167.645144
# 3      0.611083
# 4     71.865838
# Name: col1, dtype: float64
