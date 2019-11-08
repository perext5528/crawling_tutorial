import six, os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

credential_path = "temp191107-e51d2e83b360.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

text = '세계 최초 5G 스마트폰의 타이틀을 가진 갤럭시S10 모델 중 LTE 모델에 세일 딱지가 붙었다.'
text2 = '지난 9월 부산의 한 아파트에서 불이 났습니다.'

client = language.LanguageServiceClient()

if isinstance(text2, six.binary_type):
    text2 = text2.decode('utf-8')

# Instantiates a plain text2 document.
document = types.Document(content=text2, type=enums.Document.Type.PLAIN_TEXT)

# Detects entities in the document. You can also analyze HTML with:
#   document.type == enums.Document.Type.HTML
entities = client.analyze_entities(document).entities

for entity in entities:
    entity_type = enums.Entity.Type(entity.type)
    print('=' * 20)
    print(u'{:<16}: {}'.format('name', entity.name))
    print(u'{:<16}: {}'.format('type', entity_type.name))
    print(u'{:<16}: {}'.format('salience', entity.salience))


for i in range(0,2):
    print(u'{}'.format(entities[i].name))