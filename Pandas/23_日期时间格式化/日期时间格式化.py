# 在处理这些数据集时  可能会遇到日期格式不统一的问题  此时就需要对日期时间作统一的格式化处理

# Python 内置的strptime()方法能够将字符串日期转换为datetime类型
from datetime import datetime
import pandas as pd
import numpy as np
# 将日期定义为字符串
date_str1 = 'Wednesday,July 18, 2020'
date_str2 = '18/7/20'
date_str3 = '18-07-2020'
# 将日期转化为datetime对象
# dmy_dt1 = datetime.strptime(date_str1, '%A,%B %d,%Y')
dmy_dt2 = datetime.strptime(date_str2, '%d/%m/%y')
dmy_dt3 = datetime.strptime(date_str3, '%d-%m-%Y')
# print(dmy_dt1)
print(dmy_dt2)
print(dmy_dt3)
# 注意  strftime()可以将datetime类型转换为字符串类型  恰好与strptime()相反

# 除了使用Python内置的strptime()方法外  你还可以使用Pandas模块的pd.to_datetime()和
# pd.DatetimeIndex()进行转换
date = ['2012-5-6 11:00:00', '2012-5-16 11:00:00']
pd_date = pd.to_datetime(date)
df = pd.Series(np.random.randn(2), index=pd_date)
print(df)
# 2012-05-06 11: 00: 00    0.092893
# 2012-05-16 11: 00: 00    1.031312
# dtype: float64

# DatetimeIndex()
# 使用DatetimeIndex()函数设置时间序
date1 = pd.DataFrame(
    ['1/1/2008', '1/2/2008', '1/3/2008', '1/4/2008', '1/5/2008'])
dt = pd.Series(np.random.randn(5), index=date1)
print(dt)
# (1/1/2008,) - 1.538816
# (1/2/2008,) - 0.414159
# (1/3/2008,) - 0.795360
# (1/4/2008,) - 1.349197
# (1/5/2008,) - 1.348834
# dtype: float64
