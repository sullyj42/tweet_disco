#!/usr/bin/env python3

import twitter
# import csv      # Format things nicely
import re         # Clean up tweets (remove "RT", @(...), etc)


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
api = twitter.Api(consumer_key        = consumer_key,       \
                  consumer_secret     = consumer_secret,    \
                  access_token_key    = access_token,       \
                  access_token_secret = access_token_secret); 

# api = twitter.Api(consumer_key        = consumer_key, consumer_secret     = consumer_secret, access_token_key    = access_token,  access_token_secret = access_token_secret); 
print('')
print(api.VerifyCredentials())
print('')

usertoanalyze = 'Brabbott42';

tweets = api.GetUserTimeline(screen_name = usertoanalyze, count     = 200,   \
                             include_rts = False,         since_id  = '',   \
                             max_id      = '',            trim_user = True, \
                             exclude_replies = True \
                             )



for s in tweets:
    print(s.text)
    print('')
    print('')

#w = csv.writer(open("output_" + usertoanalyze + '.csv', "w"))
#for key, val in t.items():
#    w.writerow([key, val])