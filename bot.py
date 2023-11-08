import tweepy
import os
from dotenv import load_dotenv
load_dotenv()


bearer_token = os.environ['BEARER_TOKEN']
twitter_api_key = os.environ['TWITTER_API_KEY']
api_secret = os.environ['API_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']

auth = tweepy.OAuthHandler(twitter_api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


def CreatePost():
    api.update_status("Hello? This post was made by a bot.")


while True:
    CreatePost()
    print("Tweet posted successfully")

