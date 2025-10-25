# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
suma = 0
for contador in range(100):
    num = float(input("Introduce un número: "))
    print(f"[{contador+1}] numeros ingresados.")
    suma += num
contador += 1
media = suma / contador
print(f"El promedio de los numeros ingresado es: {media}")
   