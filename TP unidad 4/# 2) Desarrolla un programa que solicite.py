# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

while True: # profe estas cosas las estoy haciendo recien el 23 de octubre por si ve algo nuevo es por eso
    try:
        numero = int(input("Ingrese un Número Entero: "))
        break
    except ValueError:
        print("INGRESE UN NÚMERO ENTERO VÁLIDO")
numero_abs = abs(numero)
digitos = 0
if numero_abs == 0:
    digitos = 1
else:
    while numero_abs > 0:

        numero_abs //= 10
        digitos += 1

print(f"El número {numero} tiene {digitos} dígitos.")

