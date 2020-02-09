from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.IntegerField()
    ingrediente = models.ManyToManyField("Ingrediente")
    cantidad = models.CharField(max_length=50)
    imagen = models.TextField()
    tamano = models.ForeignKey("Tamano", on_delete=models.CASCADE)
    categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    

class Tamano(models.Model):
    tamano = models.CharField(max_length=50)
    def __str__(self):
        return self.tamano

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.categoria

class Rol(models.Model):
    rol = models.CharField(max_length=50)
    def __str__(self):
        return self.rol

class Compania(models.Model):
    compania = models.CharField(max_length=50)
    rif = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    def __str__(self):
        return self.compania

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False) 
    rol = models.ForeignKey("Rol", on_delete=models.CASCADE)
    carrito = models.ManyToManyField("Carrito")
    transacciones = models.ManyToManyField("Transaccion")
    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()   
    compania = models.ForeignKey("Compania", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    productos = models.ManyToManyField("Producto")
    cantidad = models.IntegerField()
    def __str__(self):
        return str(self.productos.nombre)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    metodo_de_pago = models.CharField(max_length=50)
    productos = models.ManyToManyField("Producto")
    fecha = models.TimeField(auto_now=False, auto_now_add=True)
    numero_de_transaccion = models.IntegerField()
    def __str__(self):
        return str(self.productos)

