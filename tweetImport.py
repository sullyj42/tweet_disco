#!/usr/bin/env python3

import twitter
# import csv      # Format things nicely
import re         # Clean up tweets (remove "RT", @(...), etc)

from datetime import datetime
import sys
import subprocess
import subprocess
from   os.path import isfile

class tweetImport():
    def __init__(self): 
        self.consumer_key        = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_consumer.token'
        self.consumer_secret     = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_consumer_secret.token'
        self.access_token        = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_access.token'
        self.access_token_secret = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_access_secret.token'

    def analyzeUsername(self, username):
        print('This is working')
        self.user = username
        api    = self.makeTwitterApi();
        tweets = self.analyzeUser(api); 
        self.writeTweetData(tweets); 

    def getKeyFromTxt(self, fName):
        if isfile(fName):
            fid = open(fName, 'r')
            key = fid.readline(); 
            fid.close(); 
            return(key)
        else:
            print('\nWas the key entered as a string?\n')
            return(fName)

    def makeTwitterApi(self):

        api = twitter.Api(consumer_key        = self.getKeyFromTxt(self.consumer_key),        \
                          consumer_secret     = self.getKeyFromTxt(self.consumer_secret),     \
                          access_token_key    = self.getKeyFromTxt(self.access_token),        \
                          access_token_secret = self.getKeyFromTxt(self.access_token_secret), \
                          tweet_mode          = 'extended') 
        return(api)


    def analyzeUser(self, api):
        usertoanalyze = self.user
        tweets = api.GetUserTimeline(screen_name = usertoanalyze, count     = 200,    \
                                          include_rts = False,         since_id  = '',    \
                                          max_id      = '',            trim_user = False, \
                                          exclude_replies = True                          \
                                        )
        return tweets
    def writeTweetData(self, stringData):
        timestr = datetime.now().strftime('%Y_%m_%d_%H%M')
        fName = 'tweetData_' + self.user + '_' + timestr + '.txt'
        fid = open(fName, 'w')
        for s in stringData:
            text = s.full_text
            urlstrip = re.sub(r"http\S+", "", text) # Remove url
            atstrip  = re.sub('@\w*', "", urlstrip) # Remove mentions, this is questionable
            text = atstrip
            fid.write(text + '\n\n')
        fid.close();
