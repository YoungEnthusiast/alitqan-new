from django.contrib import admin
from .models import Person
from .forms import CustomRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class PersonAdmin(UserAdmin):
    list_display = ['created', 'username', 'first_name', 'last_name', 'role', 'classe', 'gender', 'is_staff', 'is_superuser']
    list_display_links = ['username', 'role']
    search_fields = ['username', 'email', 'phone_number']
    list_filter = ['is_staff', 'is_superuser', 'role']
    list_editable = ['gender', 'is_staff', 'is_superuser']
    list_per_page = 10

    add_form = CustomRegisterForm
    fieldsets = (
            *UserAdmin.fieldsets,
            (
                "uu ttt",
                {
                    'fields': ('classe', 'phone_number', 'role', 'photograph', 'gender', 'subject', 'address', 'dob')
                }
            )
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'classe', 'subject', 'email', 'phone_number', 'gender', 'role', 'subject', 'photograph', 'address', 'dob')}
        ),
    )
admin.site.register(Person, PersonAdmin)
