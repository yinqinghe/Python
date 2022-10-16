# 为了能更好地处理数值型数据  Pandas提供了几种窗口函数
# 比如移动函数(rolling)  扩展函数(expanding) 和指数加权函数(ewm)
# 窗口是一种形象化的叫法  这些函数在执行操作时   就如同窗口一样在数据区间上移动

# 主要学习主要讲解如何在DataFrame和Series对象上应用窗口函数

import pandas as pd
import numpy as np
# 生成时间序列
df = pd.DataFrame(np.random.randn(8, 4), index=pd.date_range(
    '12/1/2020', periods=8), columns=['A', 'B', 'C', 'D'])
print(df)
# rolling()又称移动窗口函数  它可以与mean count  sum  median std等聚合函数一起使用
# Pandas为移动函数定义了专门的方法聚合方法  比如rolling_mean()  rolling_count()  rolling_sum()
# 每三个数求一次均值    window默认值为1  表示窗口的大小   也就是观测值的数量
print(df.rolling(window=3).mean())
# window=3表示是每一列中依次紧邻的每3个数求一次均值   当不满足3个数时  所求值均为NaN值
# 因此前两列的值为NaN   直到第三行值才满足要求window=3
# (index1+index2+index3)/3

# expanding()又叫扩展窗口函数  扩展是指由序列的第一个元素开始  逐个向后计算元素的聚合值
# min_periods=n表示向后移动n个值计求一次平均值
print(df.expanding(min_periods=3).mean())
#  设置min_periods=3  表示至少3个数求一次均值  计算公式(index0+index1+index2)/3
# 而index3的计算方式是(index0+index1+index2+index3)/3


# ewm()表示指数加权移动  ewn()函数先会对序列元素做指数加权运算  其次计算加权后的均值
# 该函数通过指定com  span或者halflife参数来实现指数加权移动

# 设置com=0.5   先加权再求均值
print(df.ewm(com=0.5).mean())


# 在数据分析的过程中  使用窗口函数能够提升数据的准确性  并且使数据曲线的变化趋势更加平滑
# 从而让数据分析变得更加准确  可靠
