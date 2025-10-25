# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
intentos = 1
numeroRandom = random.randint(0, 9)

while True:
    try:
        numeroUsuario = int(input("Adivine el Número del 0 al 9: "))
        if 0 <= numeroUsuario <= 9:
            if numeroUsuario == numeroRandom:
                print(f"¡Usted adivinó el número aleatorio: {numeroRandom}!")
                print(f"Intentos: {intentos}")
                break
            else:
                intentos += 1
        else:
            print("Por favor, ingrese un número dentro del rango (0 al 9).")
    except ValueError:
        print("Por favor, ingrese un número que este dentro del rango (0 al 9).")
    
