# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        cuenta = 1 if (numero % 10) == digito else 0
        return cuenta + contar_digito(numero // 10, digito)
numero_usuario = int(input("Ingrese un número entero positivo: "))
digito_usuario = int(input("Ingrese un dígito entre 0 y 9: "))
if numero_usuario < 0 or digito_usuario < 0 or digito_usuario > 9:
    print("Por favor, ingrese un número entero positivo y un dígito válido (0-9).")
else:
    resultado = contar_digito(numero_usuario, digito_usuario)
    print(f"El dígito {digito_usuario} aparece {resultado} veces en el número {numero_usuario}.")
    