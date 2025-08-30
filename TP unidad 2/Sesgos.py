#6) La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.

#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

from statistics import mode, median, mean
import random
numero_aleatorio = [random.randint(1,100) for i in range(50)]
print(f"Moda es: ",[mode(numero_aleatorio)],", Mediana es: ",[median(numero_aleatorio)]," Media es: ",[mean(numero_aleatorio)])
if mean(numero_aleatorio) > median(numero_aleatorio) and median(numero_aleatorio) > mode(numero_aleatorio):
    print("Sesgo positivo")
elif mean(numero_aleatorio) < median(numero_aleatorio) and median(numero_aleatorio) < mode(numero_aleatorio):
    print("Sesgo negativo")
elif mean(numero_aleatorio) == median(numero_aleatorio) and median(numero_aleatorio) == mode(numero_aleatorio):
    print("Sin Sesgo")