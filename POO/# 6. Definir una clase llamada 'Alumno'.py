# 6. Definir una clase llamada 'Alumno' que tenga atributos para el nombre y una lista de notas. Implementar métodos para calcular el promedio de las notas y determinar si el alumno está aprobado (promedio >= 6) o desaprobado.
class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def estado(self):
        if self.promedio() >= 6:
            return "Aprobado"
        else:
            return "Desaprobado"

# Ejemplo
a = Alumno("Micaela", [8, 7, 9])
print(f"Promedio: {a.promedio():.2f} | Estado: {a.estado()}")
