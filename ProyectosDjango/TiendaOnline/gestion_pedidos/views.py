from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import Articulo


# Create your views here.


def get_search_form(request):
    return render(request, 'search_productos.html')


def handle_get_request(request):
    if request.GET["prd"]:
        # message = 'Article searched: {}'.format(request.GET["prd"])
        producto = request.GET["prd"]
        articulos = Articulo.objects.filter(nombre__icontains=producto)
        return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto})
    else:
        message = 'Nothing entered!'
    return HttpResponse(message)
