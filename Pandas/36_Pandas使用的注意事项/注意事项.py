import numpy as np
# if语句使用
import pandas as pd
# if pd.Series([False, True, False]):
#     print('I am True')
# ValueError: The truth value of a Series is ambiguous.
# Use a.empty, a.bool(), a.item(), a.any() or a.all().
# 上述代码引发了ValueError错误  并告诉我们Series的真值是不明确的


# 使用any()方法解决
if pd.Series([False, True, False]).any():
    print('I am True')

# 如果要是计算单个布尔元素的Series对象  那么你可以使用bool()方法进行修改
print(pd.Series([False]).bool())


# 布尔运算
s = pd.Series(range(4))
# 返回布尔值序列  行索引为3的位置为True
print(s == 3)

# isin()操作
# isin()也会返回一个布尔序列  它用来判断元素值是否包含在的Series序列中
ss = pd.Series(list('abc'))
ss = ss.isin(['a', 'c', 'e'])
print(ss)
# 0     True
# 1    False
# 2     True
# dtype: bool


# reindex()操作
df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three', 'four'],
                  index=['a', 'b', 2, 3, 'e', 5])
print(df)
# 数字与字符混合后取数据
print(df.reindex(['a', 'b', 5]))
print(df.reindex([2, 'e']))
