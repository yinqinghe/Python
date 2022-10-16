

from PIL import Image

im = Image.open(r'D:\C#\VSCODE\python\image\pic\03.jpg')
print(im.format, '   ', im.mode, '  ', im.info)

# 注意  并非所有的图片格式都可以用save()方法转换完成  PNG格式的图片保存为JPG格式
# 直接使用save()方法就会出现错误

# PNG是四通道RGBA模式  即红色、绿色、蓝色、Alpha透明色
# JPG是三通道RGB模式
image = im.convert('RGBA')
image.save(r'D:\C#\VSCODE\python\image\pic\33.png')
im1 = Image.open(r'D:\C#\VSCODE\python\image\pic\33.png')
print(im1.format, '   ', im1.mode, '   ', im1.info)
