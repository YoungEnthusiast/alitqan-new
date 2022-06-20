from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth.models import User
from .models import Person
from django.core.exceptions import ValidationError
import datetime
from django.forms.widgets import NumberInput

class CustomRegisterForm(UserCreationForm):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Admin', 'Admin')
    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    #role = forms.ChoiceField(choices=ROLE_CHOICES)
    address = forms.CharField(max_length=200, required=False)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    referrer = forms.CharField(max_length=20, required=False)
    # def clean_email(self):
    #    email = self.cleaned_data.get('email')
    #    if Person.objects.filter(email=email).exists():
    #        raise ValidationError("A user with the supplied email already exists")
    #    return email

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if Person.objects.filter(username=username).exists():
           raise ValidationError("A user with the supplied username already exists")
       return username

    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'classe', 'phone_number', 'gender', 'address', 'dob',  'photograph', 'referrer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'Admission No (Username)'
        self.fields['email'].help_text = "This field must be a valid email address"
        self.fields['password1'].help_text = "<ul><li>Be rest assured that your password will be encrypted (hidden). That means even the website developer will not be able to see it.</li><li>Your password can’t be too similar to your other Personal information.<li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>"
        self.fields['password2'].label = "Password Confirmation"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"
        #self.fields['role'].label = "Role"





















class UserEditForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

class PersonEditForm(forms.ModelForm):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Admin', 'Admin')
    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    #role = forms.ChoiceField(choices=ROLE_CHOICES)
    address = forms.CharField(max_length=200, required=False)

    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

    class Meta:
        model = Person
        fields = ['classe', 'phone_number', 'gender', 'address', 'dob',  'photograph']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"
        self.fields['role'].label = "Role"

class UserEditForm2(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

    def __init__(self, *args, **kwargs):
        super(UserEditForm2, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['username'].required = False
            self.fields['username'].widget.attrs['disabled'] = 'disabled'
            self.fields['first_name'].required = False
            self.fields['first_name'].widget.attrs['disabled'] = 'disabled'
            self.fields['last_name'].required = False
            self.fields['last_name'].widget.attrs['disabled'] = 'disabled'

class PersonEditForm2(forms.ModelForm):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Admin', 'Admin')
    ]
    phone_number = forms.CharField(label='Phone Number')
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    #role = forms.ChoiceField(choices=ROLE_CHOICES)
    address = forms.CharField(max_length=200, required=False)

    def clean_dob(self):
       dob = self.cleaned_data.get('dob')
       if dob > datetime.date.today():
           raise ValidationError("The selected date is invalid. Please re-select another")
       return dob

    class Meta:
        model = Person
        fields = ['phone_number', 'gender', 'address', 'dob',  'photograph']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Phone Number"
        self.fields['dob'].label = "Date of Birth"
        self.fields['role'].label = "Role"

    def __init__(self, *args, **kwargs):
        super(PersonEditForm2, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['classe'].required = False
            self.fields['classe'].widget.attrs['disabled'] = 'disabled'
            self.fields['role'].required = False
            self.fields['role'].widget.attrs['disabled'] = 'disabled'
