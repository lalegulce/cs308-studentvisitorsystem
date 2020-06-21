from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class University(models.Model):
    university_name = models.CharField(max_length=100, primary_key=True)
    university_address = models.CharField(max_length=200)
    university_contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    university_mail = models.EmailField()
    university_faculties = models.CharField(max_length=500)
    user_type = "university"

    def __str__(self):
        return self.university_name


class UniversityAdmin(models.Model):
    university_name = models.ForeignKey(University, on_delete=models.CASCADE)
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=32)

    def __str__(self):
        return self.admin_name


class UniversitySchedule(models.Model):
    university_name = models.ForeignKey(University, on_delete=models.CASCADE)
    university_start_date = models.DateTimeField()
    university_end_date = models.DateTimeField()
    capacity = models.IntegerField()
    availability = models.BooleanField(default=True)
