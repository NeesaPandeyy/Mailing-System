from django.urls import path,include

urlpatterns = [
    path('',include('users.apis.urls')),
]
