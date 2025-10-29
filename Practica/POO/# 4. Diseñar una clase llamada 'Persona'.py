# 4. Diseñar una clase llamada 'Persona' que tenga atributos para el nombre y la edad, y métodos para presentarse y verificar si es mayor de edad.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo
p = Persona("Lucía", 20)
p.presentarse()
print("¿Es mayor de edad?", p.es_mayor_de_edad())
