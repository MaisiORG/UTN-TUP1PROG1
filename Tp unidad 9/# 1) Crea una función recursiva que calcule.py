# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"El factorial de {i} es {factorial(i)}")
numero_usuario = int(input("Ingrese un número entero positivo: "))
mostrar_factoriales(numero_usuario)

