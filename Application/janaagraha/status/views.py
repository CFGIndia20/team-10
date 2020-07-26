from django.shortcuts import render
from .models import Status
import tweepy
from tweepy import API
from tweepy import OAuthHandler
import json

# Create your views here.

def feed(request):
    stat = Status.objects.all()[:1].get()
    return render(request, 'feedback.html', {'stats': stat})

def res(request):
    userid = request.POST.get('uid', False)
    
    # assign the values accordingly 
    # consumer_key = "DCwomfDjMvo1y82MPJmQQCpcT" 
    # consumer_secret = "jyJJwBAn3rPtXFdPYptDSeh3WX9slmn4qOf0DQonzzaV6OoRgj" 
    # access_token = "1094274318979219456-n9LNBeNluDK3CodJRqqDJYli7a7gK3" 
    # access_token_secret = "T7QYu8r0Ok764TLiPBIVB5WBBVlVyq7bkqJTwIV7VEDdG6kG0J" 
    
    # # authorization of consumer key and consumer secret 
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
    # # set access to user's access key and access secret  
    # auth.set_access_token(access_token, access_token_secret) 
    
    # # calling the api  
    # api = tweepy.API(auth) 
    
    # # 1284157038298140679 753647504672129000
    # # ID of the recipient 
    # recipient_id = 799489430482460673
    
    # # text to be sent 
    # text = "Hey Smit this is Aditya"
    
    # # sending the direct message 
    # direct_message = api.send_direct_message(recipient_id, text) 
    
    # # printing the text of the sent direct message 
    # print(direct_message.message_create['message_data']['text']) 


    consumer_key = "DCwomfDjMvo1y82MPJmQQCpcT"
    consumer_secret = "T7QYu8r0Ok764TLiPBIVB5WBBVlVyq7bkqJTwIV7VEDdG6kG0J"
    access_token = "1094274318979219456-n9LNBeNluDK3CodJRqqDJYli7a7gK3"
    access_token_secret = ""

    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # set access to user's access key and access secret
    auth.set_access_token(access_token, access_token_secret)

    # calling the api
    api = tweepy.API(auth)

    query = '#ichangemycitycomplaint'
    searched_tweets = []

    for status in tweepy.Cursor(api.search, q=query).items(1):
        data = json.dumps(status._json)
        searched_tweets.append(data)

    # creating response
    response = []
    for tweet in searched_tweets:
        data = json.loads(tweet)
        response.append(data)

    tweet_id = response[0]['id']
    user = response[0]['user']
    api.update_status('world', tweet_id)
    # API.send_direct_message(1284157038298140679, text['Your complaint has been registered'])
    
    desc = request.POST.get('desc', False)
    loct = request.POST.get('loct', False)
    stat = Status.objects.all()[:1].get()
    return render(request, 'result.html', {'status': stat.stat})