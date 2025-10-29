# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    lineas = contenido.splitlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")