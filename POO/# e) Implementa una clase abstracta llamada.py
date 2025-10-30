# e) Implementa una clase abstracta llamada "FiguraGeometrica" con un método abstracto "area". Luego, crea una clase concreta llamada "Cuadrado" que herede de "FiguraGeometrica" y implemente el método "area" para calcular el área del cuadrado.
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Ejemplo
cuadro = Cuadrado(5)
print("Área del cuadrado:", cuadro.area())
