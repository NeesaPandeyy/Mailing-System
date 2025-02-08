from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('compose/', views.compose, name='compose'),
]   