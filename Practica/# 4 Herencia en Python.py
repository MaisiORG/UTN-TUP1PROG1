# 4 Herencia en Python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Ejemplo
mi_perro = Perro("Firulais")
mi_perro.hablar()

