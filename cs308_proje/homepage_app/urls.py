from django.urls import path, include
from . import views
from cs308_proje.decorators import user_type_check

urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('search-university/', views.search_university, name='search_university'),
    path('loginhomepage/', views.loginhomepage, name='loginhomepage'),
    path('profile/', user_type_check(views), name='profilepageredirect'),
    path('logout/', views.logout, name='userlogout')
]
