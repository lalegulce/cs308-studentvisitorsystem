from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from .tables import UniversityRequestTable, HighSchoolRequestTable, IndividualRequestTable
from .models import UniversityRequest, HighSchoolRequest, IndividualRequest
from .database_handler import university_database_handler, high_school_database_handler, individual_database_handler
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
import pprint
# Create your views here.


def system_login(request):
    login_form = AuthenticationForm()
    return render(request, 'website_admin_app/admin_login.html', {'login_form': login_form})


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        val = "Login Successful!"
    else:
        val = "Login Failed"

    messages.info(request, val)
    return redirect("http://127.0.0.1:8000/website-admin/")


@login_required(login_url='admin-login/')
def system_logout(request):
    logout(request)
    return HttpResponseRedirect("http://127.0.0.1:8000/website-admin/admin-login/")


@login_required(login_url='admin-login/')
def admin_page(request):
    uni_data = UniversityRequest.objects.all()
    uni_table = UniversityRequestTable(uni_data)
    RequestConfig(request).configure(uni_table)
    school_data = HighSchoolRequest.objects.all()
    school_table = HighSchoolRequestTable(school_data)
    RequestConfig(request).configure(school_table)
    individual_data = IndividualRequest.objects.all()
    individual_table = IndividualRequestTable(individual_data)
    RequestConfig(request).configure(individual_table)
    return render(request, 'website_admin_app/admin.html', {'university_request_table': uni_table, 'high_school_request_table': school_table, 'individual_request_table': individual_table})


@login_required(login_url='admin-login/')
def result_handler(request):
    if 'accept-selected-universities' in request.POST:
        for uni_name in request.POST.getlist('to_change'):
            university_database_handler(uni_name, True)
    elif 'reject-selected-universities' in request.POST:
        for uni_name in request.POST.getlist('to_change'):
            university_database_handler(uni_name, False)
    elif 'accept-selected-schools' in request.POST:
        for school_name in request.POST.getlist('to_change'):
            high_school_database_handler(school_name, True)
    elif 'reject-selected-schools' in request.POST:
        for school_name in request.POST.getlist('to_change'):
            high_school_database_handler(school_name, False)
    elif 'accept-selected-individuals' in request.POST:
        for ind_name in request.POST.getlist('to_change'):
            individual_database_handler(ind_name, True)
    elif 'reject-selected-individuals' in request.POST:
        for ind_name in request.POST.getlist('to_change'):
            individual_database_handler(ind_name, False)

    return redirect("http://127.0.0.1:8000/website-admin/")
