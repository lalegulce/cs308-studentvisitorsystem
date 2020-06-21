from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class UniversityRequest(models.Model):
    university_name = models.CharField(max_length=100, primary_key=True)
    university_address = models.CharField(max_length=200)
    university_contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    university_mail = models.EmailField()
    university_faculties = models.CharField(max_length=500)
    school_type = 'university'

    def __str__(self):
        return "Request By: " + self.university_name

class HighSchoolRequest(models.Model):
    school_name = models.CharField(max_length=100, primary_key=True)
    school_address = models.CharField(max_length=200)
    school_contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    school_mail = models.EmailField()
    school_type = "highschool"

    def __str__(self):
        return "Request By: " + self.school_name

class IndividualRequest(models.Model):
    individual_name = models.CharField(max_length=100, primary_key=True)
    individual_contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    individual_mail = models.EmailField()

    def __str__(self):
        return "Request By: " + self.individual_name

