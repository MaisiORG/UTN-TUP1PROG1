# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
numero_usuario = int(input("Ingrese un número entero positivo: "))
if numero_usuario < 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    resultado = suma_digitos(numero_usuario)
    print(f"La suma de los dígitos de {numero_usuario} es: {resultado}")
    