from django.contrib import admin
from .models import *

# Register your models here.

#Agregamos los modelos en el panel de administracion de Django
admin.site.register(Categoria)
admin.site.register(Producto)

