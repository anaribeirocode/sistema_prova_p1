from django.http import JsonResponse

from .models import Livro

def listar_livros(request):
    livros = Livro.objects.all().values('id', 'titulo', 'autor', 'data_publicacao', 'categoria_id')
    return JsonResponse(list(livros), safe=False)

def listar_livros_disponiveis(request):
    disponiveis = Livro.objects.all().values('id', 'titulo', 'autor', 'data_publicacao', 'categoria_id', 'status')
    return JsonResponse(list(disponiveis), safe=False)