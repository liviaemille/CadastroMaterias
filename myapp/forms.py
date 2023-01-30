from django import forms
from django.db.models.base import Model
from django.forms import fields
from myapp.models import Registros
from myapp.models import Materias

class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        # fields = ['nome', 'email', 'telefone']
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
        }
class MateriasForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = ['materia', 'professor', 'cargaHoraria']
        widgets = {
            'materia': forms.TextInput(attrs={'class':'form-control'}),
            'professor': forms.TextInput(attrs={'class':'form-control'}),
            'cargaHoraria': forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'materia': 'Matéria',
            'professor': 'Professor',
            'cargaHoraria': 'Carga Horária',
        }