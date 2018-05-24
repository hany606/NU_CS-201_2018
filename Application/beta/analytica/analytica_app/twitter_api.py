import tweepy
from django.conf import settings

#Authentication Process
auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def search_by_hashtag(q, limit=100):
    q = '#'+q.replace(' ', '_')
    tweets = tweepy.Cursor(api.search, q=q, tweet_mode='extended').items(limit)
    return tweets
