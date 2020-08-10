from django.contrib import admin
from django.urls import path
from App_Proyecto_ORM.views import menu, producto, editarProducto, eliminarProducto, listarProducto
from App_Proyecto_ORM.views import cliente, editarCliente, eliminarCliente, listarCliente
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='index'),
    path('producto/', producto, name='producto'),
    path('editarproducto/<int:id>/', editarProducto, name='editarproducto'),
    path('listarproducto/', listarProducto, name='listarproducto'),
    path('eliminarproducto/<int:id>', eliminarProducto, name='eliminarproducto'),
    path('cliente/', cliente, name='cliente'),
    path('editarcliente/<int:id>/', editarCliente, name='editarcliente'),
    path('listarcliente/', listarCliente, name='listarcliente'),
    path('eliminarcliente/<int:id>', eliminarCliente, name='eliminarcliente'),

]