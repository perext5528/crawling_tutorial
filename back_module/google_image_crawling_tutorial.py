# -*- coding:utf-8 -*-
import six, os
from google.cloud import language
from google.cloud.language import enums, types
from google_images_download import google_images_download
from PIL import Image, ImageDraw, ImageFont, ExifTags
from datetime import datetime


now = datetime.now().strftime('%Y%m%draw%H%M%S')

##### Extract keywords #####

# User Authentication
credential_path = "temp191107-e51d2e83b360.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates Client
client = language.LanguageServiceClient()

# Instantiates downloader
response = google_images_download.googleimagesdownload()

# Analysing Entities in Text
# text = '맛있다.'
#text = '세계 최초 5G 스마트폰의 타이틀을 가진 갤럭시S10 모델 중 LTE 모델에 세일 딱지가 붙었다.'
text2 = '지난 9월 부산의 한 아파트에서 불이 났습니다.'
text3 = '카카오는 올해 3분기 연결 기준 매출 7832억원, 영업이익 591억원을 각각 기록했다고 7일 공시했다.'
text = '고양이는 정말 귀엽습니다.'

# Preprocessing: Encoding
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

# Instantiates a plain text document.
document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

# Detects entities in the document
entities = client.analyze_entities(document).entities

# Set query
search_queries = []

# Split entity case
entity_num = 0
for entity in entities:
    entity_num += 1
if entity_num == 0:
    print("Keyword None\n Exit")
    exit()
elif entity_num == 1:
    search_queries.append(entities[0].name)
else:
    for i in range(0, 2):
        search_queries.append(entities[i].name)


# print(search_queries)

##### Google image downloader #####
def download_images(query):
    # Set arguments
    arguments = {
        "keywords": query,
        "limit": 1,
        "print_urls": True,
        "size": "medium",
        "output_directory": "temp",
        "no_directory": True,

    }
    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 1,
                     "print_urls": True,
                     "size": "medium"
                     }
        try:
            response.download(arguments)
        except:
            pass
for query in search_queries:
    download_images(query)
    print()

# Image rename
i = 0

for filename in os.listdir("temp"):
    #dst = now + "_" + str(i) + ".jpg"
    dst = str(i) + ".jpg"
    src = 'temp/' + filename
    dst = 'temp/' + dst
    os.rename(src, dst)
    i += 1


# os.rmdir("temp/")

##### Image edit #####

# Image open
base_image = Image.open('temp/')

# resizing
base_image.thumbnail((500, 500), Image.ANTIALIAS)

width, height = base_image.size

# Text draw
draw = ImageDraw.Draw(base_image)
draw.rectangle((0, 250, width, height), fill='black')
draw.text((20, height*0.82), text, font=ImageFont.truetype("tmon.ttf", 30), fill=(255, 255, 255))

base_image.save('pillow_temp/' + now + '.jpg')
