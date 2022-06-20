from django import forms
from .models import Video, Category
from django.core.exceptions import ValidationError

class VideoForm(forms.ModelForm):
    def clean_title(self):
       title = self.cleaned_data.get('title')
       if Video.objects.filter(title=title).exists():
           raise ValidationError("The title already exists")
       return title
    class Meta:
        model = Video
        fields = ['category', 'title', 'video', 'home_page']

class VideoFormUp(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['category', 'title', 'video', 'home_page']

class CategoryForm(forms.ModelForm):
    def clean_category(self):
       category = self.cleaned_data.get('category')
       if Category.objects.filter(category=category).exists():
           raise ValidationError("The category already exists")
       return category
    class Meta:
        model = Category
        fields = ['category']

class CategoryFormUp(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
