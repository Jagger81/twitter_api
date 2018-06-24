import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter


CONSUMER_KEY = 'YTotqVnLO1VwR5OCn99UbvGdU'
CONSUMER_SECRET = 'h3hCb6hZ0FJ8tP5a4rIRRgehvcsw42n8b4NjSXXi7K2CryHW0D'
OAUTH_TOKEN = '17812083-h3CqJxJ7ppQaymwNNbONN4S2n7NXwX5L2pBsOjz0S'
OAUTH_TOKEN_SECRET= 'BZGUl8ZhqQDuXXU1oaOMvItuiWRWQQAIZsRceEe1Xhw4G'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 150
query = 'Ireland'

# get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10  # the min amount of times a status is retweeted to gain entry to our list
# reset this value to suit your own tastes

pop_tweets = [status for status in results if status._json['retweet_count'] > min_retweets]

# create a list of tweet tuples associating each tweet's text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r'  # align the columns
print(table)