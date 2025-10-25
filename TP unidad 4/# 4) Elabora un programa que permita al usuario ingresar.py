# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

sumatotal = 0
while True:
    try:
        numero = int(input("Ingresa un numero entero para sumarlo: "))
        if numero == 0:
            print("0 ingresado, saliendo.")
            break
        else:
            sumatotal += numero
            print(f"Suma total: {sumatotal}")
    except ValueError:
        print("INGRESE UN NÚMERO ENTERO VÁLIDO")
print(f"La suma total de los numeros es: {sumatotal}")