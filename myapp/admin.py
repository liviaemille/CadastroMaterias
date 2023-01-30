from django.contrib import admin
from myapp.models import Registros
@admin.register(Registros)

class RegistrosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']
