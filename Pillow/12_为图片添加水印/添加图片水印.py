

from cgi import print_arguments
from PIL import Image, ImageFont, ImageDraw

font = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc', size=100)


def creating_watermark(im, text, font=font):
    # 给水印添加透明度   因此需要转换图片的格式
    im_rgba = im.convert('RGBA')
    im_text_canvas = Image.new('RGBA', im_rgba.size, (255, 255, 255, 0))
    print(im_rgba.size[0])
    draw = ImageDraw.Draw(im_text_canvas)

    # 设置文本文字大小
    text_x_width, text_y_height = draw.textsize(text, font=font)
    print(text_x_width, text_y_height)

    text_xy = (im_rgba.size[0]-text_x_width, im_rgba.size[1]-text_y_height)

    print(text_xy)
    # 设置文本颜色(绿色)和透明度(半透明)
    draw.text(text_xy, text, font=font, fill=(100, 255, 100, 255))

    # 将原图片与文字复合
    im_text = Image.alpha_composite(im_rgba, im_text_canvas)

    return im_text


image = Image.open(r'D:\C#\VSCODE\python\02.png')

image.show()

image_water = creating_watermark(image, '语言中文网')

image_water.show()
image_water.save(r'D:\C#\VSCODE\python\Pillow\12_为图片添加水印\01.png')
