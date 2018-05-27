# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:31:50 2018

@author: Hany
"""

from textblob import TextBlob
import tweepy
import re
import pandas as pd

def cleanTweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9])|(#.*)|(\w+:\/\/\S+)", " ", tweet).split())

#Auth Keys
#Deleted Check the messanger



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)	


itemsCount = 10
tweets = tweepy.Cursor(api.search, q="#SALAH_Dont_Cry",lang="en").items(itemsCount)


#Extract Tweets
listTweetsObj = [tweet for tweet in tweets]
listTweetsTxt = [cleanTweet(tweet.text) for tweet in listTweetsObj]

tweetsResult = []

for i in listTweetsTxt:
    blob = TextBlob(i)
    res = blob.sentences[0].sentiment.polarity
    resVal = 0
    if(res > 0):    
        resVal = 1
    elif(res < 0):
        resVal = -1

    tweetsResult.append((res,resVal,i))
    

df = pd.DataFrame({"Tweets":listTweetsTxt,
                   "date":[i.created_at for i in listTweetsObj],
                   "analysis":[i[1] for i in tweetsResult]
                   })
print(df.head(5))
