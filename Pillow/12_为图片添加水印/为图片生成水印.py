
from PIL import Image, ImageDraw, ImageFont
# 创建Image对象  当做背景图
im = Image.new('RGB', (200, 200), color='gray')
# 创建ImageDraw对象
draw = ImageDraw.Draw(im)

# 以左上角为原点  绘制矩形  元祖坐标序列表示矩形的位置  大小
# fill设置填充色  outline设置边框线为黑色
# draw.rectangle((50, 100, 100, 150), fill=(255, 0, 0), outline=(0, 0, 0))

# ImageFont模块通过加载不同格式的字体文件  在图像上绘制不同类型的文字
# 比如TrueType和OpenType类型的字体

# 加载计算机本地字体文件
font = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc', size=30)

# 在原图像上添加文本   xy()图像左上角为坐标原点   (x,y)表示添加文本的起始坐标位置
draw.text(xy=(80, 50), text='语言中文网', fill=(255, 0, 0), font=font)
im.show()

im.save(r'D:\C#\VSCODE\python\Pillow\12_为图片添加水印\01.png')
