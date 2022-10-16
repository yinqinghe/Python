

from PIL import Image

im = Image.open(r'D:\C#\VSCODE\python\Pillow\12_为图片添加水印\01.png')
print(im.size)
try:
    # 放大图片
    # image = im.resize((550, 260))

    # 对局部位置进行放大  box  对指定图片区域进行缩放  (左,上,右,下)
    image = im.resize((1080, 1080), resample=Image.LANCZOS,
                      box=(300, 380, 820, 780))

    image.save(r'D:\C#\VSCODE\python\Pillow\6_图像缩放操作\02.png')
    print('查看新图像的尺寸 ', image.size)
except:
    print('放大图像失败')
