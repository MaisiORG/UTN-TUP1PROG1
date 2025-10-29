# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# TECNICATURA UNIVERSITARIA
# EN PROGRAMACIÓN
# A DISTANCIA
# 3
# Programación 1
# agenda = {
#    ("lunes", "10:00"): "Reunion"
#   ("martes", "15:00"): "Clase de Inlés"
#   }
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("jueves", "10:00"): "Reunión de equipo",
    ("viernes", "14:00"): "Clase de Matemáticas"
}
print("Bienvenido a la agenda de eventos.")
while True:
    dia = input("Ingrese el día (o 'salir' para terminar): ").lower()
    if dia == "salir":
        print("Saliendo de la agenda...")
        break
    hora = input("Ingrese la hora (formato HH:MM): ")
    evento = agenda.get((dia, hora))
    if evento:
        print(f"El evento programado para {dia} a las {hora} es: {evento}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")

