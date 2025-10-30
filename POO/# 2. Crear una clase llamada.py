# 2. Crear una clase llamada 'Calculadora' que tenga métodos para sumar, restar, multiplicar y dividir dos números.
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: división por cero"

# Ejemplo
c = Calculadora()
print("Suma:", c.sumar(10, 5))
print("División:", c.dividir(8, 0))
