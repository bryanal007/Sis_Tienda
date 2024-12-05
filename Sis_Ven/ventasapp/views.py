#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Clientes, Productos, Empresas, Proveedores, Empleados, Factura
from .serializers import ClienteSerializer, ProductoSerializer, EmpresaSerializer, ProveedorSerializer, EmpleadoSerializer, FacturaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresaSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedorSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadoSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer