# concat()函数用于沿某个特定的轴执行连接操作

import pandas as pd
a = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                  'B': ['B0', 'B1', 'B2', 'B3'],
                  'C': ['C0', 'C1', 'C2', 'C3'],
                  'D': ['D0', 'D1', 'D2', 'D3'], }, index=[0, 1, 2, 3])

b = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                  'B': ['B4', 'B5', 'B6', 'B7'],
                  'C': ['C4', 'C5', 'C6', 'C7'],
                  'D': ['D4', 'D5', 'D6', 'D7'], })
# 连接a与b
print(pd.concat([a, b]))

c = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                  'B': ['B4', 'B5', 'B6', 'B7'],
                  'C': ['C4', 'C5', 'C6', 'C7'],
                  'D': ['D4', 'D5', 'D6', 'D7']}, index=[2, 3, 4, 5])
# 连接a与b  并给a,b连接一个指定的键
print(pd.concat([a, c], keys=['x', 'y']))
#      A   B   C   D
# x 0  A0  B0  C0  D0
# 1  A1  B1  C1  D1
# 2  A2  B2  C2  D2
# 3  A3  B3  C3  D3
# y 2  A4  B4  C4  D4
# 3  A5  B5  C5  D5
# 4  A6  B6  C6  D6
# 5  A7  B7  C7  D7
# 可以看出行索引index存在重复使用的现象  如果想让输出的行索引遵循依次递增的规则
# 那么需要将ignore_index设置为True

print(pd.concat([a, c], keys=['x', 'y'], ignore_index=True))
# 此时的索引顺序被改变了  而且键keys指定的键也被覆盖了


# 如果沿着axis=1添加两个对象  那么将会追加新的列
print(pd.concat([a, c], axis=1))


# 沿着axis=0  使用append()方法连接a与b
print(a.append(c))


# append()函数也可接受多个对象   我这里程序报错
print(a.append(a))
