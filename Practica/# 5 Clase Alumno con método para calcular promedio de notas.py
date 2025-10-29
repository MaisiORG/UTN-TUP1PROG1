# 5 Clase Alumno con método para calcular promedio de notas
class Alumno:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def mostrar_info(self):
        print(f"Alumno: {self.nombre} | Promedio: {self.promedio():.2f}")

# Ejemplo
a1 = Alumno("María", [8, 9, 10])
a1.mostrar_info()

