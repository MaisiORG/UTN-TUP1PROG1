# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

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
for producto in productos:
    print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
print("Lista de productos cargada en diccionarios con éxito.")