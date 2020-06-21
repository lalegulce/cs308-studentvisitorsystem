from django.forms import ModelForm
from django import forms
from .models import HighSchool
from .models import HighSchoolAdmin
from phonenumber_field.formfields import PhoneNumberField


class HighSchoolForm(ModelForm):
    school_contact_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+905xxxxxxxxx'}))
    class Meta:
        model = HighSchool
        fields = ['school_name', 'school_address', 'school_contact_number',
                  'school_mail', 'responsible_person_first_name', 'responsible_person_last_name',
                   'responsible_person_mail']


class HighSchoolProfileEditForm(ModelForm):
    class Meta:
        model = HighSchool
        fields = ['school_address', 'school_contact_number', 'school_mail','responsible_person_first_name', 'responsible_person_last_name',
                   'responsible_person_mail']

class HighSchoolEditImage(ModelForm):
    class Meta:
        model = HighSchool
        fields = ['school_image']


class HighSchoolLoginForm(ModelForm):
    class Meta:
        model = HighSchoolAdmin
        widgets = {'admin_password': forms.PasswordInput()}
        fields = ['admin_name', 'admin_password']