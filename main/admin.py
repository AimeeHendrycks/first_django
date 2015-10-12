from django.contrib import admin
from main.models import State, StateCapital, City
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbrev')
    search_fields = ['name']

class CapitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'pop')
    search_fields = ['name']

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'zip_code')
    search_fields = ['name']


admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, CapitalAdmin)
admin.site.register(City, CityAdmin)