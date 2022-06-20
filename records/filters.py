import django_filters
from django_filters import CharFilter
from .models import Pupil, Student

class PupilFilter(django_filters.FilterSet):
    class Meta:
        model = Pupil
        fields = ['user', 'user__first_name', 'user__last_name', 'classe']

    def __init__(self, *args, **kwargs):
        super(PupilFilter, self).__init__(*args, **kwargs)
        self.filters['user'].label="Admission No"
        self.filters['classe'].label="Class"
        self.filters['user__first_name'].label="First Name"
        self.filters['user__last_name'].label="Last Name"

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['user', 'user__first_name', 'user__last_name', 'classe']

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)
        self.filters['user'].label="Admission No"
        self.filters['classe'].label="Class"
        self.filters['user__first_name'].label="First Name"
        self.filters['user__last_name'].label="Last Name"
