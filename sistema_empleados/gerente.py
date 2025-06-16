

from empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")