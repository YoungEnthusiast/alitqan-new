from django.contrib import admin
from .models import FirstTerm, SecondTerm, ThirdTerm

class FirstTermAdmin(admin.ModelAdmin):
    list_display = ['session', 'pupil', 'get_classe', 'school_fees', 'literacy_ca1', 'literacy_ca2',
        'literacy_exam', 'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam',
        'general_studies_ca1', 'general_studies_ca2', 'general_studies_exam',
        'science_ca1', 'science_ca2', 'science_exam', 'cumulative']

    search_fields = ['pupil__user__username', 'pupil__classe__name']
    list_filter = ['pupil__classe__name']
    list_display_links = ['pupil']
    list_editable = ['school_fees']
    list_per_page = 10

    def get_classe(self, obj):
        return obj.pupil.classe
    get_classe.admin_order_field = 'pupil'
    get_classe.short_description = 'Class'

admin.site.register(FirstTerm, FirstTermAdmin)

class SecondTermAdmin(admin.ModelAdmin):
    list_display = ['session', 'pupil', 'get_classe', 'school_fees', 'literacy_ca1', 'literacy_ca2',
        'literacy_exam', 'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam',
        'general_studies_ca1', 'general_studies_ca2', 'general_studies_exam',
        'science_ca1', 'science_ca2', 'science_exam', 'cumulative']

    search_fields = ['pupil__user__username', 'pupil__classe__name']
    list_filter = ['pupil__classe__name']
    list_editable = ['school_fees']
    list_display_links = ['pupil']
    list_per_page = 10

    def get_classe(self, obj):
        return obj.pupil.classe
    get_classe.admin_order_field = 'pupil'
    get_classe.short_description = 'Class'

admin.site.register(SecondTerm, SecondTermAdmin)

class ThirdTermAdmin(admin.ModelAdmin):
    list_display = ['session', 'pupil', 'get_classe', 'school_fees', 'literacy_ca1', 'literacy_ca2',
        'literacy_exam', 'numeracy_ca1', 'numeracy_ca2', 'numeracy_exam',
        'general_studies_ca1', 'general_studies_ca2', 'general_studies_exam',
        'science_ca1', 'science_ca2', 'science_exam', 'cumulative', 'cumulative_1st', 'cumulative_2nd', 'all_cumulative']

    search_fields = ['pupil__user__username', 'pupil__classe__name']
    list_filter = ['pupil__classe__name']
    list_editable = ['school_fees']
    list_display_links = ['pupil']
    list_per_page = 10

    def get_classe(self, obj):
        return obj.pupil.classe
    get_classe.admin_order_field = 'pupil'
    get_classe.short_description = 'Class'

admin.site.register(ThirdTerm, ThirdTermAdmin)
