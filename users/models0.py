from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Person(AbstractUser):
    GENDER_CHOICES = [
		('MALE','MALE'),
		('FEMALE', 'FEMALE')
	]
    ROLE_CHOICES = [
        ('Student', 'Student'),
		('Staff', 'Staff'),
        ('Admin', 'Admin'),
    ]
    phone_number = models.CharField(max_length=20, unique=False, null=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    classe = models.ForeignKey('management.Class', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Class")
    address = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student', null=True)
    photograph = models.ImageField(upload_to='pupil_img/%Y/%m/%d', null=True, blank=True, verbose_name="Student's Photograph")
    referrer = models.CharField(max_length=20, default="None", null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        try:
            return str(self.username)
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

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Student(models.Model):
    student = models.OneToOneField('users.Person', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('student',)

    def __str__(self):
        try:
            return str(self.student)
        except:
            return str(self.id)

class Member(models.Model):
    member = models.OneToOneField('users.Person', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('member',)
        verbose_name = 'Member'
        verbose_name_plural = 'Staff'

    def __str__(self):
        try:
            return str(self.member)
        except:
            return str(self.id)

class WebAdmin(models.Model):
    web_admin = models.OneToOneField('users.Person', on_delete=models.SET_NULL, null=True, verbose_name="Admin")

    class Meta:
        ordering = ('web_admin',)
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    def __str__(self):
        try:
            return str(self.web_admin)
        except:
            return str(self.id)
