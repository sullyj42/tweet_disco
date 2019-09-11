#!/usr/bin/env python3

import twitter
# import csv      # Format things nicely
import re         # Clean up tweets (remove "RT", @(...), etc)

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import sys
import subprocess
import subprocess
#path = "/Users/JP-Macbook/Documents/ec601/miniproject01/" +\
#       "tweet_disco/My First Project-a3003cd7fced.json"

# addGoogs = 'export GOOGLE_APPLICATION_CREDENTIALS="'+ path + '"'
# addGoogs = 'export GOOGLE_APPLICATION_CREDENTIALS="/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/My_First_Project_a3003cd7fced.json"'
#print('')
#print(addGoogs)
#print('')
#subprocess.run([addGoogs])
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

from time import sleep # Debugging

credentials = GoogleCredentials.get_application_default()

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
# print('')
# print('Consumer Key:        ' + consumer_key)
# print('Consumer Secret:     ' + consumer_secret)
# print('Access Token:        ' + access_token)
# print('Access Token Secret: ' + access_token_secret)
# print('')
api = twitter.Api(consumer_key        = consumer_key,        \
                  consumer_secret     = consumer_secret,     \
                  access_token_key    = access_token,        \
                  access_token_secret = access_token_secret, \
                  tweet_mode          = 'extended'           # Ugh wasted an hour on this
                  ); 

# api = twitter.Api(consumer_key        = consumer_key, consumer_secret     = consumer_secret, access_token_key    = access_token,  access_token_secret = access_token_secret); 
# print('')
# print(api.VerifyCredentials())
# print('')

usertoanalyze = 'Brabbott42';


'''
tweets = api.GetUserTimeline(screen_name = usertoanalyze, count     = 10,   \
                             include_rts = False,         since_id  = '',   \
                             max_id      = '',            trim_user = False, \
                             exclude_replies = True,      tweet_mode= 'extended' \
                             )
'''
tweets = api.GetUserTimeline(screen_name = usertoanalyze, count     = 200,    \
                             include_rts = False,         since_id  = '',    \
                             max_id      = '',            trim_user = False, \
                             exclude_replies = True                          \
                             )
fid = open('tweets_' + usertoanalyze + '.txt', 'w')
for s in tweets:
    text = s.full_text

    urlstrip = re.sub(r"http\S+", "", text) # Remove url
    atstrip  = re.sub('@\w*', "", urlstrip) # Remove mentions, this is questionable



    # How do emojis and hashtags effect google NLP? 
    #   I don't think we want to remove these
    # emojistrip   = 
    # hashtagstrip = 
    text = atstrip

    fid.write(text + '\n\n')

fid.close();

client = language.LanguageServiceClient()

# The text to analyze

with open('tweets_' + usertoanalyze + '.txt', 'r') as file:
    data = file.read().replace('\n', '')
# print(data)
#text = u('Some text goes here') # u converts a string to unicode 
text = str(data) # I think this is unecessary in python3
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
