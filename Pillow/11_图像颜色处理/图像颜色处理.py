

from PIL import Image, ImageColor

color1 = ImageColor.getrgb('blue')
print(color1)
color2 = ImageColor.getrgb('#DCDCDC')
print(color2)
color3 = ImageColor.getrgb('HSL(0,100%,50%)')
print(color3)


im = Image.new('RGB', (200, 200), ImageColor.getrgb('#EEB4B4'))
# im.show()

# getcolor()与getrgb()类似  同样用来获取颜色值  它多了一个mode参数
# 因此该函数可以获取指定色彩模式的颜色值
color4 = ImageColor.getcolor('#EEA9B8', 'L')
print(color4)
color5 = ImageColor.getcolor('yellow', 'RGBA')
print(color5)
