# Una empresa de software les brinda a sus empleados como parte de sus beneficios 
# la posibilidad de acceder de forma gratuita a una máquina de Golosinas. Nuestra 
# tarea será la programación de las funcionalidades necesarias para llevar adelante 
# este beneficio. 
# Codifique la siguiente Lista de 2 dimensiones “golosinas”, que se corresponde a 
# una máquina expendedora de golosinas donde la columna 0 es el código de la 
# golosina, la columna 1 es la golosina, y la columna 2 es la cantidad (stock) actual de 
# golosinas  

# ==============================
# PRACTICA INTEGRADORA 1 - UTN
# Máquina de Golosinas
# ==============================

# --- Datos iniciales ---

# Lista de golosinas [Código, Nombre, Stock]
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M's", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

# Diccionario de empleados {Legajo: Nombre}
empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

# Tupla de claves para el técnico
clavesTecnico = ("admin", "CCCDDD", "2020")

# Historial de pedidos: [Código, Golosina, Cantidad Pedida]
golosinasPedidas = []


# --- Funciones ---

def mostrar_menu():
    print("""
========= MÁQUINA DE GOLOSINAS =========
a) Pedir golosina
b) Mostrar golosinas disponibles
c) Rellenar golosinas (técnico)
d) Apagar máquina
=======================================
""")


def mostrar_golosinas():
    print("\n Golosinas disponibles:")
    for codigo, nombre, stock in golosinas:
        print(f"{codigo:2} - {nombre:20} | Stock: {stock}")
    print()


def buscar_golosina(codigo):
    for g in golosinas:
        if g[0] == codigo:
            return g
    return None


def pedir_golosina():
    try:
        legajo = int(input("Ingrese su legajo: "))
        if legajo not in empleados:
            print("Usted no es un empleado de la empresa.")
            return

        print(f"Bienvenido {empleados[legajo]}!")
        while True:
            mostrar_golosinas()
            codigo = input("Ingrese el código de la golosina o 'salir' para volver al menú: ")

            if codigo.lower() == "salir":
                break

            try:
                codigo = int(codigo)
                golosina = buscar_golosina(codigo)

                if not golosina:
                    print("Código inválido.")
                    continue

                if golosina[2] <= 0:
                    print(f"Lo sentimos, {golosina[1]} no se encuentra disponible.")
                    continue

                # Descontar stock
                golosina[2] -= 1
                print(f"Usted retiró un/a {golosina[1]}.\n")

                # Registrar en el historial
                for registro in golosinasPedidas:
                    if registro[0] == codigo:
                        registro[2] += 1
                        break
                else:
                    golosinasPedidas.append([codigo, golosina[1], 1])

            except ValueError:
                print("Ingrese un número válido.")

    except ValueError:
        print("Legajo inválido.")


def rellenar_golosinas():
    print("Acceso restringido para técnicos.")
    clave1 = input("Ingrese la primera clave: ")
    clave2 = input("Ingrese la segunda clave: ")
    clave3 = input("Ingrese la tercera clave: ")

    if (clave1, clave2, clave3) != clavesTecnico:
        print("No tiene permiso para ejecutar la función de recarga.")
        return

    try:
        mostrar_golosinas()
        codigo = int(input("Ingrese el código de la golosina a recargar: "))
        golosina = buscar_golosina(codigo)

        if not golosina:
            print("Código inválido.")
            return

        cantidad = int(input("Ingrese la cantidad a agregar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return

        golosina[2] += cantidad
        print(f"Se recargaron {cantidad} unidades de {golosina[1]}. Stock actual: {golosina[2]}")

    except ValueError:
        print("Ingrese un valor numérico válido.")


def apagar_maquina():
    print("\nGolosinas pedidas durante la sesión:")
    total = 0
    for codigo, nombre, cantidad in golosinasPedidas:
        print(f"{nombre:20} | Cantidad pedida: {cantidad}")
        total += cantidad
    print(f"\nTotal de golosinas pedidas: {total}")
    print("Apagando máquina... ¡Hasta luego!")
    exit()


# --- Programa Principal ---
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            pedir_golosina()
        elif opcion == "b":
            mostrar_golosinas()
        elif opcion == "c":
            rellenar_golosinas()
        elif opcion == "d":
            apagar_maquina()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
