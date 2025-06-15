class Producto:
    def __init__(self, nombre, precio, cantidad): #Método constructor
        self.nombre = nombre
        self.precio = 0.0       #Atributos por defecto
        self.cantidad = 0

        if not isinstance(precio,(int,float)): #Validación del atributo precio
            print("El precio debe ser un número")
        elif precio < 0:
            print("El precio no puede ser menor que 0")
        else:
            self.precio = float(precio)
        
        if not isinstance(cantidad,int): #Validación del atributo cantidad
            print("La cantidad debe ser un número")
        elif cantidad < 0:
            print("La cantidad no puede ser menor que 0")
        else:
            self.cantidad = cantidad

    def __str__(self):                     #Método que se ejecuta al poner el objeto en un print
        return f"Productos: {self.nombre} | Precio: {self.precio} | Cantidad: {self.cantidad}"
    
    def __add__(self, otro):               #Método suma, se ejecuta al sumar dos objetos Producto
        if self.nombre.lower == otro.nombre.lower:
            return f"Producto con cantidad: {self.cantidad+otro.cantidad}"
        else:
            return "Los productos no tienen el mismo nombre"
        
    def __mul__(self, num):               #Método multiplicación, se ejecuta al multiplicar un objeto Producto con un número
        return f"{self.precio*num}"
    
    def __eq__(self, otro):               #Método equal, sirve para comparar los atributos de dos objetos Productos
        return self.nombre == otro.nombre and self.precio == otro.precio
    
    def __del__(self):                    #Método del,  da un mensaje elimina el objeto y libera memora
        print(f"Eliminando el siguiente producto: {self.nombre}")