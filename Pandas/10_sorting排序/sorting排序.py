# Pandas 提供了两种排序方法  分别是按标签排序和按数值排序
import pandas as pd
import numpy as np
unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[
                           1, 6, 4, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
print(unsorted_df)
#        col2      col1
# 1 -0.355594 -0.308201
# 6  0.393410 -1.543614
# 4  0.192292 -0.044944
# 2  1.731349  1.135649
# 3  1.348194 -0.783658
# 5  1.831924  0.124542
# 9  0.914955 -0.991147
# 8  0.175869  1.208269
# 0 -0.573710 -0.310749
# 7  0.504884 -1.676071
# 上述事例  行标签和数值元素均未排序  下面分别使用标签排序  数值排序对其进行操作

# 按标签排序
# 使用sort_index()方法对行标签排序  指定轴参数(axis)或者排序顺序
sorted_df = unsorted_df.sort_index()
print(sorted_df)
#        col2      col1
# 0 - 0.605657 - 0.616540
# 1 - 1.376781 - 1.190373
# 2 - 2.236370 - 0.529089
# 3 - 0.118507 - 1.625682
# 4 - 0.886624 - 1.830348
# 5 - 1.382624 - 0.553449
# 6  1.268932  1.771279
# 7  0.427188  1.039658
# 8  0.432776  0.086684
# 9  0.598348  1.306913

# 通过将布尔值传递给ascending参数  可以控制排序的顺序
sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)

# 按列标签排序
sorted_df = unsorted_df.sort_index(axis=1)
print(sorted_df)

# 按值排序
sorted_df = unsorted_df.sort_values(by='col1')
print(sorted_df)

# 当col1列排序时  相应的col2列的元素值和行索引也会随col1一起改变  by参数可以接受一个列表参数值
sorted_df = unsorted_df.sort_values(by=['col1', 'col2'])
print('\n', sorted_df)

# 排序算法
# sort_values() 提供了参数 kind 用来指定排序算法  这里有三种排序算法
# mergesort
# heapsort
# quicksort
# 默认为quicksort(快速排序)  其中Mergesort归并排序是最稳定的算法
sorted_df = unsorted_df.sort_values(by='col1', kind='mergesort')
print(sorted_df)
