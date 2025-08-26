#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
import math
pi = math.pi
radio = int(input("Ingrese Radio: "))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"Su Radio fue de {radio} \nSu área fue de {area}\nSu perímetro fue de {perimetro}")

