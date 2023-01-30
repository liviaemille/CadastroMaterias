from django.db import models
#from django.forms import widgets

# Create your models here.
class Registros(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=70)

class Materias(models.Model):
    materia = models.CharField(max_length=100)
    cargaHoraria = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
