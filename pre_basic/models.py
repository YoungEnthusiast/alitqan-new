from django.db import models
from django.contrib.auth.models import User
import random

class FirstTerm(models.Model):
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
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True, related_name="pre_basic_session")
    pupil = models.OneToOneField('records.Pupil', on_delete = models.SET_NULL, unique = True, null=True, related_name="pre_basic_pupil")
    school_fees = models.BooleanField(max_length=5, default = False)
    literacy_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (1st CA)")
    numeracy_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (1st CA)")
    general_studies_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (1st CA)")
    science_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (1st CA)")
    literacy_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (2nd CA)")
    numeracy_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (2nd CA)")
    general_studies_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (2nd CA)")
    science_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (2nd CA)")
    literacy_exam = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (EXAM)")
    numeracy_exam = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (EXAM)")
    general_studies_exam = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (EXAM)")
    science_exam = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (EXAM)")
    numeracy_tot = models.IntegerField(blank=True, default = 0)
    literacy_tot = models.IntegerField(blank=True, default = 0)
    general_studies_tot = models.IntegerField(blank=True, default = 0)
    science_tot = models.IntegerField(blank=True, default = 0)
    cumulative = models.IntegerField(blank=True, default = 0)
    number_present = models.CharField(max_length=8, blank=True, null=True, verbose_name="No of Days Present")
    concentration = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    responsiveness = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    comprehension = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    interest = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True, verbose_name="Interest in Learning")
    homework = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True, verbose_name="Homework Completion")
    reading = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    writing = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    spoken = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True, verbose_name="Spoken English")
    innovative = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('pupil__user__username',)
        verbose_name = "First Term Score"
        verbose_name_plural = "First Term Scores"

    def grade_literacy(self):
        if self.literacy_tot < 50:
            return "E"
        elif self.literacy_tot >= 50 and self.literacy_tot < 60:
            return "D"
        elif self.literacy_tot >= 60 and self.literacy_tot < 70:
            return "C"
        elif self.literacy_tot >= 70 and self.literacy_tot < 85:
            return "B"
        else:
            return "A"

    def grade_numeracy(self):
        if self.numeracy_tot < 50:
            return "E"
        elif self.numeracy_tot >= 50 and self.numeracy_tot < 60:
            return "D"
        elif self.numeracy_tot >= 60 and self.numeracy_tot < 70:
            return "C"
        elif self.numeracy_tot >= 70 and self.numeracy_tot < 85:
            return "B"
        else:
            return "A"

    def grade_general_studies(self):
        if self.general_studies_tot < 50:
            return "E"
        elif self.general_studies_tot >= 50 and self.general_studies_tot < 60:
            return "D"
        elif self.general_studies_tot >= 60 and self.general_studies_tot < 70:
            return "C"
        elif self.general_studies_tot >= 70 and self.general_studies_tot < 85:
            return "B"
        else:
            return "A"

    def grade_science(self):
        if self.science_tot < 50:
            return "E"
        elif self.science_tot >= 50 and self.science_tot < 60:
            return "D"
        elif self.science_tot >= 60 and self.science_tot < 70:
            return "C"
        elif self.science_tot >= 70 and self.science_tot < 85:
            return "B"
        else:
            return "A"

    def grade_general(self):
        if self.cumulative/4 < 50:
            return "Poor"
        elif self.cumulative/4 >= 50 and self.cumulative/4 < 60:
            return "Average"
        elif self.cumulative/4 >= 60 and self.cumulative/4 < 70:
            return "Good"
        elif self.cumulative/4 >= 70 and self.cumulative/4 < 85:
            return "Very Good"
        else:
            return "Excellent"

    def teacher_comment(self):
        if self.pupil.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.pupil.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.pupil.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Dear " + self.pupil.user.first_name + "! Your efforts fall short of the required level, try to upgrade your performance next term.",
            "I have truly enjoyed being " + self.pupil.user.first_name + "'s teacher and hope for improvement next term.",
            self.pupil.user.first_name + " is really trying, but " + pronoun0 + " needs to do more for a better result."]
        choices_60 = [self.pupil.user.first_name + ", I believe you can do better than this. We can’t wait for your improvement next term!",
            self.pupil.user.first_name + " is a valued member of the class. Significant improvement in " + pronoun + " commitment to studies will make " + pronoun2 + " great.",
            "Great effort, " + self.pupil.user.first_name + "! Consistency will make your performance better. I wish you all the best.",
            "Dear " + self.pupil.user.first_name + "! Ability to stay on task without distraction will guarantee better result. Hope that would be achieved next term."]
        choices_80 = ["What a great performance from you, " + self.pupil.user.first_name + "! You can perform even better next term.",
            self.pupil.user.first_name + " has worked very hard this term and I am proud of all of " + pronoun + " accomplishments.",
            self.pupil.user.first_name + "'s strength is evident in this result. I look forward for improvement in the weak areas.",
            self.pupil.user.first_name + ", you really tried with this result and I commend your attitude to learning. May Allah bless you.",
            "I am so proud of you " + self.pupil.user.first_name +  ", and wish you well in your academics subsequent terms."]
        choices_else = ["It is my pleasure being " + self.pupil.user.first_name + "'s class teacher for " + pronoun + " zeal to study is on the highest level!",
            self.pupil.user.first_name + "'s dedication to study is topnotch! No wonder " + pronoun0 + " has excellent grades throughout.",
            "What an excellent result! " + self.pupil.user.first_name + "'s  performance this term is really outstanding!"]

        if self.cumulative/4 < 50:
            return random.choice(choices_50)
        elif self.cumulative/4 >= 50 and self.cumulative/4 < 60:
            return random.choice(choices_60)
        elif self.cumulative/4 >= 60 and self.cumulative/4 < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

    def head_comment(self):
        if self.pupil.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.pupil.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.pupil.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Your performance is not bad, but you need to try harder. May you accomplish that with ease.",
            "You can do better next term; you need to. May Allah make that an easy one for you.",
            "Your performance is not that poor as a fresher. But try to improve your performance next term.",
            "The adventure just begins; nothing to worry about. You will excel in sha Allah."]
        choices_60 = ["I believe you will do better next term. You can, actually. May Allah bless you.",
            "What a good performance! Keep it up. May Allah bless you.",
            "Great effort. I hope to see more next term. May Allah bless you.",
            "What a beginning! I believe the future is promising. May Allah bless you."]
        choices_80 = ["A deserving result for a child who has been wonderful. May Allah bless you.",
            "A praiseworthy performance! You deserve all credits. May Allah bless you.",
            "Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.",
            "This is an excellent performance. Thumbs up. May Allah bless you.",
            "Great performance. This result shows how wonderful you are. May Allah bless you."]
        choices_else = ["A praiseworthy performance! Keep it up. May Allah bless you.",
            "Surely, this is a five-star performance! May Allah bless you.",
            "Maa sha Allah, this is awesome! May Allah bless you.",
            "Maa sha Allah, this is impressive! The sky is surely your starting point. May Allah bless you."]

        if self.cumulative/4 < 50:
            return random.choice(choices_50)
        elif self.cumulative/4 >= 50 and self.cumulative/4 < 60:
            return random.choice(choices_60)
        elif self.cumulative/4 >= 60 and self.cumulative/4 < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

    def cum_perc(self):
        return str(round((self.cumulative/4),2))


    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'pk': self.pk})

class SecondTerm(models.Model):
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
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True)
    pupil = models.OneToOneField('records.Pupil', on_delete = models.SET_NULL, unique = True, null=True)
    school_fees = models.BooleanField(max_length=5, default = False)
    literacy_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (1st CA)")
    numeracy_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (1st CA)")
    general_studies_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (1st CA)")
    science_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (1st CA)")
    literacy_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (2nd CA)")
    numeracy_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (2nd CA)")
    general_studies_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (2nd CA)")
    science_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (2nd CA)")
    literacy_exam = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (EXAM)")
    numeracy_exam = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (EXAM)")
    general_studies_exam = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (EXAM)")
    science_exam = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (EXAM)")
    numeracy_tot = models.IntegerField(blank=True, default = 0)
    literacy_tot = models.IntegerField(blank=True, default = 0)
    general_studies_tot = models.IntegerField(blank=True, default = 0)
    science_tot = models.IntegerField(blank=True, default = 0)
    cumulative = models.IntegerField(blank=True, default = 0)
    number_present = models.CharField(max_length=8, blank=True, null=True, verbose_name="No of Days Present")
    concentration = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    responsiveness = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    comprehension = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    interest = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True, verbose_name="Interest in Learning")
    homework = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True, verbose_name="Homework Completion")
    reading = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    writing = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    spoken = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True, verbose_name="Spoken English")
    innovative = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('pupil__user__username',)
        verbose_name = "Second Term Score"
        verbose_name_plural = "Second Term Scores"

    def grade_literacy(self):
        if self.literacy_tot < 50:
            return "E"
        elif self.literacy_tot >= 50 and self.literacy_tot < 60:
            return "D"
        elif self.literacy_tot >= 60 and self.literacy_tot < 70:
            return "C"
        elif self.literacy_tot >= 70 and self.literacy_tot < 85:
            return "B"
        else:
            return "A"

    def grade_numeracy(self):
        if self.numeracy_tot < 50:
            return "E"
        elif self.numeracy_tot >= 50 and self.numeracy_tot < 60:
            return "D"
        elif self.numeracy_tot >= 60 and self.numeracy_tot < 70:
            return "C"
        elif self.numeracy_tot >= 70 and self.numeracy_tot < 85:
            return "B"
        else:
            return "A"

    def grade_general_studies(self):
        if self.general_studies_tot < 50:
            return "E"
        elif self.general_studies_tot >= 50 and self.general_studies_tot < 60:
            return "D"
        elif self.general_studies_tot >= 60 and self.general_studies_tot < 70:
            return "C"
        elif self.general_studies_tot >= 70 and self.general_studies_tot < 85:
            return "B"
        else:
            return "A"

    def grade_science(self):
        if self.science_tot < 50:
            return "E"
        elif self.science_tot >= 50 and self.science_tot < 60:
            return "D"
        elif self.science_tot >= 60 and self.science_tot < 70:
            return "C"
        elif self.science_tot >= 70 and self.science_tot < 85:
            return "B"
        else:
            return "A"

    def grade_general(self):
        if self.cumulative/4 < 50:
            return "Poor"
        elif self.cumulative/4 >= 50 and self.cumulative/4 < 60:
            return "Average"
        elif self.cumulative/4 >= 60 and self.cumulative/4 < 70:
            return "Good"
        elif self.cumulative/4 >= 70 and self.cumulative/4 < 85:
            return "Very Good"
        else:
            return "Excellent"

    def teacher_comment(self):
        if self.pupil.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.pupil.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.pupil.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Dear " + self.pupil.user.first_name + "! Your efforts fall short of the required level, try to upgrade your performance next term.",
            "I have truly enjoyed being " + self.pupil.user.first_name + "'s teacher and hope for improvement next term.",
            self.pupil.user.first_name + " is really trying, but " + pronoun0 + " needs to do more for a better result."]
        choices_60 = [self.pupil.user.first_name + ", I believe you can do better than this. We can’t wait for your improvement next term!",
            self.pupil.user.first_name + " is a valued member of the class. Significant improvement in " + pronoun + " commitment to studies will make " + pronoun2 + " great.",
            "Great effort, " + self.pupil.user.first_name + "! Consistency will make your performance better. I wish you all the best.",
            "Dear " + self.pupil.user.first_name + "! Ability to stay on task without distraction will guarantee better result. Hope that would be achieved next term."]
        choices_80 = ["What a great performance from you, " + self.pupil.user.first_name + "! You can perform even better next term.",
            self.pupil.user.first_name + " has worked very hard this term and I am proud of all of " + pronoun + " accomplishments.",
            self.pupil.user.first_name + "'s strength is evident in this result. I look forward for improvement in the weak areas.",
            self.pupil.user.first_name + ", you really tried with this result and I commend your attitude to learning. May Allah bless you.",
            "I am so proud of you " + self.pupil.user.first_name +  ", and wish you well in your academics subsequent terms."]
        choices_else = ["It is my pleasure being " + self.pupil.user.first_name + "'s class teacher for " + pronoun + " zeal to study is on the highest level!",
            self.pupil.user.first_name + "'s dedication to study is topnotch! No wonder " + pronoun0 + " has excellent grades throughout.",
            "What an excellent result! " + self.pupil.user.first_name + "'s  performance this term is really outstanding!"]

        if self.cumulative/4 < 50:
            return random.choice(choices_50)
        elif self.cumulative/4 >= 50 and self.cumulative/4 < 60:
            return random.choice(choices_60)
        elif self.cumulative/4 >= 60 and self.cumulative/4 < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

    def head_comment(self):
        if self.pupil.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.pupil.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.pupil.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Your performance is not bad, but you need to try harder. May you accomplish that with ease.",
            "You can do better next term; you need to. May Allah make that an easy one for you.",
            "Your performance is not that poor as a fresher. But try to improve your performance next term.",
            "The adventure just begins; nothing to worry about. You will excel in sha Allah."]
        choices_60 = ["I believe you will do better next term. You can, actually. May Allah bless you.",
            "What a good performance! Keep it up. May Allah bless you.",
            "Great effort. I hope to see more next term. May Allah bless you.",
            "What a beginning! I believe the future is promising. May Allah bless you."]
        choices_80 = ["A deserving result for a child who has been wonderful. May Allah bless you.",
            "A praiseworthy performance! You deserve all credits. May Allah bless you.",
            "Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.",
            "This is an excellent performance. Thumbs up. May Allah bless you.",
            "Great performance. This result shows how wonderful you are. May Allah bless you."]
        choices_else = ["A praiseworthy performance! Keep it up. May Allah bless you.",
            "Surely, this is a five-star performance! May Allah bless you.",
            "Maa sha Allah, this is awesome! May Allah bless you.",
            "Maa sha Allah, this is impressive! The sky is surely your starting point. May Allah bless you."]

        if self.cumulative/4 < 50:
            return random.choice(choices_50)
        elif self.cumulative/4 >= 50 and self.cumulative/4 < 60:
            return random.choice(choices_60)
        elif self.cumulative/4 >= 60 and self.cumulative/4 < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

    def cum_perc(self):
        return str(round((self.cumulative/4),2))

class ThirdTerm(models.Model):
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
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True)
    pupil = models.OneToOneField('records.Pupil', on_delete = models.SET_NULL, unique = True, null=True)
    school_fees = models.BooleanField(max_length=5, default = False)
    literacy_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (1st CA)")
    numeracy_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (1st CA)")
    general_studies_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (1st CA)")
    science_ca1 = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (1st CA)")
    literacy_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (2nd CA)")
    numeracy_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (2nd CA)")
    general_studies_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (2nd CA)")
    science_ca2 = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (2nd CA)")
    literacy_exam = models.IntegerField(blank=True, default = 0, verbose_name="Literacy (EXAM)")
    numeracy_exam = models.IntegerField(blank=True, default = 0, verbose_name="Numeracy (EXAM)")
    general_studies_exam = models.IntegerField(blank=True, default = 0, verbose_name="General Studies (EXAM)")
    science_exam = models.IntegerField(blank=True, default = 0, verbose_name="Science and Health (EXAM)")
    numeracy_tot = models.IntegerField(blank=True, default = 0)
    numeracy_tot1 = models.IntegerField(blank=True, null=True, default = 0)
    numeracy_tot2 = models.IntegerField(blank=True, null=True, default = 0)
    numeracy_cum = models.IntegerField(blank=True, default = 0)
    literacy_tot = models.IntegerField(blank=True, default = 0)
    literacy_tot1 = models.IntegerField(blank=True, null=True, default = 0)
    literacy_tot2 = models.IntegerField(blank=True, null=True, default = 0)
    literacy_cum = models.IntegerField(blank=True, default = 0)
    general_studies_tot = models.IntegerField(blank=True, default = 0)
    general_studies_tot1 = models.IntegerField(blank=True, null=True, default = 0)
    general_studies_tot2 = models.IntegerField(blank=True, null=True, default = 0)
    general_studies_cum = models.IntegerField(blank=True, default = 0)
    science_tot = models.IntegerField(blank=True, default = 0)
    science_tot1 = models.IntegerField(blank=True, null=True, default = 0)
    science_tot2 = models.IntegerField(blank=True, null=True, default = 0)
    science_cum = models.IntegerField(blank=True, default = 0)
    cumulative = models.IntegerField(blank=True, default = 0)
    cumulative_1st = models.IntegerField(blank=True, null=True, default = 0, verbose_name="1st Cumulative")
    cumulative_2nd = models.IntegerField(blank=True, null=True, default = 0, verbose_name="2nd Cumulative")
    all_cumulative = models.IntegerField(blank=True, default = 0)
    cum_perc = models.IntegerField(blank=True, default = 0)
    number_present = models.CharField(max_length=8, blank=True, null=True, verbose_name="No of Days Present")
    concentration = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    responsiveness = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    comprehension = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True)
    interest = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True, verbose_name="Interest in Learning")
    homework = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, null=True, verbose_name="Homework Completion")
    reading = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    writing = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    spoken = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True, verbose_name="Spoken English")
    innovative = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username)
        except:
            return str(self.id)

    class Meta:
        ordering = ('pupil__user__username',)
        verbose_name = "Third Term Score"
        verbose_name_plural = "Third Term Scores"

    def grade_literacy(self):
        if self.literacy_cum < 50:
            return "E"
        elif self.literacy_cum >= 50 and self.literacy_cum < 60:
            return "D"
        elif self.literacy_cum >= 60 and self.literacy_cum < 70:
            return "C"
        elif self.literacy_cum >= 70 and self.literacy_cum < 85:
            return "B"
        else:
            return "A"

    def grade_numeracy(self):
        if self.numeracy_cum < 50:
            return "E"
        elif self.numeracy_cum >= 50 and self.numeracy_cum < 60:
            return "D"
        elif self.numeracy_cum >= 60 and self.numeracy_cum < 70:
            return "C"
        elif self.numeracy_cum >= 70 and self.numeracy_cum < 85:
            return "B"
        else:
            return "A"

    def grade_general_studies(self):
        if self.general_studies_cum < 50:
            return "E"
        elif self.general_studies_cum >= 50 and self.general_studies_cum < 60:
            return "D"
        elif self.general_studies_cum >= 60 and self.general_studies_cum < 70:
            return "C"
        elif self.general_studies_cum >= 70 and self.general_studies_cum < 85:
            return "B"
        else:
            return "A"

    def grade_science(self):
        if self.science_cum < 50:
            return "E"
        elif self.science_cum >= 50 and self.science_cum < 60:
            return "D"
        elif self.science_cum >= 60 and self.science_cum < 70:
            return "C"
        elif self.science_cum >= 70 and self.science_cum < 85:
            return "B"
        else:
            return "A"

    def grade_general(self):
        if self.cum_perc < 50:
            return "Poor"
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return "Average"
        elif self.cum_perc >= 60 and self.cum_perc < 70:
            return "Good"
        elif self.cum_perc >= 70 and self.cum_perc < 85:
            return "Very Good"
        else:
            return "Excellent"

    def teacher_comment(self):
        if self.pupil.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.pupil.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.pupil.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Dear " + self.pupil.user.first_name + "! Your efforts fall short of the required level, try to upgrade your performance next term.",
            "I have truly enjoyed being " + self.pupil.user.first_name + "'s teacher and hope for improvement next term.",
            self.pupil.user.first_name + " is really trying, but " + pronoun0 + " needs to do more for a better result."]
        choices_60 = [self.pupil.user.first_name + ", I believe you can do better than this. We can’t wait for your improvement next term!",
            self.pupil.user.first_name + " is a valued member of the class. Significant improvement in " + pronoun + " commitment to studies will make " + pronoun2 + " great.",
            "Great effort, " + self.pupil.user.first_name + "! Consistency will make your performance better. I wish you all the best.",
            "Dear " + self.pupil.user.first_name + "! Ability to stay on task without distraction will guarantee better result. Hope that would be achieved next term."]
        choices_80 = ["What a great performance from you, " + self.pupil.user.first_name + "! You can perform even better next term.",
            self.pupil.user.first_name + " has worked very hard this term and I am proud of all of " + pronoun + " accomplishments.",
            self.pupil.user.first_name + "'s strength is evident in this result. I look forward for improvement in the weak areas.",
            self.pupil.user.first_name + ", you really tried with this result and I commend your attitude to learning. May Allah bless you.",
            "I am so proud of you " + self.pupil.user.first_name +  ", and wish you well in your academics subsequent terms."]
        choices_else = ["It is my pleasure being " + self.pupil.user.first_name + "'s class teacher for " + pronoun + " zeal to study is on the highest level!",
            self.pupil.user.first_name + "'s dedication to study is topnotch! No wonder " + pronoun0 + " has excellent grades throughout.",
            "What an excellent result! " + self.pupil.user.first_name + "'s  performance this term is really outstanding!"]

        if self.cum_perc < 50:
            return random.choice(choices_50)
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return random.choice(choices_60)
        elif self.cum_perc >= 60 and self.cum_perc < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

    def head_comment(self):
        if self.pupil.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.pupil.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.pupil.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Your performance is not bad, but you need to try harder. May you accomplish that with ease.",
            "You can do better next term; you need to. May Allah make that an easy one for you.",
            "Your performance is not that poor as a fresher. But try to improve your performance next term.",
            "The adventure just begins; nothing to worry about. You will excel in sha Allah."]
        choices_60 = ["I believe you will do better next term. You can, actually. May Allah bless you.",
            "What a good performance! Keep it up. May Allah bless you.",
            "Great effort. I hope to see more next term. May Allah bless you.",
            "What a beginning! I believe the future is promising. May Allah bless you."]
        choices_80 = ["A deserving result for a child who has been wonderful. May Allah bless you.",
            "A praiseworthy performance! You deserve all credits. May Allah bless you.",
            "Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.",
            "This is an excellent performance. Thumbs up. May Allah bless you.",
            "Great performance. This result shows how wonderful you are. May Allah bless you."]
        choices_else = ["A praiseworthy performance! Keep it up. May Allah bless you.",
            "Surely, this is a five-star performance! May Allah bless you.",
            "Maa sha Allah, this is awesome! May Allah bless you.",
            "Maa sha Allah, this is impressive! The sky is surely your starting point. May Allah bless you."]

        if self.cum_perc < 50:
            return random.choice(choices_50)
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return random.choice(choices_60)
        elif self.cum_perc >= 60 and self.cum_perc < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

    def head_comment2(self):
        if self.literacy_cum < 50 and self.numeracy_cum < 50:
            return "To repeat the class!"
        elif self.general_studies_cum < 50 and self.science_cum < 50 and self.literacy_cum < 50:
            return "To repeat the class!"
        elif self.general_studies_cum < 50 and self.science_cum < 50 and self.numeracy_cum < 50:
            return "To repeat the class!"
        elif self.literacy_cum < 50 and self.general_studies_cum >= 50 and self.science_cum >= 50 and self.numeracy_cum >= 50:
            return "Promoted to the next class on trial!"
        elif self.numeracy_cum < 50 and self.general_studies_cum >= 50 and self.science_cum >= 50 and self.literacy_cum >= 50:
            return "Promoted to the next class on trial!"
        elif self.science_cum < 50 and self.general_studies_cum < 50 and self.numeracy_cum >= 50 and self.literacy_cum >= 50:
            return "Promoted to the next class on trial!"
        else:
            return "Promoted to the next class!"




    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'pk': self.pk})
