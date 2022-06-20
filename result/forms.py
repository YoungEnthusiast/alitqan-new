from django import forms
from .models import First, Second, Third
from management.models import Subject

class FirstForm(forms.ModelForm):
    class Meta:
        model = First
        fields = ['session', 'subject', 'ca1', 'ca2', 'exam']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request") # store value of request
        super().__init__(*args, **kwargs)

        self.fields['subject'] = forms.ModelChoiceField(queryset=Subject.objects.filter(teacher=self.request.user))

class SecondForm(forms.ModelForm):
    class Meta:
        model = Second
        fields = ['session', 'subject', 'ca1', 'ca2', 'exam']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request") # store value of request
        super().__init__(*args, **kwargs)

        self.fields['subject'] = forms.ModelChoiceField(queryset=Subject.objects.filter(teacher=self.request.user))

class ThirdForm(forms.ModelForm):
    class Meta:
        model = Third
        fields = ['session', 'subject', 'ca1', 'ca2', 'exam']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request") # store value of request
        super().__init__(*args, **kwargs)

        self.fields['subject'] = forms.ModelChoiceField(queryset=Subject.objects.filter(teacher=self.request.user))

class FirstFormUp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FirstFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['subject'].required = False
            self.fields['subject'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = First
        fields = ['session', 'student', 'subject', 'ca1', 'ca2', 'exam']

class SecondFormUp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SecondFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['subject'].required = False
            self.fields['subject'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = Second
        fields = ['session', 'student', 'subject', 'ca1', 'ca2', 'exam']

class ThirdFormUp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ThirdFormUp, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['subject'].required = False
            self.fields['subject'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = Third
        fields = ['session', 'student', 'subject', 'ca1', 'ca2', 'exam']

class FirstFormBeha(forms.ModelForm):
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
    TEACHER_CHOICES = [
        ('It is my pleasure being his class teacher for his dedication to studies is on the highest level.', '(Above 79%) - It is my pleasure being his class teacher for his dedication to studies is on the highest level.'),
        ('It is my pleasure being her class teacher for her dedication to studies is on the highest level.', '(Above 79%) - It is my pleasure being her class teacher for her dedication to studies is on the highest level.'),
        ('It is my pleasure being your class teacher for your dedication to studies is on the highest level', '(Above 79%) - -	It is my pleasure being your class teacher for your dedication to studies is on the highest level'),
        ('His dedication to studies is topnotch! No wonder he has excellent grades throughout.', '(Above 79%) - His dedication to studies is topnotch! No wonder he has excellent grades throughout.'),
        ('Her dedication to studies is topnotch! No wonder she has excellent grades throughout.', '(Above 79%) - Her dedication to studies is topnotch! No wonder she has excellent grades throughout.'),
        ('What a start to his new class! His performance this term is really outstanding!', '(Above 79%) - What a start to his new class! His performance this term is really outstanding!'),
        ('What a start to her new class! Her performance this term is really outstanding!', '(Above 79%) - What a start to her new class! Her performance this term is really outstanding!'),
        ('What a start to your new class! Your performance this term is really outstanding!', '(Above 79%) - What a start to your new class! Your performance this term is really outstanding!'),

        ('What a great performance from him! He can perform even better next term.', '(Above 49%) - What a great performance from him! He can perform even better next term.'),
        ('What a great performance from her! She can perform even better next term.', '(Above 49%) - What a great performance from her! She can perform even better next term.'),
        ('He has worked very hard this term and I am proud of him of his accomplishments.', '(Above 49%) - He has worked very hard this term and I am proud of him of his accomplishments.'),
        ('She has worked very hard this term and I am proud of her of her accomplishments.', '(Above 49%) - She has worked very hard this term and I am proud of her of her accomplishments.'),
        ('His strength is evident in this result. I look forward for improvement in the weak areas', '(Above 49%) - His strength is evident in this result. I look forward for improvement in the weak areas'),
        ('Her strength is evident in this result. I look forward for improvement in the weak areas', '(Above 49%) - Her strength is evident in this result. I look forward for improvement in the weak areas'),
        ('He really tried with this result and I commend his attitude to learning. May Allah bless him.', '(Above 49%) - He really tried with this result and I commend his attitude to learning. May Allah bless him.'),
        ('She really tried with this result and I commend her attitude to learning. May Allah bless her.', '(Above 49%) - She really tried with this result and I commend her attitude to learning. May Allah bless her.'),
        ('I am so proud of him and wish him well in his academic subsequent terms.', '(Above 49%) - I am so proud of him and wish him well in his academic subsequent terms.'),
        ('I am so proud of her and wish her well in her academic subsequent terms.', '(Above 49%) - I am so proud of her and wish her well in her academic subsequent terms.'),
        ('I am so proud of you and wish you well in your academic subsequent terms.', '(Above 49%) - I am so proud of you and wish you well in your academic subsequent terms.'),

        ('His efforts fall short of the required level, he should try to upgrade his performance next term.', '(Below 50%) - His efforts fall short of the required level, he should try to upgrade his performance next term.'),
        ('Her efforts fall short of the required level, she should try to upgrade her performance next term.', '(Below 50%) - Her efforts fall short of the required level, she should try to upgrade her performance next term.'),
        ('Your efforts fall short of the required level, try to upgrade your performance next term.', '(Below 50%) - Your efforts fall short of the required level, try to upgrade your performance next term.'),
        ('I have truly enjoyed being his teacher and hope for improvement next term.', '(Below 50%) - I have truly enjoyed being his teacher and hope for improvement next term.'),
        ('I have truly enjoyed being her teacher and hope for improvement next term.', '(Below 50%) - I have truly enjoyed being her teacher and hope for improvement next term.'),
        ('He is really trying, but he needs to do more for a better result.', '(Below 50%) - He is really trying, but he needs to do more for a better result.'),
        ('She is really trying, but she needs to do more for a better result.', '(Below 50%) - She is really trying, but she needs to do more for a better result.'),
    ]

    HEAD_CHOICES = [
        ('A praiseworthy performance! Keep it up. May Allah bless you.', '(Above 95%) - A praiseworthy performance! Keep it up. May Allah bless you.'),
        ('Surely, this is a five-star performance. May Allah bless him.', '(Above 95%) - Surely, this is a five-star performance. May Allah bless him.'),
        ('Surely, this is a five-star performance. May Allah bless her.', '(Above 95%) - Surely, this is a five-star performance. May Allah bless her.'),
        ('Maa sha Allah, this is awesome! May Allah bless him.', '(Above 95%) - Maa sha Allah, this is awesome! May Allah bless him.'),
        ('Maa sha Allah, this is awesome! May Allah bless her.', '(Above 95%) - Maa sha Allah, this is awesome! May Allah bless her.'),
        ('Maa sha Allah, this is very impressive! The sky is surely your starting point. May Allah bless you.', '(Above 95%) - Maa sha Allah, this is very impressive! The sky is surely your starting point. May Allah bless you.'),
        ('An excellent performance. He surely deserves a treat. May Allah bless him.', '(Above 95%) - An excellent performance. He surely deserves a treat. May Allah bless him.'),
        ('An excellent performance. She surely deserves a treat. May Allah bless her.', '(Above 95%) - An excellent performance. She surely deserves a treat. May Allah bless her.'),

        ('A deserving result for a child who has been wonderful. May Allah bless him.', '(Above 80%) - A deserving result for a child who has been wonderful. May Allah bless him.'),
        ('A deserving result for a child who has been wonderful. May Allah bless her.', '(Above 80%) - A deserving result for a child who has been wonderful. May Allah bless her.'),
        ('A praiseworthy performance! You deserve all credits. May Allah bless you.', '(Above 80%) - A praiseworthy performance! You deserve all credits. May Allah bless you.'),
        ('Great performance! This result shows how wonderful he is. May Allah bless him.', '(Above 80%) - Great performance! This result shows how wonderful he is. May Allah bless him.'),
        ('Great performance! This result shows how wonderful she is. May Allah bless her.', '(Above 80%) - Great performance! This result shows how wonderful she is. May Allah bless her.'),
        ('Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.', '(Above 80%) - Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.'),
        ('This is an excellent performance! Thumbs up. May Allah bless you.', '(Above 80%) - This is an excellent performance! Thumbs up. May Allah bless you.'),

        ('I believe he will do better next term. He can, actually. May Allah bless him.', '(Above 50%) - I believe he will do better next term. He can, actually. May Allah bless him.'),
        ('I believe she will do better next term. She can, actually. May Allah bless her.', '(Above 50%) - I believe she will do better next term. She can, actually. May Allah bless her'),
        ('What a beginning! I believe the future is promising. May Allah bless him.', '(Above 50%) - What a beginning! I believe the future is promising. May Allah bless him.'),
        ('What a beginning! I believe the future is promising. May Allah bless her.', '(Above 50%) - What a beginning! I believe the future is promising. May Allah bless her.'),
        ('What a good performance! Keep it up. May Allah bless you.', '(Above 50%) - What a good performance! Keep it up. May Allah bless you.'),
        ('Great effort. I hope to see more next term. May Allah bless you.', '(Above 50%) - Great effort. I hope to see more next term. May Allah bless you.'),

        ('He can do better next term; he needs to. May Allah make that an easy one for him.', '(Below 50%) - He can do better next term; he needs to. May Allah make that an easy one for him.'),
        ('She can do better next term; she needs to. May Allah make that an easy one for her.', '(Below 50%) - She can do better next term; she needs to. May Allah make that an easy one for her.'),
        ('His performance is not bad, but he needs to try harder. May he accomplish that with ease.', '(Below 50%) - His performance is not bad, but he needs to try harder. May he accomplish that with ease.'),
        ('Her performance is not bad, but she needs to try harder. May she accomplish that with ease.', '(Below 50%) - Her performance is not bad, but she needs to try harder. May she accomplish that with ease.'),
        ('Your performance is not that poor as a fresher. But try to improve your performance next term.', '(Below 50%) - Your performance is not that poor as a fresher. But try to improve your performance next term.'),
        ('The adventure just begins; nothing to worry about. You will excel in sha Allah.', '(Below 50%) - The adventure just begins; nothing to worry about. You will excel in sha Allah.'),
    ]

    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken Arabic/English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)


    def __init__(self, *args, **kwargs):
        super(FirstFormBeha, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = First
        fields = ['session', 'student', 'number_present', 'concentration', 'responsiveness', 'comprehension',
        'interest', 'homework', 'reading', 'writing', 'spoken', 'innovative', 'teacher_comment']

class SecondFormBeha(forms.ModelForm):
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
    TEACHER_CHOICES = [
        ('It is my pleasure being his class teacher for his dedication to studies is on the highest level.', '(Above 79%) - It is my pleasure being his class teacher for his dedication to studies is on the highest level.'),
        ('It is my pleasure being her class teacher for her dedication to studies is on the highest level.', '(Above 79%) - It is my pleasure being her class teacher for her dedication to studies is on the highest level.'),
        ('It is my pleasure being your class teacher for your dedication to studies is on the highest level', '(Above 79%) - -	It is my pleasure being your class teacher for your dedication to studies is on the highest level'),
        ('His dedication to studies is topnotch! No wonder he has excellent grades throughout.', '(Above 79%) - His dedication to studies is topnotch! No wonder he has excellent grades throughout.'),
        ('Her dedication to studies is topnotch! No wonder she has excellent grades throughout.', '(Above 79%) - Her dedication to studies is topnotch! No wonder she has excellent grades throughout.'),
        ('What a start to his new class! His performance this term is really outstanding!', '(Above 79%) - What a start to his new class! His performance this term is really outstanding!'),
        ('What a start to her new class! Her performance this term is really outstanding!', '(Above 79%) - What a start to her new class! Her performance this term is really outstanding!'),
        ('What a start to your new class! Your performance this term is really outstanding!', '(Above 79%) - What a start to your new class! Your performance this term is really outstanding!'),

        ('What a great performance from him! He can perform even better next term.', '(Above 49%) - What a great performance from him! He can perform even better next term.'),
        ('What a great performance from her! She can perform even better next term.', '(Above 49%) - What a great performance from her! She can perform even better next term.'),
        ('He has worked very hard this term and I am proud of him of his accomplishments.', '(Above 49%) - He has worked very hard this term and I am proud of him of his accomplishments.'),
        ('She has worked very hard this term and I am proud of her of her accomplishments.', '(Above 49%) - She has worked very hard this term and I am proud of her of her accomplishments.'),
        ('His strength is evident in this result. I look forward for improvement in the weak areas', '(Above 49%) - His strength is evident in this result. I look forward for improvement in the weak areas'),
        ('Her strength is evident in this result. I look forward for improvement in the weak areas', '(Above 49%) - Her strength is evident in this result. I look forward for improvement in the weak areas'),
        ('He really tried with this result and I commend his attitude to learning. May Allah bless him.', '(Above 49%) - He really tried with this result and I commend his attitude to learning. May Allah bless him.'),
        ('She really tried with this result and I commend her attitude to learning. May Allah bless her.', '(Above 49%) - She really tried with this result and I commend her attitude to learning. May Allah bless her.'),
        ('I am so proud of him and wish him well in his academic subsequent terms.', '(Above 49%) - I am so proud of him and wish him well in his academic subsequent terms.'),
        ('I am so proud of her and wish her well in her academic subsequent terms.', '(Above 49%) - I am so proud of her and wish her well in her academic subsequent terms.'),
        ('I am so proud of you and wish you well in your academic subsequent terms.', '(Above 49%) - I am so proud of you and wish you well in your academic subsequent terms.'),

        ('His efforts fall short of the required level, he should try to upgrade his performance next term.', '(Below 50%) - His efforts fall short of the required level, he should try to upgrade his performance next term.'),
        ('Her efforts fall short of the required level, she should try to upgrade her performance next term.', '(Below 50%) - Her efforts fall short of the required level, she should try to upgrade her performance next term.'),
        ('Your efforts fall short of the required level, try to upgrade your performance next term.', '(Below 50%) - Your efforts fall short of the required level, try to upgrade your performance next term.'),
        ('I have truly enjoyed being his teacher and hope for improvement next term.', '(Below 50%) - I have truly enjoyed being his teacher and hope for improvement next term.'),
        ('I have truly enjoyed being her teacher and hope for improvement next term.', '(Below 50%) - I have truly enjoyed being her teacher and hope for improvement next term.'),
        ('He is really trying, but he needs to do more for a better result.', '(Below 50%) - He is really trying, but he needs to do more for a better result.'),
        ('She is really trying, but she needs to do more for a better result.', '(Below 50%) - She is really trying, but she needs to do more for a better result.'),
    ]

    HEAD_CHOICES = [
        ('A praiseworthy performance! Keep it up. May Allah bless you.', '(Above 95%) - A praiseworthy performance! Keep it up. May Allah bless you.'),
        ('Surely, this is a five-star performance. May Allah bless him.', '(Above 95%) - Surely, this is a five-star performance. May Allah bless him.'),
        ('Surely, this is a five-star performance. May Allah bless her.', '(Above 95%) - Surely, this is a five-star performance. May Allah bless her.'),
        ('Maa sha Allah, this is awesome! May Allah bless him.', '(Above 95%) - Maa sha Allah, this is awesome! May Allah bless him.'),
        ('Maa sha Allah, this is awesome! May Allah bless her.', '(Above 95%) - Maa sha Allah, this is awesome! May Allah bless her.'),
        ('Maa sha Allah, this is very impressive! The sky is surely your starting point. May Allah bless you.', '(Above 95%) - Maa sha Allah, this is very impressive! The sky is surely your starting point. May Allah bless you.'),
        ('An excellent performance. He surely deserves a treat. May Allah bless him.', '(Above 95%) - An excellent performance. He surely deserves a treat. May Allah bless him.'),
        ('An excellent performance. She surely deserves a treat. May Allah bless her.', '(Above 95%) - An excellent performance. She surely deserves a treat. May Allah bless her.'),

        ('A deserving result for a child who has been wonderful. May Allah bless him.', '(Above 80%) - A deserving result for a child who has been wonderful. May Allah bless him.'),
        ('A deserving result for a child who has been wonderful. May Allah bless her.', '(Above 80%) - A deserving result for a child who has been wonderful. May Allah bless her.'),
        ('A praiseworthy performance! You deserve all credits. May Allah bless you.', '(Above 80%) - A praiseworthy performance! You deserve all credits. May Allah bless you.'),
        ('Great performance! This result shows how wonderful he is. May Allah bless him.', '(Above 80%) - Great performance! This result shows how wonderful he is. May Allah bless him.'),
        ('Great performance! This result shows how wonderful she is. May Allah bless her.', '(Above 80%) - Great performance! This result shows how wonderful she is. May Allah bless her.'),
        ('Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.', '(Above 80%) - Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.'),
        ('This is an excellent performance! Thumbs up. May Allah bless you.', '(Above 80%) - This is an excellent performance! Thumbs up. May Allah bless you.'),

        ('I believe he will do better next term. He can, actually. May Allah bless him.', '(Above 50%) - I believe he will do better next term. He can, actually. May Allah bless him.'),
        ('I believe she will do better next term. She can, actually. May Allah bless her.', '(Above 50%) - I believe she will do better next term. She can, actually. May Allah bless her'),
        ('What a beginning! I believe the future is promising. May Allah bless him.', '(Above 50%) - What a beginning! I believe the future is promising. May Allah bless him.'),
        ('What a beginning! I believe the future is promising. May Allah bless her.', '(Above 50%) - What a beginning! I believe the future is promising. May Allah bless her.'),
        ('What a good performance! Keep it up. May Allah bless you.', '(Above 50%) - What a good performance! Keep it up. May Allah bless you.'),
        ('Great effort. I hope to see more next term. May Allah bless you.', '(Above 50%) - Great effort. I hope to see more next term. May Allah bless you.'),

        ('He can do better next term; he needs to. May Allah make that an easy one for him.', '(Below 50%) - He can do better next term; he needs to. May Allah make that an easy one for him.'),
        ('She can do better next term; she needs to. May Allah make that an easy one for her.', '(Below 50%) - She can do better next term; she needs to. May Allah make that an easy one for her.'),
        ('His performance is not bad, but he needs to try harder. May he accomplish that with ease.', '(Below 50%) - His performance is not bad, but he needs to try harder. May he accomplish that with ease.'),
        ('Her performance is not bad, but she needs to try harder. May she accomplish that with ease.', '(Below 50%) - Her performance is not bad, but she needs to try harder. May she accomplish that with ease.'),
        ('Your performance is not that poor as a fresher. But try to improve your performance next term.', '(Below 50%) - Your performance is not that poor as a fresher. But try to improve your performance next term.'),
        ('The adventure just begins; nothing to worry about. You will excel in sha Allah.', '(Below 50%) - The adventure just begins; nothing to worry about. You will excel in sha Allah.'),
    ]

    concentration = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    responsiveness = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    comprehension = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    interest = forms.ChoiceField(label="Interest in Learning", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    homework = forms.ChoiceField(label="Homework Completion", choices=ATTITUDE_CHOICES, widget=forms.RadioSelect, required=False)
    reading = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    writing = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    spoken = forms.ChoiceField(label="Spoken Arabic/English", choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)
    innovative = forms.ChoiceField(choices=SCHOLASTIC_CHOICES, widget=forms.RadioSelect, required=False)


    def __init__(self, *args, **kwargs):
        super(SecondFormBeha, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = Second
        fields = ['session', 'student', 'number_present', 'concentration', 'responsiveness', 'comprehension',
        'interest', 'homework', 'reading', 'writing', 'spoken', 'innovative', 'teacher_comment']

class FirstFormHead(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FirstFormHead, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = First
        fields = ['session', 'student', 'head_comment']

class SecondFormHead(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SecondFormHead, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = Second
        fields = ['session', 'student', 'head_comment']

class FirstFormPay(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FirstFormPay, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = First
        fields = ['session', 'student', 'school_fees']

class SecondFormPay(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SecondFormPay, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['session'].required = False
            self.fields['session'].widget.attrs['disabled'] = 'disabled'
            self.fields['student'].required = False
            self.fields['student'].widget.attrs['disabled'] = 'disabled'

    def clean_session(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.session
        else:
            return self.cleaned_data.get('session', None)

    def clean_subject(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.subject
        else:
            return self.cleaned_data.get('subject', None)

    def clean_student(self):
        instance = getattr(self, 'instance', None)
        if instance:
            return instance.student
        else:
            return self.cleaned_data.get('student', None)

    class Meta:
        model = Second
        fields = ['session', 'student', 'school_fees']
