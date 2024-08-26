from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'passport', 'pinfl', 'gender', 'birth_date', 'direction', 'status', 'district', 'accepted_at', 'created')
    list_filter = ('status', 'gender', 'direction', 'district', 'created')
    search_fields = ('first_name', 'last_name', 'passport', 'pinfl')
    readonly_fields = ('accepted_at', 'created')
    fieldsets = (
        (None, {
            'fields': ('user', 'first_name', 'last_name', 'passport', 'pinfl', 'gender', 'birth_date', 'direction', 'district', 'status')
        }),
        ('Timestamps', {
            'fields': ('accepted_at', 'created'),
        }),
    )

admin.site.register(Application, ApplicationAdmin)
