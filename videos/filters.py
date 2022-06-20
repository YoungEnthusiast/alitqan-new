import django_filters
from django_filters import CharFilter, DateFilter
from .models import Video, Category
from django.forms.widgets import TextInput

class VideoFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    category__category = CharFilter(field_name='category__category', lookup_expr='icontains', label='Category')
    created = DateFilter(input_formats=['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%d/%m/%Y'], lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'E.g. 1-1-2021'}))

    class Meta:
        model = Video
        fields = ['title', 'category__category', 'created']

    def __init__(self, *args, **kwargs):
        super(VideoFilter, self).__init__(*args, **kwargs)
        self.filters['category__category'].label="Category"
        self.filters['created'].label="Date"

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['category']
