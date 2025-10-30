# f) Getters y Setters para la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

# Ejemplo
p = Persona("Pedro", 25)
print(p.nombre)   # usa el getter
p.nombre = "Juan" # usa el setter
print(p.nombre)

