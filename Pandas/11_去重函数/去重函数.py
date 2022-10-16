import pandas as pd
data = {
    'A': [1, 0, 1, 1],
    'B': [0, 2, 5, 0],
    'C': [4, 0, 4, 4],
    'D': [1, 0, 1, 1]
}
df = pd.DataFrame(data=data)
print(df)
#    A  B  C  D
# 0  1  0  4  1
# 1  0  2  0  0
# 2  1  5  4  1
# 3  1  0  4  1

# 默认保留第一次出现的重复项
print(df.drop_duplicates())
#    A  B  C  D
# 0  1  0  4  1
# 1  0  2  0  0
# 2  1  5  4  1

# keep=False删除所有重复项
print(df.drop_duplicates(keep=False))
#    A  B  C  D
# 1  0  2  0  0
# 2  1  5  4  1

# 根据指定列标签去重  去除所有重复项  对于B列来说两个0是重复项
print(df.drop_duplicates(subset=['B'], keep=False))
#    A  B  C  D
# 1  0  2  0  0
# 2  1  5  4  1

data1 = {
    'A': [1, 3, 3, 3],
    'B': [0, 1, 2, 0],
    'C': [4, 5, 4, 4],
    'D': [3, 3, 3, 3]
}
df1 = pd.DataFrame(data=data1)
df1 = df1.drop_duplicates(subset=['B'], keep=False)
# 重置索引  从0重新开始
print(df1.reset_index(drop=True))
#    A  B  C  D
# 0  3  1  5  3
# 1  3  2  4  3

# 指定多列同时去重
df_2 = pd.DataFrame({'Country ID': [1, 1, 2, 12, 34, 23, 45, 34, 23, 12, 2, 3, 4, 1],
                     'Age': [12, 12, 15, 18, 19, 25, 21, 25, 25, 18, 25, 12, 32, 18],
                     'Group ID': ['a', 'z', 'c', 'a', 'b', 's', 'd', 'a', 'b', 's', 'a', 'd', 'a', 'f']})
# last只保留最后一个重复项

print(df_2.drop_duplicates(['Age', 'Group ID'], keep='last'))
