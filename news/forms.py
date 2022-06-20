from django import forms
from .models import News
from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):
    def clean_headline(self):
       headline = self.cleaned_data.get('headline')
       if News.objects.filter(headline=headline).exists():
           raise ValidationError("The headline already exists")
       return headline
    class Meta:
        model = News
        fields = ['headline', 'content', 'image', 'home_page']

class NewsFormUp(forms.ModelForm):
    class Meta:
        model = News
        fields = ['headline', 'content', 'image', 'home_page']
