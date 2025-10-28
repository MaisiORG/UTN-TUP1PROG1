# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# El operador remove() eliminó al numero maximo de la lista por otro operador max() 
# 22 es el numero mas alto asi que remove(max(numeros)) elimina al 22 (el mas alto)