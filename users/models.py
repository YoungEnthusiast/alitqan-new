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
        ('A---n', 'A---n'),
    ]
    username = models.CharField(max_length=40, unique=True, verbose_name="Admission Number/Username")
    phone_number = models.CharField(max_length=20, unique=False, null=True, verbose_name="Phone Number")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    classe = models.ForeignKey('management.Class', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Class")
    address = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student', null=True)
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Class(es) and Subject(s) I teach")
    photograph = models.ImageField(upload_to='pupil_img/%Y/%m/%d', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        try:
            return str(self.username) + " | " + str(self.first_name) + " " + str(self.last_name)
        except:
            return str(self.id)

    @property
    def photographURL(self):
        try:
            url = self.photograph.url
        except:
            url = ''
        return url

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
