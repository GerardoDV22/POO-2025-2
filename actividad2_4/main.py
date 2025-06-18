from cuenta import Cuenta
bandera = 0
while True:
    print("\n1. Crear cuenta\n2. Ver el saldo\n3. Depositos/Retiros\n4. Salir")
    opc = int(input("Elije un número: "))
    if opc == 1:
        nombre = input("\nIngrese el nombre del titular: ")
        saldo = float(input("Ingrese el saldo inicial: "))
        while True:
            opc2 = int(input("Tipo de cuenta\n1. Ahorro\n2. Corriente\nSeleccione: "))
            if opc2 == 1:
                tipo = "Ahorro"
                break
            elif opc2 == 2:
                tipo = "Corriente"
                break
            else:
                input("\nOpción invalida. Presione enter...")
        c = Cuenta(nombre, saldo, tipo)
        bandera = 1
    elif opc == 2:
        if bandera == 1:
            c.mostrar_saldo()
        else:
            input("\nAun no se crea una cuenta. Presione enter..")
    elif opc == 3:
        if bandera == 1:
            while True:
                print("\n1. Deposito\n2. Retiro\n3. Volver")
                opc2 = int(input("Selecciona: "))
                if opc2 == 1:
                    c.depositar(float(input("\nIngresa la cantidad a depositar: ")))
                    break
                elif opc2 == 2:
                    c.retirar(float(input("\nIngresa la cantidad a retirar: ")))
                    break
                elif opc2 == 3:
                    break
                else:
                    input("\nOpción invalida. Presione enter...")
        else:
             input("\nAun no se crea una cuenta. Presione enter..")
    elif opc == 4:
        print("Hasta luego")
        break
    else:
        input("\n\nOpción invalida. Presiona enter...")