# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

bebidas = {"cocacola": 30, "pepsi": 26, "talca": 19, "fanta": 15}

print("Seleccione la bebida que quiera consumir:", list(bebidas.keys()))

while True:
    nombreProducto = input("Ingrese el nombre del producto (o 'salir' para terminar): ").lower()

    if nombreProducto == "salir":
        print("Saliendo del sistema...")
        break

    if nombreProducto not in bebidas:
        print("El producto no existe.")
        continue  # vuelve a pedir el nombre

    print(f"Stock actual de {nombreProducto}: {bebidas[nombreProducto]}")

    accion = input("¿Desea agregar unidades al stock? (s/n): ").lower()
    if accion == 's':
        try:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
                continue
            bebidas[nombreProducto] += cantidad
            print(f"Nuevo stock de {nombreProducto}: {bebidas[nombreProducto]}")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    elif accion == 'n':
        print("No se realizaron cambios.")
    else:
        print("Opción inválida. Intente de nuevo.")

