# 两张图片合并 要求两张图片的模式、图像大小必须要保持一致  否则不能合并

from PIL import Image
im_1 = Image.open(r'D:\C#\VSCODE\python\image\pic1\11.png')
im_2 = Image.open(r'D:\C#\VSCODE\python\image\pic1\22.png')


image = im_2.resize(im_1.size)

r1, g1, b1, a1 = im_1.split()
r2, g2, b2, a2 = image.split()

# 合并图片需要图片格式一致  图片大小一致
# 合并图像
im_3 = Image.merge('RGB', [r2, g1, b2])

im_3.show()

# im_3.save(r'D:\C#\VSCODE\python\image\pic1\12.png')

# 混合rgba模式的图像
# alpha表示透明度   取值范围为0到1  当取值为0时  输出图像相当于im_1的拷贝
# 而取值为1时  则是im_2的拷贝   只有当取值为0.5时  才为两个图像的中合
Image.blend(im_1, im_2, 0.5).save(r'D:\C#\VSCODE\python\image\pic1\blend.png')
