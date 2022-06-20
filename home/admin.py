from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message', 'date_submitted', 'status']
    search_fields = ['name', 'email' 'phone_number', 'date_submitted', 'status']
    list_filter = ['status']
    list_display_links = ['email']
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)

class BackgroundAdmin(admin.ModelAdmin):
    list_display = ['created', 'title', 'home_page', 'audio', 'updated']
    search_fields = ['created', 'title']
    list_filter = ['home_page']
    list_display_links = ['title', 'home_page']
    list_per_page = 10

admin.site.register(Background, BackgroundAdmin)
