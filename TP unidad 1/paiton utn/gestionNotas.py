# Puse el diccionario de alumnos
alumnosDiccionario = {  
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}
# la lista de materias
materias = [
    ["Ciencias",0 ,0 ,0],
    ["Historia",0 ,0 ,0],
    ["Geografia",0 ,0 ,0],
    ["Matematicas",0 ,0 ,0],
    ["Fisica",0 ,0 ,0]
]
# la de las notas finales
notasFinales = []

for legajo, nombre in alumnosDiccionario.items():
    print(f"Alumno: {nombre} (Legajo: {legajo})")

    # Copio la lista base 
    materias = [linea[:] for linea in materias]

    # obtengo las notas
    for linea in materias:
        materia = linea[0]
        print(f"Materia: {materia}")

        # Pedi nota 1 
        while True:
            nota1 = float(input(f"Ingrese Nota 1 para {materia}: "))
            if 0 <= nota1 <= 10:
                break
            else:
                print("Error: la nota debe estar entre 0 y 10.")

        # Pedi nota 2
        while True:
            nota2 = float(input(f"Ingrese Nota 2 para {materia}: "))
            if 0 <= nota2 <= 10:
                break
            else:
                print("Error: la nota debe estar entre 0 y 10.")

        # Calculo el promedio
        notaFinal = (nota1 + nota2) / 2

        # Guardo en la lista 
        linea[1] = nota1
        linea[2] = nota2
        linea[3] = round(notaFinal, 2)

    print("Notas cargadas:")
    for linea in materias:
        print(f"{linea[0]} - Nota1: {linea[1]}  Nota2: {linea[2]}  Final: {linea[3]}")

    # Evaluo la mejor calificacion 
    mejor_materia = materias[0]
    for linea in materias:
        if linea[3] > mejor_materia[3]:
            mejor_materia = linea

    print(f"La mejor materia de {nombre} fue {mejor_materia[0]} con {mejor_materia[3]}")

    # el promedio de todos:
    suma = 0
    for linea in materias:
        suma += linea[3]
    promedioGeneral = suma / len(materias)
    promedioGeneral = round(promedioGeneral, 2)

    # guardarlas
    notasFinales.append([nombre, promedioGeneral])

    print(f"Promedio general de {nombre}: {promedioGeneral}")

print("Promedios finales de todos los alumnos:")
for linea in notasFinales:
    print(f"{linea[0]} - Promedio General: {linea[1]}")

mejorAlumno = notasFinales[0]
for linea in notasFinales:
    if linea[1] > mejorAlumno[1]:
        mejorAlumno = linea

print("\nEl alumno con mejor promedio es:", mejorAlumno[0], "con", mejorAlumno[1])
