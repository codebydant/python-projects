from django.contrib import admin
from gestion_pedidos.models import Articulo, Cliente, Pedido


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [f.name for f in Cliente._meta.fields]
    # list_display = ('nombre', 'email', 'telefono')


class ArticuloAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [f.name for f in Articulo._meta.fields]
    list_filter = [f.name for f in Articulo._meta.fields if f.name != 'id' and f.name != 'nombre']


class PedidoAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [f.name for f in Pedido._meta.fields]
    list_filter = [f.name for f in Pedido._meta.fields if f.name != 'id' and f.name != 'nombre']


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
