# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:31:50 2018

@author: Hany
"""

from textblob import TextBlob
import tweepy
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def cleanTweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9])|(#.*)|(\w+:\/\/\S+)", " ", tweet).split())

def extractTweets(tweets):
    return(list(tweet for tweet in tweets))
    
def analysisTweet(tweet):
    res = TextBlob(tweet).sentences[0].sentiment.polarity
    if(res > 0):    
        return res,1
    elif(res < 0):
        return res,-1
    return res,0

def createDataFrame(tweetsList):
    return pd.DataFrame({"Tweets":[i[2].text for i in tweetsList],
                   "date":[i[2].created_at.date() for i in tweetsList],
                   "analysis":[i[1] for i in tweetsList]
                   })
def plotSettings():
    plt.yticks(np.arange(-1, 2, 1.0))
#Auth Keys
#Deleted Check the messanger fro security issues


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)	


itemsCount = 10
tweets = tweepy.Cursor(api.search, q="#SALAH_Dont_Cry",lang="en").items(itemsCount)


#Extract Tweets
listTweetsObj = extractTweets(tweets)


tweetsResult = []
for i in listTweetsObj:
    result = analysisTweet(cleanTweet(i.text))
    tweetsResult.append((result[0],result[1],i))


df = createDataFrame(tweetsResult)

plotSettings()
plt.scatter(df['date'].tolist(),df['analysis'])
plt.show()


