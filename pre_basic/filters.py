import django_filters
from django_filters import CharFilter
from .models import FirstTerm, SecondTerm, ThirdTerm

class FirstFilter(django_filters.FilterSet):
    class Meta:
        model = FirstTerm
        fields = ['pupil', 'pupil__user__first_name', 'pupil__user__last_name', 'pupil__classe']

    def __init__(self, *args, **kwargs):
        super(FirstFilter, self).__init__(*args, **kwargs)
        self.filters['pupil'].label="Admission No"
        self.filters['pupil__classe'].label="Class"
        self.filters['pupil__user__first_name'].label="First Name"
        self.filters['pupil__user__last_name'].label="Last Name"

class SecondFilter(django_filters.FilterSet):
    class Meta:
        model = SecondTerm
        fields = ['pupil', 'pupil__user__first_name', 'pupil__user__last_name', 'pupil__classe']

    def __init__(self, *args, **kwargs):
        super(SecondFilter, self).__init__(*args, **kwargs)
        self.filters['pupil'].label="Admission No"
        self.filters['pupil__classe'].label="Class"
        self.filters['pupil__user__first_name'].label="First Name"
        self.filters['pupil__user__last_name'].label="Last Name"

class ThirdFilter(django_filters.FilterSet):
    class Meta:
        model = ThirdTerm
        fields = ['pupil', 'pupil__user__first_name', 'pupil__user__last_name', 'pupil__classe']

    def __init__(self, *args, **kwargs):
        super(ThirdFilter, self).__init__(*args, **kwargs)
        self.filters['pupil'].label="Admission No"
        self.filters['pupil__classe'].label="Class"
        self.filters['pupil__user__first_name'].label="First Name"
        self.filters['pupil__user__last_name'].label="Last Name"
