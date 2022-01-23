from django.contrib import admin
from .models import tata_rec
from import_export.admin import ImportExportModelAdmin
@admin.register(tata_rec)

class tata_rec_class(ImportExportModelAdmin):
    pass

class studentadmin(admin.ModelAdmin):
    list_display = ['__all__']
# Register your models here.
