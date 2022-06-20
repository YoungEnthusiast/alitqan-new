from django import forms
from users.models import Person
from .models import Session, Class, Subject
from django.core.exceptions import ValidationError

class SessionForm(forms.ModelForm):
    first_head = forms.ModelChoiceField(queryset=Person.objects.filter(role="Staff"))
    def clean_session(self):
       session = self.cleaned_data.get('session')
       if Session.objects.filter(session=session).exists():
           raise ValidationError("The session already exists")
       return session
    class Meta:
        model = Session
        fields = ['session', 'first_head', 'school', 'first_number', 'first_next', 'first_report']

class SessionFormUp(forms.ModelForm):
    first_head = forms.ModelChoiceField(queryset=Person.objects.filter(role="Staff"))
    class Meta:
        model = Session
        fields = ['session', 'first_head', 'school', 'first_number', 'first_next', 'first_report']

class ClassForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Person.objects.filter(role="Staff"))
    def clean_classe(self):
       classe = self.cleaned_data.get('classe')
       if Class.objects.filter(classe=classe).exists():
           raise ValidationError("The class already exists")
       return classe
    class Meta:
        model = Class
        fields = ['classe', 'teacher', 'signature']

class ClassFormUp(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Person.objects.filter(role="Staff"))
    class Meta:
        model = Class
        fields = ['classe', 'teacher', 'signature']

class SubjectForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Person.objects.filter(role="Staff"))
    class Meta:
        model = Subject
        fields = ['serial', 'classe', 'subject', 'teacher']
