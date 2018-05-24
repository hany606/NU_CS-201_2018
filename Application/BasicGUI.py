# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:30:22 2018

@author: CSTEAM
"""

#importing libraries
import tkinter
import tweepy  #to commmunicate with twitter api
from time import sleep



#Auth Keys
###############################################
#Access tokens is deleted 
###############################################

#Authuntication Process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Customize the Query
#extended mode for long tweets
limit = 5
tweets = tweepy.Cursor(api.search, q="#CSP1Test",tweet_mode='extended').items(limit)
counter = 1

top = tkinter.Tk()

text = tkinter.Text(top)

while True:
    try:
        tweet = tweets.next()
        text.insert(tkinter.INSERT,"Tweet #{:d}:\n{:s}\n-----------------------------\n".format(counter,tweet.full_text))
        print("Tweet #{:d}:\n{:s}\n-----------------------------\n".format(counter,tweet.full_text))
        counter += 1
        # Insert into db
    except tweepy.TweepError:
        sleep(60 * 15)
        print("Error: ",tweepy.TweepError)
        continue
    except StopIteration:
        break



text.pack()
top.mainloop()