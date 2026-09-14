from django.urls import path

from .views import listar_livros, listar_livros_disponiveis

urlpatterns = [
    path('livros/', listar_livros),
    path('livros/disponiveis', listar_livros_disponiveis),
]