import tweepy
import time
import datetime
import schedule
import os
from dotenv import load_dotenv
load_dotenv()

bearer_token = os.environ['bearer_token']
api_key = os.environ['api_key']
api_secret = os.environ['api_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']

# Initialize Tweepy
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Get the current date and time
current_date = datetime.date.today()

# Format the date as a string
formatted_date = current_date.strftime("%B, %d, %Y")


def sendPost():
    # Send the tweet
    client.create_tweet(text=f"Hello Python 🐍. It is {formatted_date} today!🚀🚀.\nI am a bot 🤖. Meet me on Github https://github.com/Gerry-Aballa/twitter-Api-V2-bot")

    # Print a message to indicate that the request was successful
    print("Tweet posted successfully")

# Schedule the method to be exectued everday at a set time
# schedule.ever().day.at("8:00").do(sendPost)

# Main loop
while True:
    sendPost()
    # Checks if scheduler has pending tasks
    # schedule.run_pending()

    # Scheduler sleeps for 1 day
    # time.sleep(1)