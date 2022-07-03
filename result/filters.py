import django_filters
from django_filters import CharFilter
from .models import First, Second, Third

class FirstFilter(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    subject = CharFilter(field_name='subject__subject', lookup_expr='icontains', label="Subject")

    class Meta:
        model = First
        fields = ['session']

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #
    #     super(FirstFilter, self).__init__(*args, **kwargs)
    #     self.filters['subject'] = ModelChoiceFilter(queryset=First.objects.filter(subject__teacher=self.user))

    # def __init__(self, *args, **kwargs):
    #     super(FirstFilter, self).__init__(*args, **kwargs)
    #     self.filters['student__role'].label="Admission No"
    #     self.filters['student__classe'].label="Class"
    #     self.filters['student__user__first_name'].label="First Name"
    #     self.filters['student__user__last_name'].label="Last Name"

class SecondFilter(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    subject = CharFilter(field_name='subject__subject', lookup_expr='icontains', label="Subject")
    class Meta:
        model = Second
        fields = ['session']

class ThirdFilter(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    subject = CharFilter(field_name='subject__subject', lookup_expr='icontains', label="Subject")
    class Meta:
        model = Third
        fields = ['session']

class FirstFilter2(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = First
        fields = ['session']

class SecondFilter2(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = Second
        fields = ['session']

class ThirdFilter2(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = Third
        fields = ['session']

class FirstFilter3(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    subject = CharFilter(field_name='subject__subject', lookup_expr='icontains', label="Subject")

    class Meta:
        model = First
        fields = ['session']

class SecondFilter3(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    subject = CharFilter(field_name='subject__subject', lookup_expr='icontains', label="Subject")
    class Meta:
        model = Second
        fields = ['session']

class ThirdFilter3(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    subject = CharFilter(field_name='subject__subject', lookup_expr='icontains', label="Subject")
    class Meta:
        model = Third
        fields = ['session']

class FirstFilter4(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")

    class Meta:
        model = First
        fields = ['session']

class SecondFilter4(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    class Meta:
        model = Second
        fields = ['session']

class ThirdFilter4(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    class Meta:
        model = Third
        fields = ['session']

class FirstFilterPay(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = First
        fields = ['session']

    # def __init__(self, *args, **kwargs):
    #     super(FirstFilterPay, self).__init__(*args, **kwargs)
    #     self.filters['student__classe'].label="Class"

class SecondFilterPay(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = Second
        fields = ['session']

class ThirdFilterPay(django_filters.FilterSet):
    static_class = CharFilter(field_name='static_class', lookup_expr='icontains', label="Class")
    admission_no = CharFilter(field_name='student__username', lookup_expr='icontains', label="Admission No")
    first_name = CharFilter(field_name='student__first_name', lookup_expr='icontains', label="First Name")
    last_name = CharFilter(field_name='student__last_name', lookup_expr='icontains', label="Last Name")
    class Meta:
        model = Third
        fields = ['session']
