from django.contrib import admin

# Register your models here.
from .models import FileUploadAPI
from .usuario.models import Usuario


@admin.register(FileUploadAPI)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_on", "description")
    search_fields = ("file", "description")
    list_filter = ("uploaded_on",)
    date_hierarchy = "uploaded_on"
    ordering = ("uploaded_on",)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "password")
    search_fields = ("nome", "sobrenome", "email", "password")
    list_filter = ("nome", "sobrenome", "email", "password")
    date_hierarchy = "nome"
    ordering = ("nome",)
