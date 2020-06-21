import django_tables2 as tables
from university_app.models import University

class UniversityTable(tables.Table):

    class Meta:
        model = University
        fields = ('university_name','university_faculties', 'university_mail')
        sequence = fields
        template_name = 'django_tables2/bootstrap-responsive.html'