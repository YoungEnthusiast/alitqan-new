from django import forms
from .models import FirstTerm, SecondTerm, ThirdTerm

class FirstTermForm(forms.ModelForm):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)

    class Meta:
        model = FirstTerm
        fields = ['session', 'pupil', 'literacy_ca1', 'literacy_ca2', 'literacy_exam',
            'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam', 'general_studies_ca1',
            'general_studies_ca2', 'general_studies_exam', 'science_ca1', 'science_ca2',
            'science_exam', 'number_present', 'concentration', 'responsiveness', 'comprehension', 'interest',
            'homework', 'reading', 'writing', 'spoken', 'innovative']

class FirstTermFormUp(forms.ModelForm):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)

    def __init__(self, *args, **kwargs):
        super(FirstTermFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['pupil'].required = False
            self.fields['pupil'].widget.attrs['disabled'] = 'disabled'
            # self.fields['classe'].required = False
            # self.fields['classe'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_pupil(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.pupil
        else:
            return self.cleaned_data.get('pupil', None)

    class Meta:
        model = FirstTerm
        fields = ['session', 'pupil', 'literacy_ca1', 'literacy_ca2', 'literacy_exam',
            'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam', 'general_studies_ca1',
            'general_studies_ca2', 'general_studies_exam', 'science_ca1', 'science_ca2',
            'science_exam', 'number_present', 'concentration', 'responsiveness', 'comprehension', 'interest',
            'homework', 'reading', 'writing', 'spoken', 'innovative']

class SecondTermForm(forms.ModelForm):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)

    class Meta:
        model = SecondTerm
        fields = ['session', 'pupil', 'literacy_ca1', 'literacy_ca2', 'literacy_exam',
            'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam', 'general_studies_ca1',
            'general_studies_ca2', 'general_studies_exam', 'science_ca1', 'science_ca2',
            'science_exam', 'number_present', 'concentration', 'responsiveness', 'comprehension', 'interest',
            'homework', 'reading', 'writing', 'spoken', 'innovative']

class SecondTermFormUp(forms.ModelForm):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)

    def __init__(self, *args, **kwargs):
        super(SecondTermFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['pupil'].required = False
            self.fields['pupil'].widget.attrs['disabled'] = 'disabled'
            # self.fields['classe'].required = False
            # self.fields['classe'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_pupil(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.pupil
        else:
            return self.cleaned_data.get('pupil', None)

    class Meta:
        model = SecondTerm
        fields = ['session', 'pupil', 'literacy_ca1', 'literacy_ca2', 'literacy_exam',
            'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam', 'general_studies_ca1',
            'general_studies_ca2', 'general_studies_exam', 'science_ca1', 'science_ca2',
            'science_exam', 'number_present', 'concentration', 'responsiveness', 'comprehension', 'interest',
            'homework', 'reading', 'writing', 'spoken', 'innovative']

class ThirdTermForm(forms.ModelForm):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)

    class Meta:
        model = ThirdTerm
        fields = ['session', 'pupil', 'literacy_ca1', 'literacy_ca2', 'literacy_exam',
            'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam', 'general_studies_ca1',
            'general_studies_ca2', 'general_studies_exam', 'science_ca1', 'science_ca2',
            'science_exam', 'number_present', 'concentration', 'responsiveness', 'comprehension', 'interest',
            'homework', 'reading', 'writing', 'spoken', 'innovative']

class ThirdTermFormUp(forms.ModelForm):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)

    def __init__(self, *args, **kwargs):
        super(ThirdTermFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['pupil'].required = False
            self.fields['pupil'].widget.attrs['disabled'] = 'disabled'
            # self.fields['classe'].required = False
            # self.fields['classe'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_pupil(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.pupil
        else:
            return self.cleaned_data.get('pupil', None)

    class Meta:
        model = ThirdTerm
        fields = ['session', 'pupil', 'literacy_ca1', 'literacy_ca2', 'literacy_exam',
            'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam', 'general_studies_ca1',
            'general_studies_ca2', 'general_studies_exam', 'science_ca1', 'science_ca2',
            'science_exam', 'number_present', 'concentration', 'responsiveness', 'comprehension', 'interest',
            'homework', 'reading', 'writing', 'spoken', 'innovative']
