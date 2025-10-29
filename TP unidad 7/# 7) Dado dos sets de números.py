# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Creamos dos sets con los nombres de los estudiantes
parcial1 = {"Ana", "Luis", "María", "Juan", "Sofía"}
parcial2 = {"María", "Carlos", "Sofía", "Pedro"}

# 1 Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1.intersection(parcial2)

# 2 Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1.symmetric_difference(parcial2)

# 3Estudiantes que aprobaron al menos uno (unión)
al_menos_uno =  parcial1.union(parcial2)

# Mostramos los resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)
