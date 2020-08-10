from django.contrib import admin
from .models import Producto, Cliente, Factura, DetalleFactura

#admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #readonly_fields = ['creacion', 'modificacion']
    list_display = ('descripcion', 'precio','stock','iva')
    ordering = ('descripcion',)
    search_fields = ('descripcion', 'precio')
    list_filter = ('descripcion',)


admin.site.register(Producto, ProductoAdmin)
############################################################################################

class ClienteAdmin(admin.ModelAdmin):
    #readonly_fields = ['creacion', 'modificacion']
    list_display = ('ruc', 'nombre','direccion')
    ordering = ('ruc',)
    search_fields = ('ruc', 'nombre')
    list_filter = ('ruc',)


admin.site.register(Cliente, ClienteAdmin)



