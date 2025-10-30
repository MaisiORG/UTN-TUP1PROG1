# c) Definición de la clase base Animal y las clases derivadas Perro y Gato

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # será sobreescrito en las clases hijas

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Ejemplo
mi_perro = Perro("Bobby")
mi_gato = Gato("Mimi")

print(mi_perro.hacer_sonido())
print(mi_gato.hacer_sonido())

