# 图像降噪操作  就是使用不同的滤波器来处理图像从而实现图像的平滑、锐化、边界增强

# 图像降噪通过某些算法来构造滤波器是图像降噪的主要方式
from PIL import Image, ImageFilter

im = Image.open(r'D:\C#\VSCODE\python\image\pic\01.jpg')

# 图像模糊处理
# im_blur = im.filter(ImageFilter.BLUR)
# im_blur.show()
# im_blur.save(r'D:\C#\VSCODE\python\Pillow\10_图像降噪处理\blur.jpg')

# 轮廓图
# im2 = im.filter(ImageFilter.CONTOUR)
# im2.show()
# im2.save(r'D:\C#\VSCODE\python\Pillow\10_图像降噪处理\contour.jpg')

# 边缘检测
# im3 = im.filter(ImageFilter.FIND_EDGES)
# im3.show()
# im3.save(r'D:\C#\VSCODE\python\Pillow\10_图像降噪处理\边缘检测.jpg')

# 浮雕图
# im4 = im.filter(ImageFilter.EMBOSS)
# im4.show()
# im4.save(r'D:\C#\VSCODE\python\Pillow\10_图像降噪处理\浮雕图.jpg')


# 平滑图像
im5 = im.filter(ImageFilter.SMOOTH)
im5.show()
im5.save(r'D:\C#\VSCODE\python\Pillow\10_图像降噪处理\平滑图像.jpg')
