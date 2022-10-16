# CSV文件读取
import sqlite3
import pandas
# 仅仅一行代码就完成了数据读取
df = pandas.read_csv(r'D:\C#\VSCODE\python\Pandas\29_Pandas读取文件\01.csv')
print(df)


# json读取文件
# data=pandas.read_json('')
# print(data)


# SQL数据库读取
# 建立数据连接
con = sqlite3.connect('database.db')
df = pandas.read_sql_query("SQL语句", con)
