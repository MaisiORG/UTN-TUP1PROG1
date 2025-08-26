#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#( °C × 9/5) + 32
celsius = float(input("Escriba una temperatura en celsius sin el signo: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Su temperatura en Fahrenheit es: {fahrenheit} F°")
