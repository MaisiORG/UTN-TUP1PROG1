# 9. Diseñar una clase llamada 'Carrito' que permita agregar productos (con nombre y precio) y calcular el total a pagar.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)
        print(f"{producto.nombre} agregado al carrito.")

    def total(self):
        return sum(p.precio for p in self.productos)

# Ejemplo
p1 = Producto("Pan", 150)
p2 = Producto("Leche", 200)
carrito = Carrito()
carrito.agregar(p1)
carrito.agregar(p2)
print("Total a pagar:", carrito.total())
