from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from staff.models import Teacher
from datetime import date

class Class(models.Model):
    name = models.CharField(max_length=20, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    signature = models.ImageField(upload_to='signature_img/%Y/%m/%d', null=True, blank=True, verbose_name="Class Teacher's Signature")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.name)
        except:
            return str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ('name',)
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

class Pupil(models.Model):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Pupil', 'Pupil'),
        ('Student', 'Student'),
		('Staff', 'Staff'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    classe = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, verbose_name="Class")
    address = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Pupil', null=True)
    photograph = models.ImageField(upload_to='pupil_img/%Y/%m/%d', null=True, blank=True, verbose_name="Pupil's Photograph")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username) + " | " + str(self.user.first_name) + " " + str(self.user.last_name)
        except:
            return str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    class Meta:
        ordering = ('user__username',)

class Student(models.Model):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Pupil', 'Pupil'),
        ('Student', 'Student'),
		('Staff', 'Staff'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, unique=False, null=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    classe = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, verbose_name="Class")
    address = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Pupil', null=True)
    photograph = models.ImageField(upload_to='student_img/%Y/%m/%d', null=True, blank=True, verbose_name="Student's Photograph")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        try:
            return str(self.user.username) + " | " + str(self.user.first_name) + " " + str(self.user.last_name)
        except:
            return str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


    class Meta:
        ordering = ('user__username',)
