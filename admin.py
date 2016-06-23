from django.contrib import admin

from .models import Estudiante
# Register your models here.
@admin.register(Estudiante)

class adminEstudiante(admin.ModelAdmin):
    list_display = ['nombre', 'boleta','edad']
    list_filter = ['nombre','boleta','edad']
