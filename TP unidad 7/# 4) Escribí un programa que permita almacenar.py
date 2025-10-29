# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# contactos = {"Juan": "123456", "ana": "987654"} 
# consultar: "Juan" -> "123456"

contactos = {
"maxi": "111",
"ana": "444",
"luis": "777",
"maria": "000",
"carlos": "333" }
nombre = input("Ingrese el nombre del contacto que desea consultar: ")
nombre = nombre.lower()
if nombre in contactos:
    print(f"El número de {nombre} es: {contactos[nombre]}")
else:
    print(f"El contacto {nombre} no existe en la agenda.")

