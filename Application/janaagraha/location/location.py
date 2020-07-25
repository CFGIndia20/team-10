from geopy.geocoders import Nominatim
import tweepy
import json


def return_location(tweet):
    #Split the text into individual words
    split_tweet = tweet.split()
    pos = -1
    #Finding position of the word "location"
    for word in split_tweet:
        if word=="location":
            pos = split_tweet.index("location")
            break
    location = ""
    #Join the location part together
    if pos!=-1:
        for j in range(pos+1, len(split_tweet)):
            location+=" "+split_tweet[j]
        geolocator = Nominatim(user_agent="Janaagraha")
        print(location)
        locator = geolocator.geocode(location)
        return locator.latitude, locator.longitude
    #If location is not available
    else:
        return (0,0)

def store_location():
    responses = fetchComplaints() #From fetchfromTwitter
    locations_track = list()
    #Get latitute, longitude, and user id for each response
    for i in range(len(responses)):
        area = return_location(responses[i]['text'])
        uid = responses[i]['id']
        locations_track.append((uid,area))
    return locations_track



