# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def mostrar_fibonacci(hasta):
    for i in range(hasta):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
numero_usuario = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
mostrar_fibonacci(numero_usuario)

