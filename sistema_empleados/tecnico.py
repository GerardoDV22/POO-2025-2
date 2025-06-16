

from empleado import Empleado
class Tecnico(Empleado):
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        self.especialidad = especialidad
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")