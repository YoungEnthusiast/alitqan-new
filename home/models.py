from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User

class Contact(models.Model):
    STATUS_CHOICES = [
        ('Treated','Treated'),
        ('New', 'New'),
        ('Pending', 'Pending')
    ]
    name = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(max_length=500, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='New', null=True)

    class Meta:
        ordering = ('-date_submitted',)
        verbose_name = 'Contact us Message'
        verbose_name_plural = 'Contact us Messages'

    def __str__(self):
        return str(self.name)

class Background(models.Model):
    title = models.CharField(max_length=30, db_index=True, unique=True)
    audio = models.FileField(upload_to='audios/%Y/%m/%d', null=True, blank=True)
    home_page = models.BooleanField(max_length=5, default = False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Background Nasheed'
        verbose_name_plural = 'Background Nasheeds'
    def __str__(self):
        return str(self.title)

    @property
    def audioURL(self):
        try:
            url = self.audio.url
        except:
            url = ''
        return url
