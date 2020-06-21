"""cs308_proje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('homepage_app.urls'), name='homepage_app'),
    path('admin/', admin.site.urls),
    #path('calendar/', include('calendar_app.urls'),name='calendar_app'),
    path('high_school/', include('high_school_app.urls'), name='high_school_app'),
    path('university_app/', include('university_app.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('appointment_app/', include('appointment_app.urls')),
    path('website-admin/', include('website_admin_app.urls'), name='website_admin_app'),
    path('university_app/', include('university_app.urls')),
    path('highschool_app/', include('high_school_app.urls')),
    path('individual_app/', include('individual_app.urls')),
    path('guide/', include('guide_app.urls')),
]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)