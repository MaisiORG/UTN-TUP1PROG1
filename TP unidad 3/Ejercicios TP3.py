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

#---------------------------------------------------------------------------------------------------

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
while nota < 0 or nota > 10:
    print("SOLO NUMEROS DEL 1 AL 10")
    nota = int(input("Ingrese su nota: "))
if nota >= 6:
    (print("Aprobado"))
else:
    print("Desaprobado")

#---------------------------------------------------------------------------------------------------

#3)Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar}

numero = int(input("Ingrese un número par: "))
while numero % 2 != 0:
    numero = int(input("Por favor, ingrese un número par: "))
print("Ha ingresado un número par")

#---------------------------------------------------------------------------------------------------

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un adolecente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto/a joven")
elif edad >= 30:
    print("Eres un adult/o mayor")

#---------------------------------------------------------------------------------------------------

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese su contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#---------------------------------------------------------------------------------------------------

#6) La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.

#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

from statistics import mode, median, mean
import random
numero_aleatorio = [random.randint(1,100) for i in range(50)]
print(f"Moda es: ",[mode(numero_aleatorio)],", Mediana es: ",[median(numero_aleatorio)]," Media es: ",[mean(numero_aleatorio)])
if mean(numero_aleatorio) > median(numero_aleatorio) and median(numero_aleatorio) > mode(numero_aleatorio):
    print("Sesgo positivo")
elif mean(numero_aleatorio) < median(numero_aleatorio) and median(numero_aleatorio) < mode(numero_aleatorio):
    print("Sesgo negativo")
elif mean(numero_aleatorio) == median(numero_aleatorio) and median(numero_aleatorio) == mode(numero_aleatorio):
    print("Sin Sesgo")

#---------------------------------------------------------------------------------------------------

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

#notapara mí: 
# "maxi"
# 0,1,2,3
# -4,-3,-2,-1
frase = input("Ingrese una palabra o frase: ")
if frase[-1] in "aeiouAEIOU":
    frase = frase + "!"
print(frase)

#---------------------------------------------------------------------------------------------------

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("ingrese su nombre: ")
print("Ingrese (1) para que se nombre aparezca en mayusculas... (2) para que su nombre aparezca en minusculas... (3) para que su nombre solo aparezca con la primera letra en minuscula ")
opcion = int(input(":"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#---------------------------------------------------------------------------------------------------

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")

#---------------------------------------------------------------------------------------------------

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
