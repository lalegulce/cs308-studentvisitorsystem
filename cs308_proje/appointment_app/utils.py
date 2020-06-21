from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import HighSchoolAppointment, IndividualAppointment
from cs308_proje.decorators import logintracker
from django.db import models

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()


    # formats a day as a td
    # filter events by day
    def formatday(self, day, appointments):
        appointments_per_day = appointments.filter(appointment_date_start__day=day)
        d = ''
        user = logintracker()
        for appointment in appointments_per_day:
            if user.Object.user_type != "university":
                d += f'<li> {appointment.get_html_url} </li>'
            elif user.Object.user_type == "university":
                d += f'<li> {appointment.get_html_url_uni} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, appointments):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, appointments)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        tracker = logintracker()
        if tracker.Object.user_type == "highschool":
            appointments = HighSchoolAppointment.objects.filter(appointment_date_start__year=self.year, appointment_date_start__month=self.month, school=tracker.Object)
        elif tracker.Object.user_type == "individual":
            appointments = IndividualAppointment.objects.filter(appointment_date_start__year=self.year, appointment_date_start__month=self.month, individual=tracker.Object)
        elif tracker.Object.user_type == "university":
            appointments = HighSchoolAppointment.objects.filter(appointment_date_start__year=self.year, appointment_date_start__month=self.month, university=tracker.Object) 
            individualappointments = IndividualAppointment.objects.filter(appointment_date_start__year=self.year, appointment_date_start__month=self.month, university=tracker.Object)
            appointments.union(individualappointments)

        appointment_app = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        appointment_app += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        appointment_app += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            appointment_app += f'{self.formatweek(week, appointments)}\n'
        return appointment_app
