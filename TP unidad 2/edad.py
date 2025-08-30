#1)Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”
edad = int(input("Igrese su edad: "))
while edad < 0 or edad > 110:
    print("Numero o Caracter invalido")
    edad = int(input("Igrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")