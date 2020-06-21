from django.contrib import admin
from .models import HighSchoolAppointment, IndividualAppointment, IndividualAppointmentRequest, HighSchoolAppointmentRequest
# Register your models here.


admin.site.register(HighSchoolAppointmentRequest)
admin.site.register(IndividualAppointmentRequest)
admin.site.register(HighSchoolAppointment)
admin.site.register(IndividualAppointment)
