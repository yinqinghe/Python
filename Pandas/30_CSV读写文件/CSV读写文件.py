import pandas as pd
import numpy as np
df = pd.read_csv(r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv')
print(df)

# 自定义索引
df = pd.read_csv(
    r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv', index_col=['ID'])
print(df)

# 查看每一列的dtype
# 转换salary为float类型
df_dt = pd.read_csv(r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv', dtype={
                    'Salary': np.float64})
print(df_dt.dtypes)

# 更改文件标头名
df_na = pd.read_csv(r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv', names=[
                    'a', 'b', 'c', 'd', 'e'])
print(df_na)
#     a      b    c         d       e
# 0  ID   Name  Age      City  Salary
# 1   1   Jack   28   Beijing   22000
# 2   2   Lida   32  Shanghai   19000
# 3   3   John   43  Shenzhen   12000
# 4   4  Helen   38  Hengshui    3500
# 文件标头名是附加的自定义名称  但是原来的标头名(列表签名)并没有被删除  可以使用header参数来删除它
df_na = pd.read_csv(r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv', names=[
                    'a', 'b', 'c', 'd', 'e'], header=0)
# 假如原标头名并没有定义在第一行  可以传递相应的行号来删除它
print(df_na)

# 跳过指定的行数
df_na = pd.read_csv(r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\01.csv', names=[
                    'a', 'b', 'c', 'd', 'e'], skiprows=3)
# 包含标头所在行
print(df_na)


# to_sdv()函数用于将DataFrame转换为CSV数据
# 如果想要把CSV数据写入文件   只需向函数传递一个文件对象即可   否则  CSV数据将以字符串格式返回
data = {'Name': ['Smith', 'Parker'], 'ID': [
    101, 102], 'Language': ['Python', 'JavaScript']}
info = pd.DataFrame(data)
print('DataFrame  Values:\n', info)
# 转换为CSV数据
csv_data = info.to_csv()
print('\nCSV String Values: \n', csv_data)


# pd.NaT表示null缺失数据
data_s = {'Name': ['Smith', 'Parker'], 'ID': [
    101, pd.NaT], 'Language': ['Python', 'JavaScript']}
info = pd.DataFrame(data_s)
csv_data = info.to_csv(
    r'D:\C#\VSCODE\python\Pandas\30_CSV读写文件\02.csv', sep='|')
