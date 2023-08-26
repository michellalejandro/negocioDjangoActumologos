from django.shortcuts import render,get_object_or_404
from carrito.formulario import FormularioAgregarProducto
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("<h1>Bienvenido a la tienda<h1>")

def lista_productos(request,categoriaSlug=None):
    categoria = None
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(disponibilidad=True)

    if categoriaSlug:
        categoria = get_object_or_404(Categoria, slug=categoriaSlug)
        productos = productos.filter(categoria=categoria)

    return render(request, 'tienda/productos/lista.html',
                  {'categoria':categoria,
                   'categorias': categorias,
                   'productos': productos,})

def producto_detalle(request,id,slug):
    producto = get_object_or_404(Producto,id=id,slug=slug,disponibilidad=True)
    form_carrito_producto = FormularioAgregarProducto()

    return render(request,'tienda/productos/detalles.html',{'producto':producto,
                                                            'form_carrito_producto': form_carrito_producto})