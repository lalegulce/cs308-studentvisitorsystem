from django.urls import path, include
from . import views


login_url_pattern = [
    path('',views.guide_login_page, name='guide_login_page'),
    path('login/',views.guide_login, name='guide_login')    
]

urlpatterns = [
    path('login-guide/',include(login_url_pattern)),
    path('logout/',views.guide_logout, name='guide_logout'),
    path('guide-profile/', views.guide_profile_page, name='guide_profile_page')
]
