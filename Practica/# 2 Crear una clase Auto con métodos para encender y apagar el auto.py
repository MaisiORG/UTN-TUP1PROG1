# 2 Crear una clase Auto con métodos para encender y apagar el auto. 
class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"El {self.marca} está encendido.")

    def apagar(self):
        self.encendido = False
        print(f"El {self.marca} está apagado.")

# Ejemplo
auto1 = Auto("Toyota")
auto1.encender()
auto1.apagar()
