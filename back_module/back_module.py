
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_queries = [
    'samsung',
    u'삼성',
]


def download_images(query):
    arguments = {
        "keywords": query,
        "format": "png",
        "limit": 1,
        "print_urls": True,
        "size": "medium",
        "aspect_ratio": "panoramic"
    }

    try:
        response.download(arguments)

    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 4,
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
