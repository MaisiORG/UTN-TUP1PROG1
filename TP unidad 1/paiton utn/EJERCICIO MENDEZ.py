# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su país: ")
print(f"Soy",nombre,apellido+", tengo",edad,"años y vivo en",residencia)

#(4 )Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
import math
pi = math.pi
radio = int(input("Ingrese Radio: "))
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"Su Radio fue de {radio} \nSu área fue de {area}\nSu perímetro fue de {perimetro}")

#(5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.
segundos = int(input("Ingrese cantidad de segundos"))
hora = segundos / 3600
print(f"Equivale a {hora} horas")

#(6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero = int(input("Ingrese Numero: "))
print(f"{numero} x 1 =",numero * 1)
print(f"{numero} x 2 =",numero * 2)
print(f"{numero} x 3 =",numero * 3)
print(f"{numero} x 4 =",numero * 4)
print(f"{numero} x 5 =",numero * 5)
print(f"{numero} x 6 =",numero * 6)
print(f"{numero} x 7 =",numero * 7)
print(f"{numero} x 8 =",numero * 8)
print(f"{numero} x 9 =",numero * 9)
print(f"{numero} x 10 =",numero * 10)

# 7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese el primer numero que no sea 0: "))
numero2 = int(input("Ingrese el segundo numero que no sea 0: "))
print(f"{numero1} + {numero2} =",numero1 + numero2)
print(f"{numero1} : {numero2} =",numero1 / numero2)
print(f"{numero1} x {numero2} =",numero1 * numero2)
print(f"{numero1} - {numero2} =",numero1 - numero2)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
altura = float(input("Ingrese su altura en metros "))
peso = float(input("Ingrese su peso en kilos: "))
masacorporal = peso / (altura) ** 2
print(f"Su masa corporal es: {masacorporal}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#( °C × 9/5) + 32
celsius = float(input("Escriba una temperatura en celsius sin el signo: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Su temperatura en Fahrenheit es: {fahrenheit} F°")

#10)Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio es: {promedio}")
