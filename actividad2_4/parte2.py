#Parte 1
class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre # público
        self._correo = correo # protegido

u = Usuario("Ivette", "ivette@email.com")
print(u.nombre) # acceso permitido
print(u._correo) # posible pero no recomendado

#Parte 2
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
c = CuentaBancaria(1000)
#print(c.__saldo) # Esto dará error
print(c._CuentaBancaria__saldo) # Esto sí funciona

#Parte 3
class Producto:
    def __init__(self, precio):
        self.__precio = precio
    def get_precio(self):
        return self.__precio
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido")
p = Producto(50)
print(p.get_precio())
p.set_precio(-10)
p.set_precio(100)
print(p.get_precio())