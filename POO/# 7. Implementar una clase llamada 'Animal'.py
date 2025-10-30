# 7. Implementar una clase llamada 'Animal' con un método 'hablar' que imprima un sonido genérico. Luego, crear una subclase llamada 'Perro' que herede de 'Animal' y sobrescriba el método 'hablar' para imprimir "Guau guau".
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido genérico.")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

# Ejemplo
p = Perro("Toby")
p.hablar()
