# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (100, 30), color = 'blue')

d = ImageDraw.Draw(img)
d.text((22, 10), "안녕", font=ImageFont.truetype("font.ttf", 48), fill=(255, 255, 255))
img.save('pillow_temp/pil_blue_text32.png')
