from django.contrib import admin
from .models import OTCInfo, ETCInfo, Pill

class OTC_InfoInfo(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'effect', 'dosage', 'caution', 'nation', 'image')
admin.site.register(OTCInfo, OTC_InfoInfo)

class ETC_InfoInfo(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'effect', 'dosage', 'caution', 'nation', 'image')
admin.site.register(ETCInfo, ETC_InfoInfo)

class PillInfo(admin.ModelAdmin):
     list_display = ('name', 'maker', 'shape', 'fcolor', 'bcolor', 'fmark', 'bmark', 'image')

"""
class PhotoInline(admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
"""
admin.site.register(Pill, PillInfo)


