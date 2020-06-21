from .models import UniversityRequest, HighSchoolRequest, IndividualRequest
from university_app.models import University, UniversityAdmin
from high_school_app.models import HighSchool, HighSchoolAdmin
from individual_app.models import Individual
from django.core.mail import send_mail
import string
from random import *


def create_credentials(name):

    username = (name + "admin").strip()
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 16)))

    return username.lower(), password

def university_database_handler(uni_name, to_do):
    uni = UniversityRequest.objects.get(university_name=uni_name)
    sender = 'studentvisitorsystem@gmail.com'
    recipients = [uni.university_mail]
    if to_do:
        # add to university database
        University.objects.create(
            university_name=uni.university_name, university_address=uni.university_address, university_contact_number=uni.university_contact_number, university_mail=uni.university_mail, university_faculties=uni.university_faculties)
        subject = 'YOUR UNIVERSITY REQUEST HAS BEEN APPROVED!!'
        username, password = create_credentials(uni_name)
        message = 'Username: ' + username + '\nPassword: ' + password
        new_uni = University(
            university_name=uni.university_name, university_address=uni.university_address, university_contact_number=uni.university_contact_number, university_mail=uni.university_mail, university_faculties=uni.university_faculties)
        UniversityAdmin.objects.create(university_name = new_uni, admin_name=username, admin_password=password)
    else:
        subject = 'SUBJECT: REJECTED!!'
        message = 'REJECTED!!'
    uni.delete()
    send_mail(subject, message, sender, recipients)
    print('MAIL SENT')


def high_school_database_handler(school_name, to_do):
    school = HighSchoolRequest.objects.get(school_name=school_name)
    sender = 'studentvisitorsystem@gmail.com'
    recipients = [school.school_mail]
    if to_do:
        # add to university database
        HighSchool.objects.create(school_name=school.school_name,
                                  school_mail=school.school_mail, school_address=school.school_address, school_contact_number=school.school_contact_number)
        subject = 'YOUR UNIVERSITY REQUEST HAS BEEN APPROVED!!'
        username, password = create_credentials(school_name)
        message = 'Username: ' + username + '\nPassword: ' + password
        new_school =HighSchool(school_name=school.school_name,
                                  school_mail=school.school_mail, school_address=school.school_address, school_contact_number=school.school_contact_number)
        
        HighSchoolAdmin.objects.create(school = new_school, admin_name=username, admin_password=password)
    else:
        subject = 'SUBJECT: REJECTED!!'
        message = 'REJECTED!!'
    school.delete()
    send_mail(subject, message, sender, recipients)
    print('MAIL SENT')


def individual_database_handler(individual_name, to_do):
    individual = IndividualRequest.objects.get(individual_name=individual_name)
    sender = 'studentvisitorsystem@gmail.com'
    recipients = [individual.individual_mail]
    if to_do:
        subject = 'YOUR REQUEST HAS BEEN APPROVED!!'
        username, password = create_credentials(individual_name)
        message = 'Username: ' + username + '\nPassword: ' + password

        Individual.objects.create(full_name=individual.individual_name, username=username, password=password,
                                  mail=individual.individual_mail, contact_number=individual.individual_contact_number)
    else:
        subject = 'SUBJECT: REJECTED!!'
        message = 'REJECTED!!'
    individual.delete()
    send_mail(subject, message, sender, recipients)
    print('MAIL SENT')
