import django_filters
from django_filters import CharFilter
from .models import Person

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ['classe']

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)
        #self.filters['user'].label="Admission No"
        self.filters['classe'].label="Class"
        # self.filters['user__first_name'].label="First Name"
        # self.filters['user__last_name'].label="Last Name"

class StaffFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains', label="Username")
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='first_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = Person
        fields = []

    def __init__(self, *args, **kwargs):
        super(StaffFilter, self).__init__(*args, **kwargs)
        # self.filters['username'].label="Username"
        # self.filters['last_name'].label="Last Name"

class StudentFilter2(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains', label="Admission Number")
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='first_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = Person
        fields = ['classe']

    def __init__(self, *args, **kwargs):
        super(StudentFilter2, self).__init__(*args, **kwargs)
        self.filters['classe'].label="Class"
