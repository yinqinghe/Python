import pandas as pd
import numpy as np
data = {'Name': ['John', 'Helen', 'Sona', 'Ella'], 'score': [82, 98, 91, 87],
        'option_course': ['C#', 'Python', 'Java', 'C']}
df = pd.DataFrame(data)
print(df)

print(df.groupby('score'))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001F8561DB100>

# 查看分组结果
print(df.groupby('score').groups)
# {82: [0], 87: [3], 91: [2], 98: [1]}

# 多个列标签分组
print(df.groupby(['Name', 'score']).groups)
# {('Ella', 87): [3], ('Helen', 98): [1], ('John', 82): [0], ('Sona', 91): [2]}

grouped = df.groupby('score')
# 根据对应组的数据值  选择一个组
print(grouped.get_group(91))
#    Name  score option_course
# 2  Sona     91          Java

# 遍历分组数据
for label, option_course in grouped:
    # 其中key代表分组后字典的键  也就是score
    print(label)
    # 字典对应的值选修的科目  score
    print(option_course)

# 应用聚合函数   创建groupby对象时  通过agg()函数可以对分组对象应用多个聚合函数
groupe = df.groupby('Name')
# 应用一个聚合函数求均值
print(groupe['score'].agg(np.mean))
# Name
# Ella     87.0
# Helen    98.0
# John     82.0
# Sona     91.0
# Name: score, dtype: float64

# 也可以一次性应有多个聚合函数
print(groupe['score'].agg([np.size, np.mean, np.std]))
#        size  mean  std
# Name
# Ella      1  87.0  NaN
# Helen     1  98.0  NaN
# John      1  82.0  NaN
# Sona      1  91.0  NaN

# 组的转换操作

df_1 = pd.DataFrame({'种类': ['水果', '水果', '水果', '蔬菜', '蔬菜', '肉类', '肉类', ],
                     '产地': ['朝鲜', '中国', '缅甸', '中国', '菲律宾', '韩国', '中国'],
                     '水果': ['橘子', '苹果', '哈密瓜', '番茄', '椰子', '鱼肉', '牛肉'],
                     '数量': [3, 5, 5, 3, 2, 15, 9],
                     '价格': [2, 5, 12, 3, 4, 18, 20]})
# 在组的行或列上可以执行转换操作  最终会返回一个与组大小相同的索引对象
# 对可执行计算的数值列求均值
print(df_1.groupby('种类').transform(np.mean))
def demean(arr): return arr-arr.mean()


# transfrom()直接应用demean  实现去均值操作
print(df_1.groupby('种类').transform(demean))
# 自定义函数
# 返回分组的前n行数据


def get_rows(df_1, n):
    # 从1到n行的所有列
    return df_1.iloc[:n, :]


# 分组后的组名作为行索引
print(df_1.groupby('种类').apply(get_rows, n=1))


# 组的数据过滤操作
data1 = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings', 'Kings', 'Kings',
                  'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
         'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
         'Points': [874, 789, 863, 663, 741, 802, 756, 788, 694, 701, 812, 698]}
df_2 = pd.DataFrame(data1)
# 筛选出参加比赛超过两次的球队
print(df_2.groupby('Team').filter(lambda x: len(x) > 2))
