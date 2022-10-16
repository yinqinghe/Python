import numpy as np
arr = np.empty((3, 2), dtype=int)
print(arr)
print(arr.itemsize)


a = np.zeros(6)
print(a)
b = np.zeros(6, dtype="complex64")
print(b)

# 自定义的数据类型创建数组
c = np.zeros((3, 3), dtype=[('x', 'i4'), ('y', 'i4')])
print(c)
# [[(0, 0)(0, 0)(0, 0)]
#  [(0, 0)(0, 0)(0, 0)]
#  [(0, 0)(0, 0)(0, 0)]]

cc = np.zeros((3, 3))
print(cc)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

ccc = np.zeros((3, 3), dtype=int)
print(ccc)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]
arr1 = np.ones((3, 2), dtype=int)
print(arr1)
# [[1 1]
#  [1 1]
#  [1 1]]

# 将一个普通列表转换成numpy.ndarray类型
l = [1, 2, 3, 4, 5, 6, 7]
print(type(l))
a = np.asarray(l)
print(type(a))
print(a)
# <class 'list' >
# <class 'numpy.ndarray' >
# [1 2 3 4 5 6 7]
# 将一个普通元祖转换成numpy.ndarray类型
ll = (1, 2, 3, 4, 5, 6, 7)
print(type(ll))
aa = np.asarray(ll)
print(type(aa))
print(aa)
# <class 'tuple' >
# <class 'numpy.ndarray' >
# [1 2 3 4 5 6 7]


# 嵌套列表创建多维数组
lll = [[1, 2, 3, 4, 5, 6, 7], [8, 9]]
print(type(lll))
aaa = np.asarray(lll, dtype=object)
print(type(aaa))
print(aaa)


# 使用指定的缓冲区创建数组
llll = b'hello world'
print(type(llll))
aaaa = np.frombuffer(llll, dtype="S1")
print(aaaa)
print(type(aaaa))
# <class 'bytes'>
# [b'h' b'e' b'l' b'l' b'o' b' ' b'w' b'o' b'r' b'l' b'd']
# <class 'numpy.ndarray'>

# 该方法可以把迭代对象转换为ndarray数组，其返回值是一个一维数组
# 使用range函数创建列表对象
list = range(6)
print(list)
# 生成可迭代对象i
i = iter(list)
# 使用i迭代器，通过fromiter方法创建ndarray
array = np.fromiter(i, dtype=float)
print(array)
