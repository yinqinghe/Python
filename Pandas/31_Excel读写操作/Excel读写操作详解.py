# to_excel()函数可以将DataFrame中的数据写入到Excel文件

from operator import index
import pandas as pd
info_website = pd.DataFrame({'name': ['编程帮', 'c语言中文网', '微学院', '92python'],
                             'rank': [1, 2, 3, 4],
                             'language': ['PHP', 'C', 'PHP', 'Python'],
                             'url': ['www.bianchneg.com', 'c.bianchneg.net', 'www.ewixueyuan.com', 'www.92python.com']})
writer = pd.ExcelWriter('website.xlsx')
info_website.to_excel(writer)
writer.save()
print('输出成功')


# # read_excel()读取Excel数据
# df = pd.read_excel('website.xlsx', index_col='name', skiprows=[2])
# # 处理未命名列
# df.columns = df.columns.str.replace('Unnamed.*', 'col_label')
# print(df)

# index_col选择前两列作为索引列
# 选择前三列数据  name列作为行索引
df = pd.read_excel('website.xlsx', index_col=[0, 1], usecols=[1, 2, 3])
# 处理未命名列
df.columns = df.columns.str.replace('Unnamed.*', 'col_label')
print(df)
