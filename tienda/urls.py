from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.lista_productos,name='lista_productos_por_categoria'),
    path('<slug:categoriaSlug>/',views.lista_productos,name='lista_productos_por_categoria'),
    path('<int:id>/<slug:slug>',views.producto_detalle,name="producto_detalle"),

    #NOTA: la variable name debe ser igual a lo que devuelve la funcion get_absolute_url de models
]