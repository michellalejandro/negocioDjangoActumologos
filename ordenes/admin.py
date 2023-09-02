from django.contrib import admin
from .models import *

# Register your models here.
class OrdenItemInline(admin.TabularInline):
    model = ItemOrden
    campos_id = ['producto']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    lista_despl = ['id','nombre','primer_apellido','segundo_apellido','correo','direccion'
                   ,'codigo_postal','ciudad','pagado','creado','actualizado']
    lista_filtro = ['pagado','creado','actualizado']

    inlines = [OrdenItemInline]