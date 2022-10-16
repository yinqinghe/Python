import numpy as np
# char.add()将两个数组对应位置的字符串元素进行连接
print(np.char.add(['welcome', 'url'], ['to C net', 'is c.biancheng.net']))
# ['welcometo C net' 'urlis c.biancheng.net']

# char.multiply()函数将指定的字符串进行多次拷贝，并将拷贝结果返回
print(np.char.multiply('c.biancheng.net', 3))
# c.biancheng.netc.biancheng.netc.biancheng.net

# char.center()用于居中字符串
print(np.char.center("c.biancheng.net", 20, '*'))
# **c.biancheng.net***

# char.capitalize()将字符串的第一个字母转换为大写
print(np.char.capitalize('python  java'))
# Python

# char.title()将字符串数组中每个元素的第一个字母转换为大写
print(np.char.title("welcome to china"))
# Welcome To China

# char.lower()将字符串数组中每个元素转换为小写
print(np.char.lower("WELCOME TO MYHOME"))
# welcome to myhome

# char.upper()将数组中的每个元素转换为大写
print(np.char.upper("Welcome To Python"))
# WELCOME TO PYTHON

# char.split()该函数通过指定分隔符对字符串进行分割，并返回数组序列。默认情况下，分隔符为空格
print(np.char.split("Welcome To Python", sep=" "))
['Welcome', 'To', 'Python']

# char.splitlines()以换行符作为分隔符来分割字符串，并返回一个数组序列
print("Splitting the String line by line..")
print(np.char.splitlines("Welcome\n To \n Python"))
# ['Welcome', ' To ', ' Python']

# char.strip()用于移除开头或结尾处的空格
str = "     welcome to Python    "
print("原字符串：", str)
print(np.char.strip(str))
# 原字符串：      welcome to Python
# welcome to Python

# char.join()通过指定的分隔符来连接数组中的元素或字符串
print(np.char.join(':', 'Love'))
# L: o: v: e
# 也可以指定多个分隔符
print(np.char.join([':', '-'], ['Love', 'Python']))
# ['L:o:v:e' 'P-y-t-h-o-n']


# char.replace()使用新字符替换字符串中的指定字符
str1 = "Welcome to China"
print("原字符串：", str1)
# 更改后字符串
print(np.char.replace(str1, "Welcome to", "Hello"))
# 原字符串： Welcome to China
# Hello China

# char.encode(),char.decode()默认utf-8的形式进行编码与解码
# cp500国际编码
# 字符串进行编码
encode_str = np.char.encode("Welcome to China", 'cp500')
# 把乱码  解码成字符串
decode_str = np.char.decode(encode_str, 'cp500')
print(encode_str)
print(decode_str)
