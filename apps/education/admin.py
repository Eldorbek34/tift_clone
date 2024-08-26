from django.contrib import admin
from apps.education import  models

@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_diplay = ("ful_name", "phone_number", )