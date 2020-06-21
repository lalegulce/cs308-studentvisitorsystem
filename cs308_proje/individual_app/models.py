from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Individual(models.Model):
    individual_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200)  
    mail = models.EmailField()
    contact_number = PhoneNumberField(null=False, blank=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    user_type = "individual"

    def __str__(self):
        return self.full_name