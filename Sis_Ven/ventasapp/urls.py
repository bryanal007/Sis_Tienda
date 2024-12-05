from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ventasapp.views import (
    ClienteViewSet, ProductoViewSet, EmpresaViewSet,
    ProveedorViewSet, EmpleadoViewSet, FacturaViewSet
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'facturas', FacturaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Rutas de la API directamente aquí
]
