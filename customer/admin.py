from django.contrib import admin
from .models import Profession, Customer, Title


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fk_title','lname','fname','fk_profession','phone','phone2','fax','email','email2')
    list_filter = ['fk_profession']
    search_fields = ('lname','vname')
    date_hierarchy = 'change_time'
    ordering = ['-change_time']


class ProfessionAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name','change_time')


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name','change_time']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Profession, ProfessionAdmin)
