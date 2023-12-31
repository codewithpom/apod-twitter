import requests
import tweepy
from datetime import datetime
import sys

token = sys.argv[1]
token_secret = sys.argv[2]
consumer_key = sys.argv[3]
consumer_secret = sys.argv[4]


# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)


# Create API object
api = tweepy.API(auth)


url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

data = requests.get(url).json()

quit() if data['media_type'] == "video" else print("It is not a video today !!!")

def download_file(url):
    extension = url.split(".")[-1]
    file_path = f"image.{extension}"
    content = requests.get(url).content
    with open(file_path, "wb") as file:
        file.write(content)
        file.close()
    
    return file_path


def make_tweet():
    client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=token,
                       access_token_secret=token_secret)
    hash_tag = "#astronomy #spaceshost #NASA #images"
    file_path = download_file(data['hdurl'])
    media = api.media_upload(file_path)
    client.create_tweet(text=f"Today's Astronomical Picture of the day\n{hash_tag}", media_ids=[media.media_id])

    
    print("Made POST !!!!!!!!")

make_tweet()




