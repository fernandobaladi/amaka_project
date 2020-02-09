from django.contrib import admin
from .models import Producto, Tamano, Categoria, Rol, Usuario, Vendedor, Compania, Carrito, Ingrediente, Transaccion
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre', 'cantidad', 'costo')

class UsuarioAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellido', 'email')

class VendedorAdmin(admin.ModelAdmin):
    list_display=('nombre', 'apellido')

class CompaniaAdmin(admin.ModelAdmin):
    list_display=('compania', 'rif')

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'numero_de_transaccion')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Compania, CompaniaAdmin)
admin.site.register(Tamano)
admin.site.register(Categoria)
admin.site.register(Rol)
admin.site.register(Ingrediente)
admin.site.register(Carrito)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Transaccion, TransaccionAdmin)