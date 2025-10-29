# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#  productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Manzana,0.50,100\n")
    archivo.write("Banana,0.30,150\n")
    archivo.write("Naranja,0.80,200\n")
print("Archivo productos.txt creado con éxito.")

with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


   
