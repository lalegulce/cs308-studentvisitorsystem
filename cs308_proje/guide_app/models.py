from django.db import models
from university_app.models import University

# Create your models here.

class Guide(models.Model):
    guide_id = models.AutoField(primary_key=True, default= 11)
    guide_name = models.CharField(max_length=100)
    guide_faculty = models.CharField(max_length=100)
    university_name = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.guide_name


class GuideRequest(models.Model):
    guide_id = models.AutoField(primary_key=True)
    guide_name = models.CharField(max_length=100)
    guide_faculty = models.CharField(max_length=100)
    university_name = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.guide_name

class GuideCredentials(models.Model):
    guide_id = models.ForeignKey(Guide, on_delete=models.CASCADE)
    guide_username = models.CharField(max_length=100)
    guide_password = models.CharField(max_length=32)

    def __str__(self):
        return self.guide_username