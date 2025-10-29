# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
productos = []
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    lineas = contenido.splitlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = float(partes[1])
        cantidad = int(partes[2])
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto)
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Error: Producto no encontrado.")
print("Búsqueda de producto finalizada.")
