# (7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese el primer numero que no sea 0: "))
numero2 = int(input("Ingrese el segundo numero que no sea 0: "))
print(f"{numero1} + {numero2} =",numero1 + numero2)
print(f"{numero1} : {numero2} =",numero1 / numero2)
print(f"{numero1} x {numero2} =",numero1 * numero2)
print(f"{numero1} - {numero2} =",numero1 - numero2)