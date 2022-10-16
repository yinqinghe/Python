# Pillow总是以灰度模式(L)  或调色板模式(P)  来读取GIF文件

import os
import random
from PIL import Image

# 可以将静态格式图片(png、JPG)合成为GIF动态图


def png_to_fig(png_path, gif_name):

    frames = []

    png_files = os.listdir(png_path)

    print(png_files)

    for frame_id in range(1, len(png_files)+1):
        frame = Image.open(os.path.join(png_path, png_files[frame_id-1]))
        frames.append(frame)
# 以第一张图片作为开始  将后续5张图片合并成 GIF动态图

# save_all  保存图像  transparency 设置透明背景色  duration 单位毫秒  动画持续时间
# loop=0  无限循环  disposal=2  恢复原背景颜色  参数详细说明  请参阅官方文档
    frames[0].save(gif_name, save_all=True, append_images=frames[1:],
                   transparency=0, duration=200, loop=0, disposal=2)


png_to_fig(r'D:\C#\VSCODE\python\image\pic',
           r'D:\C#\VSCODE\python\image\pic\t.gif')
