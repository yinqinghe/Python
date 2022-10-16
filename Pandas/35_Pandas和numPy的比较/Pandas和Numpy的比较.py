# 我们知道Pandas是在NumPy的基础构建而来  因此  熟悉Numpy可以更加有效的帮助我们使用Pandas

# NumPy主要C语言编写  因此  在计算还和处理一维或多维数组方面
# 它要比Python数组快得多

import numpy as np
import pandas as pd
import array
arr = np.array([2, 4, 6, 8, 10, 12])
print(type(arr))
# <class 'numpy.ndarray' >
print("打印新建数组: ", end="")

for l in range(0, 5):
    print(arr[l], end=" ")

# 虽然Python本身没有数组这个说法  不过Python提供一个array模块  用于创建数字  字符类型的数组
# 它能够容纳字符型  整型  浮点型等基本类型
arr1 = array.array('l', [2, 4, 6, 8, 10, 12])
print(type(arr1))
# <class 'array.array' >
print("打印新建数组: ", end="")

for i in range(0, 5):
    print(arr1[i], end=" ")


# 布尔索引是NumPy的重要特性之一  通常与Pandas一起使用  它的主要作用是过滤DataFrame中的数据
# 比如布尔值的掩码操作
dict = {'name': ['Smith', 'William', 'Phill', 'Parker'],
        'age': ['28', '39', '34', '36']}
info = pd.DataFrame(dict, index=[True, True, False, True])
print(info)
# 使用.loc访问索引为True的数据   返回所有为True的数据
print(info.loc[True])


# 重塑数组形状    变形操作可以通过reshape()函数实现
arr_arr = np.arange(16)
print("原数组: \n", arr_arr)
arr_arr = np.arange(16).reshape(2, 8)
print("\n变形后数组: \n", arr_arr)
arr_arr = np.arange(16).reshape(8, 2)
print("\n变形后数组: \n", arr_arr)


# 转换ndarray数组
# 在某些情况下  需要执行一些Numpy数值计算的高级函数  这个时候可以使用to_numpy()函数
# 将DataFrame对象转换为NumPy ndarray数组   并将其返回

infos = pd.DataFrame({'P': [2, 3], 'Q': [4.0, 5.8]})
# 给info添加R列
infos['R'] = pd.date_range('2020-12-23', periods=2)
print(infos)
# 将其转化为numpy数组
n = infos.to_numpy()
print(n)
print(type(n))
# [[2 4.0 Timestamp('2020-12-23 00:00:00')]
#  [3 5.8 Timestamp('2020-12-24 00:00:00')]]
# <class 'numpy.ndarray'>

info1 = pd.DataFrame([[17, 62, 35], [25, 36, 54], [42, 20, 15], [
                     48, 62, 76]], columns=['x', 'y', 'z'])
print('DataFrame \n-----------------------\n', info1)

arrs = info1.to_numpy()
print('\nNumpy Array\n-----------------------\n', arrs)
