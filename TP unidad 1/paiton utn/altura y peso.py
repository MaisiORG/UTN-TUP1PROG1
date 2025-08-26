#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
altura = float(input("Ingrese su altura en metros "))
peso = float(input("Ingrese su peso en kilos: "))
masacorporal = peso / (altura) ** 2
print(f"Su masa corporal es: {masacorporal}")