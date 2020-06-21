from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class HighSchool(models.Model):
    school_name = models.CharField(max_length=100, primary_key=True)
    school_address = models.CharField(max_length=200)
    school_contact_number = PhoneNumberField(null=False, blank=False, unique=True)
    school_mail = models.EmailField()
    school_image = models.ImageField(upload_to='images/',default='defaultLogo.png')
    user_type = "highschool"
    responsible_person_first_name = models.CharField(max_length=200)
    responsible_person_last_name = models.CharField(max_length=200)
    responsible_person_mail = models.CharField(max_length=200)

    def __str__(self):
        return self.school_name


class HighSchoolAdmin(models.Model):
    school = models.OneToOneField(HighSchool, on_delete=models.CASCADE)
    admin_name = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=32)

    def __str__(self):
        return self.admin_name