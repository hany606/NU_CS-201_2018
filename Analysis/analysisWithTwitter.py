# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:31:50 2018

@author: Hany
"""

from textblob import TextBlob

import tweepy
import re
import time


def cleanTweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9])|(#.*)|(\w+:\/\/\S+)", " ", tweet).split())

#Auth Keys
#Deleted Check the messanger


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)	


itemsCount = 10
tweets = tweepy.Cursor(api.search, q="#SALAH_Dont_Cry",lang="en").items(itemsCount)


listTweets = []
while True:
    try:
        tweet = tweets.next().text
        print(cleanTweet(tweet))
        listTweets.append(cleanTweet(tweet))
        
    except tweepy.TweepError:
        time.sleep(60 * 15)
        print("Error: ",tweepy.TweepError)
        continue
    except StopIteration:
        break



allText = ". ".join(listTweets)
blob = TextBlob(allText)

tweetsResult = []
for sentence in blob.sentences:
    res = sentence.sentiment.polarity
    if(res > 0):    
        tweetsResult.append((res,1,str(sentence)))
    elif(res < 0):
        tweetsResult.append((res,-1,str(sentence)))
    else:
        tweetsResult.append((res,0,str(sentence)))

print(tweetsResult)


