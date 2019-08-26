from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Country


'''
class StateResource(resources.ModelResource):
    class Meta:
        model = State
        export_order = ('id', 'year', 'state_name', 'country_id', 'migrant_num')
'''
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name', 'create_time', 'last_updated_time')
    ordering = ("id",)
'''
@admin.register(State)
class StateAdmin(ImportExportModelAdmin):
    list_display = ('id', 'year', 'state_name', 'country_name', 'migrant_num')
    ordering = ('year',)
'''