from django.urls import path, include
from . import views
from cs308_proje.decorators import user_type_check


urlpatterns = [
    path('login_individual', views.individual_login, name='individuallogin'),
    path('register_individual/', views.individual_registration, name='individualregistration'),
    path('profile/', views.individual_edit, name='individualedit'),
]