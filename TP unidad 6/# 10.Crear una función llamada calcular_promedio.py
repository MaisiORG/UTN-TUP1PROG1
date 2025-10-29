# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3
    
input1 = float(input("Ingrese el primer número: "))
input2 = float(input("Ingrese el segundo número: "))  
input3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(input1, input2, input3)
print("El promedio es:", promedio)  
