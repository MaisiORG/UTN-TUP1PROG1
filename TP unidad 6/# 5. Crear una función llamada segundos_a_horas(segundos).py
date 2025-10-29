# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y
# mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos_usuario = int(input("Ingrese la cantidad de segundos: "))
print(f"La cantidad de horas es: {segundos_a_horas(segundos_usuario)}")

