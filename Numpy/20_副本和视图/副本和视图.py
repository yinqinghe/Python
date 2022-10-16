# 对numpy数组执行些函数操作时 其中一部分函数会返回数组的副本  而另一部分函数则返回数组的视图

# 其实从内存角度来说  副本就是对原数组进行深拷贝  新产生的副本与原数组具有不同的存储位置
# 而视图可理解为数组的引用  他和原数组有着相同的内存位置

from pprint import pprint
from re import A
import numpy as np
a = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])

# print("原数组： \n", a)
# print("a数组的ID  :", id(a))
# # a数组的ID: 2410726689456
# # 赋值操作是数组引用的一种方法  被赋值后的变量b与a组具有相同的内存id
# # 因此  无论操作a、b中哪个数组    另一个数组也会受到影响
# b = a
# print("数组B的ID: ", id(b))
# # 数组B的ID:  2410726689456
# b.shape = 4, 3
# print("b数组形状的更改也会反映到a数组上: \n", a)


# view()返回一个新生成的数组副本  因此对该数组的操作  不会影响到原数组
print("a数组的ID  :", id(a))
# a数组的ID: 2385577362992
b = a.view()
print("数组B的ID: ", id(b))
# 数组B的ID:  2385850982192
b.shape = 4, 3
print("原数组a： \n", a)
print("原数组b： \n", b)


# 使用切片可以创建视图数组  若要修改视图就会影响到原数组
arr = np.arange(10)
print('数组arr: \n', arr)

a = arr[3:]
b = arr[3:]
print(a, '\n', b)
a[1] = 123
b[2] = 234
# 切片修改arr原数组
print(arr)
# [  0   1   2   3 123 234   6   7   8   9]


# copy()该方法返回原数组的副本  对副本的修改不会影响到原数组

gg = np.array([[1, 2, 3, 4], [9, 0, 2, 3], [1, 2, 3, 19]])
print("原数组  \n", gg)
print("a数组ID:", id(gg))
# a数组ID: 2379662764432
hh = gg.copy()
print("b数组ID:", id(hh))
# b数组ID: 2379662764336
print("打印经过copy方法的b数组: \n", hh)
hh.shape = 4, 3
print("原数组  \n", gg)
print("经过copy方法的b数组: \n", hh)
