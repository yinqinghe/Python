# 时间序列包含三种应用场景  分别是
# 特定的时刻(timestamp)  也就是时间戳
# 固定的日期(period)   比如某年某月某日
# 时间间隔(interval)   每隔一段时间具有规律性
from sqlite3 import Timestamp
import numpy as np
from datetime import datetime
from traceback import print_last
import pandas as pd
print(datetime.now())

print(pd.Timestamp('1970-1-1'))
print(pd.Timestamp(1888855555, unit='s'))

# 创建时间范围  通过date_range()方法可以创建某段连续的时间或者固定间隔的时间时间段
# freq表示时间频率  没30min变化一次         freq  时间频率  默认为"D" (天)
print(pd.date_range("9:00", "18:10", freq="30min").time)

# 更改时间频率    为一个小时
print(pd.date_range("6:10", "11:45", freq="H").time)
# [datetime.time(6, 10) datetime.time(7, 10) datetime.time(8,10)
#  datetime.time(9, 10) datetime.time(10, 10) datetime.time(11, 10)]

# 转化为时间戳
# 可以使用to_datetime()函数将Series或list转换为日期对象  其中list会转换为Datetimeindex
print(pd.to_datetime(pd.Series(['Jun 3,2020', '2020-12-10', None])))
# 0   2020-06-03
# 1   2020-12-10
# 2          NaT
# dtype: datetime64[ns]
# 注意  NaT标示顿不是时间  它等效于NAN

# 传入list 生成Datetimeindex
print(pd.to_datetime(['Jun 3,2020', '2020-12-10', None]))
# DatetimeIndex(['2020-06-03', '2020-12-10', 'NaT'],
#               dtype='datetime64[ns]', freq=None)

# 频率和周期转换
# Periods()方法  可以将频率"M"(月)转换为Period(时间段)
x = pd.Period('2014', freq='M')
# start参数

print(x.asfreq('D', 'start'))
# end参数
print(x.asfreq('D', 'end'))
# 2014-01-01
# 2014-01-31


# 时间周期计算
# 周期计算  指的是对时间周期进行算术运算  所有的操作将在"频率"的基础上执行
x = pd.Period('2014', freq='S')
print(x)
print(x+1)

p1 = pd.Period('2020')
p2 = pd.Period('2019')
print(f'p1={p1}年')
print(f'p2={p2}年')
print(f'p1和p2间隔{p1-p2}年')

print(f'五年前是{p1-5}年')


# 创建时间周期
p = pd.period_range('2011', '2018', freq='Y')
print(p)
# PeriodIndex(['2016', '2017', '2018'], dtype='period[A-DEC]')

# 时间序列转换
# 如果想要把字符串日期转换为Period  首先需要将字符串转换为日期格式  然后再将日期转换为Period
# 创建时间序列
index = pd.date_range('2020-3-17', "2020-3-30", freq='1.5H')
# 随即选取4个互不相同的数
loc = np.random.choice(np.arange(len(index)), size=4, replace=False)
loc.sort()
ts_index = index[loc]
pd_index = ts_index.to_period('D')
print(pd_index)

# 使用to_timestamp()能够将Period时期转换为时间戳(Timestamp)
ppd = pd.Period("2020-2-3")
print(ppd.to_timestamp())
# 2020-02-03 00:00:00

# 创建日期范围
# Pandas提供了用来创建日期序列的函数date_range()
# 该函数的默认频率为"D"  也就是天   日期序列只包含年 月  日  不包含时  分  秒
print(pd.date_range('12/15/2020', periods=5))
# 当我们使用date_range()来创建日期范围时  该函数含结束的日期  用数学术语来说就是区间左闭右闭
# 即包含起始值  也包含结束值

# 建议使用Python的datetime模块创建时间
start = pd.datetime(2019, 1, 1)
end = pd.datetime(2019, 1, 5)
print(pd.date_range(start, end))


# 更改日频率
print(pd.date_range('12/15/2011', periods=5, freq='M'))

print(pd.bdate_range('11/25/2020', periods=8))
# bdate_range()表示创建工作日的日期范围  它与date_range()不同  它不包括周六  周日
# date_range()默认频率是日历日  bdate_range()的默认频率是工作日
