from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=25, db_index=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.category)

class Video(models.Model):
    title = models.CharField(max_length=200, db_index=True, unique=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='videos')
    home_page = models.BooleanField(max_length=5, default = False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return str(self.title)

    @property
    def videoURL(self):
        try:
            url = self.video.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        #return reverse('videos', 'gallery')
        return reverse('videos', args=['gallery'])
