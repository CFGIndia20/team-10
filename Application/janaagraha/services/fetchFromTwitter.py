import tweepy
import datetime
import json

# ACCESS_TOKEN = 'ACCESS_TOKEN'
# ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
# CONSUMER_KEY = 'CONSUMER_KEY'
# CONSUMER_SECRET = 'CONSUMER_SECRET'

def fetchComplaints():

    #timestamp of one hour less from now
    ts = datetime.datetime.utcnow() - datetime.timedelta(minutes=60)
    ts = ts.strftime("%Y-%m-%d %H:%M:%S")

    #authentication with twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

    #creating API object
    api = tweepy.API(auth)

    #fetching tweets containing complaints
    query = '#ichangemycitycomplaint'
    searched_tweets = []
    for status in tweepy.Cursor(api.search, q=query).items():
        data = json.dumps(status._json)
        searched_tweets.append(data) 
        created_at = json.loads(data)['created_at']
        created_at = datetime.datetime.strptime(created_at,"%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S")
        if created_at < ts:
            break
    
    #creating response
    response = []
    for tweet in searched_tweets:
        data = json.loads(tweet)
        response.append(data)

    return response



    


