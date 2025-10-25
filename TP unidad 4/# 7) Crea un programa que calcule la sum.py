# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

while True:
    try:
        numeroUsuario = int(input("Ingrese un Número para sumar los anteriores hasta el 0: "))
        if numeroUsuario > 0:
                suma = 0
                for i in range(numeroUsuario):
                    
                    print(i)
                    suma += i
                print(f"la suma de los numeros son: {suma}")
        
        elif numeroUsuario == 0:
            print("Su numero es 0")
        else:
            ValueError
            print("INGRESE UN NUMERO VALIDO")   
            
    except ValueError:
        print("INGRESE UN NUMERO VALIDO")