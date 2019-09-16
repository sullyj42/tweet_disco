#!/usr/bin/env python3

import twitter
# import csv      # Format things nicely
import re         # Clean up tweets (remove "RT", @(...), etc)

from datetime import datetime
import sys
import subprocess
import subprocess
from os.path import isfile

class tweetImport():
    def __init__(self, user, fName_consumer_key, fName_consumer_secret, \
                             fName_access_token, fName_access_token_secret): 
        self.user = user
        self.consumer_key        = fName_consumer_key
        self.consumer_secret     = fName_consumer_secret
        self.access_token        = fName_access_token
        self.access_token_secret = fName_access_token_secret


    def getKeyFromTxt(fName):
        if isfile(fName):
            fid = open(fName, 'r')
            key = fid.readline(); 
            fid.close(); 
            return(key)
        else:
            print('\nWas the key entered as a string?\n')
            return(fName)

    def makeTwitterApi(self):

        api = twitter.Api(consumer_key        = getKeyFromTxt(self.consumer_key),        \
                          consumer_secret     = getKeyFromTxt(self.consumer_secret),     \
                          access_token_key    = getKeyFromTxt(self.access_token),        \
                          access_token_secret = getKeyFromTxt(self.access_token_secret), \
                          tweet_mode          = 'extended') 

    def analyzeUser(self):
        usertoanalyze = self.user
        tweets = api.GetUserTimeline(screen_name = usertoanalyze, count     = 200,    \
                                     include_rts = False,         since_id  = '',    \
                                     max_id      = '',            trim_user = False, \
                                     exclude_replies = True                          \
                                     )
    def writeTweetData(self):
        timestr = datetime.now().strftime('%Y_%m_%d_%H%M')
        fName = 'tweetData_' + self.user + '_' + timestr + '.txt'
        fid = fopen(fName)
        for s in tweets:
            text = s.full_text
            urlstrip = re.sub(r"http\S+", "", text) # Remove url
            atstrip  = re.sub('@\w*', "", urlstrip) # Remove mentions, this is questionable
            text = atstrip
            fid.write(text + '\n\n')
        fid.close();
