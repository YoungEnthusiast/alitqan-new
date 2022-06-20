from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ['created', 'updated', 'headline', 'content', 'image', 'home_page']
    search_fields = ['headline', 'content', 'created', 'updated']
    list_filter = ['home_page']
    list_display_links = ['headline', 'image']
    list_editable = ['home_page']
    list_per_page = 10

admin.site.register(News, NewsAdmin)
