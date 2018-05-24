import tweepy, json 

# Consumer keys and access tokens, used for OAuth
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)



# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status

'''print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))'''

cricTweet = tweepy.Cursor(api.search, q='Mo salah').items(10)

for tweet in cricTweet:
    print (tweet.created_at, tweet.text, tweet.lang)