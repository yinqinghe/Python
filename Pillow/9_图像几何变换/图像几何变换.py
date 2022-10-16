# 图像的几何变换主要包括图像翻转  图像旋转和图像变换操作

# transpose翻转操作

from PIL import Image

im = Image.open(r'D:\C#\VSCODE\python\image\pic\01.jpg')

# FLIP_LEFT_RIGHT:左右水平翻转
# FLIP_TOP_BOTTOM: 上下垂直翻转
# ROTAME_90:图像旋转90度
# ROTAME_180:图像旋转180度
# ROTAME_270:图像旋转270度
# TRANSPOSE:图像转置
# TRANSVERSE:图像横向翻转
# im_out = im.transpose(Image.FLIP_LEFT_RIGHT)
# im_out.show()

# im_out.save(r'D:\C#\VSCODE\python\Pillow\9_图像几何变换\transpose.jpg')


# rotate()任意角度旋转
# translate的参数值可以为负数  并将旋转图之外的区域填充为绿色
# im_out = im.rotate(45, translate=(0, -25), fillcolor='green')
# im_out.show()

# im_out.save(r'D:\C#\VSCODE\python\Pillow\9_图像几何变换\rotate.jpg')


# transform()图像变换
im_out = im.transform((250, 250), Image.EXTENT, data=[
                      0, 0, 30+im.width//4, im.height//3])

im_out.show()

im_out.save(r'D:\C#\VSCODE\python\Pillow\9_图像几何变换\transform.jpg')
