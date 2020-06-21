from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, timedelta, date
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from .models import HighSchoolAppointment, IndividualAppointment, HighSchoolAppointmentRequest, IndividualAppointmentRequest
from .utils import Calendar
from .forms import HighSchoolAppointmentForm, IndividualAppointmentForm, HighSchoolAppointmentRequestForm, IndividualAppointmentRequestForm, NewIndividualAppointmentRequestForm, NewHighSchoolAppointmentRequestForm
from cs308_proje.decorators import logintracker , login_check_required
from django.contrib import messages
from django.forms import TextInput
from django.forms import modelform_factory

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = HighSchoolAppointment or IndividualAppointment
    template_name = 'appointment_app/calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)  
        d = get_date(self.request.GET.get('month', None))
        appointment = Calendar(d.year, d.month)
        html_appointment = appointment.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_appointment)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['user'] = logintracker()
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def appointment(request, appointment_id=None):
    user = logintracker()

    if appointment_id:
        if user.Object.user_type == "highschool": 
            instance = get_object_or_404(HighSchoolAppointment, pk=appointment_id)
            form = HighSchoolAppointmentForm(request.POST or None, instance=instance)
        elif user.Object.user_type == "individual":
            instance = get_object_or_404(IndividualAppointment, pk=appointment_id)
            form = IndividualAppointmentForm(request.POST or None, instance=instance)
        
    if request.POST and form.is_valid():
        if 'make' == request.POST.get('action'):
            newObject = form.save(commit=False)
            if user.Object.user_type == "highschool":
                newObject.school = user.Object
            elif user.Object.user_type == "individual":
                newObject.individual = user.Object
            newObject.save()
        elif 'delete' == request.POST.get('action'):
            if user.Object.user_type == "highschool":
                instance = HighSchoolAppointment.objects.filter(school=user.Object)
            elif user.Object.user_type == "individual":
                instance = IndividualAppointment.objects.filter(individual=user.Object)   
            instance.delete()
        return HttpResponseRedirect(reverse('appointment_app:calendar'))
    return render(request, 'appointment_app/appointment.html', {'form': form, 'check': True, 'id': appointment_id})

def appointmentRequest(request, appointment_id=None):
    user = logintracker()
    buttonVisible = True

    if appointment_id:
        if user.Object.user_type == "highschool": 
            instance = get_object_or_404(HighSchoolAppointmentRequest, pk=appointment_id)
            form = HighSchoolAppointmentRequestForm(request.POST or None, instance=instance)
        elif user.Object.user_type == "individual":
            instance = get_object_or_404(IndividualAppointmentRequest, pk=appointment_id)
            form = IndividualAppointmentRequestForm(request.POST or None, instance=instance)
    else:
        if user.Object.user_type == "highschool":
            form = NewHighSchoolAppointmentRequestForm(request.POST or None)
        elif user.Object.user_type == "individual":
            form = NewIndividualAppointmentRequestForm(request.POST or None)
        buttonVisible = False
        
    if request.POST and form.is_valid():
        if 'make' == request.POST.get('action'):
            newObject = form.save(commit=False)
            if user.Object.user_type == "highschool":
                newObject.school = user.Object
            elif user.Object.user_type == "individual":
                newObject.individual = user.Object
            newObject.save()
        elif 'delete' == request.POST.get('action'):
            if user.Object.user_type == "highschool":
                instance = HighSchoolAppointmentRequest.objects.filter(school=user.Object)
            elif user.Object.user_type == "individual":
                instance = IndividualAppointmentRequest.objects.filter(individual=user.Object)   
            instance.delete()
        return HttpResponseRedirect(reverse('appointment_app:calendar'))
    return render(request, 'appointment_app/appointment.html', {'form': form, 'check': buttonVisible, 'id': appointment_id})

def login(request):
    val = "Have to login first!!"
    messages.info(request, val)
    return render(request, 'appointment_app/loginredirect.html')


def pendingappointments(request):
    user = logintracker()
    if user.Object.user_type == "highschool":
        instance = HighSchoolAppointmentRequest.objects.filter(school=user.Object)
    elif user.Object.user_type == "individual":
        instance = IndividualAppointmentRequest.objects.filter(individual=user.Object)   
    
    return render(request, 'appointment_app/pendingappointments.html', {'list': instance})