from django.contrib import admin
from .models import University, UniversityAdmin, UniversitySchedule
# Register your models here.

admin.site.register(University)
admin.site.register(UniversityAdmin)
admin.site.register(UniversitySchedule)