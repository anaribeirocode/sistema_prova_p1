from django.http import JsonResponse

from .models import Categoria

def listar_categorias(request):
    categorias = Categoria.objects.all().values('id', 'nome', 'tipo')
    return JsonResponse(list(categorias), safe=False)