from django.shortcuts import render, redirect
from university_app.models import University
from .tables import UniversityTable
from django_tables2 import RequestConfig
from cs308_proje.decorators import logintracker, login_check_required
from django.db.models import Q
from django.contrib import messages

# Create your views here.


def homepage(request):
    tracker = logintracker()
    data = University.objects.all()
    university = request.GET.get('search-university')
    city = request.GET.get('search-city')
    faculty = request.GET.get('search-faculty')
    if university != '' and university is not None:
        data = data.filter(university_name__icontains=university)
    elif city != '' and university is not None:
        data = data.filter(university_address__icontains=city)
    elif faculty !='' and university is not None:
        data = data.filter(university_faculties__icontains=faculty)


    if tracker.status == False:
        return render(request, 'homepage_app/homepage.html', {"university_table":data})
    else:
        return render(request, 'homepage_app/loginhomepage.html', {"university_table":data})

"""
def search_university(request):
    tracker = logintracker()
    data = request.GET['search-university']
    university = University.objects.filter(Q(university_name__icontains=data))
    table = UniversityTable(university)
    RequestConfig(request).configure(table)
    if tracker.status == False:
        return render(request, 'homepage_app/homepage.html', {"university_table":table})
    else:
        return render(request, 'homepage_app/loginhomepage.html', {"university_table":table})
"""

def loginhomepage(request):
    tracker = logintracker()
    data = University.objects.all()
    university = request.GET.get('search-university')
    city = request.GET.get('search-city')
    faculty = request.GET.get('search-faculty')
    if university != '' and university is not None:
        data = data.filter(university_name__icontains=university)
    elif city != '' and university is not None:
        data = data.filter(university_address__icontains=city)
    elif faculty !='' and university is not None:
        data = data.filter(university_faculties__icontains=faculty)

    if tracker.status == False:
        return render(request, 'homepage_app/loginhomepage.html', {"university_table":data})
    else:
        return render(request, 'homepage_app/loginhomepage.html', {"university_table":data})

def logout(request):
    user = logintracker()
    user.deactivate()
    messages.info(request,"SUCCESSFULLY LOGGED OUT!")
    return redirect('http://127.0.0.1:8000')

"""
def search_university(request):
    data = request.GET['search-university']
    university = University.objects.filter(university_name__icontains=data)
    table = UniversityTable(university)
    RequestConfig(request).configure(table)
    return render(request, 'homepage_app/loginhomepage.html', {"university_table": table})
"""
