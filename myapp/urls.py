from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('materias/', views.materias, name='materias'),
    #path('index/', views.index, name='index'),
    path('adicionar/', views.adicionarMateria, name='adicionarMateria'),
    path('update/<int:id>', views.updateMateria, name='updateMateria'),
    path('delete/<int:id>', views.deleteMateria, name='deleteMateria'),
    path('listagem/', views.listagemMaterias, name='listagemMaterias'),
    path('consulta/', views.consultaMateria, name='consultaMateria'),
    path('busca/', views.buscaMateria, name='buscaMateria'),
    path('sobre/', views.sobre, name='sobre'),
]