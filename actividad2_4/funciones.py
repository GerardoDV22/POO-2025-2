def validar_numero(numero):
    if not isinstance(numero,(int,float)):
        print("Solo se permiten valores numéricos.")
        return 0.0
    elif numero < 0:
        print("El valor no puede ser negativo.")
        return 0.0
    else:
        return numero