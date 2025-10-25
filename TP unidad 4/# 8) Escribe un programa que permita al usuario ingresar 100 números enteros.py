# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = 0
impares = 0
negativos = 0
positivos = 0
for contador in range(100):
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    else:
        positivos += 1
print(f"[{contador+1}] numeros ingresados.")

print(f"En total estuvieron estos numeros: \n{pares} numeros pares \n{impares} numeros impares \n{negativos} numeros negativos \n{positivos} numeros positivos")

