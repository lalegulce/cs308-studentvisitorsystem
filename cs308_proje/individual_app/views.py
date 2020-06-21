from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import IndividualForm, IndividualLoginForm
from .models import Individual
from website_admin_app.models import IndividualRequest
from django.db import IntegrityError
from django.contrib import messages
from cs308_proje.decorators import logintracker, login_check_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

def individual_registration(request):   
    if request.method == 'POST':
        form = IndividualForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            mail = form.cleaned_data['mail']
            contact_number = form.cleaned_data['contact_number']

            try:
                IndividualRequest.objects.create(individual_name=full_name, individual_mail=mail, 
                                                    individual_contact_number=contact_number)
                val = "Individual request has been sent."
            except IntegrityError:
                val = "Registration failed."
            messages.info(request,val)
            
            return redirect('http://127.0.0.1:8000/') 
    else:
        form = IndividualForm()

    return render(request, 'individual_app/signup.html', {'Individual_form': form})

def individual_login(request):
    if request.method =='POST':
        form = IndividualLoginForm(request.POST)
        if form.is_valid():
            admin_name = form.cleaned_data['username']
            admin_password = form.cleaned_data['password']
            try:
                Admin = Individual.objects.get(username = admin_name)
            
                if admin_password == Admin.password:
                    loginchecker = logintracker()
                    loginchecker.activate(admin_name, Admin)
                    messages.info(request, "Login Successful")
                    return redirect('http://127.0.0.1:8000/loginhomepage/')
                else:   
                    messages.info(request, "Wrong password")
            except ObjectDoesNotExist:
                messages.info(request, "Wrong username and password")
    
    form = IndividualLoginForm()
    return render(request, 'individual_app/signin.html', {'Individual_form': form})

@login_check_required
def individual_edit(request):
    user = logintracker()
    individual = user.Object
    msg = ""
    if request.method == 'POST':
        form = IndividualForm(request.POST, instance=individual)
        if form.is_valid():  
            try:
                form.save()
                msg = "Succesfully updated information"
            except:
                msg = "Couldn't update your information." 
    else:
        form = IndividualForm(instance = individual)
    
    messages.success(request, msg)
    return render(request, 'individual_app/profilepage.html', {'Individual_form': form})