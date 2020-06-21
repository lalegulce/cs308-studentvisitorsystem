from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignupRequestForm, UniLoginForm, UniUpdateForm
from website_admin_app.models import UniversityRequest
from university_app.models import UniversityAdmin, University
from django.db import IntegrityError, DataError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from cs308_proje.decorators import logintracker, login_check_required
# Create your views here.


def signuprequest(request):

    if request.method == 'POST':
        form = SignupRequestForm(request.POST)

        if form.is_valid():
            university_name = form.cleaned_data['university_name']
            university_address = form.cleaned_data['university_address']
            university_faculties = form.cleaned_data['university_faculties']
            university_mail = form.cleaned_data['university_mail']
            university_contact_number = form.cleaned_data['university_contact_number']
            school_type = 'university'
            try:
                UniversityRequest.objects.create(university_name=university_name, university_address=university_address,
                                             university_faculties=university_faculties, university_mail=university_mail, university_contact_number=university_contact_number, school_type = school_type)
                val = "University request has been sent."
            except IntegrityError:
                val = "University already exits. Registration failed."
            messages.info(request,val)

            return redirect('http://127.0.0.1:8000/')
    else:
        form = SignupRequestForm()

    return render(request, 'university_app/signupform.html', {'signupform': form})

def unilogin(request):
    if request.method =='POST':
        form = UniLoginForm(request.POST)
        if form.is_valid():
            admin_name = form.cleaned_data['admin_name']
            admin_password = form.cleaned_data['admin_password']
            try:
                TheAdmin = UniversityAdmin.objects.get(admin_name = admin_name)
                uni = TheAdmin.university_name
            
                if admin_password == TheAdmin.admin_password:
                    loginchecker = logintracker()
                    loginchecker.activate(admin_name, uni)
                    messages.info(request, "Login Successful")

                    return redirect('http://127.0.0.1:8000/loginhomepage')
            except ObjectDoesNotExist:
                messages.info(request, "User does not exist")
         
                return redirect('http://127.0.0.1:8000/university_app/universitylogin')
    else:
        form = UniLoginForm()
    
    return render(request, 'university_app/uni_login.html', {'unilogin': form})


@login_check_required
def uniprofile(request):
    
    university_name = logintracker().Object.university_name
    university = University.objects.get(university_name = university_name)

    if request.method == 'POST':
        form = UniUpdateForm(request.POST, instance=university)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("http://127.0.0.1:8000/university_app/universityprofile")
    else:
        form = UniUpdateForm(instance=university)

    context = {'university': university, 'uniprofile': form}
    return render(request, 'university_app/uni_profile.html', context)
    '''
    loginchecker = logintracker()
    universityname = loginchecker.schoolObject.university_name
    university = University.objects.get(university_name = universityname)

    args = {'university': university}
    
    return render(request, 'university_app/uni_profile.html',args)
    '''