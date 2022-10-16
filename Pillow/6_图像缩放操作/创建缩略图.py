
from PIL import Image

im = Image.open(r'D:\C#\VSCODE\python\Pillow\12_为图片添加水印\01.png')


# thumbnail(size,resample)
# resample  可选参数  指图像重采样滤波器  有四种过滤方式
# Image.BICUBIC(双立方插值法)
# Image.NEAREST(最近邻插值法)
# Image.BILINEAR(双线性插值法)
# Image.LANCZOS(下采样过滤插值法)

im.thumbnail((150, 50))

print('缩略图尺寸', im.size)
# 注意  缩略图的尺寸可能与你指定的尺寸不一致  这是一位Pillow会对原图像的场、宽进行等比例缩小
# 当指定的尺寸不符合图像的尺寸规格时  缩略图就会创建失败  比如指定的尺寸超出了原图像的尺寸规格

# 将缩略图保存至桌面
im.save(r'D:\C#\VSCODE\python\Pillow\6_图像缩放操作\03.png')
