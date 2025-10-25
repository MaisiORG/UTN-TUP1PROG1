# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

while True:
    try:
        num1 = int(input("Ingrese el primer Número: "))
        break
    except ValueError:
        print("INGRESE UN NÚMERO ENTERO VÁLIDO")
while True:
    try:
        num2 = int(input("Ingrese el segundo Número: "))
        break
    except ValueError:
        print("INGRESE UN NÚMERO ENTERO VÁLIDO")

if num1 > num2:
    num1, num2 = num2, num1
suma_total = 0
for numero in range(num1 + 1, num2):
    suma_total += numero
if num1 + 1 >= num2:
    
    print(f"No hay números enteros entre {num1} y {num2}. La suma es 0.")
else:
    print(f"Los números a sumar son: {list(range(num1 + 1, num2))}")
    print(f"La suma de los números enteros entre {num1} y {num2} (excluyéndolos) es: {suma_total}")
        
