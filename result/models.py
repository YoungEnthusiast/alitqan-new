from django.db import models
from users.models import Person
import random

class First(models.Model):
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
        ('He has worked very hard this term and I am proud of his accomplishments.', '(Above 49%) - He has worked very hard this term and I am proud of his accomplishments.'),
        ('She has worked very hard this term and I am proud of her accomplishments.', '(Above 49%) - She has worked very hard this term and I am proud of her accomplishments.'),
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

    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True)
    subject = models.ForeignKey('management.Subject', on_delete=models.SET_NULL, null=True, related_name='result_subject')
    student = models.ForeignKey('users.Person', on_delete = models.SET_NULL, null=True)
    school_fees = models.BooleanField(max_length=5, default = False, verbose_name="School Fees")
    value = models.IntegerField(blank=True, default = 0)
    ca1 = models.IntegerField(blank=True, default = 0, verbose_name="1st CA")
    ca2 = models.IntegerField(blank=True, default = 0, verbose_name="2nd CA")
    exam = models.IntegerField(blank=True, default = 0, verbose_name="Exam")
    total = models.IntegerField(blank=True, default = 0)
    subject_total = models.IntegerField(blank=True, default = 0)
    subject_avg = models.FloatField(blank=True, default = 0)
    subject_pos = models.IntegerField(default = 0, null=True, verbose_name="Subject Position")
    grade = models.CharField(max_length=1, blank=True, null=True)
    cumulative = models.IntegerField(blank=True, default = 0)
    cum_perc = models.FloatField(blank=True, default = 0)
    number_present = models.CharField(max_length=7, blank=True, null=True, verbose_name="No of Days Present")
    concentration = models.CharField(max_length=11, blank=True, choices=ATTITUDE_CHOICES, null=True)
    responsiveness = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True)
    comprehension = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True)
    interest = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Interest in Learning")
    homework = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Homework Completion")
    reading = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    writing = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    spoken = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True, verbose_name="Spoken Arabic/English")
    innovative = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    teacher_comment = models.CharField(max_length=135, choices=TEACHER_CHOICES, blank=True, null=True, verbose_name="Class Teacher's Comment")
    head_comment = models.CharField(max_length=135, choices=HEAD_CHOICES, blank=True, null=True, verbose_name="Head of School's Comment")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    static_class = models.CharField(max_length=20, blank=True, null=True)
    static_class_teacher = models.CharField(max_length=30, blank=True, null=True)
    static_head_teacher = models.CharField(max_length=30, blank=True, null=True)
    static_teacher_signature = models.ImageField(null=True, blank=True)
    static_school_stamp = models.ImageField(null=True, blank=True)
    static_student_image = models.ImageField(null=True, blank=True)
    static_age = models.CharField(max_length=3, blank=True, null=True)
    static_number_in_class = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        try:
            return str(self.student.first_name) + " " + str(self.student.last_name) + " " + str(self.cumulative)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = "First Term Score"
        verbose_name_plural = "First Term Scores"

    def grade(self):
        if self.total < 50:
            return "E"
        elif self.total >= 50 and self.total < 60:
            return "D"
        elif self.total >= 60 and self.total < 70:
            return "C"
        elif self.total >= 70 and self.total < 85:
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

        if self.cum_perc < 50:
            return random.choice(choices_50)
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return random.choice(choices_60)
        elif self.cum_perc >= 60 and self.cum_perc < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

class Second(models.Model):
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
        ('He has worked very hard this term and I am proud of his accomplishments.', '(Above 49%) - He has worked very hard this term and I am proud of his accomplishments.'),
        ('She has worked very hard this term and I am proud of her accomplishments.', '(Above 49%) - She has worked very hard this term and I am proud of her accomplishments.'),
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
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True)
    subject = models.ForeignKey('management.Subject', on_delete=models.SET_NULL, null=True, related_name='result_subject_second')
    student = models.ForeignKey('users.Person', on_delete = models.SET_NULL, null=True, related_name='student_second')
    school_fees = models.BooleanField(max_length=5, default = False, verbose_name="School Fees")
    value = models.IntegerField(blank=True, default = 0)
    ca1 = models.IntegerField(blank=True, default = 0, verbose_name="1st CA")
    ca2 = models.IntegerField(blank=True, default = 0, verbose_name="2nd CA")
    exam = models.IntegerField(blank=True, default = 0, verbose_name="Exam")
    total = models.IntegerField(blank=True, default = 0)
    subject_total = models.IntegerField(blank=True, default = 0)
    subject_avg = models.FloatField(blank=True, default = 0)
    subject_pos = models.IntegerField(default = 0, null=True, verbose_name="Subject Position")
    grade = models.CharField(max_length=1, blank=True, null=True)
    cumulative = models.IntegerField(blank=True, default = 0)
    cum_perc = models.FloatField(blank=True, default = 0)
    number_present = models.CharField(max_length=7, blank=True, null=True, verbose_name="No of Days Present")
    concentration = models.CharField(max_length=11, blank=True, choices=ATTITUDE_CHOICES, null=True)
    responsiveness = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True)
    comprehension = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True)
    interest = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Interest in Learning")
    homework = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Homework Completion")
    reading = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    writing = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    spoken = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True, verbose_name="Spoken Arabic/English")
    innovative = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    teacher_comment = models.CharField(max_length=135, choices=TEACHER_CHOICES, blank=True, null=True, verbose_name="Class Teacher's Comment")
    head_comment = models.CharField(max_length=135, choices=HEAD_CHOICES, blank=True, null=True, verbose_name="Head of School's Comment")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    static_class = models.CharField(max_length=20, blank=True, null=True)
    static_class_teacher = models.CharField(max_length=30, blank=True, null=True)
    static_head_teacher = models.CharField(max_length=30, blank=True, null=True)
    static_teacher_signature = models.ImageField(null=True, blank=True)
    static_school_stamp = models.ImageField(null=True, blank=True)
    static_student_image = models.ImageField(null=True, blank=True)
    static_age = models.CharField(max_length=3, blank=True, null=True)
    static_number_in_class = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        try:
            return str(self.student.first_name) + " " + str(self.student.last_name) + " " + str(self.cumulative)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Second Term Score"
        verbose_name_plural = "Second Term Scores"

    def grade(self):
        if self.total < 50:
            return "E"
        elif self.total >= 50 and self.total < 60:
            return "D"
        elif self.total >= 60 and self.total < 70:
            return "C"
        elif self.total >= 70 and self.total < 85:
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

        if self.cum_perc < 50:
            return random.choice(choices_50)
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return random.choice(choices_60)
        elif self.cum_perc >= 60 and self.cum_perc < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

class Third(models.Model):
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
        ('He has worked very hard this term and I am proud of his accomplishments.', '(Above 49%) - He has worked very hard this term and I am proud of his accomplishments.'),
        ('She has worked very hard this term and I am proud of her accomplishments.', '(Above 49%) - She has worked very hard this term and I am proud of her accomplishments.'),
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
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True)
    subject = models.ForeignKey('management.Subject', on_delete=models.SET_NULL, null=True, related_name='result_subject_third')
    student = models.ForeignKey('users.Person', on_delete = models.SET_NULL, null=True, related_name='student_third')
    school_fees = models.BooleanField(max_length=5, default = False, verbose_name="School Fees")
    value = models.IntegerField(blank=True, default = 0)
    ca1 = models.IntegerField(blank=True, default = 0, verbose_name="1st CA")
    ca2 = models.IntegerField(blank=True, default = 0, verbose_name="2nd CA")
    exam = models.IntegerField(blank=True, default = 0, verbose_name="Exam")
    total = models.IntegerField(blank=True, default = 0)
    terms_total = models.IntegerField(blank=True, default = 0)
    subject_total = models.IntegerField(blank=True, default = 0)
    # terms_subject_total = models.IntegerField(blank=True, default = 0)
    subject_avg = models.FloatField(blank=True, default = 0)
    subject_pos = models.IntegerField(default = 0, null=True, verbose_name="Subject Position")
    grade = models.CharField(max_length=1, blank=True, null=True)
    cumulative = models.IntegerField(blank=True, default = 0)
    cum_perc = models.FloatField(blank=True, default = 0)
    number_present = models.CharField(max_length=7, blank=True, null=True, verbose_name="No of Days Present")
    concentration = models.CharField(max_length=11, blank=True, choices=ATTITUDE_CHOICES, null=True)
    responsiveness = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True)
    comprehension = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True)
    interest = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Interest in Learning")
    homework = models.CharField(max_length=11, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Homework Completion")
    reading = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    writing = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    spoken = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True, verbose_name="Spoken Arabic/English")
    innovative = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    teacher_comment = models.CharField(max_length=135, choices=TEACHER_CHOICES, blank=True, null=True, verbose_name="Class Teacher's Comment")
    head_comment = models.CharField(max_length=135, choices=HEAD_CHOICES, blank=True, null=True, verbose_name="Head of School's Comment")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    static_class = models.CharField(max_length=20, blank=True, null=True)
    static_class_teacher = models.CharField(max_length=30, blank=True, null=True)
    static_head_teacher = models.CharField(max_length=30, blank=True, null=True)
    static_teacher_signature = models.ImageField(null=True, blank=True)
    static_school_stamp = models.ImageField(null=True, blank=True)
    static_student_image = models.ImageField(null=True, blank=True)
    static_age = models.CharField(max_length=3, blank=True, null=True)
    static_number_in_class = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        try:
            return str(self.student.first_name) + " " + str(self.student.last_name) + " " + str(self.cumulative)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Third Term Score"
        verbose_name_plural = "Third Term Scores"

    def grade(self):
        if self.total < 50:
            return "E"
        elif self.total >= 50 and self.total < 60:
            return "D"
        elif self.total >= 60 and self.total < 70:
            return "C"
        elif self.total >= 70 and self.total < 85:
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


        if self.cum_perc < 50:
            return random.choice(choices_50)
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return random.choice(choices_60)
        elif self.cum_perc >= 60 and self.cum_perc < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)































    # def teacher_comment(self):
    #     if self.student.gender == "FEMALE":
    #         pronoun0 = "she"
    #     else:
    #         pronoun0 = "he"
    #     if self.student.gender == "FEMALE":
    #         pronoun = "her"
    #     else:
    #         pronoun = "his"
    #     if self.student.gender == "FEMALE":
    #         pronoun2 = "her"
    #     else:
    #         pronoun2 = "him"
    #     choices_50 = ["Dear " + self.student.first_name + "! Your efforts fall short of the required level, try to upgrade your performance next term.",
    #         "I have truly enjoyed being " + self.student.first_name + "'s teacher and hope for improvement next term.",
    #         self.student.first_name + " is really trying, but " + pronoun0 + " needs to do more for a better result."]
    #     choices_60 = [self.student.first_name + ", I believe you can do better than this. We can’t wait for your improvement next term!",
    #         self.student.first_name + " is a valued member of the class. Significant improvement in " + pronoun + " commitment to studies will make " + pronoun2 + " great.",
    #         "Great effort, " + self.student.first_name + "! Consistency will make your performance better. I wish you all the best.",
    #         "Dear " + self.student.first_name + "! Ability to stay on task without distraction will guarantee better result. Hope that would be achieved next term."]
    #     choices_80 = ["What a great performance from you, " + self.student.first_name + "! You can perform even better next term.",
    #         self.student.first_name + " has worked very hard this term and I am proud of all of " + pronoun + " accomplishments.",
    #         self.student.first_name + "'s strength is evident in this result. I look forward for improvement in the weak areas.",
    #         self.student.first_name + ", you really tried with this result and I commend your attitude to learning. May Allah bless you.",
    #         "I am so proud of you " + self.student.first_name +  ", and wish you well in your academics subsequent terms."]
    #     choices_else = ["It is my pleasure being " + self.student.first_name + "'s class teacher for " + pronoun + " zeal to study is on the highest level!",
    #         self.student.first_name + "'s dedication to study is topnotch! No wonder " + pronoun0 + " has excellent grades throughout.",
    #         "What an excellent result! " + self.student.first_name + "'s  performance this term is really outstanding!"]
    #
    #     if self.cum_perc < 50:
    #         return random.choice(choices_50)
    #     elif self.cum_perc >= 50 and self.cum_perc < 60:
    #         return random.choice(choices_60)
    #     elif self.cum_perc >= 60 and self.cum_perc < 80:
    #         return random.choice(choices_80)
    #     else:
    #         return random.choice(choices_else)

    # def head_comment(self):
    #     if self.student.gender == "FEMALE":
    #         pronoun0 = "she"
    #     else:
    #         pronoun0 = "he"
    #     if self.student.gender == "FEMALE":
    #         pronoun = "her"
    #     else:
    #         pronoun = "his"
    #     if self.student.gender == "FEMALE":
    #         pronoun2 = "her"
    #     else:
    #         pronoun2 = "him"
    #     choices_50 = ["Your performance is not bad, but you need to try harder. May you accomplish that with ease.",
    #         "You can do better next term; you need to. May Allah make that an easy one for you.",
    #         "Your performance is not that poor as a fresher. But try to improve your performance next term.",
    #         "The adventure just begins; nothing to worry about. You will excel in sha Allah."]
    #     choices_60 = ["I believe you will do better next term. You can, actually. May Allah bless you.",
    #         "What a good performance! Keep it up. May Allah bless you.",
    #         "Great effort. I hope to see more next term. May Allah bless you.",
    #         "What a beginning! I believe the future is promising. May Allah bless you."]
    #     choices_80 = ["A deserving result for a child who has been wonderful. May Allah bless you.",
    #         "A praiseworthy performance! You deserve all credits. May Allah bless you.",
    #         "Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.",
    #         "This is an excellent performance. Thumbs up. May Allah bless you.",
    #         "Great performance. This result shows how wonderful you are. May Allah bless you."]
    #     choices_else = ["A praiseworthy performance! Keep it up. May Allah bless you.",
    #         "Surely, this is a five-star performance! May Allah bless you.",
    #         "Maa sha Allah, this is awesome! May Allah bless you.",
    #         "Maa sha Allah, this is impressive! The sky is surely your starting point. May Allah bless you."]
