# Pillow提供了两种创建Image实例对象的方法

from operator import mod
from PIL import Image
# 可以创建一个Image对象
# im=Image.open('')


# new()方法可以创建一个新的Image对象   size是图像的大小  color图片的颜色 参数值支持(R,G,B)三元组数字格式
# 、颜色的十六进制值以及颜色英文单词
im1 = Image.new(mode='RGB', size=(260, 100), color='#ff0000')
im1.show()
