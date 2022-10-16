import numpy as np
# 表示在指定的数值区间内，返回均匀间隔的一维等差数组
a = np.linspace(1, 19, 10)
print(a)
b = np.linspace(1, 21, 10, endpoint=False)
print(b)

arr = np.linspace(10, 20, 5)
print("数组数值范围：", arr)

x = np.linspace(1, 2, 5, retstep=True)  # restep表示生成的数组中会显示公差，反之不显示

print(x)

# 该函数返回一个ndarray数组，它用于创建等比数组
a_log = np.logspace(1.0, 2.0, num=10)
print(a_log)
b_log = np.logspace(1, 5, num=5, base=10)
print(b_log)
