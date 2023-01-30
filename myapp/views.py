from django.shortcuts import render, HttpResponseRedirect
from myapp.forms import RegistrosForm
from myapp.forms import MateriasForm
from myapp.models import Registros
from myapp.models import Materias
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import redirect

def home(request):
    return render(request, 'flexy-bootstrap-lite/html/home.html')

def index(request):
    return render(request, 'flexy-bootstrap-lite/html/index.html')

def materias(request):
    materias = Materias.objects.all()
    return render(request, 'flexy-bootstrap-lite/html/CRUD.html', {'materias':materias})

def adicionarMateria(request):
    form = MateriasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/materias')
    return render(request, 'flexy-bootstrap-lite/html/adicionar.html', {'form':form})

def updateMateria(request, id):
    materia = Materias.objects.get(id=id)
    form = MateriasForm(request.POST or None, instance=materia)
    if form.is_valid():
        form.save()
        return redirect('/materias')
    return render(request, 'flexy-bootstrap-lite/html/update.html', {'form':form, 'materia':materia})



def deleteMateria(request, id):
    materia = Materias.objects.get(id=id)
    materia.delete()
    return redirect('/')

def listagemMaterias(request):
    listaMaterias = Materias.objects.all()
    return render(request, 'flexy-bootstrap-lite/html/listagem.html', {'listaMaterias':listaMaterias})

def consultaMateria(request):
    return render(request, 'flexy-bootstrap-lite/html/consulta.html')

def buscaMateria(request):
    buscar = request.GET.get('buscaMateria')
    resultados = Materias.objects.filter(materia__icontains=buscar)
    return render(request, 'flexy-bootstrap-lite/html/busca.html', {'resultados': resultados})

def sobre(request):
    return render(request, 'flexy-bootstrap-lite/html/sobre.html')