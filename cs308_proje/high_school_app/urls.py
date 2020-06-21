from django.urls import path, include
from . import views
from cs308_proje.decorators import logintracker , login_check_required, user_type_check


login_url_pattern = [
    path('',views.highschoolloginpage, name='highschoolloginpage'),
    path('login/',views.high_school_login, name='highschool_login')    
]

urlpatterns = [
    path('register-highschool/', views.high_school_registration, name='highschool_register'),
    path('login-highschool/', views.high_school_login, name='highschool_login'),
    path('profile/', views.highschool_profile, name ='highschool_profile'),
    path('profile/edit/', views.highschool_edit_profile, name='edit_profile'),
    path('profile/editimage/', views.highschool_edit_image, name = 'edit_image')
]