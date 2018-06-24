import json
import tweepy

from tweepy import OAuthHandler

'inser consumer keys here

auth = OAuthHandler( CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
NY_WOE_ID = 2459115

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
NY_trends = api.trends_place(NY_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])
                    
lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])

NY_trends_set = set([trend['name']
                    for trend in NY_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set, NY_trends_set)

print(common_trends)
