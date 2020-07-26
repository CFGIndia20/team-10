from django.urls import path
from .views import TwitterComplaints, ComplaintsView, shareUrl, categorization

app_name = 'complaints'
urlpatterns = [
    path('twitter/',TwitterComplaints.as_view(),name = "twitter-api"),
    path('categorization/',categorization.as_view(),name = "categorization"),
    path('addcomplain/',ComplaintsView.as_view(),name="add-complain"),
    path('Complainstatus/<id>/',shareUrl, name='shareurl')
]
