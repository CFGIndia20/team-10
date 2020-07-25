from django.shortcuts import render
from .models import Status
import tweepy
from tweepy import API

# Create your views here.

def feed(request):
    stat = Status.objects.all()[:1].get()
    return render(request, 'feedback.html', {'stats': stat})

def res(request):
    userid = request.POST.get('uid', False)
    
    # assign the values accordingly 
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
    
    # 1284157038298140679
    # ID of the recipient 
    recipient_id = 753647504672129000
    
    # text to be sent 
    text = "This is a Direct Message."
    
    # sending the direct message 
    direct_message = api.send_direct_message(recipient_id, text) 
    
    # printing the text of the sent direct message 
    print(direct_message.message_create['message_data']['text']) 
    
    # API.send_direct_message(1284157038298140679, text['Your complaint has been registered'])
    desc = request.POST.get('desc', False)
    loct = request.POST.get('loct', False)
    stat = Status.objects.all()[:1].get()
    return render(request, 'result.html', {'status': stat.stat})