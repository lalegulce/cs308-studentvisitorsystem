from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.signuprequest, name='universitysignup'),
    path('universitylogin/', views.unilogin, name ='unilogin'),
    path('universityprofile/', views.uniprofile, name ='uniprofile')
]
