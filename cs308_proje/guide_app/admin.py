from django.contrib import admin
from .models import Guide,GuideRequest, GuideCredentials

# Register your models here.

admin.site.register(Guide)
admin.site.register(GuideRequest)
admin.site.register(GuideCredentials)