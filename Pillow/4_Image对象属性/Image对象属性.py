from PIL import Image

im = Image.open(r'../pillow/ss.jpg')
print(im)

print(f'宽是{im.width}  高度{im.height}')

print('图像的大小size：', im.size)

# 查看图像格式
print('图像的格式：', im.format)

# 查看图片是否为只读
print('图像是否为只读: ', im.readonly)

# 查看图片相关信息
print('图像信息', im.info)

# 图像模式
print('图像模式信息: ', im.mode)
