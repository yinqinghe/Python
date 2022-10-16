# 随机抽样  是统计学中常用的一种方法  它可以帮助我们从大量的数据中快速地构建出一组数据分析模型
# 在Pandas中  如果想要对数据集进行随机抽样  需要使用sample()函数

import pandas as pd
dict = {'name': ['Jack', 'Tom', 'Helen', 'John'],
        'age': [28, 39, 34, 36], 'score': [98, 92, 91, 89]}
info = pd.DataFrame(dict)
# 默认随机选择两行
print(info.sample(n=2))
# 随机选择两列
print(info.sample(n=2, axis=1))

info1 = pd.DataFrame({'data1': [2, 6, 8, 0], 'data2': [2, 5, 0, 8], 'data3': [12, 2, 1, 8]},
                     index=['John', 'Parker', 'Smith', 'William'])
# 随机抽取3个数据
print(info1['data1'].sample(n=3))
# 总体 的25%
print(info1.sample(frac=0.25, replace=True))
#        data1  data2  data3
# Smith      8      0      1
# Smith      8      0      1
# data3序列为权重值  并且允许重复数据出现
print(info1.sample(n=2, weights='data3', random_state=1))
