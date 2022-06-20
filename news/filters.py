import django_filters
from django_filters import CharFilter, DateFilter
from .models import News
from django.forms.widgets import TextInput

class NewsFilter(django_filters.FilterSet):
    headline = CharFilter(field_name='headline', lookup_expr='icontains', label='Headline')
    content = CharFilter(field_name='content', lookup_expr='icontains', label='Content')
    created = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'E.g. 1-1-2021'}))

    class Meta:
        model = News
        fields = ['headline', 'content', 'created']

    def __init__(self, *args, **kwargs):
        super(NewsFilter, self).__init__(*args, **kwargs)
        self.filters['created'].label="Date"
