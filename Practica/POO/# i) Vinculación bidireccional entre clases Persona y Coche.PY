# i) Vinculación bidireccional entre clases Persona y Coche
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.coche = None

    def asignar_coche(self, coche):
        self.coche = coche
        coche.propietario = self  # vínculo en ambas direcciones

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.propietario = None

    def mostrar_info(self):
        if self.propietario:
            print(f"Este {self.marca} {self.modelo} pertenece a {self.propietario.nombre}.")
        else:
            print(f"Este {self.marca} {self.modelo} no tiene propietario.")

# Ejemplo
persona = Persona("Lucía")
auto = Coche("Honda", "Civic")
persona.asignar_coche(auto)
auto.mostrar_info()

