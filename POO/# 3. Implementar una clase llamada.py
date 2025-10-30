# 3. Implementar una clase llamada 'Coche' que tenga atributos para la marca, el modelo y la velocidad actual.
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"El coche {self.marca} acelera a {self.velocidad} km/h.")

    def frenar(self, cantidad):
        self.velocidad = max(0, self.velocidad - cantidad)
        print(f"El coche {self.marca} frena a {self.velocidad} km/h.")

# Ejemplo
auto = Coche("Toyota", "Corolla")
auto.acelerar(50)
auto.frenar(20)
