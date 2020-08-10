from django import forms
from .models import Producto, Cliente, Factura, DetalleFactura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock','iva')
        label = {'descripcion': 'Descripcion', 'precio': 'Precio', 'stock': 'Stock', 'iva':'Iva'}


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion','producto')
        label = {'ruc': 'ruc', 'nombre': 'Nombre', 'direccion': 'Direccion', 'producto':'Producto'}



