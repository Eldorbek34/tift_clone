from django.contrib import admin
from apps.common import models

@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "order_id")
    list_editable = ("order_id",)

    def __sstr__(self):
        return self.title


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "region__title", "order_id")
    list_editable = ("order_id",)

    def __str__(self):
        return self.title


@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "social", )
    list_editable = ("social", )