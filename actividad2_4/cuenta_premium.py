from cuenta import Cuenta
class Cuenta_Premium(Cuenta):
    def __init__(self, titular, saldo, tipo, beneficios):
        super().__init__(titular, saldo, tipo)
        self._beneficios = beneficios

    def mostrar_beneficios(self):
        print("Su cuenta premium tiene los siguientes beneficios:")
        print(self._beneficios)