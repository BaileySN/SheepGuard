from django.contrib import admin
from .models import Sheep, Pasture

class SheepAdmin(admin.ModelAdmin):
    list_display = ('code','name','state','birthdate','fk_color','sex','fk_pasture_ground')
    list_filter = ['fk_pasture_ground']
    search_fields = ('code','name','sex','state')
    date_hierarchy = 'birthdate'
    ordering = ['-birthdate']


class PastureAdmin(admin.ModelAdmin):
    list_display = ('name','place','postalcode')
    search_fields = ('name','place')


admin.site.register(Sheep, SheepAdmin)
admin.site.register(Pasture, PastureAdmin)

