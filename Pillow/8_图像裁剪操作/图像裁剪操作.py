

# 图像裁剪操作

from PIL import Image

im = Image.open(r'D:\C#\VSCODE\python\image\pic\01.jpg')
box = (0, 0, 500, 500)
im_crop = im.crop(box)
# im_crop.show()


# 图像拷贝和粘贴
im_copy = im.copy()
im_crop = im_copy.crop((0, 0, 200, 100))

# 创建一个新的图像作为蒙版  L模式   单颜色值
image_new = Image.new('L', (200, 100), 200)

# 将裁剪后的副本粘贴至副本图像上  并添加蒙版  mask为图片添加蒙版效果
im_copy.paste(im_crop, (100, 100, 300, 200), mask=image_new)

im_copy.show()
