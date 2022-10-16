# 图像的分离与合并  指的就是图像颜色的分离与合并


from PIL import Image
im = Image.open(r'D:\C#\VSCODE\python\Pillow\12_为图片添加水印\01.png')

image = im.resize((400, 400), Image.NEAREST)

# image.save(r'D:\C#\VSCODE\python\Pillow\7_图像分离与合并\01.png')

# 由于是png  分离颜色通道  产生三个Image对象
r, g, b, a = image.split()

# a.show()
r.show()
# g.show()
# b.show()

# 重新组合颜色通道  返回先的Image对象
image_merge = Image.merge('RGBA', (r, g, b, a))

# image_merge.show()


# image_merge.save(r'D:\C#\VSCODE\python\Pillow\7_图像分离与合并\02.png')
