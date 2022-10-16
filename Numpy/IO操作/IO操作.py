# NumPy IO操作是以文件的形式从磁盘中加载ndarray对象
# NumPy可以两种文件类型处理ndarray对象
# 一类是二进制文件  （以.npy结尾）  另一类是普通文本文件


import numpy as np

# 二进制文件保存方法   load()   save()
# 普通文本文件保存方法 loadtxt()  savetxt()


a = np.array([1, 2, 3, 4, 5])
# np.save('first', a)

b = np.load('first.npy')
print(b)

np.savetxt('second.txt', a)
bb = np.loadtxt('second.txt')
print(b)
