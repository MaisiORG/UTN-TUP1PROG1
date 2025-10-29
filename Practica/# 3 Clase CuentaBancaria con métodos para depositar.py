# 3 Clase CuentaBancaria con métodos para depositar y retirar dinero

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron ${cantidad}. Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron ${cantidad}. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

# Ejemplo
cuenta = CuentaBancaria("Luis", 1000)
cuenta.retirar(300)
cuenta.depositar(500)
