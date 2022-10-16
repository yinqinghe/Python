# 通常情况下  数据集中会存在许多同一类别的信息  比如相同国家  相同行政编码  相同性别
# 当这些相同类别的数据多次出现时  就会给数据处理增添许多麻烦  导致数据集变得臃肿
# 不能直观  清晰地展示数据
# 针对上述问题  Pandas提供了分类对象  该对象能够现有序排列  自动去重的功能
# 但是它不能执行运算

import pandas as pd
import numpy as np
# 指定dtype创建
s = pd.Series(['a', 'b', 'c', 'a'], dtype="category")
print(s)
# 0    a
# 1    b
# 2    c
# 3    a
# dtype: category
# Categories(3, object): ['a', 'b', 'c']
# 虽然传递给series四个元素值  但是它的类别为3  这是因为a的类别存在重复

# pd.Categorical创建一个类别对象
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)

cats = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'])
print(cats)
# ['a', 'b', 'c', 'a', 'b', 'c', NaN]
# Categories(3, object): ['c', 'b', 'a']
# 第二个参数值表示类别  当列表中不存在某一类别时  会自动将类别值设置为NA

# ordered=True来实现有序分类
cat1 = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], [
                      'c', 'b', 'a'], ordered=True)
print(cat1)
# ['a', 'b', 'c', 'a', 'b', 'c', NaN]
# Categories(3, object): ['c' < 'b' < 'a']
# 求最小值
print(cat1.min())
# c

# 获取统计信息
# 对已经分类的数据使用describe()方法  你会得到和数据统计相关的摘要信息
cat2 = pd.Categorical(['a', 'c', 'c', np.nan], categories=['b', 'a', 'c'])
df = pd.DataFrame({'cat': cat2, 's': ['a', 'c', 'c', np.nan]})
print(df.describe())
print(df['cat'].describe())
#        cat  s
# count    3  3
# unique   2  2
# top      c  c
# freq     2  2

# count     3
# unique    2
# top       c
# freq      2
# Name: cat, dtype: object


# 获取类别属性
print(cat2.categories)
# Index(['b', 'a', 'c'], dtype='object'
# False 表示未指定排序
print(cat.ordered)


# 重命名类别
# 对类名重命名
# s.cat.categories = ["Group %s" % g for g in s.cat.categories]
# print(s.cat.categories)
# Index(['Group a', 'Group b', 'Group c'], dtype='object')

# 追加新类别
s = s.cat.add_categories([5])
print(s.cat.categories)
# Index(['a', 'b', 'c', 5], dtype='object')

# 删除类别
print(s.cat.remove_categories('a'))
# 0    NaN
# 1      b
# 2      c
# 3    NaN
# dtype: category
# Categories(3, object): ['b', 'c', 5]

# 分类对象比较
s1 = ['a', 'a', 'b', 'd', 'c']
s2 = ['a', 'b', 'b', 'd', 'c']

# 当满足两个类别长度相同时
ss0 = pd.Categorical(s1, categories=['a', 'd', 'b', 'c'])
ss1 = pd.Categorical(s1)
print(ss0 == ss1)
# [ True  True  True  True  True]

# 满足上述第二个条件  类别相同  并且ordered均为True
ss2 = pd.Categorical(s1, categories=['a', 'd', 'b', 'c'], ordered=True)
ss3 = pd.Categorical(s2, categories=['a', 'd', 'b', 'c'], ordered=True)
print(ss2 < ss3)
