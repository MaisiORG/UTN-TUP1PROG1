# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
numInvertido = 0
if num < 0:
    num = abs(num)
    while num != 0:

        numInvertido = numInvertido * 10 + num % 10
        num //= 10
    print(f"-{numInvertido}")
else:
    while num != 0:

        numInvertido = numInvertido * 10 + num % 10
        num //= 10

    print(numInvertido)
