from empleado import Empleado
from gerente import Gerente
from tecnico import Tecnico

e = Empleado("Gera", 1000)
g = Gerente("Chris", 2000, "Producción")
t = Tecnico("Diego", -1500, "Redes")
print()
e.mostrar_info()
print()
g.mostrar_info()
print()
t.mostrar_info()