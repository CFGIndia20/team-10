from django.urls import path
from .views import TwitterComplaints
urlpatterns = [
    path('twitter/',TwitterComplaints.as_view(),name = "twitter-api")
]
