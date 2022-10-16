from PIL import Image

import numpy as np

# 创建 300*400的图像  3个颜色通道
# array = np.zeros([300, 400, 3], dtype=np.uint8)

# array[:, :200] = [255, 0, 0]
# array[:, 200:] = [255, 255, 0]
# img = Image.fromarray(array)

# img.show()

# img.save('数组生成图像.png')


img = Image.open('../pillow/ss.jpg')
img.show()
# Image图像转换为ndarray数组
img_2 = np.array(img)
print(img_2)
# ndarray转换为Image图像
arr_img = Image.fromarray(img_2)

arr_img.show()

arr_img.save(r'D:\C#\VSCODE\python\02.png')
