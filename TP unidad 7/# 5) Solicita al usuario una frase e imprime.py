# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
# Entrada: "hola mundo hola"
# Salida:
# Palabras_unicas: {'hola', 'mundo'}
# recuento: {'hola': 2, 'mundo': 1}

frase = input("Ingrese una frase: ")
frase = frase.upper()
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("Recuento:", recuento)
