# Timedelta表示时间差(或者时间增量)  我们可以使用不同的时间单位来表示它
# 比如  天  小时  分  秒    时间差的最终的结果可以是正时间差  也可以是负时间差

import pandas as pd
import numpy as np
# 字符串
print(pd.Timedelta('5 days 8 hours 6 minutes 59 seconds'))
# 5 days 08:06:59

# 整数
print(pd.Timedelta(19, unit='h'))
# 0 days 19: 00: 00

# 数据偏移量
print(pd.Timedelta(days=2, hours=6))
# 2 days 06:00:00

# pd.to_timedelta()方法  将具有timedelta格式的值(标量、数组、列表或Series)
# 转换为Timedelta类型   如果输入是Series 则返回Series  如果输入是标量  则返回值也为标量
# 其它情况输出TimedeltaIndex

print(pd.to_timedelta(['1 days 06:05:01.00003', '15.5us', 'nan']))
# TimedeltaIndex(['1 days 06:05:01.000030', '0 days 00:00:00.000015500',
#                NaT], dtype='timedelta64[ns]', freq=None)
print(pd.to_timedelta(np.arange(5), unit='s'))
# TimedeltaIndex(['0 days 00:00:00', '0 days 00:00:01', '0 days 00:00:02',
#                 '0 days 00:00:03', '0 days 00:00:04'],
#                dtype='timedelta64[ns]', freq=None)


# 算术操作
# 通过对datetime64[ns]类型的时间序列或时间戳做算术运算  其运算结果依然是datetime64[ns]
# 数据类型
s = pd.Series(pd.date_range('2020-1-1', periods=5, freq='M'))
# 推导式用法
td = pd.Series([pd.Timedelta(days=i) for i in range(5)])
df = pd.DataFrame(dict(A=s, B=td))
print(df)
#            A      B
# 0 2020-01-01 0 days
# 1 2020-01-02 1 days
# 2 2020-01-03 2 days
# 3 2020-01-04 3 days
# 4 2020-01-05 4 days

# 加法运算
df['C'] = df['A']+df['B']
print(df)
#          A      B          C
# 0 2020-01-31 0 days 2020-01-31
# 1 2020-02-29 1 days 2020-03-01
# 2 2020-03-31 2 days 2020-04-02
# 3 2020-04-30 3 days 2020-05-03
# 4 2020-05-31 4 days 2020-06-04


# 减法运算
df['D'] = df['C']-df['B']
print(df)
