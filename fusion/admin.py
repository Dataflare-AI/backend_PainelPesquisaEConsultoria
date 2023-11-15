from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import FileUploadAPI


@admin.register(FileUploadAPI)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_on", "description")
    search_fields = ("file", "description")
    list_filter = ("uploaded_on",)
    date_hierarchy = "uploaded_on"
    ordering = ("uploaded_on",)
