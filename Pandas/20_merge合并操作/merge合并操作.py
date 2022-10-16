from cgi import print_arguments
import pandas as pd
left = pd.DataFrame({'id': [1, 2, 3, 4],
                     'Name': ['Smith', 'Maiki', 'Hunter', 'Hilen'],
                     'subject': ['sub1', 'sub2', 'sub4', 'sub6'], })
right = pd.DataFrame({'id': [1, 2, 3, 4],
                      'Name': ['William', 'Albert', 'Tony', 'Allen'],
                      'subject': ['sub2', 'sub4', 'sub3', 'sub6'], })
print(left)
print(right)

# 在单个键上进行合并操作
# 通过no参数指定一个连接键  对上述DataFrame进行合并操作
print(pd.merge(left, right, on='id'))
#    id  Name_x subject_x   Name_y subject_y
# 0   1   Smith      sub1  William      sub2
# 1   2   Maiki      sub2   Albert      sub4
# 2   3  Hunter      sub4     Tony      sub3
# 3   4   Hilen      sub6    Allen      sub6

# 在多个键上进行合并操作
print(pd.merge(left, right, on=['id', 'subject']))

#    id Name_x subject Name_y
# 0   4  Hilen    sub6  Allen

# 通过how参数可以确定DataFrame中要包含哪些键  如果在左表  右表都不存在的键
# 那么合并后该键对应的值为NAN
# left   LEFT OUTER JOIN    使用左侧对象的key
# right   RIGHT OUTER JOIN    使用右侧对象的key
# outer  FULL OUTER JOIN    使用左右两侧所有key的并集
# inner  INNER OUTER JOIN    使用左右两侧key的交集

# 以left侧的subject为键
print(pd.merge(left, right, on='subject', how="left"), '\n')

# 以right侧的subject为键
print(pd.merge(left, right, on='subject', how="right"), '\n')

# outer join(并集)
# 求出两个subject的并集  并作为键
print(pd.merge(left, right, on='subject', how="outer"), '\n')

# inner join(交集)
# 求出两个subject的交集  并作为键
print(pd.merge(left, right, on='subject', how="inner"), '\n')
# 当a与b进行内连接操作时a.join(b)不等于 b.join(a)
