from django.urls import path,reverse_lazy
from .views import dashboard, register
app_name = 'account'

urlpatterns = [
    path('dashboard/',dashboard,name='dashboard'),
    path('register/',register,name='register'),
]
