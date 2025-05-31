class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        print(f"Vehiculo\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}\n")

    def cumplir_anio(self):
        self.anio += 1
        print(f"El Vehiculo modelo {self.modelo} de la marca {self.marca} cumplio un año\n")