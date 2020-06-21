from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import HighSchoolForm
from .forms import HighSchoolLoginForm
from .forms import HighSchoolProfileEditForm
from .forms import HighSchoolEditImage
from .models import HighSchoolAdmin
from .models import HighSchool
from website_admin_app.models import HighSchoolRequest
from django.db import IntegrityError
from django.contrib import messages
from cs308_proje.decorators import logintracker , login_check_required
from django.core.exceptions import ObjectDoesNotExist
from appointment_app.models import HighSchoolAppointment


def high_school_login(request):
    if request.method == 'POST':
        form = HighSchoolLoginForm(request.POST)

        if form.is_valid():
            admin_name = form.cleaned_data['admin_name']
            admin_password = form.cleaned_data['admin_password']
            try:

                Admin = HighSchoolAdmin.objects.get(admin_name = admin_name)
                school = Admin.school
            
                if admin_password == Admin.admin_password:
                    loginchecker = logintracker()
                    loginchecker.activate(admin_name,school)
                    
                    messages.info(request,"SUCCESSFULLY LOGGED IN!")
                    return redirect('http://127.0.0.1:8000/loginhomepage/')
                else:
                    messages.info(request, "Wrong password")
            except ObjectDoesNotExist:
                messages.info(request, "Wrong username and password")
        
    form = HighSchoolLoginForm()
    return render(request, 'high_school_app/HighSchool_login.html', {'highschool_loginform': form})



def highschoolloginpage(request):
    form = HighSchoolLoginForm()

    return render(request, 'high_school_app/HighSchool_login.html', {'highschool_loginform': form})


def high_school_registration(request):

    if request.method == 'POST':
        form = HighSchoolForm(request.POST)

        if form.is_valid():
            school_name = form.cleaned_data['school_name']
            school_address = form.cleaned_data['school_address']
            school_contact_number = form.cleaned_data['school_contact_number']
            school_mail = form.cleaned_data['school_mail']
            user_type = "highschool"

            responsible_person_first_name = form.cleaned_data['responsible_person_first_name']
            responsible_person_last_name = form.cleaned_data['responsible_person_last_name']
            responsible_person_mail = form.cleaned_data['responsible_person_mail']

            try:
                HighSchoolRequest.objects.create(school_name=school_name, school_address=school_address,
                                                 school_contact_number=school_contact_number, school_mail=school_mail, school_type=user_type, 
                                                 responsible_person_first_name=responsible_person_first_name, responsible_person_last_name=responsible_person_last_name,
                                                 responsible_person_mail = responsible_person_mail)

                val = "High School request has been sent."
            except IntegrityError:
                val = "High School already exists. Registration failed."
            messages.info(request, val)

            return redirect('http://127.0.0.1:8000/')
    else:
        form = HighSchoolForm()

    return render(request, 'high_school_app/HighSchool_form.html', {'HighSchool_form': form})


def highschool_profile(request):

    loginchecker = logintracker()
    highschool = loginchecker.Object
    appointments = HighSchoolAppointment.objects.all().filter(school = highschool.school_name).order_by('-appointment_date_start')

    # dates= []
    # for n in appointments:
    #     dates.append(n.appointment_date_start)

    args = {'highschool': highschool,'calendar':appointments}

    return render(request, 'high_school_app/HighSchool_profile.html', args)

def highschool_edit_image(request): 
  
    if request.method == 'POST': 
        form = HighSchoolEditImage(request.POST, request.FILES) 
  
        if form.is_valid(): 
            loginchecker = logintracker()
            schoolname = loginchecker.Object.school_name
            schoolimage =form.cleaned_data['school_image']
            hs = HighSchool.objects.get(school_name=schoolname)
            hs.school_image =schoolimage
            hs.save(force_update=True)
            print(schoolname + "/n")
            return redirect('highschool_profile')
    else: 
        form = HighSchoolEditImage() 
    
    return render(request, 'high_school_app/HighSchool_editimage.html', {'form' : form}) 

def highschool_edit_profile(request):
    loginchecker = logintracker()
    user = loginchecker.Object
    schoolname = loginchecker.Object.school_name

    if request.method == 'POST':
        form = HighSchoolProfileEditForm(request.POST,instance=user)

        if form.is_valid():

            address = form.cleaned_data['school_address']
            contact_number = form.cleaned_data['school_contact_number']
            mail = form.cleaned_data['school_mail']
            resname = form.cleaned_data['responsible_person_first_name']
            ressurname = form.cleaned_data['responsible_person_last_name']
            resmail = form.cleaned_data['responsible_person_mail']

            hs = HighSchool.objects.get(school_name=schoolname)
            
            hs.school_address = address
            hs.school_contact_number = contact_number
            hs.school_mail = mail
            hs.responsible_person_first_name = resname
            hs.responsible_person_last_name = ressurname
            hs.responsible_person_mail = resmail

            hs.save(force_update=True)

            return redirect(reverse('highschool_profile'))
        else:
            print("INVALID FORM!")
            return redirect('edit_profile')

    else:
        print("ELSELSELELELELEELELELSELSLESLESLESLESLELSELSELSS")
        form = HighSchoolProfileEditForm()
        args = {'form': form}
        return render(request, 'high_school_app/HighSchool_editprofile.html', args)