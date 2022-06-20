from django.contrib import admin
from .models import Session, Class, Subject

class SessionAdmin(admin.ModelAdmin):
    list_display = ['session', 'first_head', 'school', 'first_report']
    search_fields = ['session',]
    list_editable = ['first_report']
    list_display_links = ['session', 'school']
    list_per_page = 10

admin.site.register(Session, SessionAdmin)

class ClassAdmin(admin.ModelAdmin):
    list_display = ['classe', 'teacher', 'signature']
    search_fields = []
    list_display_links = ['classe', 'signature']
    list_per_page = 10

admin.site.register(Class, ClassAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['classe', 'serial', 'subject', 'teacher']
    search_fields = []
    list_display_links = ['subject']
    list_filter = ['classe', 'subject']
    list_per_page = 10

admin.site.register(Subject, SubjectAdmin)
