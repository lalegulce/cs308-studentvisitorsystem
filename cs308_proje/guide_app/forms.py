from django.forms import ModelForm
from django import forms
from .models import GuideCredentials



class GuideLoginForm(ModelForm):
    class Meta:
        model = GuideCredentials
        widgets = {'guide_password': forms.PasswordInput()}
        fields = ['guide_username','guide_password']