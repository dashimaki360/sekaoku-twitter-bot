import tweepy
from pylab import *
from networkx import *
import time

# set tweeter key from ENV
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

tweets = api.search(q='"#SEKAINOOKUDA"', lang='ja', result_type='recent',count=12)
ids = []

for tweet in tweets:
    id = tweet.user.id
    screen_name = tweet.user.screen_name
