from django.contrib import admin
from .models import UniversityRequest, IndividualRequest, HighSchoolRequest
# Register your models here.


admin.site.register(UniversityRequest)
admin.site.register(HighSchoolRequest)
admin.site.register(IndividualRequest)