# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general..

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
def mostrar_potencias(base, hasta):
    for exponente in range(hasta + 1):
        print(f"{base}^{exponente} = {potencia(base, exponente)}")
base_usuario = float(input("Ingrese la base: "))
exponente_usuario = int(input("Ingrese el exponente máximo (entero no negativo): "))
mostrar_potencias(base_usuario, exponente_usuario)
