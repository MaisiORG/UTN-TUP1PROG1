# 4. Crear dos funciones: calcular_area_circulo(radio) 
# que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario y 
# llamar ambas funciones para mostrar los resultados.

import math
def calcular_Area_ciruclo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_Perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio= float(input("Ingrese el radio del circulo:"))
print(f"El area del circulo es: {calcular_Area_ciruclo(radio)}")
print(f"El perimetro del circulo es: {calcular_Perimetro_circulo(radio)}")

