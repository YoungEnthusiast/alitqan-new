import django_filters
from django_filters import CharFilter
from .models import Session, Class, Subject

class SessionFilter(django_filters.FilterSet):
    head = CharFilter(field_name='first_head', lookup_expr='icontains', label="Head of School's Name")
    number = CharFilter(field_name='first_number', lookup_expr='icontains', label="No of Days School Opens")
    class Meta:
        model = Session
        fields = ['session']

class ClassFilter(django_filters.FilterSet):
    teacher = CharFilter(field_name='teacher__first_name', lookup_expr='icontains', label="Teacher's First Name")
    teacher2 = CharFilter(field_name='teacher__last_name', lookup_expr='icontains', label="Teacher's Last Name")
    class Meta:
        model = Class
        fields = ['classe']

class SubjectFilter(django_filters.FilterSet):
    classe = CharFilter(field_name='classe__classe', lookup_expr='icontains', label="Class")
    subject = CharFilter(field_name='subject', lookup_expr='icontains', label="Subject")
    teacher = CharFilter(field_name='teacher__first_name', lookup_expr='icontains', label="Teacher's First Name")
    teacher2 = CharFilter(field_name='teacher__last_name', lookup_expr='icontains', label="Teacher's Last Name")
    class Meta:
        model = Subject
        fields = []
    # def __init__(self, *args, **kwargs):
    #     super(SubjectFilter, self).__init__(*args, **kwargs)
    #     self.filters['classe__classe'].label="Class"
