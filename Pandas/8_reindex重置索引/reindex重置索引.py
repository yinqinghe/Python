from os import rename
import pandas as pd
import numpy as np
N = 20
df = pd.DataFrame({'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
                   'x': np.linspace(0, stop=N-1, num=N),
                   'y': np.random.rand(N),
                   'C': np.random.choice(['low', 'Medium', 'High'], N).tolist(),
                   'D': np.random.normal(100, 10, size=(N)).tolist()})
# 重置行、列索引标签
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print(df_reindexed)
#            A     C   B
# 0 2016-01-01   low NaN
# 2 2016-01-03  High NaN
# 5 2016-01-06   low NaN

# 如果想让a的行索引与b相同  可以使用reindex_like()方法
a = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
b = pd.DataFrame(np.random.randn(2, 3), columns=['col1', 'col2', 'col3'])
# 使df2和df1行标签相同
bb = b.reindex_like(a)
print(bb)
#         col1      col2      col3
# 0  0.221579 - 1.062870  0.576998
# 1 - 1.683853  1.047728  1.467943
# 2       NaN       NaN       NaN
# 3       NaN       NaN       NaN
# 4       NaN       NaN       NaN
# 5       NaN       NaN       NaN

# 向前填充
print(b.reindex_like(a, method='ffill'))
#        col1      col2      col3
# 0 -0.490670  0.082455  0.212921
# 1  1.189147  0.684883  0.165854
# 2 -2.233542 -0.484595 -0.847544
# 3  1.201940 -0.737309  0.898093
# 4  0.810703 -0.194798 -0.208768
# 5 -0.427316 -0.251596  0.223938
# 6 -0.540622  0.386336  1.031348
# 限制填充行数
# 提供了一个额外参数limit  该参数用来控制填充的最大行数
print(b.reindex_like(a, method="ffill", limit=2))

# 重命名标签
# rename()方法允许你使用某些映射(dict series)或任意函数 来对行、列标签重新命名
print(a.rename(columns={'col1': 'c1', 'col2': 'c2'},
      index={0: 'apple', 1: 'banana', 2: 'durian'}))
#               c1        c2      col3
# apple   0.781167  0.330946  1.946078
# banana -0.971585  0.367913 -1.687204
# durian -0.986285 -0.219709  0.856333
# 3       1.968184  1.710638  0.038831
# 4       1.669267  0.147883 -0.354979
# 5       0.528437  0.121950 -0.822681

# rename()方法提供了一个inplace参数  默认值为False  表示拷贝一份原数据  并在复制后的数据做重命名操作
# 若inplace=True  则表示在原数据的基础上重命名
