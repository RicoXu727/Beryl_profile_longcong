import tweepy
import requests
import json
import csv
import time
# https://towardsdatascience.com/twitter-json-data-processing-3f353a5deac4
# https://www.sciencedirect.com/science/article/pii/S2405918817300247
# https://www.google.com/search?q=clean+twitter+api+data+of+profile+into+relevant+data+table&rlz=1C5MACD_enUS1021US1023&ei=nFIOZN6cFYaq5NoPpIetuAY&ved=0ahUKEwje2qjguNf9AhUGFVkFHaRDC2cQ4dUDCBA&uact=5&oq=clean+twitter+api+data+of+profile+into+relevant+data+table&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEMgUIABCiBDIHCAAQHhCiBDIFCAAQogQ6BAgAEEdKBAhBGABQ7gVYjDNgqEdoAHABeAKAAdIDiAGKF5IBCTQuMS4yLjMuMpgBAKABAcgBCMABAQ&sclient=gws-wiz-serp#fpstate=ive&vld=cid:9f109127,vid:1gQ6uG5Ujiw

# Twitter API credentials
consumer_key = 'CiEoUCdhGHUHBJhSswR41wB3N'
consumer_secret = 'vwa9jCOPAptT27vCM2inqvQ1MkZRTwWvZbctzFarXBemeRQslK'
access_token = '1357785878819659780-jFC0pjxMTCZEpEXM7hoBBXBDo5uGsM'
access_token_secret = 'A6BKFyezJXsZnzMO6VwEBaHDqewzsAZfDMiAVGI8ayQyL'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)



# Send request to tweets api
screen_name = 'intelcapital'
tweets = tweepy.Cursor(api.user_timeline, screen_name=screen_name, tweet_mode='extended').items(100)

with open('ICtweet.json', 'a') as f:
    for tweet in tweets:
        json.dump(tweet._json, f)
        f.write('\n')


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



