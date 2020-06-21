from django.forms import ModelForm
from django import forms
from .models import Individual
from phonenumber_field.formfields import PhoneNumberField

class IndividualForm(ModelForm):
    contact_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+905xxxxxxxxx'}))
    mail = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'mail@mail.com'}))
    class Meta:
        model = Individual
        fields = ['full_name', 'mail', 'contact_number']

class IndividualLoginForm(ModelForm):
    class Meta:
        model = Individual
        widgets = {'password': forms.PasswordInput()}
        fields = ['username','password']