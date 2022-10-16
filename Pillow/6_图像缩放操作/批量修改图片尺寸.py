

from fileinput import filename
import os
from PIL import Image

fileName = os.listdir(r'D:\C#\VSCODE\python\image\pic')

print(filename)

width = 350
height = 350

if not os.path.exists(r'D:\C#\VSCODE\python\image\pic2'):
    os.mkdir(r'D:\C#\VSCODE\python\image\pic2')

for img in fileName:
    old_pic = Image.open(r'D:\C#\VSCODE\python\image\pic/'+img)
    new_image = old_pic.resize((width, height), Image.BILINEAR)
    print(new_image)

    new_image.save(r'D:\C#\VSCODE\python\image\pic2/'+img)
