from django.forms import ModelForm
from django import forms
from .models import University, UniversityAdmin
from phonenumber_field.modelfields import PhoneNumberField

class SignupRequestForm(ModelForm):
    class Meta:
        model = University
        fields = ['university_name', 'university_faculties', 'university_address', 'university_mail', 'university_contact_number']

class UniLoginForm(ModelForm):
    class Meta:
        model = UniversityAdmin
        widgets = {'admin_password': forms.PasswordInput()}
        fields = ['admin_name','admin_password']

class UniUpdateForm(ModelForm):
    university_address = forms.CharField(required = False)
    university_faculties = forms.CharField(required = False)
    class Meta:
        model = University
        fields = ['university_faculties', 'university_address', 'university_mail', 'university_contact_number']