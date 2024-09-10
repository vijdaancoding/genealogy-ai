from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin
from .models import Person
# Register your models here.
class PersonAdmin(dj_admin.ModelAdmin):
    list_display = ("name", "alias", "date_of_birth", "date_of_death", "gender")
neo_admin.register(Person, PersonAdmin)
