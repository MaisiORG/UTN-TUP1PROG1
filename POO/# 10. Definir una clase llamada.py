# 10. Definir una clase llamada 'Jugador' que tenga un atributo privado para los puntos y métodos para sumar, restar y mostrar los puntos del jugador.

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__puntos = 0  # atributo privado

    def sumar_puntos(self, cantidad):
        self.__puntos += cantidad
        print(f"{self.nombre} ganó {cantidad} puntos.")

    def restar_puntos(self, cantidad):
        self.__puntos = max(0, self.__puntos - cantidad)
        print(f"{self.nombre} perdió {cantidad} puntos.")

    def mostrar_puntos(self):
        print(f"{self.nombre} tiene {self.__puntos} puntos.")

# Ejemplo
j = Jugador("Nico")
j.sumar_puntos(40)
j.restar_puntos(10)
j.mostrar_puntos()
