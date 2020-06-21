from django.forms import ModelForm, DateInput
from django import forms
from .models import HighSchoolAppointment, IndividualAppointment, HighSchoolAppointmentRequest, IndividualAppointmentRequest
from cs308_proje.decorators import logintracker
from bootstrap_datepicker_plus import DateTimePickerInput


class HighSchoolAppointmentRequestForm(ModelForm):
    appointment_date_start = forms.DateTimeField(widget=DateTimePickerInput())
    appointment_date_end = forms.DateTimeField(widget=DateTimePickerInput())
    class Meta:
        model = HighSchoolAppointmentRequest
        fields = '__all__'
        exclude = ('school',)
        widgets = {'university': forms.TextInput(attrs={'readonly': True})}

class IndividualAppointmentRequestForm(ModelForm):
    appointment_date_start = forms.DateTimeField(widget=DateTimePickerInput())
    appointment_date_end = forms.DateTimeField(widget=DateTimePickerInput())
    class Meta:
        model = IndividualAppointmentRequest
        fields = '__all__'
        exclude = ('individual',)
        widgets = {'university': forms.TextInput(attrs={'readonly': True})}


class NewHighSchoolAppointmentRequestForm(ModelForm):
    appointment_date_start = forms.DateTimeField(widget=DateTimePickerInput())
    appointment_date_end = forms.DateTimeField(widget=DateTimePickerInput())
    class Meta:
        model = HighSchoolAppointmentRequest
        fields = '__all__'
        exclude = ('school',)


class NewIndividualAppointmentRequestForm(ModelForm):
    appointment_date_start = forms.DateTimeField(widget=DateTimePickerInput())
    appointment_date_end = forms.DateTimeField(widget=DateTimePickerInput())
    class Meta:
        model = IndividualAppointmentRequest
        fields = '__all__'
        exclude = ('individual',)


class HighSchoolAppointmentForm(ModelForm):
    appointment_date_start = forms.DateTimeField(widget=DateTimePickerInput())
    appointment_date_end = forms.DateTimeField(widget=DateTimePickerInput())
    class Meta:
        model = HighSchoolAppointment
        fields = '__all__'
        exclude = ('school',)
        widgets = {'university': forms.TextInput(attrs={'readonly': True}),
                    'guide': forms.TextInput(attrs={'readonly': True})}

class IndividualAppointmentForm(ModelForm):
    appointment_date_start = forms.DateTimeField(widget=DateTimePickerInput())
    appointment_date_end = forms.DateTimeField(widget=DateTimePickerInput())
    class Meta:
        model = IndividualAppointment
        fields = '__all__'
        exclude = ('individual',)
        widgets = {'university': forms.TextInput(attrs={'readonly': True}),
                    'guide': forms.TextInput(attrs={'readonly': True})}