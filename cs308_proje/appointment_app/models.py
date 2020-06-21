from django.db import models
from university_app.models import University, UniversitySchedule
from high_school_app.models import HighSchool
from individual_app.models import Individual
from guide_app.models import Guide
from django.urls import reverse

class HighSchoolAppointmentRequest(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    faculties = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    school = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    appointment_date_start = models.DateTimeField()
    appointment_date_end = models.DateTimeField()
    capacity = models.IntegerField()

class IndividualAppointmentRequest(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    faculties = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    appointment_date_start = models.DateTimeField()
    appointment_date_end = models.DateTimeField()
    capacity = models.IntegerField()


class HighSchoolAppointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    faculties = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    appointment_date_start = models.DateTimeField()
    appointment_date_end = models.DateTimeField()
    capacity = models.IntegerField()

    @property
    def get_html_url_uni(self):
        url = reverse('appointment_app:appointment_edit', args=(self.appointment_id,))
        return f'<a href="{url}"> School Name: {self.school.school_name} <br />Starting Time: {self.appointment_date_start.strftime("%H:%M:%S")} <br />Finishing Time: {self.appointment_date_end.strftime("%H:%M:%S")} <br />Capacity: {self.capacity}</a>'

    @property
    def get_html_url(self):
        url = reverse('appointment_app:appointment_edit', args=(self.appointment_id,))
        return f'<a href="{url}"> Uni Name: {self.university.university_name} <br /> Starting Time: {self.appointment_date_start.strftime("%H:%M:%S")} <br />Finishing Time: {self.appointment_date_end.strftime("%H:%M:%S")} <br />Capacity: {self.capacity}</a>'


class IndividualAppointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    faculties = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)
    appointment_date_start = models.DateTimeField()
    appointment_date_end = models.DateTimeField()
    capacity = models.IntegerField()

    @property
    def get_html_url_uni(self):
        url = reverse('appointment_app:appointment_edit', args=(self.appointment_id,))
        return f'<a href="{url}"> Individual Name: {self.individual.full_name} <br />Starting Time: {self.appointment_date_start.strftime("%H:%M:%S")} <br />Finishing Time: {self.appointment_date_end.strftime("%H:%M:%S")} <br />Capacity: {self.capacity}</a>'

    @property
    def get_html_url(self):
        url = reverse('appointment_app:appointment_edit', args=(self.appointment_id,))
        return f'<a href="{url}"> Uni Name: {self.university.university_name} <br /> Starting Time: {self.appointment_date_start.strftime("%H:%M:%S")} <br />Finishing Time: {self.appointment_date_end.strftime("%H:%M:%S")} <br />Capacity: {self.capacity}</a>'