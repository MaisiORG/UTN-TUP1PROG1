# j) Relación de composición entre clases Empresa y Empleado
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        empleado.empresa = self

    def mostrar_empleados(self):
        print(f"Empleados de {self.nombre}:")
        for e in self.empleados:
            print(f"- {e.nombre}")

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empresa = None

    def mostrar_empresa(self):
        if self.empresa:
            print(f"{self.nombre} trabaja en {self.empresa.nombre}.")
        else:
            print(f"{self.nombre} no tiene empresa asignada.")

# Ejemplo
empresa = Empresa("TechCorp")
e1 = Empleado("Ana")
e2 = Empleado("Luis")
empresa.agregar_empleado(e1)
empresa.agregar_empleado(e2)
empresa.mostrar_empleados()
e1.mostrar_empresa()
