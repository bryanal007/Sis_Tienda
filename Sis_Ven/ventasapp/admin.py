from django.contrib import admin
from .models import Clientes, Empleados, Factura, Productos, Proveedores, Empresas

# Uso de decoradores para mejorar la presentación en el panel de administración

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'direccion', 'email', 'fecha_creacion', 'Fecha_nacimiento')
    search_fields = ('cedula', 'nombre', 'apellido', 'email')
    list_filter = ('fecha_creacion', 'Fecha_nacimiento')
    ordering = ('cedula',)

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'fecha_creacion', 'fecha_nacimiento')
    search_fields = ('cedula', 'nombre', 'apellido', 'email')
    list_filter = ('fecha_creacion', 'fecha_nacimiento')
    ordering = ('cedula',)

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'marca', 'caracteristicas_categoria', 'precio', 'cantidad_stock', 'fecha_ingreso', 'fecha_elaboracion', 'fecha_vencimiento')
    search_fields = ('codigo', 'nombre', 'marca', 'caracteristicas_categoria')
    list_filter = ('caracteristicas_categoria', 'fecha_ingreso', 'fecha_vencimiento')
    ordering = ('codigo',)

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('codigo_factura', 'fecha_factura', 'cliente', 'empleado', 'producto', 'cantidad', 'get_subtotal', 'get_iva', 'get_total')
    search_fields = ('codigo_factura', 'cliente__nombre', 'producto__nombre')
    list_filter = ('fecha_factura',)
    ordering = ('codigo_factura',)

    # Métodos para mostrar los campos calculados
    def get_subtotal(self, obj):
        return obj.subtotal
    get_subtotal.short_description = 'Subtotal'

    def get_iva(self, obj):
        return obj.iva
    get_iva.short_description = 'IVA'

    def get_total(self, obj):
        return obj.total
    get_total.short_description = 'Total'

@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'email', 'empresa')
    search_fields = ('cedula', 'nombre', 'apellido', 'email', 'empresa__nombre')
    list_filter = ('empresa',)
    ordering = ('cedula',)

@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'nombre', 'telefono', 'email', 'direccion')
    search_fields = ('ruc', 'nombre', 'email')
    list_filter = ('nombre',)
    ordering = ('ruc',)
