from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('complaints/',include("complaints.urls")),
    path('',include('account.urls',namespace='account')),
    path('',include('django.contrib.auth.urls')),
]
