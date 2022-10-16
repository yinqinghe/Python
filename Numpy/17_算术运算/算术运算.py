import numpy as np
# Numpy数组的“加减乘除”算术运算，分别对应add(),subtract(),multiple(),divide()
# 做算术运算时，输入数组必须具有相同的形状，或者符合数组的广播规则，才可以执行运算
a = np.arange(9, dtype=np.float_).reshape(3, 3)
print(a)
# [[0. 1. 2.]
#  [3. 4. 5.]
#  [6. 7. 8.]]
b = np.array([10, 10, 10])
print(b)
# 数组加法运算
print(np.add(a, b))
# 数组减法运算
print(np.subtract(a, b))
# [[-10. - 9. - 8.]
#  [-7. - 6. - 5.]
#  [-4. - 3. - 2.]]
# 数组乘法运算
print(np.multiply(a, b))
# 数组除法运算
print(np.divide(a, b))
# [[0.  0.1 0.2]
#  [0.3 0.4 0.5]
#  [0.6 0.7 0.8]]

# reciprocal()该函数对数组中的每个元素取倒数，并以数组的形式将它们返回
# 当数组元素的数据类型为整数（int）时，对于绝对值小于1的元素，返回值为0
# 而当数组中包含0元素时，返回值将出现overflow（INF）溢出提示

# 此处注意有0
a_arr = np.array([0.25, 1.33, 1, 0, 100])
# 数组a默认为浮点类型数据
print(a_arr)
# 对数组a使用求倒数操作
print(np.reciprocal(a_arr))

b_arr = np.array([100], dtype=int)
# 数组b_arr的数据类型为整数int
print(b_arr)

print(np.reciprocal(b_arr))


a_power = np.array([10, 100, 1000])
# power()该函数将a数组中的元素作为底数，把b数组与a相对应的元素作幂，
# 最后一数组形式返回两者的计算结果
print('我们的数组是；')
print(np.power(a_power, 2))
# [100   10000 1000000]
b_power = np.array([1, 2, 3])
print(b_power)

print(np.power(a_power, b_power))
# [        10      10000 1000000000]

# mod()返回两个数组相对应位置上元素相除后的余数，它与numpy.remainder()的作用相同
a_mod = np.array([11, 22, 33])
b_mod = np.array([3, 5, 7])
# a与b相应位置的元素做除法
print(np.mod(a_mod, b_mod))
# [2 2 5]
# remainder方法一样
print(np.remainder(a_mod, b_mod))
# [2 2 5]


# Numpy提供了诸多处理复数类型数组的函数，主要有：
# 1.numpy.real()返回复数数组的实部
# 2.numpy.imag()返回复数数组的虚部
# 3.numpy.conj()通过更改虚部的符号，从而返回共  复数
# 4.numpy.angle()返回复数参数的角度，该函数的提供了一个deg参数
# 如果deg=True,则返回的值会以角度制来表示，否则以弧度制来表示

tt = np.array([-5.6j, 0.2j, 11., 1+1j])
print(tt)
# [-0.-5.6j  0.+0.2j 11.+0.j   1.+1.j]
print(np.real(tt))  # 返回实部
# [-0.  0. 11.  1.]
print(np.imag(tt))  # 返回虚部
# [-5.6  0.2  0.   1.]
print(np.conj(tt))
# [-0.+5.6j  0.-0.2j 11.-0.j   1.-1.j]
print(np.angle(tt))
# [-1.57079633  1.57079633  0. 0.78539816]
print(np.angle(tt, deg=True))
# [-90.  90.   0.  45.]
