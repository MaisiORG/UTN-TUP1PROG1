#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

#Desde el 21 de diciembre hasta el 20 de marzo (incluidos) #12 - 3

#Desde el 21 de marzo hasta el 20 de junio (incluidos) #3 - 6

#Desde el 21 de junio hasta el 20 de septiembre (incluidos) #6 - 9

#Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) #9 - 12

hemisferio = input("Ingrese su hemisferio (S/N): ").upper()
while hemisferio != "S" and hemisferio != "N":
    print("Entrada inválida, debe ser S o N.")
    hemisferio = input("Ingrese su hemisferio (S/N): ").upper()

print("Ingresaste:", hemisferio)

mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if 1 <= mes <= 12 and 1 <= dia <= 31:
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        hemisferioNorte = "invierno"
        hemisferioSur = "verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        hemisferioNorte = "primavera" 
        hemisferioSur = "otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        hemisferioNorte = "verano"
        hemisferioSur = "invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        hemisferioNorte = "otoño" 
        hemisferioSur = "primavera"
    else:
        print("ERROR")
    
    if hemisferio == "N":
        print(f"La estación es: {hemisferioNorte}")
    elif hemisferio == "S":
        print(f"La estación es: {hemisferioSur}")
else:
    print("ERROR")
