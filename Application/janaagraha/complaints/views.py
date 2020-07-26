from django.shortcuts import render,HttpResponse,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from services import fetchFromTwitter,location
# from . import classification
import json
from .models import Complaints
from .forms import ComplaintsForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
            data['location'] = location.return_location(data['text'])
            data['category_id'] = getCategory(data['text'])
            response.append(data)      
        return Response(response)

class categorization(APIView):
    def get(self, request, format=None):
        data={
            'category_id':getCategory(request.query_params.get('slug'))
        }
        return Response(data)


@method_decorator(login_required, name='dispatch')
class ComplaintsView(View):
    
    def get(self, request, *args, **kwargs):
        form = ComplaintsForm()
        return render(request,'complaints/complain.html',{'form':form})

    def post(self, request, *args, **kwargs):
        form = ComplaintsForm(request.POST)
        print(form)
        form.non_field_errors()
        field_errors = [ (field.label, field.errors) for field in form] 
        print(field_errors)
        if form.is_valid():
            print("enter")
            form = form.save(commit=False)
            form.categories = getCategory(form.Topic)
            form.user = request.user
            form.save()
            return HttpResponse('Success')
        return render(request,'complaints/complain.html',{'form':form})


def shareUrl(request,id):
    complain = get_object_or_404(Complaints,id=id)
    status = complain.statuses.all().order_by('-created').reverse()
    statobj = status[0]

    if statobj.stat == "resolved":
        return render(request,'complaints/feedback.html',{})
    else:
        data = {
            'Topic':complain.Topic,
            'categories':complain.categories,
            'location':complain.location
        }
        form = ComplaintsForm(initial=data)
        return render(request, 'feedback.html', {'form':form,'stats':status})


import pickle
import numpy as np
from sklearn.svm import LinearSVC

def getCategory(text):
    modelling = LinearSVC()
    filename = 'C:\\Users\\Smit\\Documents\\GitHub\\team-10\\Application\\janaagraha\\complaints\\classify.pkl'
    with open(filename, 'rb') as f:
        modelling.clf = pickle.load(f)
    filename1 = 'C:\\Users\\Smit\\Documents\\GitHub\\team-10\\Application\\janaagraha\\complaints\\tfidf_pre.pkl'
    with open(filename1, 'rb') as f:
        modelling.vectorizer = pickle.load(f)
    print(modelling)
    resp = modelling.clf.predict(modelling.vectorizer.transform([text]))
    return resp
    

