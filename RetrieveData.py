import tweepy
import requests
import json
import csv
import time

# Twitter API credentials
consumer_key = '12345'
consumer_secret = '12345'
access_token = '123'
access_token_secret = '123'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)

# If we want to update data, use poll function

# # User ID of the Twitter user to track
# user_id = '123456789'


# # Initial number of followers
# initial_followers = api.get_user(user_id).followers_count

# # Polling interval in seconds
# interval = 60

# while True:
#     # Wait for the specified interval
#     time.sleep(interval)

#     # Get the current number of followers
#     current_followers = api.get_user(user_id).followers_count

#     # Check for changes
#     if current_followers != initial_followers:
#         # Update the initial number of followers
#         initial_followers = current_followers

#         # Do something with the updated information
#         print(f'Number of followers has changed to {current_followers}!')

# Screen name of the user to retrieve tweets for
screen_name = 'IntelCapital'

# Send request to tweets api
tweets = tweepy.Cursor(api.user_timeline, screen_name=screen_name, tweet_mode='extended').items()

# Open a CSV file for writing
with open('tweets.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write a header row to the CSV file
    writer.writerow(['created_at', 'full_text', 'retweet_count', 'favorite_count'])

    # Use a Cursor object to get the 100 most recent tweets
    tweets = tweepy.Cursor(api.user_timeline, screen_name=screen_name, tweet_mode='extended').items(100)

    # Loop through the tweets and write the desired information to the CSV file
    for tweet in tweets:
        created_at = tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
        full_text = tweet.full_text.replace('\n', ' ').replace('\r', '')
        retweet_count = tweet.retweet_count
        favorite_count = tweet.favorite_count

        writer.writerow([created_at, full_text, retweet_count, favorite_count])





