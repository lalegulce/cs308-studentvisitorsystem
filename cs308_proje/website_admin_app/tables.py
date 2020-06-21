import django_tables2 as tables
from .models import UniversityRequest, HighSchoolRequest, IndividualRequest


class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class UniversityRequestTable(tables.Table):

    to_change = CheckBoxColumnWithName(verbose_name="", accessor='university_name')

    class Meta:
        model = UniversityRequest
        fields = ('to_change', 'university_name', 'university_address',
                  'university_contact_number', 'university_mail', 'university_faculties')
        sequence = fields
        template_name = 'django_tables2/bootstrap-responsive.html'


class HighSchoolRequestTable(tables.Table):

    to_change = CheckBoxColumnWithName(verbose_name="", accessor='school_name')

    class Meta:
        model = HighSchoolRequest
        fields = ('to_change', 'school_name', 'school_address',
                  'school_contact_number', 'school_mail')
        sequence = fields
        template_name = 'django_tables2/bootstrap-responsive.html'


class IndividualRequestTable(tables.Table):

    to_change = CheckBoxColumnWithName(verbose_name="", accessor='individual_name')

    class Meta:
        model = IndividualRequest
        fields = ('to_change', 'individual_name',
                  'individual_contact_number', 'individual_mail')
        sequence = fields
        template_name = 'django_tables2/bootstrap-responsive.html'
