from django.contrib import admin
from .models import medicine

class MedicineInfo(admin.ModelAdmin):
    list_display = ('id', 'name', 'ingredient', 'effect', 'dosage')

admin.site.register(medicine, MedicineInfo)

