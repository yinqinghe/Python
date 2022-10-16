# 几个常见的统计函数  比如百分比函数  协方差函数  相关函数
import pandas as pd
import numpy as np
# Series 结构
s = pd.Series([1, 2, 3, 4, 5, 4])
# pct_change()函数  该函数将每个元素与其前一个元素进行比较  并计算前后数值的百分比变化
print(s.pct_change())
df = pd.DataFrame(np.random.randn(5, 2))
print(df)
print(df.pct_change())
# 默认情况下  pct_change()对列进行操作  如果想要操作行  则需要传递参数axis=1参数
df1 = pd.DataFrame(np.random.randn(3, 2))
print(df1.pct_change(axis=1))
#     0         1
# 0 NaN -0.175734
# 1 NaN -1.648676
# 2 NaN -2.646207

# 协方差cov Series对象提供了一个cov方法用来计算series对象之间的协方差
# 同时  该方法也会将缺失值(NAN)自动排除
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))

# 当应用于DataFrame时  协方差(cov)将计算所有列之间的协方差
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# 计算a与b之间的协方差值
print(frame['a'].cov(frame['b']))
# 计算所有数列的协方差值
print(frame.cov())

# 相关系数(corr)
# 相关系数显示任意两个Series之间的线性关系  Pandas提供了计算相关性的三种方法
# 分别是 pearson(default)  spearman()和kendall()
# df_corr = pd.DataFrame(np.random.randn(
#     10, 5), columns=['a', 'b', 'c', 'd', 'e'])
# print(df['b'].corr(frame['c']))
# print(df.corr())

ss = pd.Series(np.random.randn(5), index=list('abcde'))
ss['d'] = ss['b']
print(ss)
# a - 0.763732
# b - 0.156366
# c - 1.137596
# d - 0.156366
# e - 0.407802
# dtype: float64
# a/b排名分别为2和3 其平均排名为2.5
# rank()按照某种规则(升序或者降序)对序列中的元素值排名  该函数的返回值的也是一个序列
# 包含了原序列中每个元素值的名次  如果序列中包含两个相同的元素值  那么会为其分配两者的平均排名
print(ss.rank())
# a    2.0
# b    4.5
# c    1.0
# d    4.5
# e    3.0
# dtype: float64


a = pd.DataFrame(np.arange(12).reshape(3, 4), columns=list("abcd"))
a = a.sort_index(axis=1, ascending=False)
print(a)
a.iloc[[1, 1], [1, 2]] = 6
print(a)
# 按行排名  将相同数值设置为所在行数值的最大排名
print(a.rank(axis=1, method="max"))
#      d    c    b    a
# 0  4.0  3.0  2.0  1.0
# 1  4.0  3.0  3.0  1.0
# 2  4.0  3.0  2.0  1.0

# 按行排名  将相同数值设置为所在行数值的最小排名
print(a.rank(axis=1, method="min"))
