# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ExifTags
from datetime import datetime

h = Image.open('pillow_temp/hodu.jpg')
h.show()

# resizing
base_img = Image.open('pillow_temp/nero.jpg')


resize_img = base_img.resize((500, 500), Image.LANCZOS)
thumb_img = base_img.thumbnail((500,500), Image.ANTIALIAS)
#base_img.show()

img = Image.new('RGB', (500, 500), color='#82B1F6')

d = ImageDraw.Draw(img)

text_background = ""

# text(xy, text, fill=글자색상, font
d.text((20, 350), "안녕하세요, 고양이는 정말 귀엽습니다.", font=ImageFont.truetype("tmon.ttf", 50), fill=(255, 255, 255))
d.text((20, 420), "안녕하세요, 고양이는 정말 귀엽습니다.", font=ImageFont.truetype("tmon.ttf", 50), fill=(255, 255, 255))
# filename
now = datetime.now().strftime('%Y%m%d%H%M%S')
# img.save('pillow_temp/'+now+'.png')

#resize_img.rotate(270).show()

base_img.thumbnail((1000,1000), Image.ANTIALIAS)

#base_img.save('pillow_temp/'+now+'.png')
#resize_img.save('pillow_temp/' + now + '.png')
