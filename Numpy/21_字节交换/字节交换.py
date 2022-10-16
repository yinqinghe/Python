# 数据以字节的形式存储在计算机内存中  而存储规则可分为两类   即小端字节序与大端字节序
# 小端字节序  表示低位字节排放在内存的低地址端  高位字节排放在高地址段  它与大端字节序恰好相反
from audioop import byteswap
import numpy as np
a = np.array([1, 256, 8755], dtype=np.int16)

print(a)
# 以十六进制形式表示内存中的数据
print(map(hex, a))
# <map object at 0x0000022E7226D400 >

# byteswap()该函数将数组中每个元素的字节顺序进行大小端调换
print(a.byteswap(True))
# [256     1 13090]
print(map(hex, a))
# <map object at 0x0000022E7226D130>
