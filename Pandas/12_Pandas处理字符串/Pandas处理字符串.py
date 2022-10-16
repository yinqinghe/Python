from cgi import print_arguments
import pandas as pd
import numpy as np
s = pd.Series(['C', ' Python', 'java', 'go', np.nan, ' 1125', 'javascript'])
print(s.str.lower)

print(s.str.len())
# 0     1.0
# 1     6.0
# 2     4.0
# 3     2.0
# 4     NaN
# 5     4.0
# 6    10.0
# dtype: float64

print(s.str.strip())
# 0             C
# 1        Python
# 2          java
# 3            go
# 4           NaN
# 5          1125
# 6    javascript
# dtype: object

print(s.str.split(" "))

# 会自动忽略NaN
print(s.str.cat(sep="_"))
# C_ Python_java_go_ 1125_javascript

# 返回一个带有独热编码值的DataFrame结构
print(s.str.get_dummies())

# 检查Series中的每个字符  如果字符中包含空格  则返回True  否则返回False
print(s.str.contains(" "))
# 0    False
# 1     True
# 2    False
# 3    False
# 4      NaN
# 5     True
# 6    False
# dtype: object

print(s.str.repeat(3))
# 0                               CCC
# 1              Python Python Python
# 2                      javajavajava
# 3                            gogogo
# 4                               NaN
# 5                    1125 1125 1125
# 6    javascriptjavascriptjavascript
# dtype: object

# 若以指定的“j"开头则返回True
print(s.str.startswith("j"))

# 如果返回-1表示该字符串没有出现指定的字符
print(s.str.find("j"))

print(s.str.findall("j"))

# 交换大小写
print(s.str.swapcase())

# 返回一个布尔值  用来判断是否存在数字型字符串
print(s.str.isnumeric())
