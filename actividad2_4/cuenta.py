from funciones import validar_numero
class Cuenta:
    def __init__(self, titular, saldo, tipo):
        self.__titular = titular
        self.__tipo = tipo
        self.__saldo = validar_numero(saldo)

    def depositar(self, cantidad):
        deposito = validar_numero(cantidad)
        if not deposito == 0:
            self.__saldo += deposito
            print(f"Deposito de {deposito} pesos exitoso")
        else:
            print("No es valido depositar 0 pesos")

    def retirar(self, cantidad):
        retiro = validar_numero(cantidad)
        if retiro == 0:
            print("No es valido retirar 0 pesos")
        elif retiro > self.__saldo:
            print("Fondos insuficientes")
        else:
            self.__saldo -= retiro
            print(f"Retiro de {retiro} pesos exitoso")

    def mostrar_saldo(self):
        print(f"El saldo es de: {self.__saldo} pesos")

    def get_titular(self):
        return self.__titular
    def set_titular(self, titular):
        self.__titular = titular
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self, tipo):
        self.__tipo = tipo