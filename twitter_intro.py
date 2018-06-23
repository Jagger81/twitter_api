import json
import tweepy

from tweepy import OAuthHandler

CONSUMER_KEY = 'YTotqVnLO1VwR5OCn99UbvGdU'
CONSUMER_SECRET = 'h3hCb6hZ0FJ8tP5a4rIRRgehvcsw42n8b4NjSXXi7K2CryHW0D'
OAUTH_TOKEN = '17812083-h3CqJxJ7ppQaymwNNbONN4S2n7NXwX5L2pBsOjz0S'
OAUTH_TOKEN_SECRET= 'BZGUl8ZhqQDuXXU1oaOMvItuiWRWQQAIZsRceEe1Xhw4G'

auth = OAuthHandler( CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print(json.dumps(dub_trends, indent=1))

