from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone Number')
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']
