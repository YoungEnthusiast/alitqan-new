from django.contrib import admin
from .models import First, Second, Third

class FirstAdmin(admin.ModelAdmin):
    list_display = ['session', 'value', 'student', 'static_number_in_class', 'school_fees', 'static_class', 'subject', 'ca1', 'ca2', 'exam', 'total', 'subject_total', 'subject_avg', 'subject_pos', 'grade', 'cumulative', 'cum_perc', 'created', 'updated']
    search_fields = []
    list_editable = ['static_number_in_class']
    list_filter = ['subject', 'student__classe', 'static_class', 'static_number_in_class']
    list_display_links = ['student']
    list_per_page = 10
    # def get_classe(self, obj):
    #     return obj.student.classe
    # get_classe.admin_order_field = 'Student'
    # get_classe.short_description = 'Class'
admin.site.register(First, FirstAdmin)

class SecondAdmin(admin.ModelAdmin):
    list_display = ['session', 'value', 'student', 'static_number_in_class', 'school_fees', 'static_class', 'subject', 'ca1', 'ca2', 'exam', 'total', 'subject_total', 'subject_avg', 'subject_pos', 'grade', 'cumulative', 'cum_perc', 'created', 'updated']
    search_fields = []
    list_editable = ['static_number_in_class']
    list_filter = ['subject', 'student__classe', 'static_class', 'static_number_in_class']
    list_display_links = ['student']
    list_per_page = 10
    # def get_classe(self, obj):
    #     return obj.student.classe
    # get_classe.admin_order_field = 'Student'
    # get_classe.short_description = 'Class'
admin.site.register(Second, SecondAdmin)

class ThirdAdmin(admin.ModelAdmin):
    list_display = ['session', 'value', 'student', 'static_number_in_class', 'school_fees', 'static_class', 'subject', 'ca1', 'ca2', 'exam', 'total', 'terms_total', 'subject_total', 'subject_avg', 'subject_pos', 'grade', 'cumulative', 'cum_perc', 'created', 'updated']
    search_fields = []
    list_editable = ['static_number_in_class']
    list_filter = ['subject', 'student__classe', 'static_class', 'static_number_in_class']
    list_display_links = ['student']
    list_per_page = 10
    # def get_classe(self, obj):
    #     return obj.student.classe
    # get_classe.admin_order_field = 'Student'
    # get_classe.short_description = 'Class'
admin.site.register(Third, ThirdAdmin)
