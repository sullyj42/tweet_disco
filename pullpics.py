#!/usr/bin/env python3

import twitter

fid = open('twitter_consumer.token', 'r'); 
consumer_key = fid.readline(); 
fid.close(); 

fid = open('twitter_consumer_secret.token', 'r'); 
consumer_secret = fid.readline(); 
fid.close(); 

fid = open('twitter_access.token', 'r'); 
access_token = fid.readline(); 
fid.close(); 

fid = open('twitter_access_secret.token', 'r'); 
access_token_secret = fid.readline(); 
fid.close(); 
print('')
print('Consumer Key:        ' + consumer_key)
print('Consumer Secret:     ' + consumer_secret)
print('Access Token:        ' + access_token)
print('Access Token Secret: ' + access_token_secret)
print('')
# api = twitter.Api(consumer_key        = consumer_key,       \
#                   consumer_secret     = consumer_secret,    \
#                   access_token_key    = access_token,       \
#                   access_token_secret = access_token_secret); 

api = twitter.Api(consumer_key        = consumer_key, consumer_secret     = consumer_secret, access_token_key    = access_token,  access_token_secret = access_token_secret); 
print('')
print(api.VerifyCredentials())
print('')

# usertoanalyze = 'Brabbott42';

# t = api.GetUserTimeline(screen_name=usertoanalyze, count=10)

# tweets = [i.AsDict() for i in t]

# for t in tweets:
#     print(t['id'], t['text'])
