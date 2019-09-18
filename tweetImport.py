#!/usr/bin/env python3

import twitter
# import csv      # Format things nicely
import re         # Clean up tweets (remove "RT", @(...), etc)

from datetime import datetime
import sys
import subprocess
import subprocess
from   os.path import isfile, sep, isdir
from   os      import makedirs, remove
# Debug
from time import sleep

class tweetImport():
    def __init__(self): 
        self.consumer_key        = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_consumer.token'
        self.consumer_secret     = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_consumer_secret.token'
        self.access_token        = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_access.token'
        self.access_token_secret = '/Users/JP-Macbook/Documents/ec601/miniproject01/tweet_disco/twitter_access_secret.token'

    def makeoutputfolder(self):
        datestr = datetime.now().strftime('%Y_%m_%d')
        timestr = datetime.now().strftime('%H_%M%S')
        if not isdir('output'):
            makedirs('output'); 
        curFolder = 'output' + sep + datestr
        if not isdir(curFolder):
            makedirs(curFolder)

        curFolder = curFolder + sep + self.user
        if not isdir(curFolder):
            makedirs(curFolder)
        else: 
            # This logic is useful if we are iterating over multiple tweets
            i = 1
            temp = curFolder
            while isdir(temp):
                temp = curFolder + '_' + str(i)
                i += 1; 
            makedirs(temp)
            curFolder  = temp; 
        self.curFolder = curFolder; 



    def analyzeUsername(self, username, since_id):
        self.user = username
        self.makeoutputfolder(); 

        for ids in since_id:
            print('The id being sent is: ' + str(ids))
            # Throw a try/catch here in case we give an invalid since-id
            api    = self.makeTwitterApi();
            tweets = self.analyzeUser(api, ids); 
            self.writeTweetData(tweets); 
            sleep(2)

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
                          consumer_secret     = self.getKeyFromTxt(self.consumer_secret),      \
                          access_token_key    = self.getKeyFromTxt(self.access_token),          \
                          access_token_secret = self.getKeyFromTxt(self.access_token_secret),    \
                          tweet_mode          = 'extended'                                    ) 
        return(api)


    def analyzeUser(self, api, since_id):
        usertoanalyze = self.user
        print('')
        print('The since_id is: ' + str(since_id))
        print('')
        tweets = api.GetUserTimeline(screen_name = usertoanalyze,             count  = 1000,      \
                                          include_rts     = False,         since_id  = since_id,       \
                                          max_id          = '', trim_user = False,    \
                                          exclude_replies = True
                                        )
        print(tweets)
        for dates in tweets.Created
        return tweets
    def writeTweetData(self, stringData):

        


        fName = self.curFolder + sep + 'tweetData_' + self.user + '.txt'
        fid = open(fName, 'w+')
        for s in stringData:
            text = s.full_text
            urlstrip = re.sub(r"http\S+", "", text) # Remove url
            atstrip  = re.sub('@\w*', "", urlstrip) # Remove mentions, this is questionable
            text = atstrip
            fid.write(text + '\n\n')
        fid.close();
