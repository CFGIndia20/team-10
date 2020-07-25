from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from services import fetchFromTwitter
import json
# Create your views here
class TwitterComplaints(APIView):
    def get(self, request, format=None):
        complaints = fetchFromTwitter.fetchComplaints()
        response = []
        for comp in complaints:
            data = {}
            data['created_at'] = comp['created_at']
            data['text'] = comp['text']
            data['user_id'] = comp['user']['id']
            data['retweet_count'] = comp['retweet_count']
            data['favorite_count'] = comp['favorite_count']
            if "extended_entities" in comp:
                if "media" in comp["extended_entities"]:
                    data['media_url'] = comp['extended_entities']['media'][0]['media_url']
            else :
                data['media_url'] = None
            response.append(data)
        return Response(response)
    

