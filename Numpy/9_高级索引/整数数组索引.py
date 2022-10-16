'''
Author: 殷清贺 987746808@qq.com
Date: 2022-10-05 16:43:22
LastEditors: 殷清贺 987746808@qq.com
LastEditTime: 2022-10-05 16:45:13
FilePath: \python\Numpy\高级索引\整数数组索引.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
# 创建二维数组
x = np.array([[1, 2], [3, 4], [5, 6]])

y = x[[0, 1, 2], [0, 1, 0]]


print(y)
# [1 4 5]
