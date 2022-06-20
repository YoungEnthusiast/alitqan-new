from django.db import models
from django.conf import settings

class News(models.Model):
    headline = models.CharField(max_length=80, null=True)
    content = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='news_img/%Y/%m/%d', null=True, blank=True)
    home_page = models.BooleanField(max_length=5, default = False, verbose_name="Home Page")
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'News or Event'
        verbose_name_plural = 'News and Events'

    def __str__(self):
        return str(self.headline)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
