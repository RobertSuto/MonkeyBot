import os
import random
import tweepy

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords": "monkey",
             "limit": 6, "print_urls": False}
paths = response.download(arguments)

path = random.choice(os.listdir("downloads/monkey"))
path2 = "downloads/monkey/"+path
API_KEY = ''
API_SECRET = ''
ACCES_TOKEN = ''
ACCES_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCES_TOKEN, ACCES_TOKEN_SECRET)

api = tweepy.API(auth)


def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids=[media.media_id_string])


upload_media('mnonkey' , path2)

folder = 'downloads/monkey'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)

