from pydoc import describe
import pandas as pd
# get_option()该函数接受单一参数  用来获取显示上限的行数或者列数
print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_columns"))
# 60
# 0
# 由此可知  默认值显示上限是(60,20)

# set_option()该函数用来更改要默认显示的行数和列数   修改默认行数
pd.set_option("display.max_rows", 70)
print(pd.get_option("display.max_rows"))
# 70

# 修改默认列数
pd.set_option("display.max_columns", 40)
print(pd.get_option("display.max_columns"))
# 40


# reset_option()该方法接受一个参数  并将修改后的设置回默认值
pd.reset_option("display.max_rows")
print(pd.get_option("display.max_rows"))
# 60

# describe_option()该方法输出参数的描述信息
print(pd.describe_option("display.max_rows"))

# option_context()上下文管理器  用于临时设置with语句块中的默认显示参数  当你退出with语句块时 参数值会自动恢复
with pd.option_context("display.max_rows", 10):

    print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_rows"))
# 当第一个Print语句打印option_context()设置的临时值   当退出with语句块时  第二个Print语句打印解释器默认值
