# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:31:50 2018

@author: Hany
"""

from textblob import TextBlob

import tweepy
import re
import time

#Auth Keys
#Deleted Check the messanger

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)	


itemsCount = 5
tweets = tweepy.Cursor(api.search, q="#SALAH_Dont_Cry").items(itemsCount)


listTweets = []
while True:
    try:
        tweet = tweets.next().text
        
        match = re.search('#.*',tweet)
        newTweet = tweet.replace(match.group(),"")
        match = re.search('\\n',tweet)
        newTweet2 = newTweet.replace(match.group()," ")
        listTweets.append(newTweet2)
#        print(tweet)
#        match = re.search(r'(#.*)|(\n)',tweet)
#        print(match)
#        newTweet = tweet.replace(match.group()," ")
#        listTweets.append(newTweet)
        

    except tweepy.TweepError:
        time.sleep(60 * 15)
        print("Error: ",tweepy.TweepError)
        continue
    except StopIteration:
        break



#print(listTweets)
allText = ". ".join(listTweets)
blob = TextBlob(allText)
#print(blob.tags)
#print(blob.sentences)
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