# 数据重采样是将时间序列从一个频率转换至另一个频率的过程  它主要有两种实现方式
# 分别是降采样和升采样  降采样指将高频率的数据转换为低频率  升采样则与其恰好相反
# 降采样:将高频率(间隔短)数据转换为低频率(间隔长)
# 升采样:将低频率数据转换为高频率

# Pandas提供了resample()函数来实现数据的重采样
# 降采样
import pandas as pd
import numpy as np
rng = pd.date_range('1/1/2021', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# 降采样后并聚合   按天计数的频率转换为按月计数
print(ts.resample('M').mean())
# 2021-01-31    0.235876
# 2021-02-28 - 0.001725
# 2021-03-31    0.125796
# 2021-04-30 - 0.207662
# Freq: M, dtype: float64

# 如果你只想看到月份  可以设置kind=period
print(ts.resample('M', kind='period').mean())

# 升采样是将低频率(时间间隔)转换为高频率
r = pd.date_range('1/1/2021', periods=20, freq='3D')
tss = pd.Series(np.random.randn(len(r)), index=r)
print(tss.head())
# 使用asfreq()在原数据基础上实现频率转换
print(tss.resample('D').asfreq().head())

# 频率转换
# asfreq()方法不仅能够实现频率转换  还可以保留原频率对应的数值  同时它也可以单独使用
index = pd.date_range('1/1/2021', periods=6, freq='T')
series = pd.Series([0.0, None, 2.0, 3.0, 4.0, 5.0], index=index)
df = pd.DataFrame({'s': series})
print(df.asfreq("60s"))
#                        s
# 2021-01-01 00:00:00  0.0
# 2021-01-01 00:01:00  NaN
# 2021-01-01 00:02:00  2.0
# 2021-01-01 00:03:00  3.0
# 2021-01-01 00:04:00  4.0
# 2021-01-01 00:05:00  5.0

# 插值处理
# 升采样的结果会产生缺失值  那么就需要对缺失值进行处理

print(tss.resample('D').asfreq().head())
# 使用ffill处理缺失值
print(tss.resample('D').asfreq().ffill().head())
