from django.urls import path, include
from django.conf.urls import url
from cs308_proje.decorators import login_check_required, logintracker
from . import views

app_name = 'appointment_app'
user = logintracker()
urlpatterns = [
    url(r'^loginpage/$', views.login, name="appLogin"),
    url(r'^calendar/$', login_check_required(views.CalendarView.as_view()),  name='calendar'),
    url(r'^appointment/new/$', views.appointmentRequest, name='appointment_new'),
    url(r'^appointment/edit/(?P<appointment_id>\d+)/$', views.appointment, name='appointment_edit'),
    url(r'^appointment/editRequest/(?P<appointment_id>\d+)/$', views.appointmentRequest, name='appointment_edit_request'),
    url(r'^pendingappointments/$', views.pendingappointments, name='pending_appointments'),
]