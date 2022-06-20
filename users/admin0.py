from django.contrib import admin
from .models import Person, Student, Member, WebAdmin
from .forms import CustomRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class PersonAdmin(UserAdmin):
    list_display = ['created', 'username', 'first_name', 'last_name', 'role', 'referrer', 'phone_number', 'gender', 'is_staff', 'is_superuser']
    list_display_links = ['username']
    search_fields = ['username', 'email', 'phone_number']
    list_filter = ['is_staff', 'is_superuser', 'role']
    list_editable = ['gender', 'is_staff']
    list_per_page = 10

    add_form = CustomRegisterForm
    fieldsets = (
            *UserAdmin.fieldsets,
            (
                "uu ttt",
                {
                    'fields': ('classe', 'phone_number', 'role', 'photograph', 'gender', 'address', 'dob', 'referrer')
                }
            )
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'classe', 'email', 'phone_number', 'gender', 'role', 'photograph', 'address', 'dob', 'referrer')}
        ),
    )
admin.site.register(Person, PersonAdmin)

# from django.contrib import admin
# from .models import Person
#
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ['user', 'classe']
#     # search_fields = ['user__username', 'user__first_name', 'user__last_name']
#     # list_per_page = 10
#
# admin.site.register(Person, PersonAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student']
admin.site.register(Student, StudentAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['member']
admin.site.register(Member, MemberAdmin)

class WebAdminAdmin(admin.ModelAdmin):
    list_display = ['web_admin']
admin.site.register(WebAdmin, WebAdminAdmin)
