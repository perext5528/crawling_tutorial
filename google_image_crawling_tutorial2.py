from google_images_download import google_images_download
#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":u"cat,kittens","limit":1,"print_urls":True}
paths = response.download(arguments)
#print complete paths to the downloaded images
print(paths)