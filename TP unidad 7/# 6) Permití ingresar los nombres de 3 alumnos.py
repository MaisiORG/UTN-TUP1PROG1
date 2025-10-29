# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:
# alumnos = { 
#   "Juan": (10, 9, 8),
#   "Ana": (7, 8, 9),
# }

alumnos = {}

for c in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
                if nota < 0 or nota > 10:
                    raise ValueError("La nota debe estar entre 0 y 10.")
                notas.append(nota)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido entre 0 y 10.")
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio}")

    