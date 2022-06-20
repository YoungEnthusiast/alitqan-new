from django.contrib import admin
from .models import Pupil, Class, Student

class PupilAdmin(admin.ModelAdmin):
    list_display = ['user', 'classe', 'photograph']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_per_page = 10

admin.site.register(Pupil, PupilAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'classe', 'photograph']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    list_display_links = ['user', 'photograph']
    list_per_page = 10

admin.site.register(Student, StudentAdmin)

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'signature']
    search_fields = []
    list_display_links = ['name', 'signature']
    list_per_page = 10

admin.site.register(Class, ClassAdmin)
