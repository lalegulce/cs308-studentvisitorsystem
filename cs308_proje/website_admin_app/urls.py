from django.urls import path, include
from . import views

extra_login_patterns = [
    path('', views.system_login, name='login'),
    path('login-check/', views.login_check, name='login_check'),
]


urlpatterns = [
    path('admin-login/', include(extra_login_patterns)),
    path('admin-logout/', views.system_logout, name='logout'),
    path('', views.admin_page, name='admin_page'),
    path('request-result/', views.result_handler, name='result_handler'),
]
