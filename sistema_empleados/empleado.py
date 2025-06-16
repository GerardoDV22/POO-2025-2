
class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = 0.0

        if not isinstance(salario,(int,float)):
            print("El salario debe ser un número")
        elif salario < 0:
            print("El salario no puede ser menor que 0")
        else:
            self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nSalario: {self.salario}")



