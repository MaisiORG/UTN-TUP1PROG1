# 1. Definir una clase llamada 'Rectangulo' que tenga atributos para la base y la altura.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Ejemplo
r = Rectangulo(5, 3)
print("Área:", r.area())
print("Perímetro:", r.perimetro())
