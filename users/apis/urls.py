from django.urls import path
from .views import RegisterAPIView, LoginAPIView,RegisterView,LoginView

urlpatterns = [
    path('register/',RegisterView.as_view(), name='user-register'),
    path('login/',LoginView.as_view(), name='user-login'),
    path('register/apis',RegisterAPIView.as_view(), name='user-registerapi'),
    path('login/apis',LoginAPIView.as_view(), name='userloginapi'),
]
