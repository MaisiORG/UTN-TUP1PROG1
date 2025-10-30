# 5. Crear una clase llamada 'CuentaBancaria' que tenga atributos para el titular de la cuenta y el saldo, y métodos para depositar y retirar dinero.
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: ${self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo restante: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

# Ejemplo
cuenta = CuentaBancaria("Martín", 500)
cuenta.depositar(200)
cuenta.retirar(100)
