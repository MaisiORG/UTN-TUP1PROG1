# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

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
# Aquí podrías agregar, modificar o eliminar productos en la lista 'productos'
with open("productos.txt", "w") as archivo:
    for producto in productos:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
print("Archivo productos.txt actualizado con éxito.")



